from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms_first import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mass_mail, send_mail

import folium
import markdown



def Index(request):
	if request.user.is_authenticated:
		messages.info(request,f'bienvenido {request.user.username}')
		return render(request,'main.html' )
	else:
		return render(request,'main.html' )

@login_required
def Adm_Site(request):
	staffs = User.objects.filter(username=request.user.username).values_list('is_staff')
	for staff in staffs:
		if staff==(True,):
			return render(request,'adm/index_adm.html')
		else:
			username=request.user.username
			messages.success(request,f'Usuario {username} no es miembro de staff')
			return render(request,'main.html')

def prueba(request):
	return render(request,'main.html')




def visit_virt(request):
	return render(request, 'mapa/crud/pruebas/list_test.html')

def registro(request):
	if request.method =='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			usuario=form.save()
			username = form.cleaned_data['username']
			messages.success(request,f'Usuario {username} creado')
			login(request, usuario)
			messages.info(request,f"bienvenido{username}")
			return redirect('crud:index')
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}: {form.error_messages[msg]}")

	else:
		form = UserRegisterForm()
	context = {
	'form':form
	}
	return render(request,'adm/register_adm.html',context)


def logout_request(request):
	logout(request)
	messages.info(request,"usted a cerrado sesion")
	return redirect('crud:index')

def login_request(request):
	if request.method == 'POST':
		print("llego a post")
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			usuario = form.cleaned_data.get('username')
			contraseña = form.cleaned_data.get('password')
			user = authenticate(username=usuario, password=contraseña)
			if user is not None:
				login(request, user)
				return redirect('crud:index')
			else:
				messages.error(request,"usuario o contraseña invalido")
		else:
			messages.error(request,"usuario o contraseña invalido")

	print("ingresa como get")
	form = AuthenticationForm()
	return render(request,"adm/login_adm.html",{"form":form})

def Mapa(request):
	#obteniendo datos de la db
	gral_lista = ubicacion.objects.all().values_list()

	grupo_plaza=folium.FeatureGroup(name='plazas')
	grupo_comidas=folium.FeatureGroup(name='e. comidas')
	grupo_comercial=folium.FeatureGroup(name='z. comerciales')
	grupo_alojamiento=folium.FeatureGroup(name='alojamientos')
	grupo_medico=folium.FeatureGroup(name='e. medicos')
	grupo_religioso=folium.FeatureGroup(name='e. religiosos')
	grupo_atractivos=folium.FeatureGroup(name='a. turistico')

	#llenando Iframe

	#creando mapa
	m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, tiles='cartodbpositron',)
	#marcadores y estableciendo capas
	for x in gral_lista:

		v_popup= x[1].title()+" "+x[2].title()+" "+x[3].title()
		if x[1]=='plaza':
			v_icon=folium.Icon(color='green',icon='tree-conifer')

			feature_g=grupo_plaza
		if x[1]=='comida':
			v_icon=folium.Icon(color='orange',icon='cutlery')

			feature_g=grupo_comidas
		if x[1]=='comercial':
			v_icon=folium.Icon(color='black',icon='shopping-cart')

			feature_g=grupo_comercial
		if x[1]=='alojamiento':
			v_icon=folium.Icon(color='blue',icon='home')

			feature_g=grupo_alojamiento

		if x[1]=='medico':
			v_icon=folium.Icon(color='red',icon='plus')

			feature_g=grupo_medico
		if x[1]=='religioso':
			v_icon=folium.Icon(color='yellow',icon='ok-sign')

			feature_g=grupo_religioso

		if x[1]=='atractivo':
			v_icon = folium.Icon(color='purple',icon='fa-binoculars')

			feature_g = grupo_atractivos

		folium.Marker(location=[x[4],x[5]], popup=v_popup,icon =v_icon ).add_to(feature_g)

	#agregando capas y control de capas
	m.add_child(grupo_plaza)
	m.add_child(grupo_comidas)
	m.add_child(grupo_comercial)
	m.add_child(grupo_alojamiento)
	m.add_child(grupo_medico)
	m.add_child(grupo_religioso)
	m.add_child(grupo_atractivos)
	m.add_child(folium.map.LayerControl())
	# representacion html del mapa
	m = m._repr_html_()
	context={
		'm': m,
			}
	return render(request, 'prueba map.html', context)



