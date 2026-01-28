from django.contrib import admin
from django.urls import path, include
from eventos import views
from rest_framework import routers
from django.http import HttpResponse
from django.contrib.auth.models import User  # <--- NUEVO: Para crear el usuario

# 1. Creamos el Router (El mapa de la API)
router = routers.DefaultRouter()
router.register(r'eventos', views.EventoViewSet)

# Vista de bienvenida
def home(request):
    return HttpResponse("<h1>🚀 ¡API del Municipio Funcionando!</h1><p>Prueba ir a <a href='/api/eventos/'>Ver lista de eventos (JSON)</a></p>")

# 👇 FUNCIÓN SECRETA (NUEVA)
def crear_admin(request):
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', '', 'admin123')
            return HttpResponse("<h1>¡ÉXITO! 🎉</h1><p>Usuario creado: <b>admin</b></p><p>Contraseña: <b>admin123</b></p>")
        else:
            return HttpResponse("<h1>¡Ya existe! ⚠️</h1><p>El usuario 'admin' ya estaba creado. Intenta entrar.</p>")
    except Exception as e:
        return HttpResponse(f"<h1>Error ☠️</h1><p>{str(e)}</p>")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    
    # Tu API original
    path('api/', include(router.urls)), 
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),

    # 👇 LA RUTA SECRETA (NUEVA)
    path('crear_super_usuario_secreto/', crear_admin),
]