from django.core.management.base import BaseCommand
from eventos.models import Evento
from django.contrib.auth.models import User  # <--- IMPORTANTE
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Carga datos de prueba y crea un superusuario'

    def handle(self, *args, **kwargs):
        # 1. CREAR SUPERUSUARIO (Si no existe)
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('✅ ¡Usuario "admin" creado con contraseña "admin123"!'))
        else:
            self.stdout.write('ℹ️ El usuario admin ya existe.')

        # 2. BORRAR Y CREAR EVENTOS
        Evento.objects.all().delete()

        Evento.objects.create(
            titulo="Desfile de la Confraternidad",
            descripcion="El evento principal con carros alegóricos llenos de flores y frutas.",
            fecha_inicio=timezone.now() + timedelta(days=1),
            fecha_fin=timezone.now() + timedelta(days=1, hours=4),
            lugar="Av. Cevallos",
            imagen_portada="eventos/desfile.jpg",
            latitud=-1.2417,
            longitud=-78.6197
        )

        Evento.objects.create(
            titulo="Bendición de las Flores, Frutas y Pan",
            descripcion="Misa campal tradicional frente a la Catedral.",
            fecha_inicio=timezone.now() + timedelta(days=2),
            fecha_fin=timezone.now() + timedelta(days=2, hours=2),
            lugar="Atrio de la Catedral",
            imagen_portada="eventos/bendicion.jpg",
            latitud=-1.2417,
            longitud=-78.6197
        )

        self.stdout.write(self.style.SUCCESS('✅ ¡Datos de la fiesta cargados correctamente!'))