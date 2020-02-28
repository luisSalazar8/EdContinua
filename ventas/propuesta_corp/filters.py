from .models import PropuestaCorporativo
from ventas.personas_juridicas.models import Juridica
import django_filters
from django import forms


class PropuestaCorporativoFilter(django_filters.FilterSet):
    ESTADO_CHOICES= [('SG','Seguimiento'),('PD','Pendiente'),('ACP','Aceptada'),('NACP','No aceptada'),]
    """empresa_nombre=django_filters.CharFilter(lookup_expr='icontains',label='Empresa')"""
    
    estado = django_filters.ChoiceFilter(label="", empty_label="Estado", choices=ESTADO_CHOICES)
    cod_propuesta = django_filters.CharFilter(lookup_expr='icontains', label='', widget=forms.TextInput(attrs={'placeholder': 'Código de Propuesta'}))
    ruc_ci = django_filters.CharFilter(label='', widget=forms.TextInput(attrs={'placeholder': 'RUC'}))
    razon_nombres = django_filters.CharFilter(label='', widget=forms.TextInput(attrs={'placeholder': 'Empresa'}))
    area_capacitacion = django_filters.CharFilter(label='', widget=forms.TextInput(attrs={'placeholder': 'Área de capacitación '}))
    asesor = django_filters.CharFilter(label='', widget=forms.TextInput(attrs={'placeholder': 'Asesor'}))
    class Meta:
        model = PropuestaCorporativo
        
        fields=[
            'estado',
            'cod_propuesta',
            'razon_nombres',
            'ruc_ci',
            'area_capacitacion',
            'asesor'
        ]
