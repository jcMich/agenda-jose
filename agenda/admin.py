from django.contrib import admin

# Register your models here.
from agenda.models import Contactos, Grupos, Colores


admin.site.register(Colores)
admin.site.register(Grupos)
admin.site.register(Contactos)
