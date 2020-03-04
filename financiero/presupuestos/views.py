from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect

#from django.core import serializers
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.views.generic import CreateView, UpdateView, DeleteView
from datetime import date

from .models import *
from .forms import PresupuestoEventoForm, PresupuestoEventoFormUpdate
from . import forms
from dal import autocomplete

from django.core.paginator import Paginator
from .filters import PresupuestoEventoFilter


def index_presupuestos(request):
	if (request.GET.get('estado',None)!=None and 'Anulada' in request.GET['estado']):
		presupuestos_list = PresupuestoEvento.objects.all().order_by("id")
	else:
		presupuestos_list = PresupuestoEvento.objects.all().exclude(estado='Anulada').order_by("id")
	presupuestos_list_filter = PresupuestoEventoFilter(request.GET, queryset=presupuestos_list)
	return render(request, 'presupuestos/index.html', {"filter":presupuestos_list_filter})


class PresupuestoEventoCreate(CreateView):
	model=PresupuestoEvento
	form_class=PresupuestoEventoForm
	template_name='presupuestos/forma.html'
	success_url=reverse_lazy('index_presupuestos')
	
	def get_context_data(self, **kwargs):
		context = super(PresupuestoEventoCreate, self).get_context_data(**kwargs)
		context['costo_horas'] = [0]
		context['impuesto_select'] = [-1]
		context['impuesto_unitario'] = [0]
		context['impuesto_total'] = [0]
		return context
		
	def form_valid(self, form):
		try:
			pre = str(int(self.model.objects.latest('pk').pk+1))
			sec = '0'*(4-len(pre))+pre
		except self.model.DoesNotExist:
			sec = '0001'
		form.instance.codigo = sec+'-'+str(date.today().year)
		return super().form_valid(form)


class PresupuestoEventoUpdate(UpdateView):
	model=PresupuestoEvento
	form_class=PresupuestoEventoForm
	second_form_class=PresupuestoEventoFormUpdate
	template_name='presupuestos/editar.html'
	success_url=reverse_lazy('index_presupuestos')
	

	def get_context_data(self, **kwargs):
		context=super(PresupuestoEventoUpdate,self).get_context_data(**kwargs)
		pk=self.kwargs.get('pk',0)
		presupuesto=self.model.objects.get(pk=pk)
		if 'form' in context:
			if presupuesto.estado=="Grabado":
				context['form']=self.form_class(instance=presupuesto)
			else:
				context['form']=self.second_form_class(instance=presupuesto)
		context['costo_horas']=[int(i) for i in str(presupuesto.costo_hora_instructores).split(',')[:-1]]
		context['impuesto_select']= [int(i) for i in str(presupuesto.impuesto_select).split(',')[:-1]]
		context['impuesto_unitario']=[int(i) for i in str(presupuesto.impuesto_unitario).split(',')[:-1]]
		context['impuesto_total']=[int(i) for i in str(presupuesto.impuesto_total).split(',')[:-1]]
		return context

class PresupuestoEventoDelete(DeleteView):
	model=PresupuestoEvento
	template_name='presupuestos/eliminar.html'
	success_url=reverse_lazy('index_presupuestos')
	form_class=PresupuestoEventoForm

	def post(self, request, *args, **kwargs):
		self.object=self.get_object()
		self.object.estado="Anulada"
		motivo=dict(request.POST).get("motivo_anular")[0]
		self.object.motivo_anular=motivo
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())


def presupuesto_conf_elim(request):
	presupuesto_id=request.GET.get('pk')
	presupuesto=PresupuestoEvento.objects.get(id=presupuesto_id)
	form=PresupuestoEventoForm(instance=presupuesto)
	return render(request,"presupuestos/eliminar.html",{"presupuesto":presupuesto,"form":form})

