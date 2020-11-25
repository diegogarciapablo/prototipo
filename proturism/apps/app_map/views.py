from django.shortcuts import render, redirect
from .form_lugar import FormLugar, FormSchool, FormChurch, FormLodgings, FormSquare, FormRestaurant
from .models import colegio, iglesia, plaza, restaurante, alojamiento, admin_agregar
from  django.core.exceptions import ObjectDoesNotExist

def MostrarMapa(request):
	m_lista = admin_agregar.objects.all()
	c_lista = colegio.objects.filter()
	i_lista = iglesia.objects.all()
	r_lista = restaurante.objects.all()
	p_lista = plaza.objects.all()
	a_lista = alojamiento.objects.all()
	return render(request,'mapa/mapa.html',{'m_lista': m_lista,'p_lista': p_lista,'i_lista': i_lista,'c_lista': c_lista,'a_lista': a_lista,'r_lista': r_lista})


def paso1(request):
	return render(request,'mapa/crud/choice_add.html')




def AñadirLugar(request):
	if request.method == 'POST':
		flugar=FormLugar(request.POST)
		rec_lug= request.POST.get('tipo')
		if flugar.is_valid():
			flugar.save()
			if(rec_lug=='colegio'):
				return redirect('AColegio/')
			if (rec_lug=='plaza'):
				return redirect('square/')
			if (rec_lug=='iglesia'):
				return redirect('church/')
			if (rec_lug=='restaurante'):
				return redirect('restaurant/')
			if (rec_lug=='alojamiento'):
				return redirect('lodgings/')
	else:
		flugar=FormLugar()
	return render(request,'mapa/formLugar.html', {'flugar': flugar})


def CrearColegio(request):
	if request.method=='POST':
		var_cole= FormSchool(request.POST)
		if var_cole.is_valid():
			var_cole.save()
			return redirect('mapa')
	else:
		var_cole = FormSchool()
	return render(request,'mapa/crud/lugares/form_colegio.html',{'var_cole': var_cole})


def CrearIglesia(request):
	if request.method=='POST':
		var_iglesia=FormChurch(request.POST)
		if var_iglesia.is_valid():
			var_iglesia.save()
			return redirect('mapa')
	else:
		var_iglesia=FormChurch()
	return render(request,'mapa/crud/lugares/form_iglesia.html',{'var_iglesia': var_iglesia})



def CrearAlojamiento(request):
	if request.method=='POST':
		var_alojamiento=FormLodgings(request.POST)
		if var_alojamiento.is_valid():
			var_alojamiento.save()
			return redirect('mapa')
	else:
		var_alojamiento=FormLodgings()
	return render(request,'mapa/crud/lugares/form_alojamiento.html',{'var_alojamiento': var_alojamiento})


def CrearPlaza(request):
	if request.method=='POST':
		var_plaza=FormSquare(request.POST)
		if var_plaza.is_valid():
			var_plaza.save()
			return redirect('mapa')
	else:
		var_plaza=FormSquare()
	return render(request,'mapa/crud/lugares/form_plaza.html',{'var_plaza': var_plaza})

def CrearRestaurante(request):
	if request.method=='POST':
		var_restau=FormRestaurant(request.POST)
		if var_restau.is_valid():
			var_restau.save()
			return redirect('mapa')
	else:
		var_restau=FormRestaurant()
	return render(request,'mapa/crud/lugares/form_restaurante.html',{'var_restau': var_restau})



def ListarColegio(request):
	c_lista = colegio.objects.all()
	return render(request,'mapa/crud/listar_colegio.html',{'c_lista': c_lista})


def ListarIglesia(request):
	i_lista = iglesia.objects.all()
	return render(request,'mapa/crud/listar_iglesia.html',{'i_lista': i_lista})


def ListarRestaurante(request):
	r_lista = restaurante.objects.all()
	return render(request,'mapa/crud/listar_restaurante.html',{'r_lista': r_lista})


def ListarPlaza(request):
	p_lista = plaza.objects.all()
	return render(request,'mapa/crud/listar_plaza.html',{'p_lista': p_lista})


