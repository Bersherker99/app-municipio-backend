from django.contrib import admin
from .models import Evento

# Esto hace que tu tabla aparezca en la web de administración
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'lugar_nombre') # Columnas que verás en la lista
    search_fields = ('titulo', 'lugar_nombre') # Buscador para encontrar eventos rápido