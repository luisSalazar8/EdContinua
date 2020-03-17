from .models import OrdenIngreso,OrdenFacturacion
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
    fecha=django_filters.DateFilter(widget=forms.DateInput(attrs={'placeholder':'Fecha de Orden Ingreso',"class":"textbox-n", "onfocus":"(this.type='date')","onfocusout":"(this.type='text')"}))
    n_tramite = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'N° Tramite '}))
    ruc_ci = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'RUC - CI'}))
    razon_nombres = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Nombre - Razón Social'}))
    formaPago = django_filters.ChoiceFilter(label="", empty_label="Forma de pago",choices = OrdenIngreso.FORMAS_PAGO)
    estado = django_filters.ChoiceFilter(label="", empty_label="Estado Orden Ingreso",choices = OrdenIngreso.ESTADO_CHOICES)
    fecha_anulacion = django_filters.DateFilter(widget=forms.DateInput(attrs={'placeholder':'Fecha de anulación',"class":"textbox-n", "onfocus":"(this.type='date')","onfocusout":"(this.type='text')"}))

    orden_facturacion__cod_orden_fact = django_filters.CharFilter(label="", widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Código Orden Facturación '}))

    # def __init__(self, *args, **kwargs):
    #     argumentos = 0
    #     if (kwargs['data']):
    #         for i in kwargs['data']:
    #             if kwargs['data'][i] != "":
    #                argumentos+=1
    #     if(argumentos>1):
    #         kwargs['queryset']=OrdenIngreso.objects.filter(orden_facturacion__estado='PNDP').order_by('cod_orden_ing')
                
    #     super().__init__(*args, **kwargs)
        
       
        
        
      