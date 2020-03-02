from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Juridica
from .models import Ciudad
from .models import Sector
from .models import TipoEmpresa
from .models import Contacto_natural
#Forms
from .forms import *
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
	#naturales_list = Persona_Natural.objects.all().order_by("pk")
	filter = JuridicaFilter(request.GET, queryset=juridicas_list )
	#filter2 = forms.Contacto_Filter(request.GET)
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
		form = JuridicaForm(request.POST)
		if(form.is_valid()):
			form.save()
			ruc = form.cleaned_data["ruc"]
			url = reverse_lazy('editar_juridica', kwargs={'pk': ruc})
			return HttpResponseRedirect(url)
	else:
		form = JuridicaForm()
	return render(request,"personas_juridicas/forma.html", {"form":form})



def juridicas_editar(request,pk):
	if(request.method == "POST"):
		if("eliminar_contacto" not in request.POST):
				print(request.POST)
				p = get_object_or_404(Juridica, pk=pk)
				final = Persona_Natural.objects.filter(contacto_natural__empresa = pk)
				form = JuridicaForm(request.POST,instance=p)
				form_contacto = OrdenFacturacionForm()
				form_cedulas = Contacto_Natural_Form()
				if(form.is_valid()):
					pase = False
					##PROBAR QUE SI ESTEN BIEN LOS CONTACTOS
					cedulas_post = []
					cedulas_modelo = []
					for i in request.POST:
						if "extra_field" in i and request.POST[i] not in cedulas_post:
							cedulas_post.append(request.POST[i])
					if len(cedulas_post) == 0:
						pase = True
					else:
						for i in cedulas_post:
							try:
								c = get_object_or_404(Persona_Natural, cedula=i)
								p.contacto_natural_set.create(contacto = c)
								pase = True
							except:
								form_contacto = OrdenFacturacionForm(request.POST)
								form_contacto.add_error("ruc_ci",forms.ValidationError("Problemas con " + str(i) + " Dicho contacto ya pertenece a otra persona juridica"))
								pase = False
					
					# contactos_empresa = Contacto_natural.objects.filter(empresa = pk)
					
					# if(len(contactos_empresa)!=0):
					# 	for i in contactos_empresa:
					# 		cedulas_modelo.append(i.contacto.cedula)
					
					# for i in cedulas_post:
					# 		if i not in cedulas_modelo:
					# 			try:
					# 				c = get_object_or_404(Persona_Natural, cedula=i)
					# 				p.contacto_natural_set.create(contacto = c)
					# 			except:
					# 				form_contacto.add_error("ruc_ci",forms.ValidationError("No we"))



					# for i in cedulas_post:
					# 	if i not in cedulas_modelo:
					# 		p.contacto_natural_set.create(contacto = i)
						


					# for i in request.POST:
					# 	if "cedula" in i:
					# 		cedulas_post.append(request.POST[i] )
					# cedulas_contactos = Contacto_natural.objects.filter(empresa = pk)
					# for i in cedulas_contactos:
					# 	cedulas_modelo.append(i.contacto)
					# for i in cedulas_post:
					# 	if i not in cedulas_modelo:
					# 		p.contacto_natural_set.create(contacto = i )	
					if(pase):
						form.save()
						return HttpResponseRedirect(reverse_lazy("index_juridicas"))
		else:
			c = get_object_or_404(Contacto_natural,contacto=request.POST.get("eliminar_contacto"))
			c.delete()
			url = reverse_lazy('editar_juridica', kwargs={'pk': pk})
			return HttpResponseRedirect(url)
			
	else:
		final = Persona_Natural.objects.filter(contacto_natural__empresa = pk)
		p = get_object_or_404(Juridica, pk=pk)
		form = JuridicaForm(instance=p)
		form_contacto = OrdenFacturacionForm()
		form_cedulas = Contacto_Natural_Form()
	return render(request, 'personas_juridicas/editar_forma.html', {'form_cedulas':form_cedulas,'form': form,"form_contacto":form_contacto,"naturales":final})


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