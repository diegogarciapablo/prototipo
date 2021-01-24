from django import forms
from .models import ubicacion, e_comida, z_comercial, alojamiento, e_educativo, e_medico, e_medico, e_religioso


class FormUbicacion(forms.ModelForm):
	class Meta:
		model= ubicacion
		fields = ['t_ubi','n_ubi','direccion','latit','longi','foto']
		labels = {
			't_ubi':'Tipo',
			'n_ubi':'Nombre',
			'direccion':'Direccion',
			'latit':'Latitud',
			'longi':'Longitud',
			'foto':'Foto',
		}
		widgets ={
			't_ubi' : forms.TextInput(attrs={'class':'form-control'}),
			'n_ubi' : forms.TextInput(attrs={'class':'form-control'}),
			'direccion' : forms.TextInput(attrs={'class':'form-control'}),
			'latit' : forms.TextInput(attrs={'class':'form-control'}),
			'longi' : forms.TextInput(attrs={'class':'form-control'}),
			'foto' : forms.TextInput(attrs={'class':'form-control'}),
		}

class FormEComida(forms.ModelForm):
	class Meta:
		model= e_comida
		fields = ['phone','ubi']
		labels = {
			'phone':'telefono',
			'ubi':'lugar'
		}
		widgets = {
			'phone' : forms.TextInput(attrs={'class':'form-control'}),

		}

class FormZComercial(forms.ModelForm):
	class Meta:
		model= z_comercial
		fields = ['hora','ubi']
		labels = {
			'hora':'horario',
			'ubi':'lugar'
		}
		widgets = {
			'hora' : forms.TextInput(attrs={'class':'form-control'}),
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

class FormEEducativo(forms.ModelForm):
	class Meta:
		model= e_educativo
		fields = ['n_ini','prim','sec','n_sup']

class FormEMedico(forms.ModelForm):
	class Meta:
		model= e_medico
		fields = ['telf','nivel','ubi']

class FormEReligioso(forms.ModelForm):
	class Meta:
		model= e_religioso
		fields = ['relg','ubi']