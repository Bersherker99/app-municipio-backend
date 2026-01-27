from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eventos.views import EventoViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from eventos import views

# Esto crea las rutas automáticas para la API
router = DefaultRouter()
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include(router.urls)), # La puerta de entrada para la app
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 