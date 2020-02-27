from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import PropuestaCorporativo
from .forms import PropuestaCorporativoForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from ventas.reporte_contacto.models import ReporteContacto
from django.db.models import Q
from dal import autocomplete
from datetime import date
from .filters import PropuestaCorporativoFilter

def propuesta_list(request):
    f = PropuestaCorporativoFilter(request.GET, queryset=PropuestaCorporativo.objects.all().order_by('cod_propuesta'))
    return render(request, 'propuesta_corp_list.html', {'filter': f})

class PropuestaCorporativoCreate(CreateView):
    model=PropuestaCorporativo
    form_class=PropuestaCorporativoForm
    template_name='propuesta_corp_form.html'
    success_url=reverse_lazy('propuesta_corporativa')

    def post(self, request,*args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST, request.FILES)
        print("yep")
        print(form.instance.ruc_ci)
        if form.is_valid():
            try:
                pre = str(int(self.model.objects.latest('pk').pk+1))
                sec = '0'*(4-len(pre))+pre
            except self.model.DoesNotExist:
                sec = '0001'
            form.instance.cod_propuesta = 'PRO-CEC-'+sec+'-'+str(date.today().year)
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            print("no fue valida")
            return self.render_to_response(self.get_context_data(form=form))


class PropuestaCorporativoUpdate(UpdateView):
    model=PropuestaCorporativo
    form_class=PropuestaCorporativoForm
    template_name='propuesta_corp_form.html'
    success_url=reverse_lazy('propuesta_corporativa')

    def get_context_data(self, **kwargs):
        context =super(PropuestaCorporativoUpdate, self).get_context_data(**kwargs)
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
        return context

    def post(self, request, *args, **kwargs):
        print("lol")
        self.object=self.get_object
        form=self.form_class(request.POST, request.FILES)
        if form.is_valid():
            pk=self.kwargs.get('pk',0)
            form.instance.version= self.model.objects.get(pk=pk).version+1
            form.save()
            
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class PropuestaCorporativoDelete(DeleteView):
    model=PropuestaCorporativo
    template_name='propuesta_corp_delete.html'
    form_class=PropuestaCorporativoForm
    success_url=reverse_lazy('propuesta_corporativa')