from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView

from .forms_first import FormUbicacion, FormEComida, FormZComercial, FormAlojamiento, FormEEducativo, FormEMedico, FormEReligioso
from .models import ubicacion, e_comida, z_comercial, alojamiento, e_educativo, e_medico, e_religioso
from  django.core.exceptions import ObjectDoesNotExist
import folium


def Index(request):
	return render(request,'main.html' )

def visit_virt(request):
	return render(request, 'mapa/crud/pruebas/list_test.html')

def Mapa(request):
	#obteniendo datos de la db
	lat_lista = ubicacion.objects.all().values_list()
	ca_lista = e_comida.objects.all().values_list()
	cl_lista = z_comercial.objects.all().values_list()
	a_lista = alojamiento.objects.all().values_list()
	e_lista = e_educativo.objects.all().values_list()
	m_lista = e_medico.objects.all().values_list()
	r_lista = e_religioso.objects.all().values_list()
	grupo_plaza=folium.FeatureGroup(name='plazas')
	grupo_comidas=folium.FeatureGroup(name='e. comidas')
	grupo_comercial=folium.FeatureGroup(name='z. comerciales')
	grupo_alojamiento=folium.FeatureGroup(name='alojamientos')
	grupo_educativo=folium.FeatureGroup(name='e. educativos')
	grupo_medico=folium.FeatureGroup(name='e. medicos')
	grupo_religioso=folium.FeatureGroup(name='e. religiosos')


	#llenando Iframe


	#creando mapa
	m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, tiles='cartodbpositron',)
	#marcadores y estableciendo capas
	for x in lat_lista:
		print(x[0])
		if x[1]=='plaza':
			v_icon=folium.Icon(color='green',icon='tree-conifer')
			v_popup="la "+x[1]+" "+x[2]+" "+x[3]
			feature_g=grupo_plaza
		if x[1]=='comida':
			v_icon=folium.Icon(color='orange',icon='cutlery')
			v_popup=" "+x[2]+" "+x[3]
			feature_g=grupo_comidas
		if x[1]=='comercial':
			v_icon=folium.Icon(color='black',icon='shopping-cart')
			v_popup="zona comercial"
			feature_g=grupo_comercial
		if x[1]=='alojamiento':
			v_icon=folium.Icon(color='blue',icon='home')
			v_popup="alojamiento"
			feature_g=grupo_alojamiento
		if x[1]=='educativo':
			v_icon=folium.Icon(color='gray',icon='ok-sign')
			v_popup="establecimiento educativo"
			feature_g=grupo_educativo
		if x[1]=='medico':
			v_icon=folium.Icon(color='red',icon='plus')
			v_popup="edificio medico"
			feature_g=grupo_medico
		if x[1]=='religioso':
			v_icon=folium.Icon(color='green',icon='ok-sign')
			v_popup="establecimiento religioso"
			feature_g=grupo_religioso

		folium.Marker(location=[x[4],x[5]], popup=v_popup,icon =v_icon ).add_to(feature_g)

	#agregando capas y control de capas
	m.add_child(grupo_plaza)
	m.add_child(grupo_comidas)
	m.add_child(grupo_comercial)
	m.add_child(grupo_alojamiento)
	m.add_child(grupo_educativo)
	m.add_child(grupo_medico)
	m.add_child(grupo_religioso)
	m.add_child(folium.map.LayerControl())
	# representacion html del mapa
	m = m._repr_html_()
	context={
		'm': m,
			}
	return render(request, 'prueba map.html', context)



