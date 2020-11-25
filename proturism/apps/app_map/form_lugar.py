from django import forms
from .models import admin_agregar, colegio, iglesia, alojamiento, plaza, restaurante


class DateInput(forms.DateInput):
	input_type='date'

class FormLugar(forms.ModelForm):
	class Meta:
		model= admin_agregar
		fields = ['latitud','longitud','tipo']

class FormSchool(forms.ModelForm):
	class Meta:
		model= colegio
		fields= ['nombre','fecha_fundacion','clasificacion','cod_ubicacion']
		widgets = { 'fecha_fundacion': DateInput(),}


class FormChurch(forms.ModelForm):
	class Meta:
		model= iglesia
		fields=['nombre','fecha_fundacion','religion','capacidad','cod_ubicacion']
		widgets = { 'fecha_fundacion': DateInput(),}


class FormLodgings(forms.ModelForm):
	class Meta:
		model= alojamiento
		fields=['nombre','clasificacion','fecha_fundacion','cod_ubicacion']
		widgets = { 'fecha_fundacion': DateInput(),}

class FormSquare(forms.ModelForm):
	class Meta:
		model= plaza
		fields=['nombre','fecha_fundacion','cod_ubicacion']
		widgets = { 'fecha_fundacion': DateInput(),}


class FormRestaurant(forms.ModelForm):
	class Meta:
		model= restaurante
		fields=['nombre','capacidad','clasificacion','cod_ubicacion']