@login_required
def CreateUbicacion(request):
	staffs = User.objects.filter(username=request.user.username).values_list('is_staff')
	for staff in staffs:
		if staff==(True,):
			if request.method == 'POST':
				rec_lug= request.POST.get('t_ubi')
				print('llego a post')
				ubicacion_form = FormUbicacion(request.POST)

				ubi_valid= ubicacion_form.is_valid()
				print(ubi_valid)
				if ubi_valid:
					print('paso validacion')
					ubicacion_form.save()
					if (rec_lug=='comida'):
						return redirect('confir_comi/')
					if (rec_lug=='alojamiento'):
						return redirect('confir_aloj/')
					if (rec_lug=='medico'):
						return redirect('confir_medi/')
					if (rec_lug=='religioso'):
						return redirect('confir_reli/')
					else:
						return redirect('confir_plaza/')
			else:
				ubicacion_form=FormUbicacion()
				gral_lista = ubicacion.objects.all().values_list()
				#creando mapa
				m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, )

				for x in gral_lista:
					v_popup= x[1].title()+" "+x[2].title()+" "+x[3].title()
					if x[1]=='plaza':
						v_icon=folium.Icon(color='green',icon='tree-conifer')

					if x[1]=='comida':
						v_icon=folium.Icon(color='orange',icon='cutlery')

					if x[1]=='comercial':
						v_icon=folium.Icon(color='black',icon='shopping-cart')

					if x[1]=='alojamiento':
						v_icon=folium.Icon(color='blue',icon='home')

					if x[1]=='medico':
						v_icon=folium.Icon(color='red',icon='plus')

					if x[1]=='religioso':
						v_icon=folium.Icon(color='yellow',icon='ok-sign')

					if x[1]=='atractivo':
						v_icon = folium.Icon(color='purple',icon='fa-binoculars')

					folium.Marker(location=[x[4],x[5]], popup=v_popup,icon =v_icon ).add_to(m)
				# obtencion de coordenadas
				m.add_child(folium.LatLngPopup())
				# representacion html del mapa
				m = m._repr_html_()
				context={
				'm': m,
				'ubi_form':ubicacion_form,
					}
				return render(request,'mapa/crud/new_ubi.html', context)
		else:
			username=request.user.username
			messages.success(request,f'Usuario {username} no es miembro de staff')
			return render(request,'main.html')

@login_required
def confirm_plaza(request):
	staffs = User.objects.filter(username=request.user.username).values_list('is_staff')
	for staff in staffs:
		if staff==(True,):
			if request.method == 'POST':
				return redirect('crud:mapa')
			else:
				ult_ubi = ubicacion.objects.all().values_list().last()
				mark_lat=""
				mark_long=""
				popup=""
				mark_lat=ult_ubi[4]
				mark_long=ult_ubi[5]
				popup=" "+ult_ubi[2]+" "+ult_ubi[3]
				#creando mapa
				m = folium.Map(location=[mark_lat,mark_long], zoom_start=16, )
				# marcador de anterior paso

				icon=folium.Icon(color='red',icon='question-sign')
				marcador1 = folium.Marker(location=[mark_lat,mark_long], popup=popup, icon=icon)
				marcador1.add_to(m)
				# representacion html del mapa
				m = m._repr_html_()
				context={
				'm': m,
					}
				return render(request,'mapa/crud/confir_ubi_plaza.html', context)
		else:
			username=request.user.username
			messages.success(request,f'Usuario {username} no es miembro de staff')
			return render(request,'main.html')



