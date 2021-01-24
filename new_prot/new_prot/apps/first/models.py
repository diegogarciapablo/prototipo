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
			)
	id = models.AutoField(primary_key=True)
	t_ubi=models.CharField(max_length=25, verbose_name="tipo de lugar", null=False, blank=False, choices=tipos_choices, )
	n_ubi=models.CharField(max_length=45, verbose_name="nombre de lugar", null=False, blank=False, )
	direccion=models.CharField(max_length=45, null=False, blank=False, )
	latit=models.CharField(max_length=45, verbose_name="latitud", null=False, blank=False, )
	longi=models.CharField(max_length=45, verbose_name="longitud", null=False, blank=False, )
	foto=models.CharField(max_length=90, null=True, blank=True, )

	class Meta:
		verbose_name= 'ubicacion'
		verbose_name_plural= 'ubicaciones'
		ordering =['id']

	def __verbose__(id):
		return self.n_ubi


class e_comida(models.Model):
	"""docstring for e_comida"""
	id = models.AutoField(primary_key=True)
	phone = models.CharField(max_length=15, null=False, blank=False, help_text="ingrese el telefono")
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return 'los datos de %s son' %(self.ubicacion.n_ubi)

class z_comercial(models.Model):
	id = models.AutoField(primary_key=True)
	hora = models.CharField(max_length=25, verbose_name="horario", null=False, blank=False, help_text="escriba el horario ejm. 06:30 a 15:45")
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return 'los datos de %s son' %(self.ubicacion.n_ubi)

class alojamiento(models.Model):
	id = models.AutoField(primary_key=True)
	telf= models.CharField(max_length=15, verbose_name="telefono", null=False, blank=False, help_text="numero telefonico del alojamiento")
	clas= models.CharField(max_length=20, verbose_name="clasificacion", null=False, blank=False, help_text="que lasificacion tiene ese edificio?")
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return 'los datos de %s son' %(self.ubicacion.n_ubi)

class e_educativo(models.Model):
	conf_choices=(
		('si','si'),
		('no','no'))
	id = models.AutoField(primary_key=True)
	n_ini =models.CharField(max_length=2, verbose_name="nivel inicial", null=False, blank=False, choices=conf_choices, help_text="el establecimiento tiene nivel inicial?",)
	prim =models.CharField(max_length=2, verbose_name="primaria", null=False, blank=False, choices=conf_choices, help_text="el establecimiento tiene nivel primario?",)
	sec =models.CharField(max_length=2, verbose_name="secundaria", null=False, blank=False, choices=conf_choices, help_text="el establecimiento tiene nivel secundario?",)
	n_sup =models.CharField(max_length=2, verbose_name="nivel superior", null=False, blank=False, choices=conf_choices, help_text="el establecimiento tiene nivel superior?",)
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return 'los datos de %s son' %(self.ubicacion.n_ubi)


class e_medico(models.Model):
	id = models.AutoField(primary_key=True)
	telf =models.CharField(max_length=15, verbose_name="telefono", null=False, blank=False, help_text="cual es el numero de contacto?",)
	nivel =models.CharField(max_length=25, verbose_name="tipo o nivel", null=False, blank=False, help_text="indique tipo de consultorio o nivel en caso de hospital",)
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return 'los datos de %s son' %(self.ubicacion.n_ubi)

class e_religioso(models.Model):
	id = models.AutoField(primary_key=True)
	relg =models.CharField(max_length=2, verbose_name="religion", null=False, blank=False, help_text="que fe profesa este establecimiento?",)
	ubi = models.OneToOneField(ubicacion ,on_delete=models.CASCADE, null=False, blank=False,
								help_text="a que lugar pertenecen estos datos?")
	def __str__(self):
		return 'los datos de %s son' %(self.ubicacion.n_ubi)

