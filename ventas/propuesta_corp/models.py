from django.db import models
from ventas.reporte_contacto.models import ReporteContacto
from ventas.personas_juridicas.models import Juridica, Sector, TipoEmpresa
from multiselectfield import MultiSelectField
import ventas.validaciones

# Create your models here.



class PropuestaCorporativo(models.Model):

    ESTADO_CHOICES= [
                        ('SG','Seguimiento'),
                        ('PD','Pendiente'),
                        ('ACP','Aceptada'),
                        ('NACP','No aceptada'),
                    ]

    SERVICIOS_CHOICES=  [
                            ('CBR','Coffe Break'),
                            ('ALM','Almuerzo'),
                            ('MIP','Material impreso'),
                            ('MDG','Material digital'),
                        ]

    cod_propuesta=models.CharField(max_length=20, blank=True)
    version=models.PositiveIntegerField()
    tipo_empresa=models.ForeignKey(TipoEmpresa, on_delete=models.SET_NULL, null=True, blank=True)
    reporte=models.ForeignKey(ReporteContacto, on_delete=models.CASCADE, blank=True)
    estado=models.CharField(max_length=15,
                            choices=ESTADO_CHOICES,
                            default='SG')
    ruc_ci=models.CharField(max_length=13)
    razon_nombres=models.CharField(max_length=200)
    sector=models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_solicitud=models.CharField(max_length=12)
    numero_participantes=models.PositiveIntegerField()
    total_horas=models.PositiveIntegerField()
    cantidad_cursos=models.PositiveIntegerField()
    monto_propuesta=models.FloatField()
    margen_contribucion=models.FloatField( max_length=3)
    utilidad_esperada=models.FloatField()
    exito=models.FloatField( max_length=4)
    lugar=models.CharField(max_length=25)
    servicios_incluidos=MultiSelectField(choices=SERVICIOS_CHOICES,
                                            blank=True,
                                            null=True)
    fecha_inicio_estimada=models.CharField(max_length=12)
    fecha_envio=models.CharField(max_length=12)
    fecha_respuesta=models.CharField(max_length=12)
    observacion=models.CharField(max_length=250,blank=True,null=True)

    area_capacitacion= models.CharField(max_length=50, blank=True)
    asesor=models.CharField(max_length=50, blank=True)
    active=models.BooleanField(default = True)
    def delete(self, *arg, **kwargs):
     #   self.anexo.delete()
        super().delete(*arg,**kwargs)

class PropuestaFile(models.Model):
    file = models.FileField(upload_to='uploads/',blank=True, null=True)
    propuesta = models.ForeignKey(PropuestaCorporativo, on_delete=models.CASCADE, related_name='files')