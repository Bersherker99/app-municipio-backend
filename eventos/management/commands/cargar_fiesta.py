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
            descripcion="El evento principal con carros alegóricos llenos de flores y frutas.",
            fecha_inicio=timezone.now() + timedelta(days=1),
            fecha_fin=timezone.now() + timedelta(days=1, hours=4),
            lugar="Av. Cevallos",
            imagen_portada="eventos/desfile.jpg" 
        )

        # Evento 2
        Evento.objects.create(
            titulo="Bendición de las Flores, Frutas y Pan",
            descripcion="Misa campal tradicional frente a la Catedral.",
            fecha_inicio=timezone.now() + timedelta(days=2),
            fecha_fin=timezone.now() + timedelta(days=2, hours=2),
            lugar="Atrio de la Catedral",
            imagen_portada="eventos/bendicion.jpg"
        )

        self.stdout.write(self.style.SUCCESS('✅ ¡Datos de la fiesta cargados correctamente!'))