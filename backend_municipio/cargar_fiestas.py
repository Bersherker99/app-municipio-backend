import os
import django
from datetime import datetime

# 1. Configurar Django para que funcione fuera de la web
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_municipio.settings')
django.setup()

from eventos.models import Evento

# 2. Lista de Eventos extraídos del Programa FFF 2026
# Nota: He puesto coordenadas genéricas de Ambato, luego podrás ajustarlas en el mapa.
lista_eventos = [
    {
        "titulo": "Pregón de Fiestas",
        "descripcion": "Inicio oficial de las fiestas con comparsas y alegría.",
        "fecha": "2026-02-07 09:00",
        "lugar": "Calles de la Ciudad (Av. Cevallos)",
        "imagen": "pregon.jpg"
    },
    {
        "titulo": "Elección Reina de Ambato 2026",
        "descripcion": "Gala de elección de la nueva soberana de la ciudad.",
        "fecha": "2026-02-07 19:00",
        "lugar": "Coliseo Cerrado de Deportes",
        "imagen": "reina.jpg"
    },
    {
        "titulo": "Bendición de las Flores, Frutas y Pan",
        "descripcion": "Acto litúrgico tradicional y monumental alegoría.",
        "fecha": "2026-02-14 09:00",
        "lugar": "Atrio de la Catedral",
        "imagen": "bendicion.jpg"
    },
    {
        "titulo": "Fiesta Retro (Vilma Palma e Vampiros)",
        "descripcion": "Concierto internacional de música retro.",
        "fecha": "2026-02-14 19:00",
        "lugar": "Explanada GADMA Sur",
        "imagen": "retro.jpg"
    },
    {
        "titulo": "Desfile de la Fiesta de la Fruta y de las Flores",
        "descripcion": "El evento central con carros alegóricos y comparsas.",
        "fecha": "2026-02-15 09:00",
        "lugar": "Av. Cevallos y Bolívar",
        "imagen": "desfile.jpg"
    },
    {
        "titulo": "Mega Evento: Andrés Cepeda",
        "descripcion": "Concierto internacional gratuito.",
        "fecha": "2026-02-15 19:00",
        "lugar": "Explanada GADMA Sur",
        "imagen": "cepeda.jpg"
    },
    {
        "titulo": "Ronda Nocturnal",
        "descripcion": "Desfile nocturno lleno de luces y magia.",
        "fecha": "2026-02-16 19:00",
        "lugar": "Av. Cevallos y Bolívar",
        "imagen": "ronda.jpg"
    },
    {
        "titulo": "Mega Evento: Danny Ocean",
        "descripcion": "Gran cierre con artista internacional.",
        "fecha": "2026-02-16 21:00",
        "lugar": "Explanada GADMA Sur",
        "imagen": "danny.jpg"
    }
]

print("--- INICIANDO CARGA DE EVENTOS FFF 2026 ---")

for datos in lista_eventos:
    # Crear el evento en la base de datos
    Evento.objects.create(
        titulo=datos["titulo"],
        descripcion=datos["descripcion"],
        fecha_inicio=datos["fecha"],
        fecha_fin=datos["fecha"], # Por ahora ponemos la misma, luego puedes editar
        lugar_nombre=datos["lugar"],
        latitud=-1.241667,  # Coordenada centro Ambato (Editables luego)
        longitud=-78.619722,
        imagen_portada=None # Se cargará sin foto por ahora
    )
    print(f"✅ Cargado: {datos['titulo']}")

print("--- ¡CARGA COMPLETADA! REVISA TU PANEL DE ADMIN ---")