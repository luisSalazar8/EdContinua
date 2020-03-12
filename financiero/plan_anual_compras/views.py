from django.shortcuts import render, redirect, get_object_or_404
from .models import PlanAnualCompras, Partida
from .forms import PlanAnualComprasForm, PartidaForm
from .filters import PlanAnualComprasFilter
from datetime import date
from django.http import HttpResponseRedirect,JsonResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from dal import autocomplete
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    if (request.GET.get('estado', None) != None and 'Anulada' in request.GET['estado']):
        pac_lista = PlanAnualCompras.objects.all().order_by("-id")
    else:
        pac_lista = PlanAnualCompras.objects.all().exclude(estado='Anulada').order_by("-id")
    pac_filter = PlanAnualComprasFilter(request.GET, queryset=pac_lista)
    return render(request, "plan_anual_compras/pac_list.html", {"pac_lista":pac_lista, "filter":pac_filter})


class PACCreate(CreateView):
    model = PlanAnualCompras
    template_name = 'plan_anual_compras/pac_nuevo.html'
    form_class = PlanAnualComprasForm
    partida_form_class=PartidaForm
    success_url = '/financiero/plan_anual_compras/editar'
    def get_context_data(self,**kwargs):
        context=super(PACCreate,self).get_context_data(**kwargs)
        formset=self.partida_form_class()
        if('formset' not in context):
            context['formset']=formset
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form_Partida =self.partida_form_class(request.POST)
        if form.is_valid() and form_Partida.is_valid():
            pac=form.save(commit=False)
            partida=form_Partida.save(commit=False)
            if(pac.nombre==''):
                pac.nombre = 'Plan Anual de Compras - '+str(pac.año)
            pac.save()

            partida.pac = pac
            partida.save()
            return HttpResponseRedirect(self.get_success_url()+'/'+str(pac.pk))
        else:
            return self.render_to_response(self.get_context_data(form=form,formset=form_Partida))


class PACUpdate(UpdateView):
    model = PlanAnualCompras
    second_model = Partida
    template_name = 'plan_anual_compras/pac_editar.html'
    form_class = PlanAnualComprasForm
    partida_form_class=PartidaForm
    success_url = reverse_lazy('pac_index')

    def get_context_data(self, **kwargs):
        context = super(PACUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        partidas = self.second_model.objects.filter(pac_id=pk)
        context['partidas'] = partidas
        formset=self.partida_form_class()
        if('formset' not in context):
            context['formset']=formset
        context['pac_id'] = pk
        return context



class PACDelete(DeleteView):
    model = PlanAnualCompras
    template_name = 'plan_anual_compras/pac_eliminar.html'
    success_url = reverse_lazy('pac_index')
    form_class = PlanAnualComprasForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = "Anulada"
        motivo = dict(request.POST).get("motivo_anular")[0]
        self.object.motivo_anular = motivo
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


def pac_conf_elim(request):
    pac_id = request.GET.get('pk')
    pac = PlanAnualCompras.objects.get(id=pac_id)
    form = PlanAnualComprasForm(instance=pac)
    return render(request, "plan_anual_compras/pac_eliminar.html", {"object": pac, "form": form})

def partida_update(request):
    p_id=request.GET.get('pk')
    pac_id = request.GET.get('fk')
    partida = Partida.objects.get_object_or_404(id=p_id)
    form = PartidaForm(instance=partida)
    return render(request, "plan_anual_compras/partida_editar.html", {"form": form,"pk":p_id,"fk":pac_id})

    
def partida_eliminar(request):
    p_id=request.GET.get('pk')
    pac_id = request.GET.get('fk')
    partida = Partida.objects.get(id=p_id)
    return render(request, "plan_anual_compras/partida_eliminar.html", {"form": partida,"pk":p_id,"fk":pac_id})

class PartidaCreate(CreateView):
    model = Partida
    form_class = PartidaForm
    template_name='plan_anual_compras/partida_nuevo.html'
    success_url='/financiero/plan_anual_compras/editar'

    def get_context_data(self, **kwargs):
        context = super(PartidaCreate,self).get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        context['pac_id']=pk
        return context

    def post(self, request,*args,**kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        pac_id=kwargs['pk']
        print(pac_id)
        if form.is_valid():
            p = form.save(commit=False)
            p.pac_id = pac_id
            p.save()
            return HttpResponseRedirect(self.get_success_url()+'/'+str(pac_id))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class PartidaUpdate(UpdateView):
    model = Partida
    form_class = PartidaForm
    template_name = 'plan_anual_compras/partida_nuevo.html'
    success_url = '/financiero/plan_anual_compras/editar'

    def get_context_data(self, **kwargs):
        context = super(PartidaUpdate,self).get_context_data(**kwargs)
        fk=self.kwargs.get('fk',0)
        context['pac_id']=fk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        pac_id = kwargs['fk']
        pk = kwargs['pk']
        partida = self.model.objects.get(id=pk)
        form = self.form_class(request.POST, instance=partida)
        if form.is_valid():
            p=form.save(commit=False)
            p.pac_id = pac_id
            p.save()
            return HttpResponseRedirect(self.get_success_url()+'/'+str(pac_id))
        else:
            return self.render_to_response(self.get_context_data(form=form))


class PartidaDelete(DeleteView):
    model = Partida
    form_class = PartidaForm
    template_name = 'plan_anual_compras/partida_eliminar.html'
    success_url = '/financiero/plan_anual_compras/editar'

    def post(self, request, *args, **kwargs):
        pac_id = kwargs['fk']
        self.object=self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url()+'/'+str(pac_id))


def load_partida(request):
    partidas = Partida.objects.all() #COLOCAR EL MODELO AQUI
    tipo = request.GET.get('tipo')
    codigo = render_to_string("plan_anual_compras/dropdown_codigo.html", {"partidas": partidas})
    partida = render_to_string("plan_anual_compras/dropdown_partida.html", {"partidas": partidas})
    return JsonResponse({'codigo': codigo, 'partida': partida})
