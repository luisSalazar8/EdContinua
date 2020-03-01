from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Juridica
from .models import Ciudad
from .models import Sector
from .models import TipoEmpresa
from .models import Contacto_natural
from  ventas.personas_naturales.models import Persona_Natural
#Forms
from . import forms
from financiero.orden_facturacion.forms import OrdenFacturacionForm


from dal import autocomplete
#Models
from ventas.personas_naturales.models import Persona_Natural

#Itertools
from itertools import chain

from django.core.paginator import Paginator


class EmpresaAutocomplete(autocomplete.Select2QuerySetView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        qs = Juridica.objects.all().order_by("nombre")
        if self.q:
            qs = qs.filter(Q(nombre__icontains=self.q) | Q(ruc__istartswith=self.q))
            #qs = qs.filter(nombre__istartswith=self.q)
        return qs

    def has_add_permission(self, request):
        return True

class TipoAutocomplete(autocomplete.Select2QuerySetView):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def get_queryset(self):
		qs = TipoEmpresa.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

		
	def has_add_permission(self, request):
		return True
class SectorAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Sector.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)

		return qs
	def has_add_permission(self, request):
		return True
# Create your views here.
def index_juridicas(request):
	juridicas_list = Juridica.objects.all().order_by("pk")
	prueba = Contacto_natural.objects.select_related('empresa')
	for i in prueba:
		print(i)
	filter = forms.JuridicaFilter(request.GET, queryset=juridicas_list )
	paginator = Paginator(filter.qs, 30) 
	page = request.GET.get('page')
	juridicas = paginator.get_page(page)
	return render(request, 'personas_juridicas/index.html', {'juridicas': juridicas, "filter":filter})

	
def load_ciudades(request):
	provincia_id = request.GET.get("provincia")
	ciudades = Ciudad.objects.filter(provincia_id=provincia_id).order_by('nombre')
	
	return render(request,"personas_juridicas/dropdown_ciudades.html",{"ciudades":ciudades})

def juridicas_view(request):

	if(request.method == "POST"):
		form = forms.JuridicaForm(request.POST)
		if(form.is_valid()):
			form.save()
			ruc = form.cleaned_data["ruc"]
			url = reverse_lazy('editar_juridica', kwargs={'pk': ruc})
			return HttpResponseRedirect(url)
	else:
		form = forms.JuridicaForm()
	return render(request,"personas_juridicas/forma.html", {"form":form})


def juridicas_editar(request,pk):
	if(request.method == "POST"):
		if("eliminar_contacto" not in request.POST):
				p = get_object_or_404(Juridica, pk=pk)
				form = forms.JuridicaForm(request.POST,instance=p)
				if(form.is_valid()):
					form.save()
					##PROBAR QUE SI ESTEN BIEN LOS CONTACTOS
					cedulas_post = []
					cedulas_modelo = []
					for i in request.POST:
						if "cedula" in i:
							cedulas_post.append(request.POST[i] )
					cedulas_contactos = Contacto_natural.objects.filter(empresa = pk)
					for i in cedulas_contactos:
						cedulas_modelo.append(i.contacto)
					for i in cedulas_post:
						if i not in cedulas_modelo:
							p.contacto_natural_set.create(contacto = i)	
					
					return HttpResponseRedirect(reverse_lazy("index_juridicas"))
		else:
			c = get_object_or_404(Contacto_natural,contacto=request.POST.get("eliminar_contacto"))
			c.delete()
			url = reverse_lazy('editar_juridica', kwargs={'pk': pk})
			return HttpResponseRedirect(url)
			
	else:
		final = []
		contactos = []
		cedulas_contactos = Contacto_natural.objects.filter(empresa = pk)
		print(cedulas_contactos)
		for i in cedulas_contactos:
			if (i.contacto not in contactos):
				contactos.append(i.contacto)
		for i in contactos:
			n = Persona_Natural.objects.filter(cedula = i)
			final = list(chain(final,n))
		p = get_object_or_404(Juridica, pk=pk)
		form = forms.JuridicaForm(instance=p)
		form_contacto = OrdenFacturacionForm()
	return render(request, 'personas_juridicas/editar_forma.html', {'form': form,"form_contacto":form_contacto,"naturales":final})


def juridicas_eliminar(request,pk=None):
	if(request.method == "POST"):
		print("Si entre we al post de juridicas eliminar")
		p = get_object_or_404(Juridica,pk=pk)
		p.delete()
		return redirect("index_juridicas")
	else:
		pk= request.GET.get('pk')
		if len(pk)<13:
			pk="0"+str(pk)
		p = get_object_or_404(Juridica,pk=pk)
		return render(request, 'personas_juridicas/eliminar.html', {'object': p})

def juridica_contacto_eliminar(request,pk=None):
	
	print("entre al get de eliminar contactos")
	pk= request.GET.get('contacto')
	c = get_object_or_404(Persona_Natural,pk=pk)
	return render(request, 'personas_juridicas/eliminar_contacto.html', {'object': c})