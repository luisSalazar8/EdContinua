from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import PropuestaCorporativo, PropuestaFile
from .forms import PropuestaCorporativoForm, FileForm, FileFormset
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from ventas.reporte_contacto.models import ReporteContacto
from django.db.models import Q
from dal import autocomplete
from datetime import date
from .filters import PropuestaCorporativoFilter

def propuesta_list(request):
    f = PropuestaCorporativoFilter(request.GET, queryset=PropuestaCorporativo.objects.all().order_by('cod_propuesta', 'version'))
    return render(request, 'propuesta_corp_list.html', {'filter': f})

class PropuestaCorporativoCreate(CreateView):
    model=PropuestaCorporativo
    form_class=PropuestaCorporativoForm
    form_class2= FileForm
   #form_classes = {'propuesta': PropuestaCorporativoForm,
   #                 'anexo': FileForm}
    template_name='propuesta_corp_form.html'
    success_url=reverse_lazy('propuesta_corporativa')
    
    def get_context_data(self, **kwargs):
        data = super(PropuestaCorporativoCreate, self).get_context_data(**kwargs)
        data['formset'] = FileFormset()
        return data


    def post(self, request,*args, **kwargs):
        
        self.object=self.get_object
        #form=self.form_class(request.POST, request.FILES)
        propuestaform = PropuestaCorporativoForm(request.POST)
        formset = FileFormset(request.POST, request.FILES)
        #if form.is_valid():
        if propuestaform.is_valid() and formset.is_valid():
            print("entro doble")
            try:
                cod = PropuestaCorporativo.objects.all().order_by('cod_propuesta').latest('cod_propuesta')
                print(cod)
                datos=cod.cod_propuesta.split("-")
                codant=datos[2]
                pre=int(codant)+1
                print(pre)
                sec = '0'*(4-len(str(pre)))+str(pre)
                #pre = str(int(self.model.objects.latest('pk').pk+1))
                #sec = '0'*(4-len(pre))+pre
                
            except self.model.DoesNotExist:
                sec = '0001'
            propuestaform.instance.cod_propuesta = 'PRO-CEC-'+sec+'-'+str(date.today().year)
            #form.save()
            propuesta = propuestaform.save()
            for form in formset:
                # so that `book` instance can be attached.
                print(form)
                if(form.instance.file!=None):
                    file = form.save(commit=False)
                    file.propuesta = propuesta
                    file.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            user_form = self.form_class(None)
            formset= FileFormset(queryset=PropuestaFile.objects.none())
            #return self.render_to_response(self.get_context_data(form=form))
            return render(request, 'propuesta_corp_form.html', {'form': propuestaform, 'formset': formset})


class PropuestaCorporativoUpdate(UpdateView):
    model=PropuestaCorporativo
    form_class=PropuestaCorporativoForm
    template_name='propuesta_corp_form.html'
    success_url=reverse_lazy('propuesta_corporativa')
    formset_class=FileFormset
    def get_context_data(self, **kwargs):
        if self.request.POST:
            console.log("post")
        context =super(PropuestaCorporativoUpdate, self).get_context_data(**kwargs)
        #context['form'] = self.form_class(instance=self.object)
        
        pk=self.kwargs.get('pk',0)

        l=[]
        vals=str(self.model.objects.get(pk=pk).servicios_incluidos).split(',')
        print(vals)
        for s in self.model.SERVICIOS_CHOICES:
            print(s)
            if s[1] in vals or ' '+s[1] in vals:
                print(s[1])
                l.append(s[0])
        print(l)
        context['checked_servicios_incluidos']=l
        context['formset'] = FileFormset(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        print("lol")
        self.object=self.get_object()
        form=self.form_class(request.POST, request.FILES)
        
        formset = FileFormset(request.POST, request.FILES, instance=form.instance)
        
        if form.is_valid():
            pk=self.kwargs.get('pk',0)
            form.instance.version= self.model.objects.get(pk=pk).version+1
            #form.save()
            for form in formset:
                # so that `book` instance can be attached.
                print("new")
                print(form)
                
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class PropuestaCorporativoDelete(DeleteView):
    model=PropuestaCorporativo
    template_name='propuesta_corp_delete.html'
    form_class=PropuestaCorporativoForm
    success_url=reverse_lazy('propuesta_corporativa')

'''  def get_context_data(self, **kwargs):
        print("vera")
        #print(PropuestaFile.objects.all().latest('file').file)
        for i in PropuestaFile.objects.all():
            print(i.propuesta)
            print(i.file)
            
        context =super(PropuestaCorporativoUpdate, self).get_context_data(**kwargs)
        print(context)
        pk=self.kwargs.get('pk',0)
        l=[]
        vals=str(self.model.objects.get(pk=pk).servicios_incluidos).split(',')
        print(vals)
        for s in self.model.SERVICIOS_CHOICES:
            print(s)
            if s[1] in vals or ' '+s[1] in vals:
                print(s[1])
                l.append(s[0])
        print(l)
        context['checked_servicios_incluidos']=l
        return context'''
