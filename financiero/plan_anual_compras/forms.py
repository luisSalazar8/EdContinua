from django import forms
from .models import PlanAnualCompras, Partida
from datetime import date


def year_choices():
    return [(r, r) for r in range(1995, date.today().year+1)]


class PlanAnualComprasForm(forms.ModelForm):
    class Meta:
        model = PlanAnualCompras
        fields = '__all__'
        labels = {
            "codigo": "Código",
            "centro_costos": "Centro de Costos",
            "partida": "Partida Presupuestaria",
            "tipo_compra": "Tipo de Compra",
            "producto": "Descripción",
            "cantidad_anual": "Cantidad Anual",
            "unidad_medida": "Unidad de medida",
            "costo_unitario": "Costo Unitario",
            "subtotal": "Subtotal",
            "total": "Valor total",
            "fecha": "",
            "estado": "",
        }
        widgets = {
            "fecha": forms.DateInput(attrs={'readonly': True, 'class': 'form-control', "type": "date", "value": date.today}),
            "motivo_anular": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "fecha_envio": forms.HiddenInput(),
            "fecha_aprobado": forms.HiddenInput(),
            "año": forms.Select(choices=year_choices()),
            "estado": forms.TextInput(attrs={"readonly": True}),
        }

class PlanAnualComprasUpdateForm(forms.ModelForm):
    class Meta:
        model = PlanAnualCompras
        fields = '__all__'
        labels = {
            "codigo": "Código",
            "centro_costos": "Centro de Costos",
            "partida": "Partida Presupuestaria",
            "tipo_compra": "Tipo de Compra",
            "producto": "Descripción",
            "cantidad_anual": "Cantidad Anual",
            "unidad_medida": "Unidad de medida",
            "costo_unitario": "Costo Unitario",
            "subtotal": "Subtotal",
            "total": "Valor total",
            "fecha": "",
            "estado": "",
        }
        widgets = {
            "fecha": forms.DateInput(attrs={'readonly': True, 'class': 'form-control', "type": "date"}),
            "motivo_anular": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "fecha_envio": forms.HiddenInput(),
            "fecha_aprobado": forms.HiddenInput(),
            "año": forms.Select(attrs={'disabled':True}),
            "estado": forms.TextInput(attrs={"readonly": True}),
            "centro_costo": forms.Select(attrs={"disabled": True}),
        }


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'

        labels = {
            "codigo": "Código",
            "centro_costos": "Centro de Costos",
            "partida": "Partida Presupuestaria",
            "tipo_compra": "Tipo de Compra",
            "producto": "Descripción",
            "cantidad_anual": "Cantidad Anual",
            "unidad_medida": "Unidad de medida",
            "costo_unitario": "Costo Unitario",
            "subtotal": "Subtotal",
            "total": "Valor total",
        }

        widgets = {
            "pac": forms.HiddenInput(),
            "codigo": forms.Select(attrs={'class': 'form-control select2'}),
            "partida": forms.Select(attrs={'class': 'form-control select2'}),
            "unidad_medida": forms.TextInput(attrs={'readonly':True}),
			"costo_unitario":forms.NumberInput(attrs={'readonly':True}),
			"subtotal": forms.NumberInput(attrs={'readonly':True}),
			"iva":forms.CheckboxInput(attrs={'disabled':True}),
            "total": forms.NumberInput(attrs={'readonly':True}),
            "producto": forms.Select(attrs={"class": "select2"}),
        }