@login_required
def confir_comi(request):
	staffs = User.objects.filter(username=request.user.username).values_list('is_staff')
	for staff in staffs:
		if staff==(True,):
			if request.method == 'POST':
				comida_form = FormEComida(request.POST)
				comi_valid= comida_form.is_valid()
				if comi_valid:
					comida_form.save()
					return redirect('crud:mapa')
			else:
				var_form = FormEComida()
				ult_ubis = ubicacion.objects.all().values_list().last()
				mark_lat=""
				mark_long=""
				popup=""
				foreig=0
				for y in ult_ubis:
					foreig=y[0]
					mark_lat=y[4]
					mark_long=y[5]
					popup=" "+y[2]+" "+y[3]
				#creando mapa
				m = folium.Map(location=[mark_lat,mark_long], zoom_start=16, )
				# marcador de anterior paso
				icon=folium.Icon(color='red',icon='question-sign')
				marcador1 = folium.Marker(location=[mark_lat,mark_long], popup=popup, icon=icon)
				marcador1.add_to(m)
				# representacion html del mapa
				m = m._repr_html_()
				context={
				'm': m,
				'var_form':var_form,
				'foreig':foreig,
					}
				return render(request,'mapa/crud/confir_ubi_comi.html', context)
		else:
			username=request.user.username
			messages.success(request,f'Usuario {username} no es miembro de staff')
			return render(request,'main.html')


@login_required
def confir_aloj(request):
	staffs = User.objects.filter(username=request.user.username).values_list('is_staff')
	for staff in staffs:
		if staff==(True,):
			if request.method == 'POST':
				print("llegada de metodo")
				aloj_form = FormAlojamiento(request.POST)
				print("carga de aloj_form")
				alo_valid= aloj_form.is_valid()
				print(alo_valid)
				if alo_valid:
					print("entro al if")
					aloj_form.save()
					print("guardado")
					return redirect('crud:mapa')
			else:
				ult_ubis = ubicacion.objects.all().values_list()
				mark_lat=""
				mark_long=""
				popup=""
				foreig=0
				for y in ult_ubis:
					foreig=y[0]
					mark_lat=y[4]
					mark_long=y[5]
					popup=" "+y[2]+" "+y[3]
				#creando mapa
				m = folium.Map(location=[mark_lat,mark_long], zoom_start=16, )
				# marcador de anterior paso
				icon=folium.Icon(color='red',icon='question-sign')
				marcador1 = folium.Marker(location=[mark_lat,mark_long], popup=popup, icon=icon)
				marcador1.add_to(m)
				# representacion html del mapa
				m = m._repr_html_()
				context={
				'm': m,
				'foreig':foreig,
					}
				return render(request,'mapa/crud/confir_ubi_aloj.html', context)
		else:
			username=request.user.username
			messages.success(request,f'Usuario {username} no es miembro de staff')
			return render(request,'main.html')


@login_required
def confir_medi(request):
	staffs = User.objects.filter(username=request.user.username).values_list('is_staff')
	for staff in staffs:
		if staff==(True,):
			if request.method == 'POST':
				print("llegada de metodo")
				medi_form = FormEMedico(request.POST)
				print("carga de medi_form")
				medi_valid= medi_form.is_valid()
				print(medi_valid)
				if medi_valid:
					print("entro al if")
					medi_form.save()
					print("guardado")
					return redirect('crud:mapa')
			else:
				var_form=FormEMedico()
				ult_ubi = ubicacion.objects.all().values_list().last()
				mark_lat=""
				mark_long=""
				popup=""
				foreig=0
				foreig=ult_ubi[0]
				mark_lat=ult_ubi[4]
				mark_long=ult_ubi[5]
				popup=" "+ult_ubi[2]+" "+ult_ubi[3]
				#creando mapa
				m = folium.Map(location=[mark_lat,mark_long], zoom_start=16, )
				# marcador de anterior paso
				icon=folium.Icon(color='red',icon='question-sign')
				marcador1 = folium.Marker(location=[mark_lat,mark_long], popup=popup, icon=icon)
				marcador1.add_to(m)
				# representacion html del mapa
				m = m._repr_html_()
				context={
				'var_form':var_form,
				'm': m,
				'foreig':foreig,
					}
				return render(request,'mapa/crud/confir_ubi_medi.html', context)
		else:
			username=request.user.username
			messages.success(request,f'Usuario {username} no es miembro de staff')
			return render(request,'main.html')

