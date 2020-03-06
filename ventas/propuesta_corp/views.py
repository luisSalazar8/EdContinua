from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import PropuestaCorporativo, PropuestaFile
from .forms import PropuestaCorporativoForm, FileForm, FileFormset, PropuestaCorporativoUpdateForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from ventas.reporte_contacto.models import ReporteContacto
from django.db.models import Q
from dal import autocomplete
from datetime import date
from .filters import PropuestaCorporativoFilter
from django.db import transaction

def propuesta_list(request):
    f = PropuestaCorporativoFilter(request.GET, queryset=PropuestaCorporativo.objects.all().order_by('cod_propuesta', 'version'))
    return render(request, 'propuesta_corp_list.html', {'filter': f})

# class PropuestaCorporativoCreate(CreateView):
#     model=PropuestaCorporativo
#     form_class=PropuestaCorporativoForm
#     form_class2= FileForm
#    #form_classes = {'propuesta': PropuestaCorporativoForm,
#    #                 'anexo': FileForm}
#     template_name='propuesta_corp_form.html'
#     success_url=reverse_lazy('propuesta_corporativa')
    
#     def get_context_data(self, **kwargs):
#         data = super(PropuestaCorporativoCreate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['formset'] = FileFormset(self.request.POST,self.request.FILES)
#         else:
#             data['formset'] = FileFormset()
#         return data
    
#     def post(self, request,*args, **kwargs):
        
#         self.object=self.get_object
#         #form=self.form_class(request.POST, request.FILES)
#         propuestaform = PropuestaCorporativoForm(request.POST)
#         formset = FileFormset(request.POST, request.FILES)
#         #if form.is_valid():
#         if propuestaform.is_valid() and formset.is_valid():
#             print("entro doble")
#             try:
#                 cod = PropuestaCorporativo.objects.all().order_by('cod_propuesta').latest('cod_propuesta')
#                 print(cod)
#                 datos=cod.cod_propuesta.split("-")
#                 codant=datos[2]
#                 pre=int(codant)+1
#                 print(pre)
#                 sec = '0'*(4-len(str(pre)))+str(pre)
#                 #pre = str(int(self.model.objects.latest('pk').pk+1))
#                 #sec = '0'*(4-len(pre))+pre
                
#             except self.model.DoesNotExist:
#                 sec = '0001'
#             propuestaform.instance.cod_propuesta = 'PRO-CEC-'+sec+'-'+str(date.today().year)
#             #form.save()
#             propuesta = propuestaform.save()
#             for form in formset:
#                 # so that `book` instance can be attached.
#                 print(form.instance.file)
#                 if(form.instance.file!=None):
#                     file = form.save(commit=False)
#                     file.propuesta = propuesta
#                     file.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             user_form = self.form_class(None)
#             formset= FileFormset(queryset=PropuestaFile.objects.none())
#             #return self.render_to_response(self.get_context_data(form=form))
#             return render(request, 'propuesta_corp_form.html', {'form': propuestaform, 'formset': formset})

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
        if self.request.POST:
            data['formset'] = FileFormset(self.request.POST,self.request.FILES)
        else:
            data['formset'] =FileFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['formset']
        
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
        form.instance.cod_propuesta = 'PRO-CEC-'+sec+'-'+str(date.today().year)

        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(PropuestaCorporativoCreate, self).form_valid(form)

    def get_success_url(self):
        return self.success_url


