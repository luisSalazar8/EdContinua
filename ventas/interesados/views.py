from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from datetime import date
import threading
import queue
import os
# Create your views here.



class InteresadoCreate(CreateView):
	model=Interesado
	form_class=InteresadoForm
	template_name='interesado_form.html'
	success_url=reverse_lazy('interesados')

	def get_success_url(self, **kwargs):
			return reverse_lazy('interesados')


class InteresadoUpdate(UpdateView):
	model=Interesado
	form_class=InteresadoForm
	template_name='interesados_editar.html'
	success_url=reverse_lazy('interesados')

class InteresadoDelete(DeleteView):
	model=Interesado
	template_name='interesado_eliminar.html'
	success_url=reverse_lazy('interesados')
def interesado_conf_elim(request):

	interesado_id=request.GET.get('pk')
	interesado=Interesado.objects.get(pk=interesado_id)
	return render(request,"interesado_eliminar.html",{"interesado":interesado})
def cargar_personas_thread(f,q):
	if(f==None and f.lower().find(".csv")==-1):
		return
	fi = open(f,"r")
	c=0
	for line in fi:
		data = line.strip().split(",")
		if(len(data)==5):
			interesado = Interesado()
			interesado.nombre=data[0]
			interesado.apellido = data[1]
			interesado.celular = data[3]
			interesado.correo = data[2]
			try:
				interesado.canal_de_contacto = CanalContacto.objects.get(nombre=data[4])
				interesado.save()
				c+=1
			except:
				c+=1
				q.put(c)
				pass
	q.put(c)
	q.put("fin")		
	fi.close()
	os.remove(f)
def handle_uploaded_file(f):
	# _file = 'media/uploads/carga/'+str(f)
	_file = str(f)

	# if(os.path.isfile(_file)):
	# 	import random
	# 	_file='media/uploads/carga/'+str(random.randint(0,1000))+str(f)
	with open(_file, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	valores_retorno = queue.Queue()
	t = threading.Thread(target=cargar_personas_thread,
							 args=(_file,valores_retorno))
	t.setDaemon(True)
	t.start()
	lineas =[]
	for valores in iter(valores_retorno.get, "fin"):
		lineas.append(valores)
	return lineas
	

def cargar_interesados(request):
	if request.method == 'POST':
		form = InteresadoCargarForm(request.POST, request.FILES)
		if form.is_valid():
			errores = handle_uploaded_file(request.FILES['archivo'])
			if(len(errores)==1):
				return HttpResponseRedirect(reverse_lazy('interesados'))
			else:
				cantidad_errores = len(errores)-1
				cantidad_filas = errores[-1]
				for i in range(cantidad_errores):
					error ="Problema en la linea " + str(errores[i]) + ": El canal de contacto no es el correcto o dicho interesado ya existe"
					form.add_error("archivo",forms.ValidationError(error))
				if(cantidad_errores!= cantidad_filas):
					form.add_error("archivo",forms.ValidationError("El resto de interesados fueron creados exitosamente"))
		

	else:
		form = InteresadoCargarForm()
	return render(request, 'interesados_cargar.html', {'form': form})
