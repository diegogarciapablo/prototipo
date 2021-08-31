from django.db import models

# Create your models here.
class ubicacion(models.Model):
	tipos_choices=(
		('plaza','plaza'),
		('comida','comida'),
		('comercial','comercial'),
		('alojamiento','alojamiento'),
		('educativo','educativo'),
		('medico','medico'),
		('religioso','religioso'),
		('atractivo','atractivo'),
		('transporte','transporte'),
			)
	id = models.AutoField(primary_key=True)
	t_ubi=models.CharField(max_length=45, verbose_name="tipo de lugar", null=False, blank=False, choices=tipos_choices, )
	n_ubi=models.CharField(max_length=45, verbose_name="nombre de lugar", null=False, blank=False, )
	direccion=models.CharField(max_length=200, null=False, blank=False, )
	latit=models.CharField(max_length=45, verbose_name="latitud", null=False, blank=False, )
	longi=models.CharField(max_length=45, verbose_name="longitud", null=False, blank=False, )


	class Meta:
		verbose_name= 'ubicacion'
		verbose_name_plural= 'ubicaciones'
		ordering =['id']

	def __verbose__(id):
		return self.n_ubi

	def __str__(self):
		return self.n_ubi


class e_comida(models.Model):
	"""docstring for e_comida"""
	id = models.AutoField(primary_key=True)
	telf = models.CharField(max_length=15, null=True, blank=True, help_text="ingrese el telefono")
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return self.ubi.n_ubi


class alojamiento(models.Model):
	id = models.AutoField(primary_key=True)
	telf= models.CharField(max_length=15, verbose_name="telefono", null=True, blank=True, help_text="numero telefonico del alojamiento")
	clas= models.CharField(max_length=45, verbose_name="clasificacion", null=False, blank=False, help_text="que lasificacion tiene ese edificio?")
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return self.ubi.n_ubi


class e_medico(models.Model):
	id = models.AutoField(primary_key=True)
	telf =models.CharField(max_length=15, verbose_name="telefono", null=True, blank=True, help_text="cual es el numero de contacto?",)
	nivel =models.CharField(max_length=45, verbose_name="tipo o nivel", null=False, blank=False, help_text="indique tipo de consultorio o nivel en caso de hospital",)
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return self.ubi.n_ubi

class e_religioso(models.Model):
	id = models.AutoField(primary_key=True)
	telf = models.CharField(max_length=15, verbose_name="telefono", null=True, blank=True, help_text="cual es el numero de contacto?",)
	relig =models.CharField(max_length=100, verbose_name="religion", null=False, blank=False, help_text="que fe profesa este establecimiento?",)
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return self.ubi.n_ubi

class transporte(models.Model):
	id = models.AutoField(primary_key=True)
	telf = models.CharField(max_length=15, verbose_name="telefono", null=True, blank=True, help_text="cual es el numero de contacto?",)
	tipo = models.CharField(max_length=100, verbose_name="tipo", null=False, blank=False, help_text="cual es el tipo de transporte?")
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return self.ubi.n_ubi

class v_virtual(models.Model):
	id = models.AutoField(primary_key=True)
	url = models.CharField(max_length=512, verbose_name="url", null=False, blank=False, help_text="ingrese la url",)
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return self.ubi.n_ubi


class img_index(models.Model):
	posicion_choices=(
		('carrusel','carrusel'),
		('album','album'),
		('v_virtual','v_virtual'),
			)
	id = models.AutoField(primary_key=True)
	posicion = models.CharField(max_length=52, verbose_name="posicion", null=False, blank=False,  choices=posicion_choices,)
	direccion = models.CharField(max_length=45, verbose_name="inserte la imagen", null=False, blank=False, )
	url = models.CharField(max_length=45, verbose_name="a donde redireccionara la imagen", null=False, blank=False, default="#" )
	titulo = models.CharField(max_length=150, verbose_name="escribe una pequeña introduccion", null=False, blank=True, )
	leyenda = models.CharField(max_length=150, verbose_name="escribe una pequeña introduccion", null=False, blank=False, )