def CreateUbicacion(request):
	if request.method == 'POST':
		rec_lug= request.POST.get('t_ubi')
		print(rec_lug)
		ubicacion_form = FormUbicacion(request.POST)
		print('se imprimira ubicacion form')
		print(ubicacion_form)
		ubi_valid= ubicacion_form.is_valid()
		print(ubi_valid)
		if ubi_valid:
			ubicacion_form.save()
			if(rec_lug=='plaza'):
				return redirect('confir_plaza/')
			if (rec_lug=='comida'):
				return redirect('confir_comi/')
			if (rec_lug=='comercial'):
				return redirect('confir_comer/')
			if (rec_lug=='alojamiento'):
				return redirect('confir_aloj/')
			if (rec_lug=='educativo'):
				return redirect('confir_edu/')
			if (rec_lug=='medico'):
				return redirect('confir_medi/')
			if (rec_lug=='religioso'):
				return redirect('confir_reli/')
	else:
		ubicacion_form=FormUbicacion()
		#creando mapa
		m = folium.Map(location=[-22.01392810529076, -63.677741626018076], zoom_start=16, )
		# obtencion de coordenadas
		m.add_child(folium.LatLngPopup())
		# representacion html del mapa
		m = m._repr_html_()
		context={
		'm': m,
		'ubi_form':ubicacion_form,
			}
		return render(request,'mapa/crud/new_ubi.html', context)

def confirm_plaza(request):
	if request.method == 'POST':
		return redirect('mapa')
	else:
		ult_ubis = ubicacion.objects.all().values_list()
		mark_lat=""
		mark_long=""
		popup=""
		for y in ult_ubis:
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
			}
		return render(request,'mapa/crud/confir_ubi_plaza.html', context)

def confir_comi(request):
	if request.method == 'POST':
		comida_form = FormEComida(request.POST)
		comi_valid= comida_form.is_valid()
		if comi_valid:
			comida_form.save()
			return redirect('mapa')
	else:
		var_form = FormEComida()
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
		'var_form':var_form,
		'foreig':foreig,
			}
		return render(request,'mapa/crud/confir_ubi_comi.html', context)

def confir_comer(request):
	if request.method == 'POST':
		print("llegada de metodo")
		comercial_form = FormZComercial(request.POST)
		print("carga de coercial_form")
		comer_valid= comercial_form.is_valid()
		print(comer_valid)
		if comer_valid:
			print("entro al if")
			comercial_form.save()
			print("guardado")
			return redirect('mapa')
	else:
		var_form = FormZComercial()
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
		'var_form':var_form,
		'foreig':foreig,
			}
		return render(request,'mapa/crud/confir_ubi_comer.html', context)

def confir_aloj(request):
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
			return redirect('mapa')
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

def confir_edu(request):
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
			return redirect('mapa')
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

def confir_medi(request):
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
			return redirect('mapa')
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

def confir_reli(request):
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
			return redirect('mapa')
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

# Create your views here.
def ListarPlaza(request):
	plazas = ubicacion.objects.filter(t_ubi="plaza")

	comidas = ubicacion.objects.filter(t_ubi="comida")
	comidas_2 = e_comida.objects.all()

	comerciales = ubicacion.objects.filter(t_ubi="comercial")
	comerciales_2 = z_comercial.objects.all()

	alojamientos = ubicacion.objects.filter(t_ubi="alojamiento")
	alojamientos_2 = alojamiento.objects.all()

	educativos = ubicacion.objects.filter(t_ubi="educativo")
	educativos_2 = e_educativo.objects.all()

	medicos = ubicacion.objects.filter(t_ubi="medico")
	medicos_2 = e_medico.objects.all()

	religiosos = ubicacion.objects.filter(t_ubi="religioso")
	religiosos_2 = e_religioso.objects.all()

	context={
		'plazas':plazas,
		'comidas':comidas,
		'comidas_2':comidas_2,
		'comerciales':comerciales,
		'comerciales_2':comerciales_2,
		'alojamientos':alojamientos,
		'alojamientos_2':alojamientos_2,
		'educativos':educativos,
		'educativos_2':educativos_2,
		'medicos':medicos,
		'medicos_2':medicos_2,
		'religiosos':religiosos,
		'religiosos_2':religiosos_2,
			}
	return render(request,'mapa/list plaza.html',context)

def Formubi(request):
	return render(request,'prueba map.html',{'formubi':FormUbicacion})

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
		redirect('mapa')
	return render(request,'mapa/crud/new_ubi.html',{'ubi_form':ubi_form})

def elim_plaza(request,id):
	ubic = ubicacion.objects.get( id = id )
	ubic.delete()
	return redirect('crud:listar_plaza')