@login_required
def confir_reli(request):
	staffs = User.objects.filter(username=request.user.username).values_list('is_staff')
	for staff in staffs:
		if staff==(True,):
			if request.method == 'POST':
				print("llegada de metodo")
				aloj_form = FormAlojamiento(request.POST)
				print("carga de aloj_form")
				alo_valid= aloj_form.is_valid()
				print(alo_valid)
				if alo_valid:
					print("entro al if")
					aloj_form.save()
					print("guardado")
					return redirect('crud:mapa')
			else:
				ult_ubis = ubicacion.objects.all().values_list()
				mark_lat=""
				mark_long=""
				popup=""
				foreig=0
				for y in ult_ubis:
					foreig=y[0]
					mark_lat=y[4]
					mark_long=y[5]
					popup=" "+y[2]+" "+y[3]
				#creando mapa
				m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, )
				# marcador de anterior paso
				icon=folium.Icon(color='red',icon='question-sign')
				marcador1 = folium.Marker(location=[mark_lat,mark_long], popup=popup, icon=icon)
				marcador1.add_to(m)
				# representacion html del mapa
				m = m._repr_html_()
				context={
				'm': m,
				'foreig':foreig,
					}
				return render(request,'mapa/crud/confir_ubi_aloj.html', context)
		else:
			username=request.user.username
			messages.success(request,f'Usuario {username} no es miembro de staff')
			return render(request,'main.html')



@login_required
def confir_trans(request):
	staffs = User.objects.filter(username=request.user.username).values_list('is_staff')
	for staff in staffs:
		if staff==(True,):
			if request.method == 'POST':
				print("llegada de metodo")
				trans_form = FormTransporte(request.POST)
				print("carga de trans_form")
				trans_valid= trans_form.is_valid()
				print(trans_valid)
				if trans_valid:
					print("entro al if")
					trans_form.save()
					print("guardado")
					return redirect('crud:mapa')
			else:
				ult_ubis = ubicacion.objects.all().values_list()
				mark_lat=""
				mark_long=""
				popup=""
				foreig=0
				for y in ult_ubis:
					foreig=y[0]
					mark_lat=y[4]
					mark_long=y[5]
					popup=" "+y[2]+" "+y[3]
				#creando mapa
				m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, )
				# marcador de anterior paso
				icon=folium.Icon(color='red',icon='question-sign')
				marcador1 = folium.Marker(location=[mark_lat,mark_long], popup=popup, icon=icon)
				marcador1.add_to(m)
				# representacion html del mapa
				m = m._repr_html_()
				context={
				'm': m,
				'foreig':foreig,
					}
				return render(request,'mapa/crud/confir_ubi_aloj.html', context)
		else:
			username=request.user.username
			messages.success(request,f'Usuario {username} no es miembro de staff')
			return render(request,'main.html')

# Create your views here.
def ListarPlaza(request):
	plazas = ubicacion.objects.filter(t_ubi="plaza")

	comidas = ubicacion.objects.filter(t_ubi="comida")
	comidas_2 = e_comida.objects.all()

	comerciales = ubicacion.objects.filter(t_ubi="comercial")


	alojamientos = ubicacion.objects.filter(t_ubi="alojamiento")
	alojamientos_2 = alojamiento.objects.all()



	medicos = ubicacion.objects.filter(t_ubi="medico")
	medicos_2 = e_medico.objects.all()

	religiosos = ubicacion.objects.filter(t_ubi="religioso")
	religiosos_2 = e_religioso.objects.all()

	context={
		'plazas':plazas,

		'comidas':comidas,
		'comidas_2':comidas_2,

		'comerciales':comerciales,

		'alojamientos':alojamientos,
		'alojamientos_2':alojamientos_2,

		'medicos':medicos,
		'medicos_2':medicos_2,

		'religiosos':religiosos,
		'religiosos_2':religiosos_2,
			}
	return render(request,'mapa/list plaza.html',context)


