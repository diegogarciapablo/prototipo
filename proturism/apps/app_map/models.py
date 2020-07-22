from django.db import models
tipo_choices=(
	('colegio','Colegio'),
	('iglesia','Iglesia'),
	('plaza','Plaza'),
	('restaurante','Restaurante'),
	('alojamiento','Alojamiento'),
	)

class admin_agregar (models.Model):
	cod_ubicacion= models.AutoField(primary_key = True)
	latitud = models.CharField(max_length=200, blank=False, null=False)
	longitud = models.CharField(max_length=200, blank=False, null=False)
	tipo = models.CharField(max_length=200, blank=False, null=False, choices=tipo_choices)
	def __STR__(self):
		return self.tipo

class colegio(models.Model):
	cod_colegio=models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=200, blank=False, null=False)
	fecha_fundacion = models.CharField(max_length=200,blank=False, null=False)
	clasificacion = models.CharField(max_length=200, blank=False)
	cod_ubicacion=models.ForeignKey(admin_agregar, on_delete=models.CASCADE)

class iglesia(models.Model):
	cod_iglesia=models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=200, blank=False, null=False)
	fecha_fundacion = models.CharField(max_length=200,blank=False, null=False)
	religion= models.CharField(max_length=200, blank=False, null=False)
	capacidad=models.CharField(max_length=200, blank=False, null=False)
	cod_ubicacion=models.ForeignKey(admin_agregar, on_delete=models.CASCADE)

class alojamiento(models.Model):
	cod_alojamiento=models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=200, blank=False, null=False)
	clasificacion = models.CharField(max_length=200,blank=False, null=False)
	fecha_fundacion = models.CharField(max_length=200,blank=False, null=False)
	cod_ubicacion=models.ForeignKey(admin_agregar, on_delete=models.CASCADE)

class plaza(models.Model):
	cod_plaza=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=200, blank=False, null=False)
	fecha_fundacion = models.DateField(blank=False, null=False)
	cod_ubicacion=models.OneToOneField(admin_agregar, on_delete=models.CASCADE)



class restaurante(models.Model):
	cod_restaurante=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=200, blank=False, null=False)
	capacidad=models.CharField(max_length=200, blank=False, null=False)
	clasificacion = models.CharField(max_length=200,blank=False, null=False)
	cod_ubicacion= models.ForeignKey(admin_agregar, on_delete=models.CASCADE)