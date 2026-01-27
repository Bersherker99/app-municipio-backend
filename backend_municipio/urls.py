from django.contrib import admin
from django.urls import path, include
from eventos import views
from rest_framework import routers  # <--- IMPORTANTE: Herramienta para APIs
from django.http import HttpResponse

# 1. Creamos el Router (El mapa de la API)
router = routers.DefaultRouter()
router.register(r'eventos', views.EventoViewSet)

# Vista de bienvenida
def home(request):
    return HttpResponse("<h1>🚀 ¡API del Municipio Funcionando!</h1><p>Prueba ir a <a href='/api/eventos/'>Ver lista de eventos (JSON)</a></p>")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    
    # 👇 ESTA ES LA LÍNEA QUE FALTABA:
    path('api/', include(router.urls)), 
    
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
]