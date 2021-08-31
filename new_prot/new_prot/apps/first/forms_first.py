from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(label='nombre' ,widget=forms.TextInput)
	last_name = forms.CharField(label='primer apellido' ,widget=forms.TextInput)
	email = forms.EmailField()
	password1 = forms.CharField(label='contraseña' ,widget=forms.PasswordInput)
	password2 = forms.CharField(label='confirma contraseña' ,widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']
		help_texts = {k:"" for k in fields}

class FormUbicacion(forms.ModelForm):
	class Meta:
		model= ubicacion
		fields = ['t_ubi','n_ubi','direccion','latit','longi']
		labels = {
			't_ubi':'Tipo',
			'n_ubi':'Nombre',
			'direccion':'Direccion',
			'latit':'Latitud',
			'longi':'Longitud',

		}
		widgets ={
			't_ubi' : forms.TextInput(attrs={'class':'form-control'}),
			'n_ubi' : forms.TextInput(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'latit' : forms.TextInput(attrs={'class':'form-control'}),
			'longi' : forms.TextInput(attrs={'class':'form-control'}),

		}

class FormEComida(forms.ModelForm):
	class Meta:
		model= e_comida
		fields = ['telf','ubi']
		labels = {
			'telf':'telefono',
			'ubi':'lugar'
		}
		widgets = {
			'phone' : forms.TextInput(attrs={'class':'form-control'}),

		}



class FormAlojamiento(forms.ModelForm):
	class Meta:
		model= alojamiento
		fields = ['telf','clas','ubi']
		labels = {
			'telf':'telefono',
			'clas':'clasificacion',
			'ubi':'lugar'
		}
		widgets ={
			'telf': forms.TextInput(attrs={'class':'form-control'}),
			'clas': forms.TextInput(attrs={'class':'form-control'}),
		}



class FormEMedico(forms.ModelForm):
	class Meta:
		model= e_medico
		fields = ['telf','nivel','ubi']

class FormEReligioso(forms.ModelForm):
	class Meta:
		model= e_religioso
		fields = ['telf','relig','ubi']

class FormTransporte(forms.ModelForm):
	class Meta:
		model=transporte
		fields= ['telf','tipo','ubi']

class Formvirtual(forms.ModelForm):
	class Meta:
		model= v_virtual

		fields = ['ubi','url']
		labels = {
			'ubi':'lugar',
			'url':'url'
		}
		widgets ={

			'url': forms.Textarea(attrs={'class':'form-control'}),
		}