from django import forms
from .models import *

class InteresadoForm(forms.ModelForm):
	class Meta:
		model = Interesado
		fields = "__all__"
		widgets={
           
            'motivo_interes':forms.Textarea(attrs={'rows':5,"overflow-y": "scroll"}),
           
           
        }


class InteresadoCargarForm(forms.Form):
	archivo = forms.FileField(label="Archivo a cargar")
	
		