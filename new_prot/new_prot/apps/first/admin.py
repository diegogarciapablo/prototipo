from django.contrib import admin
from .models import ubicacion, e_comida, alojamiento, e_medico, e_religioso

# Register your models here.
admin.site.register(ubicacion)
admin.site.register(e_comida)

admin.site.register(alojamiento)

admin.site.register(e_medico)
admin.site.register(e_religioso)