def ListarServicios(request,serv=1):
	if serv == 1:
		servicio = ubicacion.objects.filter(t_ubi="comida")
		servicio_2 = e_comida.objects.all()
		tipo = 'comida'
	if serv == 2:
		servicio = ubicacion.objects.filter(t_ubi="alojamiento")
		servicio_2 = alojamiento.objects.all()
		tipo = 'alojamiento'
	if serv == 3:
		servicio = ubicacion.objects.filter(t_ubi="medico")
		servicio_2 = e_medico.objects.all()
		tipo = 'medico'
	if serv == 4:
		servicio = ubicacion.objects.filter(t_ubi="religion")
		servicio_2 = e_religioso.objects.all()
		tipo = 'religioso'
	if serv == 5:
		servicio = ubicacion.objects.filter(t_ubi="transporte")
		servicio_2 = transporte.objects.all()
		tipo = 'transporte'

	cont=0
	context={
		'cont':cont,
		'tipo':tipo,
		'servicio':servicio,
		'servicio_2':servicio_2,
	}
	return render(request,'mapa/list_serv.html',context)



@login_required
def edit_plaza(request,id):
	ubic = ubicacion.objects.get( id = id )
	if request.method == 'GET' :
		print("ingreso como get")
		print(ubic)
		ubi_form = FormUbicacion(instance = ubic )
		print(ubi_form)
	else:
		print("ingreso como post")
		ubi_form = FormUbicacion(request.POST, instance = ubic)
		if ubi_form.is_valid():
			ubi_form.save()
		redirect('crud:mapa')
	return render(request,'mapa/crud/new_ubi.html',{'ubi_form':ubi_form})

@login_required
def elim_plaza(request,id):
	ubic = ubicacion.objects.get( id = id )
	ubic.delete()
	return redirect('crud:listar_plaza')

@login_required
def crear_v_virtual(request):
	if request.method == 'POST':
		virtual_form = Formvirtual(request.POST)
		virt_valid= virtual_form.is_valid()
		if virt_valid:
			virtual_form.save()
			return redirect('crud:mapa')
	else:
		var_form = Formvirtual()

		context={
		'var_form':var_form,
			}
		return render(request,'v_virtual/form_virtual.html', context)

@login_required
def list_virtual(request):
	ubicaciones = ubicacion.objects.filter(t_ubi="plaza")
	virtuales = v_virtual.objects.all()
	url=[]
	for virtual in virtuales:
		url=virtual.url


	context ={
		'ubicaciones':ubicaciones,
		'virtuales':virtuales,
		'url':url,
	}
	return render(request,'v_virtual/list_virtual.html',context)


def env_mas_mail(request):
	asunto = 'prueba'
	mensaje = 'mensaje en masa 1'
	de = 'diegodevan789@gmail.com'
	para = ['diego.g.pablo@gmail.com','devangacia666@gmail.com','diegodevan789@gmail.com']
	para2=['diegodevan789@gmail.com']

	message1 = (asunto, mensaje, de, para)
	message2 = (asunto, mensaje, de, para)
	print(message1)
	send_mass_mail((message1, message2), fail_silently=False, auth_user=None, auth_password=None, connection=None)
	return redirect('crud:index')

def env_mail(request):
	usuarios = User.objects.all().values_list('email')
	print(usuarios)
	para=[]
	print(para)
	for usuario in usuarios:
		agregar=usuario[0]
		para.append(agregar)
	print(para)
	asunto = 'prueba'
	mensaje = 'mensaje de prueba en masa 0010'
	de = 'diegodevan789@gmail.com'

	send_mail(
    asunto,
    mensaje,
    de,
    para,
    fail_silently=False,
)
	return redirect('crud:index')

def Listar_usuarios(request):
	userss=User.objects.all()
	print(userss)
	context={
		'userss':userss
			}
	return render(request,'adm/crud/list_user.html',context)

def galeria(request):
	return render(request, 'galeria/galeria.html')

def p_materialize(request):
	return render(request, 'pruebas/p_materialize.html')