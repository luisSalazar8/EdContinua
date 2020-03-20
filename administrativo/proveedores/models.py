from django.db import models
import administrativo.validaciones

class Provincia(models.Model):
	nombre = models.CharField(max_length=50,verbose_name="Provincia")
	def __str__(self):
		return self.nombre


class Ciudad(models.Model):
	provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50,verbose_name="Ciudad")
	def __str__(self):
		return self.nombre

class TipoEmpresa(models.Model):
	nombre = models.CharField(max_length=100,verbose_name="Tipo de Empresa")
	def __str__(self):
		return self.nombre

class Sector(models.Model):
	nombre = models.CharField(max_length=100,verbose_name="Sector")
	def __str__(self):
		return self.nombre

class Proveedor(models.Model):
	TIPO_RUBRO_CHOICES = [("Bienes","Bienes"), ("Servicios","Servicios"), ("Ambos","Ambos")]
	TIPO_PROVEEDOR_CHOICES = [("Natural","Natural"), ("Jurídica","Jurídica")]
	ruc = models.CharField(max_length=13,primary_key=True, validators=[administrativo.validaciones.validate_ruc] )
	razon = models.CharField(max_length=200)
	sector = models.ForeignKey(Sector,on_delete=models.SET_NULL, null=True)
	direccion = models.CharField(max_length=200)
	provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
	ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)

	telefono = models.CharField(max_length=20, validators=[administrativo.validaciones.validate_fono_convencional])
	celular = models.CharField(max_length=20, validators=[administrativo.validaciones.validate_celular])
	correo = models.CharField(max_length=100)
	representante = models.CharField(max_length=250)
	tipo_proveedor = models.CharField(max_length=50, verbose_name="Tipo de Proveedor", choices=TIPO_PROVEEDOR_CHOICES)
	tipo_rubro = models.CharField(max_length=50, verbose_name="Tipo de Rubro", choices=TIPO_RUBRO_CHOICES)

	observaciones = models.CharField(max_length=500, verbose_name="Observaciones", blank=True, null=True)
	
	ci_contacto_uno=models.CharField(max_length=13,  blank=True, null=True, validators=[administrativo.validaciones.validate_cedula])
	nombre_contacto_uno=models.CharField(max_length=200,  blank=True, null=True)
	apellidos_contacto_uno=models.CharField(max_length=200 , blank=True, null=True)
	cargo_contacto_uno=models.CharField(max_length=200,  blank=True, null=True)
	contacto_contacto_uno=models.CharField(max_length=200,  blank=True, null=True)
	telefono_contacto_uno=models.CharField(max_length=20,  blank=True, null=True, validators=[administrativo.validaciones.validate_fono_convencional])
	celular_contacto_uno=models.CharField(max_length=20,  blank=True, null=True, validators=[administrativo.validaciones.validate_celular])
	correo_contacto_uno= models.CharField(max_length=100,  blank=True, null=True)

	ci_contacto_dos=models.CharField(max_length=13,  blank=True, null=True, validators=[administrativo.validaciones.validate_cedula])
	nombre_contacto_dos=models.CharField(max_length=200,  blank=True, null=True)
	apellidos_contacto_dos=models.CharField(max_length=200,  blank=True, null=True)
	cargo_contacto_dos=models.CharField(max_length=200,  blank=True, null=True)
	contacto_contacto_dos=models.CharField(max_length=200,  blank=True, null=True)
	telefono_contacto_dos=models.CharField(max_length=20, blank=True, null=True,  validators=[administrativo.validaciones.validate_fono_convencional])
	celular_contacto_dos=models.CharField(max_length=20,  blank=True, null=True, validators=[administrativo.validaciones.validate_celular])
	correo_contacto_dos= models.CharField(max_length=100,  blank=True, null=True)

	ci_contacto_tres=models.CharField(max_length=13,  blank=True, null=True, validators=[administrativo.validaciones.validate_cedula])
	nombre_contacto_tres=models.CharField(max_length=200,  blank=True, null=True)
	apellidos_contacto_tres=models.CharField(max_length=200,  blank=True, null=True)
	cargo_contacto_tres=models.CharField(max_length=200,  blank=True, null=True)
	contacto_contacto_tres=models.CharField(max_length=200,  blank=True, null=True)
	telefono_contacto_tres=models.CharField(max_length=20,  blank=True, null=True, validators=[administrativo.validaciones.validate_fono_convencional])
	celular_contacto_tres=models.CharField(max_length=20,  blank=True, null=True, validators=[administrativo.validaciones.validate_celular])
	correo_contacto_tres= models.CharField(max_length=100,  blank=True, null=True)

	def __str__(self):
		return self.nombre+" - "+self.ruc





# class Contacto(models.Model):
# 	ci_contacto=models.CharField(max_length=13, validators=[administrativo.validaciones.validate_cedula])
# 	nombre_contacto=models.CharField(max_length=200)
# 	apellidos_contacto=models.CharField(max_length=200)
# 	cargo_contacto=models.CharField(max_length=200)
# 	contacto_contacto=models.CharField(max_length=200)
# 	telefono_contacto=models.CharField(max_length=20, validators=[administrativo.validaciones.validate_fono_convencional])
# 	celular_contacto=models.CharField(max_length=20, validators=[administrativo.validaciones.validate_celular])
# 	correo_contacto = models.CharField(max_length=100)
# 	design=models.ForeignKey(Proveedor,null=False,blank=False,on_delete=models.CASCADE)
# 	def __str__(self):
# 		return "{}".format(self.nombre_sub)

