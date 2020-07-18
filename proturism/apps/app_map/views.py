from django.shortcuts import render
from  django.core.exceptions import ObjectDoesNotExist

def MostrarMapa(request):
	'''m_lista = admin_agregar.objects.all()
	c_lista = colegio.objects.filter()
	i_lista = iglesia.objects.all()
	r_lista = restaurante.objects.all()
	p_lista = plaza.objects.all()
	a_lista = alojamiento.objects.all()
	return render(request,'mapa_main/mapa.html',{'m_lista': m_lista,'p_lista': p_lista,'i_lista': i_lista,'c_lista': c_lista,'a_lista': a_lista,'r_lista': r_lista})'''
	return render(request,'mapa.html')