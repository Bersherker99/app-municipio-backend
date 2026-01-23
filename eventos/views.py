from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by('fecha_inicio')
    serializer_class = EventoSerializer