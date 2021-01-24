from django.urls import path

from .views import Index, Mapa, ListarPlaza, CreateUbicacion, confirm_plaza, confir_comi, confir_comer, confir_aloj, confir_edu, confir_medi, confir_reli
from .views import edit_plaza, elim_plaza, visit_virt

urlpatterns = [
	path('', Index, name='index'),
	path('map/',Mapa, name='mapa'),
	path('list_plaza/',ListarPlaza, name='listar_plaza'),

	path('ad_ubi_1/',CreateUbicacion, name='new_ubi'),
	path('ad_ubi_1/confir_plaza/', confirm_plaza, name='confir_plaza'),
	path('ad_ubi_1/confir_comi/', confir_comi, name='confir_comi'),
	path('ad_ubi_1/confir_comer/', confir_comer, name='confir_comer'),
	path('ad_ubi_1/confir_aloj/', confir_aloj, name='confir_aloj'),
	path('ad_ubi_1/confir_edu/', confir_edu, name='confir_edu'),
	path('ad_ubi_1/confir_medi/', confir_medi, name='confir_medi'),
	path('ad_ubi_1/confir_reli/', confir_reli, name='confir_reli'),

	path('edit_ubi_1/<int:id>', edit_plaza, name='edit_plaza'),

	path('elim_ubi_1/<int:id>', elim_plaza, name='elim_plaza'),

	path('ejemplo_visit_virt',visit_virt, name='visit_virt')

]