class PropuestaCorporativoUpdate(UpdateView):
    model=PropuestaCorporativo
    form_class=PropuestaCorporativoUpdateForm
    template_name='propuesta_corp_edit.html'
    success_url=reverse_lazy('propuesta_corporativa')
    formset_class=FileFormset
    def get_context_data(self, **kwargs):
        context =super(PropuestaCorporativoUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            print("entro post")
            context['formset'] = FileFormset(self.request.POST, self.request.FILES,instance=self.object)
        else:
            print("entro get")
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
            print(context)
        return context

    def post(self, request, *args, **kwargs):
        print("lol")
        self.object=self.get_object()
        
        form=self.form_class(request.POST)
        pk=self.kwargs.get('pk',0)
        print(pk)
        formset = FileFormset(request.POST, request.FILES,instance=self.object)
        
        if form.is_valid():
            prop= self.model.objects.get(pk=pk)
            print(prop.active)
            print(prop.version)
            print(form.instance.version)
            if prop.version!=form.instance.version:
                print("diferente version")
                prop.active=False
                prop.save()
                newprop=form.save()
                if formset.is_valid():
                    nel=[]
                    for obj in formset.deleted_forms:
                        nel.append(obj.instance.file)
                    print(nel)
                    for f in formset :
                        if(f.instance.file!=None):
                            if not(f.instance.file in nel):
                                print(f.instance.file)
                                #newf=PropuestaFile.objects.create(file=f.instance.file,propuesta=newprop)
                                fileobject=f.instance.file
                                fs=FileSystemStorage()
                                filename=fs.save(fileobject.name,fileobject)
                                fs.url(filename)
                                fileobject.name=filename
                                # name=fileobject.name.split(".")
                                # newname=name[0]+"_"+str(PropuestaFile.objects.all().latest("file").id)+"."+name[len(name)-1]
                                # fileobject.name=newname
                                
                                newf = PropuestaFile(file=fileobject,propuesta=newprop)
                                newf.save()
                                #formset.instance = newprop
                                #formset.save()
            else :
                print("igual version")
                formr = self.form_class(request.POST or None,request.FILES, instance=prop)
                formr.save()
                if formset.is_valid():
                     formset.instance = self.object
                     formset.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

# class PropuestaCorporativoUpdate(UpdateView):
#     model = PropuestaCorporativo
#     template_name = 'propuesta_corp_form.html'
#     form_class = PropuestaCorporativoUpdateForm
#     success_url = reverse_lazy('propuesta_corporativa')

#     def get_context_data(self, **kwargs):
#         data = super(PropuestaCorporativoUpdate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             print("entro")
#             data['formset'] = FileFormset(self.request.POST, self.request.FILES,instance=self.object)
#         else:
            
#             pk=self.kwargs.get('pk',0) 
#             l=[]
#             vals=str(self.model.objects.get(pk=pk).servicios_incluidos).split(',')
#             print(vals)
#             for s in self.model.SERVICIOS_CHOICES:
#                 print(s)
#                 if s[1] in vals or ' '+s[1] in vals:
#                     print(s[1])
#                     l.append(s[0])
#             print(l)
#             data['checked_servicios_incluidos']=l
#             data['formset'] =FileFormset(instance=self.object)
#         return data

#     def form_valid(self, form):
#         context = self.get_context_data()
#         titles = context['formset']
#         pk=self.kwargs.get('pk',0)
#         print(pk)
#         prop= self.model.objects.get(pk=pk)
#         print(prop.version)
#         with transaction.atomic():
#             if prop.version!=form.instance.version:
#                 print("diferentes versiones")
#             else :
#                 print("mismas versiones")
#                 form.instance.created_by = self.request.user    
#                 self.object = form.save()
#                 if titles.is_valid():
#                     titles.instance = self.object
#                     titles.save()
#         return super(PropuestaCorporativoUpdate, self).form_valid(form)

#     def get_success_url(self):
#         return self.success_url

# class PropuestaCorporativoUpdate(UpdateView):
#     model=PropuestaCorporativo
#     form_class=PropuestaCorporativoUpdateForm
#     template_name='propuesta_corp_form.html'
#     success_url=reverse_lazy('propuesta_corporativa')
#     formset_class=FileFormset
#     def get_context_data(self, **kwargs):
#         data = super(PropuestaCorporativoUpdate, self).get_context_data(**kwargs)
#         if self.request.POST:
#             print("entro post")
#             prueba= FileFormset(self.request.POST)
#             data['formset'] = FileFormset(self.request.POST,instance=self.object)
#             titles = data['formset']
#             print("nueva data")
#             for formf in prueba:
#                     print(formf.instance.file)
#         else:
#             print("entro get")
#             pk=self.kwargs.get('pk',0) 
#             l=[]
#             vals=str(self.model.objects.get(pk=pk).servicios_incluidos).split(',')
#             print(vals)
#             for s in self.model.SERVICIOS_CHOICES:
#                 print(s)
#                 if s[1] in vals or ' '+s[1] in vals:
#                     print(s[1])
#                     l.append(s[0])
#             print(l)
#             data['checked_servicios_incluidos']=l
#             data['formset'] =FileFormset(instance=self.object)
#             titles = data['formset']
#             for formf in titles:
#                     print(formf.instance.file)

#         return data

#     def form_valid(self, form):
#         context = self.get_context_data()
#         titles = context['formset']
#         print("entro form")
#         with transaction.atomic():
#             form.instance.created_by = self.request.user
#             self.object = form.save()
#             if titles.is_valid():
#                 titles.instance = self.object
#                 titles.save()
#         return super(PropuestaCorporativoUpdate, self).form_valid(form)

#     def get_success_url(self):
#         return self.success_url


    

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
