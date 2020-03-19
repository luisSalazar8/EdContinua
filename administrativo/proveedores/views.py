from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Proveedor
from .models import Ciudad
from .models import Sector
from .models import TipoEmpresa
from django.core.exceptions import ValidationError
#Forms
from .forms import *


from dal import autocomplete

#Itertools
from itertools import chain

from django.core.paginator import Paginator



# Create your views here.

def index_proveedores(request):
	proveedores_list = Proveedor.objects.all().order_by("pk")
	filter = ProveedorFilter(request.GET, queryset=proveedores_list )
	paginator = Paginator(filter.qs, 30) 
	page = request.GET.get('page')
	proveedores = paginator.get_page(page)
	return render(request, 'index.html', {'proveedores': proveedores, "filter":filter})

	
def load_ciudades(request):
	provincia_id = request.GET.get("provincia")
	ciudades = Ciudad.objects.filter(provincia_id=provincia_id).order_by('nombre')
	
	return render(request,"proveedores/dropdown_ciudades.html",{"ciudades":ciudades})

def proveedores_view(request):

	if(request.method == "POST"):
		form = ProveedorForm(request.POST)
		if(form.is_valid()):
			print("Acabo de entrar al post")
			form.save()
			ruc = form.cleaned_data["ruc"]
			url = reverse_lazy('', kwargs={'pk': ruc})
			return HttpResponseRedirect(url)
	else:
		form = ProveedorForm()
	return render(request,"forma.html", {"form":form})








# class proveedores_editar(UpdateView):
# 	model = Proveedor
# 	form_class = ProveedorForm
# 	template_name = 'proveedores/editar_forma.html'
# 	success_url = reverse_lazy('')





def proveedores_editar(request,pk):
	if(request.method == "POST"):
				if(form.is_valid()):
					pase = False
					if(pase):
						form.save()
						return HttpResponseRedirect(reverse_lazy("index_proveedores"))
				else:
					url = reverse_lazy('proveedores_editar', kwargs={'pk': pk})
					return HttpResponseRedirect(url)
			
	else:
		p = get_object_or_404(Proveedor, pk=pk)
		form = ProveedorForm(instance=p)
	return render(request, 'proveedores/editar_forma.html')






# def proveedores_eliminar(request,pk=None):
# 	if(request.method == "POST"):
# 		print("Si entre we al post de proveedores eliminar")
# 		p = get_object_or_404(Proveedor,pk=pk)
# 		p.delete()
# 		return redirect("index_proveedores")
# 	else:
# 		pk= request.GET.get('pk')
# 		if len(pk)<13:
# 			pk="0"+str(pk)
# 		p = get_object_or_404(Proveedor,pk=pk)
# 		return render(request, 'proveedores/eliminar.html', {'object': p})

