from django import forms
from .models import Proforma
from dal import autocomplete
from ventas.validaciones import validate_porcentaje, validate_positive, validate_anexo_corp

class ProformaForm(forms.ModelForm):

	class Meta:
		model=Proforma

		fields=[
			'codigo',
			'tipo_cliente',
			'ruc_ci',
            'razon_nombres',
			'version',
			'nombreProforma',
			'tipoEmpresa',
			'sector',
			'fechaSolicitud',
			'fechaEnvio',
			'numeroParticipantes',
			'horas',
			'cantidadCursos',
			'estado',
			'porcentExito',
			'porcentDesc',
			'montoProforma',
			'montoDesc',
			'observacion',
			'anexos',
			'nombre',
			'fechaRespuesta',
			'montoAceptado',
			'montoEjecutado',
			'montoPorEjecutarse',
		]

		labels={
			'codigo': 'Código',
			'tipo_cliente': 'Cliente',
			'ruc_ci': 'RUC',
            'razon_nombres': 'Razón social',
			'version':'Versión',
			'nombreProforma':'Nombre',
			'tipoEmpresa':'Tipo Empresa',
			'sector':'Sector',
			'fechaSolicitud':'Fecha Solicitud',
			'fechaEnvio':'Fecha Envío',
			'numeroParticipantes':'Número Participantes',
			'horas':'Total Horas',
			'cantidadCursos':'Cantidad Cursos',
			'estado':'Estado',
			'porcentExito':"% Éxito",
			'porcentDesc':"% Descuento",
			'montoProforma':'Monto Proforma',
			'montoDesc':'Monto Descuento',
			'observacion':'Observación',
			'anexos':'Anexos',
			'nombre':'Nombre',
			'fechaRespuesta':'Fecha Respuesta',
			'montoAceptado':'Monto Aceptado',
			'montoEjecutado':'Monto Ejecutado',
			'montoPorEjecutarse':'Monto por Ejecutarse',

		}

		widgets={
			'codigo': forms.TextInput(attrs={'class':'form-control'}),
			'version': forms.NumberInput(attrs={'class':'form-control','min': 0}),
			'nombreProforma': forms.TextInput(attrs={'class':'form-control'}),
			'fechaSolicitud': forms.DateInput(attrs={'class':'form-control',"type":"date"}),
			'fechaEnvio':forms.DateInput(attrs={'class':'form-control',"type":"date"}),
			'numeroParticipantes': forms.NumberInput(attrs={'class':'form-control'}),
			'horas': forms.NumberInput(attrs={'class':'form-control'}),
			'cantidadCursos': forms.NumberInput(attrs={'class':'form-control'}),
			'estado':forms.Select(choices=[(None,"---------"),("Aceptada","Aceptada"),
				("No aceptada","No aceptada"), ("Seguimiento","Seguimiento") ,("Por Enviar","Por Enviar")],
				attrs={'class':'form-control', "id":"seleccion","onchange":"run()"}),
			'porcentExito': forms.NumberInput(attrs={'class':'form-control','min': 0, 'max': 100}),
			'porcentDesc': forms.NumberInput(attrs={'class':'form-control','min': 0, 'max': 100}),
			'montoProforma': forms.NumberInput(attrs={'class':'form-control','min': 0}),
			'montoDesc': forms.NumberInput(attrs={'class':'form-control','min': 0}),
			'observacion': forms.Textarea(attrs={'class':'form-control', 'rows':2}),
			'anexos': forms.ClearableFileInput(attrs={'class':'form-control','multiple': True}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'fechaRespuesta': forms.DateInput(attrs={'class':'form-control',"type":"date"}),
			'montoAceptado': forms.NumberInput(attrs={'class':'form-control','min': 0}),
			'montoEjecutado': forms.NumberInput(attrs={'class':'form-control','min': 0}),
			'montoPorEjecutarse': forms.NumberInput(attrs={'class':'form-control','min': 0}),
			'razon_nombres': forms.Select(attrs={'class': 'form-control select2'}),
            'ruc_ci': forms.Select(attrs={'class': 'form-control select2'}),
		}


	def clean_porcentExito(self):
		exito = self.cleaned_data["porcentExito"]
		return validate_porcentaje(exito)
	
	def clean_porcentDesc(self):
		desc = self.cleaned_data["porcentDesc"]
		return validate_porcentaje(desc)