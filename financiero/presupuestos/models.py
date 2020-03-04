from django.db import models
from ventas.personas_juridicas.models import Juridica
from financiero.orden_pago.models import Centro_Costos
import financiero.validaciones


class TarifarioDocente(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	
	def __str__(self):
		return self.descripcion

class TarifarioHospedajeAlimentacionDocente(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


class TarifarioHospedajeAlimentacionPersonal(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


class TarifarioServicioAereo(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion

	
class TarifarioInstalacion(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


class TarifarioPlantillaDelPersonal(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


class TarifarioMaterial(models.Model):
	costo_con_iva = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion

class TarifarioServicioAlimentacionAlmuerzo(models.Model):
	incluye_iva = models.BooleanField(default=False)
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion

class TarifarioServicioAlimentacionBreak(models.Model):
	incluye_iva = models.BooleanField(default=False)
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion

class TarifarioPrecio(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


class TarifarioAportacion(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	porcentaje_facultades = models.BooleanField(default=False)
	def __str__(self):
		return self.descripcion


class TarifarioProducto(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


class TarifarioProspecto(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


class TarifarioPublicidad(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


class TarifarioOtroSuministro(models.Model):
	descripcion = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2,validators=[financiero.validaciones.validate_positivo])
	version = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.descripcion


ESTADO_CHOICES = [  
        ('Grabado','Grabado'),
        ('Solicitud Enviada','Solicitud Enviada'),
	    ('Autorizada por Financiero', 'Autorizada por Financiero'),
        ('Anulada','Anulada'),
	]

GENERICO=[
	(0,'No aplica'),
	(100,'Aplica')
]

CARPETA=[
	(0,'No aplica'),
	(1,'Aplica')
]
BLOCK=[
	(0,'No aplica'),
	(2,'Aplica')
]
LAPIZ=[
	(0,'No aplica'),
	(3,'Aplica')
]
PLUMA=[
	(0,'No aplica'),
	(4,'Aplica')
]
CERTIFICADOS=[
	(0,'No aplica'),
	(5,'Aplica')
]
PENDRIVE=[
	(0,'No aplica'),
	(7,'Aplica')
]

FACULTAD=[
	(4,'No aplica'),
	(5,'Aplica')
]

CAFETERIA=[(1,'No aplica'),(2,'Aplica')]

class PresupuestoEvento(models.Model):

	#evento = models.ForeignKey(Eventos, on_delete=models.SET_NULL)
	estado = models.CharField(max_length=100,default='Grabado',choices=ESTADO_CHOICES)
	codigo = models.CharField(max_length=200,verbose_name="Código", blank=True, null=True)
	fecha= models.CharField(max_length=30)
	empresa = models.ForeignKey(Juridica,on_delete=models.SET_NULL, null=True,verbose_name="Empresa")
	hora_inicio=models.TimeField(verbose_name="Hora de inicio")
	hora_fin=models.TimeField(verbose_name="Hora de fin")
	n_horas = models.IntegerField(verbose_name="No. Horas",validators=[financiero.validaciones.validate_positivo])
	n_dias = models.IntegerField(verbose_name="No. Dias",validators=[financiero.validaciones.validate_positivo])
	n_participantes = models.IntegerField(verbose_name="No. Participantes",validators=[financiero.validaciones.validate_positivo])
	centro_costos = models.ForeignKey(Centro_Costos, on_delete=models.SET_NULL, null=True)
	costo_hora_instructores = models.CharField(max_length=100)
	costo_instructores=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo instructor/es")
	
	ingreso_individual_sin_desc=models.DecimalField(max_digits=10, decimal_places=2)
	ingreso_total_sin_desc=models.DecimalField(max_digits=10, decimal_places=2)
	descuento_maximo=models.DecimalField(max_digits=10, decimal_places=2)
	descuento_individual=models.DecimalField(max_digits=10, decimal_places=2)
	descuento_total=models.DecimalField(max_digits=10, decimal_places=2)
	
	ingreso_neto_individual=models.DecimalField(max_digits=10, decimal_places=2)
	ingreso_neto_total=models.DecimalField(max_digits=10, decimal_places=2)

	porcentaje_honorario_instructor = models.DecimalField(max_digits=3,decimal_places=0)
	honorario_total_evento=models.DecimalField(max_digits=10, decimal_places=2)
	
	impuesto_select=models.CharField(max_length=10)
	impuesto_unitario=models.CharField(max_length=10)
	impuesto_total=models.CharField(max_length=10)

	pasaje_instructor=models.ForeignKey(TarifarioServicioAereo, on_delete=models.SET_NULL,null=True)
	pasaje_instructor_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	pasaje_instructor_total=models.DecimalField(max_digits=10, decimal_places=2)

	hospedaje_alimentacion_instructor=models.ForeignKey(TarifarioHospedajeAlimentacionDocente, on_delete=models.SET_NULL, null=True)
	hospedaje_alimentacion_instructor_dias=models.PositiveIntegerField(blank=True, null=True)
	hospedaje_alimentacion_instructor_n=models.PositiveIntegerField(blank=True, null=True)
	hospedaje_alimentacion_instructor_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	hospedaje_alimentacion_instructor_total=models.DecimalField(max_digits=10, decimal_places=2)

	break_instructor=models.ForeignKey(TarifarioServicioAlimentacionBreak, on_delete=models.SET_NULL, null=True)
	break_instructor_dias=models.PositiveIntegerField(blank=True, null=True)
	break_instructor_n=models.PositiveIntegerField(blank=True, null=True)
	break_instructor_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	break_instructor_total=models.DecimalField(max_digits=10, decimal_places=2)

	almuerzo_instructor=models.ForeignKey(TarifarioServicioAlimentacionAlmuerzo, on_delete=models.SET_NULL, null=True)
	almuerzo_instructor_dias=models.PositiveIntegerField(blank=True, null=True)
	almuerzo_instructor_n=models.PositiveIntegerField(blank=True, null=True)
	almuerzo_instructor_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	almuerzo_instructor_total=models.DecimalField(max_digits=10, decimal_places=2)

	pasaje_personal=models.ForeignKey(TarifarioServicioAereo, on_delete=models.SET_NULL, null=True, related_name="pasaje_personal")
	pasaje_personal_dias=models.PositiveIntegerField(blank=True, null=True)
	pasaje_personal_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	pasaje_personal_total=models.DecimalField(max_digits=10, decimal_places=2)

	hospedaje_alimentacion_personal=models.ForeignKey(TarifarioHospedajeAlimentacionPersonal, on_delete=models.SET_NULL, null=True)
	hospedaje_alimentacion_personal_dias=models.PositiveIntegerField(blank=True, null=True)
	hospedaje_alimentacion_personal_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	hospedaje_alimentacion_personal_total=models.DecimalField(max_digits=10, decimal_places=2)
	
	movilizacion_personal_dias=models.PositiveIntegerField(blank=True, null=True)
	movilizacion_personal_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	movilizacion_personal_total=models.DecimalField(max_digits=10, decimal_places=2)

	instalaciones= models.ForeignKey(TarifarioInstalacion,on_delete=models.SET_NULL,null=True,blank=True)
	instalaciones_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	instalaciones_total=models.DecimalField(max_digits=10, decimal_places=2)

	publicidad_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	publicidad_total=models.DecimalField(max_digits=10,decimal_places=2)

	personal_evento_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	personal_evento_total=models.DecimalField(max_digits=10,decimal_places=2)
	
	prospecto_evento=models.ForeignKey(TarifarioProspecto,on_delete=models.SET_NULL,null=True)
	prospecto_evento_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	prospecto_evento_total=models.DecimalField(max_digits=10,decimal_places=2)
	
	total_egresos_fijos=models.DecimalField(max_digits=10,decimal_places=2)

	#Material del evento
	certificados=models.IntegerField(choices=CERTIFICADOS)
	certificados_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	certificados_total=models.DecimalField(max_digits=10,decimal_places=2)

	carpeta=models.IntegerField(choices=CARPETA)
	carpeta_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	carpeta_total=models.DecimalField(max_digits=10,decimal_places=2)

	maletin=models.IntegerField(choices=GENERICO)
	maletin_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	maletin_total=models.DecimalField(max_digits=10,decimal_places=2)

	block=models.IntegerField(choices=BLOCK)
	block_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	block_total=models.DecimalField(max_digits=10,decimal_places=2)

	lapiz=models.IntegerField(choices=LAPIZ)
	lapiz_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	lapiz_total=models.DecimalField(max_digits=10,decimal_places=2)

	pluma=models.IntegerField(choices=PLUMA)
	pluma_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	pluma_total=models.DecimalField(max_digits=10,decimal_places=2)

	credencial_plastico=models.IntegerField(choices=GENERICO)
	credencial_plastico_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	credencial_plastico_total=models.DecimalField(max_digits=10,decimal_places=2)

	credencial_pvc=models.IntegerField(choices=GENERICO)
	credencial_pvc_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	credencial_pvc_total=models.DecimalField(max_digits=10,decimal_places=2)

	pendrive=models.IntegerField(choices=PENDRIVE)
	pendrive_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	pendrive_total=models.DecimalField(max_digits=10,decimal_places=2)

	otros_materiales=models.IntegerField(choices=GENERICO)
	otros_materiales_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	otros_materiales_total=models.DecimalField(max_digits=10,decimal_places=2)

	break_evento=models.ForeignKey(TarifarioServicioAlimentacionBreak, on_delete=models.SET_NULL, null=True, related_name="break_evento")
	break_evento_dias=models.PositiveIntegerField(blank=True, null=True)
	break_evento_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	break_evento_total=models.DecimalField(max_digits=10, decimal_places=2)

	almuerzo_evento=models.ForeignKey(TarifarioServicioAlimentacionAlmuerzo, on_delete=models.SET_NULL, null=True, related_name="almuerzo_evento")
	almuerzo_evento_dias=models.PositiveIntegerField(blank=True, null=True)
	almuerzo_evento_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	almuerzo_evento_total=models.DecimalField(max_digits=10, decimal_places=2)

	ceremonia=models.IntegerField(choices=GENERICO)
	ceremonia_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	ceremonia_total=models.DecimalField(max_digits=10, decimal_places=2)

	aportacion_espol_porcentaje=models.DecimalField(max_digits=3, decimal_places=0)
	aportacion_espol_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	aportacion_espol_total=models.DecimalField(max_digits=10, decimal_places=2)

	aportacion_espoltech_porcentaje=models.DecimalField(max_digits=3, decimal_places=0)
	aportacion_espoltech_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	aportacion_espoltech_total=models.DecimalField(max_digits=10, decimal_places=2)

	aportacion_ministerio_porcentaje=models.DecimalField(max_digits=10, decimal_places=2)
	aportacion_ministerio_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	aportacion_ministerio_total=models.DecimalField(max_digits=10, decimal_places=2)

	aportacion_facultad=models.IntegerField(choices=FACULTAD)
	aportacion_facultad_porcentaje_unitario=models.DecimalField(max_digits=3, decimal_places=0)
	aportacion_facultad_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	aportacion_facultad_total=models.DecimalField(max_digits=10, decimal_places=2)

	movilizacion_interna_unitario=models.DecimalField(max_digits=10, decimal_places=2)
	movilizacion_interna_total=models.DecimalField(max_digits=10, decimal_places=2)

	cafeteria_limpieza=models.IntegerField(choices=CAFETERIA)
	cafeteria_limpieza_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	cafeteria_limpieza_total=models.DecimalField(max_digits=10,decimal_places=2)

	imprevisto_porcentaje=models.DecimalField(max_digits=5, decimal_places=1)
	imprevisto_unitario=models.DecimalField(max_digits=10,decimal_places=2)
	imprevisto_total=models.DecimalField(max_digits=10,decimal_places=2)

	total_egresos_variables=models.DecimalField(max_digits=10,decimal_places=2)
	total_egresos=models.DecimalField(max_digits=10,decimal_places=2)
	
	egreso_variable_unit=models.DecimalField(max_digits=10,decimal_places=2)
	utilidad=models.DecimalField(max_digits=10,decimal_places=2)
	margen_contribucion=models.DecimalField(max_digits=10,decimal_places=2)
	punto_equilibrio=models.DecimalField(max_digits=10,decimal_places=2)

	n_cursos=models.PositiveIntegerField()
	participacion_total=models.DecimalField(max_digits=10,decimal_places=2)

	pago_docente_total=models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)

	motivo_anular = models.CharField(max_length=500, null=True,blank=True)

	observaciones=models.CharField(max_length=500)

	def __str__(self):
		return self.codigo+" - "+self.estado




