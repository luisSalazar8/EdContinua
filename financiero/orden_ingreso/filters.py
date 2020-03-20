from .models import OrdenIngreso,OrdenFacturacion;
from financiero.orden_facturacion.models import Centro_Costos;
import django_filters
from django import forms



class OrdenIngresoFilter(django_filters.FilterSet):
    class Meta:
        model = OrdenIngreso
        exclude = 'anexo'
    # fecha=django_filters.DateFilter(field_name='fecha', label='Fecha',
    #     widget=forms.DateInput(attrs={"type":"date"}))
    # numeroTramite=django_filters.CharFilter(lookup_expr='icontains',label='Número de Trámite')
    # numeroFactura=django_filters.CharFilter(lookup_expr='icontains',label='Número de Factura')
    # contacto_natural__contacto__cedula = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Cédula Contacto'}))
	# contacto_natural__contacto__celular = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control","type":"number",'placeholder': 'Celular Contacto'}))
	# contacto_natural__contacto__nombres = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Nombres Contacto'}))
	# contacto_natural__contacto__apellidos = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Apellidos Contacto'}))

    cod_orden_ing = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Código Orden Ingreso '}))
    fecha=django_filters.DateFilter(field_name='fecha', label='',widget=forms.DateInput(attrs={'placeholder':'Fecha Orden',"class":"textbox-n", "onfocus":"(this.type='date')"}))

    n_tramite = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'N° Tramite '}))
    ruc_ci = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'RUC - CI'}))
    razon_nombres = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Nombre - Razón Social'}))
    formaPago = django_filters.ChoiceFilter(label="", empty_label="Forma de pago",choices = OrdenIngreso.FORMAS_PAGO)
    estado = django_filters.ChoiceFilter(label="", empty_label="Estado Orden Ingreso",choices = OrdenIngreso.ESTADO_CHOICES)
    fecha_anulacion = django_filters.DateFilter(widget=forms.DateInput(attrs={'placeholder':'Fecha anulación',"class":"textbox-n", "onfocus":"(this.type='date')"}))
    centro_costos = django_filters.ModelChoiceFilter(label="", empty_label="Centro de costos", queryset=Centro_Costos.objects.all())

    orden_facturacion__cod_orden_fact = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Código Orden Facturación '}))

    # def __init__(self, *args, **kwargs):
    #     argumentos = 0
    #     if (kwargs['data']):
    #         for i in kwargs['data']:
    #             if kwargs['data'][i] != "":
    #                argumentos+=1
    #     if(argumentos):
    #         kwargs['queryset']=OrdenIngreso.objects.except(estado='ANLD').order_by('cod_orden_ing')
                
    #     super().__init__(*args, **kwargs)
    def __init__(self, *args, **kwargs):
        
        if (kwargs['data'] and kwargs['data']['estado'] != ""):
            kwargs['queryset']=OrdenIngreso.objects.all().order_by('cod_orden_ing')
        else:
             kwargs['queryset']=OrdenIngreso.objects.exclude(estado='ANLD').order_by('cod_orden_ing')
        
                
        super().__init__(*args, **kwargs)
        
       
        
        
      