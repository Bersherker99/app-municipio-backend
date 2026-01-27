from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer
# 👇 AGREGA ESTAS 2 LÍNEAS NUEVAS AL PRINCIPIO 👇
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by('fecha_inicio')
    serializer_class = EventoSerializer

# 👇 AGREGA ESTO AL FINAL DEL ARCHIVO (FUERA DE LA CLASE) 👇
def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return HttpResponse(f"<h1>Detalle del Evento {evento_id}</h1>")