def ListarAlojamiento(request):
	a_lista = alojamiento.objects.all()
	return render(request,'mapa/crud/listar_alojamiento.html',{'a_lista': a_lista})





def EditarColegio(request, cod_colegio):
	var_cole= None
	error = None
	try:
		e_colegio = colegio.objects.get(cod_colegio=cod_colegio)
		if request.method == 'GET':
			var_cole = FormSchool(instance = e_colegio)
		else:
			var_cole= FormSchool(request.POST, instance = e_colegio)
			if var_cole.is_valid():
				var_cole.save()
			return redirect('mapa')
	except ObjectDoesNotExist as e:
		error = e
	return render(request, 'mapa/crud/lugares/form_colegio.html',{'var_cole': var_cole, 'error': error})

def EditarIglesia(request, cod_iglesia):
	var_iglesia=None
	error=None
	try:
		e_iglesia = iglesia.objects.get(cod_iglesia=cod_iglesia)
		if request.method == 'GET':
			var_iglesia = FormChurch(instance = e_iglesia)
		else:
			var_iglesia=FormChurch(request.POST, instance = e_iglesia)
			if var_iglesia.is_valid():
				var_iglesia.save()
			return redirect('mapa')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'mapa/crud/lugares/form_iglesia.html', {'var_iglesia': var_iglesia, 'error': error})



def EditarAlojamiento(request, cod_alojamiento):
	var_alojamiento=None
	error=None
	try:
		e_alojamiento = alojamiento.objects.get(cod_alojamiento=cod_alojamiento)
		if request.method == 'GET':
			var_alojamiento = FormLodgings(instance = e_alojamiento)
		else:
			var_alojamiento=FormLodgings(request.POST, instance = e_alojamiento)
			if var_alojamiento.is_valid():
				var_alojamiento.save()
			return redirect('mapa')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'mapa/crud/lugares/form_alojamiento.html', {'var_alojamiento': var_alojamiento, 'error': error})


def EditarPlaza(request, cod_plaza):
	var_plaza=None
	error=None
	try:
		e_plaza = plaza.objects.get(cod_plaza=cod_plaza)
		if request.method == 'GET':
			var_plaza = FormSquare(instance = e_plaza)
		else:
			var_plaza=FormSquare(request.POST, instance = e_plaza)
			if var_plaza.is_valid():
				var_plaza.save()
			return redirect('mapa')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'mapa/crud/lugares/form_plaza.html', {'var_plaza': var_plaza, 'error': error})



def EditarRestaurante(request, cod_restaurante):
	var_restau=None
	error=None
	try:
		e_restaurante = restaurante.objects.get(cod_restaurante=cod_restaurante)
		if request.method == 'GET':
			var_restau = FormRestaurant(instance = e_restaurante)
		else:
			var_restau=FormRestaurant(request.POST, instance = e_restaurante)
			if var_restau.is_valid():
				var_restau.save()
			return redirect('mapa')
	except ObjectDoesNotExist as e:
		error=e
	return render(request,'mapa/crud/lugares/form_restaurante.html', {'var_restau': var_restau, 'error': error})


def EliminarColegio(request, cod_colegio):
	var_cole = colegio.objects.get(cod_colegio=cod_colegio)
	var_cole.delete()
	return redirect('crud:list_colegio')


def EliminarIglesia(request, cod_iglesia):
	var_iglesia = iglesia.objects.get(cod_iglesia=cod_iglesia)
	var_iglesia.delete()
	return redirect('crud:list_iglesia')


def EliminarPlaza(request, cod_plaza):
	var_plaza = plaza.objects.get(cod_plaza=cod_plaza)
	var_plaza.delete()
	return redirect('crud:list_plaza')


def EliminarRestaurante(request, cod_restaurante):
	var_restau = restaurante.objects.get(cod_restaurante=cod_restaurante)
	var_restau.delete()
	return redirect('crud:list_restaurante')

def EliminarAlojamiento(request, cod_alojamiento):
	var_alojamiento = alojamiento.objects.get(cod_alojamiento=cod_alojamiento)
	var_alojamiento.delete()
	return redirect('crud:list_alojamiento')

def Index(request):
	return render(request, 'main.html')