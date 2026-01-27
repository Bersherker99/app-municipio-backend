from django.core.management.base import BaseCommand
from eventos.models import Evento
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Carga datos de prueba para la Fiesta de la Fruta y de las Flores'

    def handle(self, *args, **kwargs):
        Evento.objects.all().delete() # Limpia lo viejo

        # Evento 1
        Evento.objects.create(
            titulo="Desfile de la Confraternidad",
            descripcion="El evento principal con carros alegóricos...",
            fecha_inicio=timezone.now() + timedelta(days=1),
            fecha_fin=timezone.now() + timedelta(days=1, hours=4),
            imagen_portada="eventos/desfile.jpg",
            # 👇 AGREGA ESTAS DOS LÍNEAS:
            latitud=-1.2417,
            longitud=-78.6197
        )

        # Evento 2
        Evento.objects.create(
            titulo="Bendición de las Flores...",
            descripcion="Misa campal tradicional...",
            fecha_inicio=timezone.now() + timedelta(days=2),
            fecha_fin=timezone.now() + timedelta(days=2, hours=2),
            imagen_portada="eventos/bendicion.jpg",
            # 👇 AGREGA ESTAS DOS LÍNEAS TAMBIÉN AQUÍ:
            latitud=-1.2417,
            longitud=-78.6197
        )
        self.stdout.write(self.style.SUCCESS('✅ ¡Datos de la fiesta cargados correctamente!'))