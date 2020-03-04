from .models import PresupuestoEvento, ESTADO_CHOICES, Juridica
import django_filters
from django import forms


class PresupuestoEventoFilter(django_filters.FilterSet):
    codigo = django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'Código orden'}))
    # evento__nombre=django_filters.CharFilter(lookup_expr='icontains', label="",widget=forms.TextInput(attrs={'placeholder':'Nombre evento'}))
    # evento__cod=django_filters.CharFilter(lookup_expr='icontains', label="",widget=forms.TextInput(attrs={'placeholder':'Nombre evento'}))
    fecha=django_filters.DateFilter(field_name='fecha', label='',widget=forms.DateInput(attrs={'placeholder':'Fecha','type':'date'}))
    empresa=django_filters.ChoiceFilter(
        empty_label='RUC o Razon Social',
        label="",
        choices=Juridica.objects.all().values_list('pk','nombre'),
        widget=forms.Select(attrs={'class':'select2'}))

    estado = django_filters.ChoiceFilter(
        empty_label='Estado',
		choices=ESTADO_CHOICES,
        label=""
    )
    class Meta:
        model = PresupuestoEvento
        
        fields=[
            'codigo',
            'fecha',
            'empresa',
            'estado'
        ]
