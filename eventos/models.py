from django.db import models

class Evento(models.Model):
    # Opciones para el tipo de evento
    CATEGORIAS = [
        ('DESFILE', 'Desfiles y Pregones'),
        ('CONCIERTO', 'Conciertos y Música'),
        ('REINA', 'Elección de Reinas'),
        ('RELIGIOSO', 'Actos Religiosos'),
        ('CINE', 'Cine en los Barrios'),
        ('TEATRO', 'Teatro y Cultura'),
        ('DEPORTE', 'Deportes'),
        ('BARRIO', 'Eventos Barriales'),
        ('OTRO', 'Otros'),
    ]
    # El campo nuevo
    categoria = models.CharField(
        max_length=20, 
        choices=CATEGORIAS, 
        default='OTRO'
    )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)
    
    # --- AQUÍ ESTÁ LA MAGIA ---
    es_megaevento = models.BooleanField(default=False, verbose_name="¿Es Megaevento?")
    tipo = models.CharField(max_length=20, choices=CATEGORIAS, default='OTRO')
    
    imagen_portada = models.URLField(max_length=500, null=True, blank=True)
    lugar_nombre = models.CharField(max_length=200)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    enlace_vivo = models.URLField(null=True, blank=True)

    def __str__(self):
        estrella = "⭐ MEGA - " if self.es_megaevento else ""
        return f"{estrella}{self.titulo}"