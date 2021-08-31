from django.urls import path

from django.contrib.auth import views as auth_views

from .views import *



urlpatterns = [
	path('', Index, name='index'),
	path('administracion/', Adm_Site, name='adm_site'),
	path('registro/', registro, name='registro'),
	path('logout/',logout_request,name="logout"),
	path('login/',login_request,name="login"),

	path('map/',Mapa, name='mapa'),
	path('list_plaza/',ListarPlaza, name='listar_plaza'),
	path('list_user/',Listar_usuarios,name='list_user'),
	path('list_serv/<int:serv>/',ListarServicios, name='list_serv'),

	path('ad_ubi_1/', CreateUbicacion, name='new_ubi'),
	path('ad_ubi_1/confir_plaza/', confirm_plaza, name='confir_plaza'),
	path('ad_ubi_1/confir_comi/', confir_comi, name='confir_comi'),
	path('ad_ubi_1/confir_aloj/', confir_aloj, name='confir_aloj'),
	path('ad_ubi_1/confir_medi/', confir_medi, name='confir_medi'),
	path('ad_ubi_1/confir_reli/', confir_reli, name='confir_reli'),
	path('ad_ubi_1/confir_trans/', confir_trans, name='confir_trans'),

	path('edit_ubi_1/<int:id>', edit_plaza, name='edit_plaza'),

	path('elim_ubi_1/<int:id>', elim_plaza, name='elim_plaza'),

	path('ejemplo_visit_virt',visit_virt, name='visit_virt'),

	path('ad_ubi_virt',crear_v_virtual,name='crear_v_virtual'),
	path('list_virtual',list_virtual, name='list_virtual'),

	path('env_mail',env_mail,name='env_mail'),

	path('galeria',galeria,name='galeria'),

	path('p_materialize',p_materialize,name='p_materialize')
]

