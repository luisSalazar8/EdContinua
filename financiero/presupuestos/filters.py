from .models import PresupuestoEvento, ESTADO_CHOICES, Juridica, TIPO_CHOICES, Centro_Costos
import django_filters
from django import forms
from dal import autocomplete


class PresupuestoEventoFilter(django_filters.FilterSet):
    all_Juridica=Juridica.objects.all()
    codigo = django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'Código orden'}))
    codigo_propuesta = django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'Código Propuesta'}))
    # evento__nombre=django_filters.CharFilter(lookup_expr='icontains', label="",widget=forms.TextInput(attrs={'placeholder':'Nombre evento'}))
    # evento__cod=django_filters.CharFilter(lookup_expr='icontains', label="",widget=forms.TextInput(attrs={'placeholder':'Nombre evento'}))
    fecha=django_filters.DateFilter(field_name='fecha', label='',widget=forms.DateInput(attrs={'placeholder':'Fecha','type':'date'}))

    # razon_nombres=django_filters.ModelChoiceFilter(
    #     label="",
    #     queryset=Juridica.objects.all(),
    #     #choices=all_Juridica.values_list('pk','nombre'),
    #     widget=autocomplete.ModelSelect2(url="empresa-autocomplete")
    # )
    centro_costos=django_filters.ChoiceFilter(
        label="",
        choices=Centro_Costos.objects.all().values_list('pk','nombre'),
        empty_label="Centro Costos"
    )
    razon_nombres=django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'Razón Social'}))
    ruc_ci=django_filters.CharFilter(lookup_expr='icontains', label="", widget=forms.TextInput(attrs={'placeholder':'RUC'}))

    estado = django_filters.ChoiceFilter(
        empty_label='Estado',
		choices=ESTADO_CHOICES,
        label=""
    )
    tipo = django_filters.ChoiceFilter(
        empty_label='Tipo',
        label="",
        choices=TIPO_CHOICES
    )

    class Meta:
        model = PresupuestoEvento
        
        fields=[
            'tipo',
            'codigo',
            'fecha',
            'razon_nombres',
            'ruc_ci',
            'estado',
            'codigo_propuesta',
            'centro_costos',
        ]