class PresupuestoEventoAprobar(UpdateView):
	model=PresupuestoEvento
	form_class=PresupuestoEventoForm
	template_name='presupuestos/aprobar.html'
	success_url=reverse_lazy('pendiente_aprobacion')

	def get_context_data(self, **kwargs):
		context=super(PresupuestoEventoAprobar,self).get_context_data(**kwargs)
		pk=self.kwargs.get('pk',0)
		presupuesto=self.model.objects.get(pk=pk)
		if 'form' in context:
			context['form']=self.form_class(instance=presupuesto)
		context['costo_horas']=[int(i) for i in str(presupuesto.costo_hora_instructores).split(',')[:-1]]
		context['impuesto_select']= [int(i) for i in str(presupuesto.impuesto_select).split(',')[:-1]]
		context['impuesto_unitario']=[int(i) for i in str(presupuesto.impuesto_unitario).split(',')[:-1]]
		context['impuesto_total']=[int(i) for i in str(presupuesto.impuesto_total).split(',')[:-1]]
		context['p_id']=presupuesto.pk
		return context

# def aprobar_presupuesto(request, pk):
# 	if(request.method == 'POST'):
# 		p = get_object_or_404(PresupuestoEvento, pk=pk)
# 		form = forms.PresupuestoEventoForm(request.POST,instance=p)
# 		if(form.is_valid()):
# 			form.save()
# 		# observaciones=dict(request.POST).get("motivo_anular")[0]
# 		# p.observaciones=observaciones
# 		# p.save()
# 		return redirect('pendiente_aprobacion')
# 	else:
# 		p = get_object_or_404(PresupuestoEvento, pk=pk)
# 		costo_horas=[int(i) for i in str(p.costo_hora_instructores).split(',')[:-1]]
# 		impuesto_select= [int(i) for i in str(p.impuesto_select).split(',')[:-1]]
# 		impuesto_unitario=[int(i) for i in str(p.impuesto_unitario).split(',')[:-1]]
# 		impuesto_total=[int(i) for i in str(p.impuesto_total).split(',')[:-1]]
# 		form = PresupuestoEventoForm(instance=p)
# 		return render(request, 'presupuestos/aprobar.html', {'form': form,"presupuesto":p,'costo_horas':costo_horas,'impuesto_select':impuesto_select,'impuesto_unitario':impuesto_unitario,'impuesto_total':impuesto_total})


def anular_presupuesto(request, pk):
	if(request.method == 'POST'):
		p = get_object_or_404(PresupuestoEvento, pk=pk)
		p.estado="Anulada"
		motivo=dict(request.POST).get("motivo_anular")[0]
		p.motivo_anular=motivo
		p.save()
		return redirect('pendiente_aprobacion')
   
def cargar_info(request):
	modelo=request.GET.get('modelo')
	id=request.GET.get('id')
	if modelo=="pasaje_instructor" or modelo=="pasaje_personal":
		valor=TarifarioServicioAereo.objects.get(pk=id).costo
	elif modelo=="hospedaje_alimentacion_instructor" or modelo=="hospedaje_alimentacion_personal":
		valor=TarifarioHospedajeAlimentacionDocente.objects.get(pk=id).costo
	elif modelo=="break_instructor" or modelo=='break_evento':
		valor=TarifarioServicioAlimentacionBreak.objects.get(pk=id).costo
	elif modelo=="almuerzo_instructor" or modelo=="almuerzo_evento":
		valor=TarifarioServicioAlimentacionAlmuerzo.objects.get(pk=id).costo
	elif modelo=="instalaciones":
		valor=TarifarioInstalacion.objects.get(pk=id).costo
	elif modelo=="prospecto_evento":
		valor=TarifarioProspecto.objects.get(pk=id).costo
	elif modelo in ['carpeta','certificados','maletin','block','pluma','lapiz','credencial_plastico','credencial_pvc','pendrive','otros_materiales','impuesto','ceremonia']:
		valor=TarifarioMaterial.objects.get(pk=id).costo_con_iva
	elif modelo=='aportacion_facultad_porcentaje':
		valor=TarifarioAportacion.objects.get(pk=id).costo
	elif modelo=="centro_costo":
		objeto=Centro_Costos.objects.get(pk=id)
		valor={'espol':objeto.espol, 'espoltech':objeto.espoltech, 'ministerio':objeto.ministerio, 'fundaespol':objeto.fundaespol}
	elif modelo=='cafeteria_limpieza':
		valor=TarifarioOtroSuministro.objects.get(pk=id).costo
	else:
		valor=0
	return JsonResponse({'costo':valor})
	