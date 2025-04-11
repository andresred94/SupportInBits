from django.core.management.base import BaseCommand
from blog.models import Seccion, Categoria

class Command(BaseCommand):
    help = 'Carga las secciones y categorías iniciales del blog'
    
    def handle(self, *args, **options):
        secciones_data = [
            {
                'nombre': 'Tutoriales',
                'categorias': ['Accesibilidad', 'Redes', 'Ordenadores']
            },
            {
                'nombre': 'Reviews',
                'categorias': ['Dispositivos móviles', 'Portátiles']
            },
            {
                'nombre': 'Guías oficiales',
                'categorias': ['Python', 'Django','W3C']
            },
            {
                'nombre': 'SEO',
                'categorias': ['Posicionamiento web','Marketing digital']
            },
            {
                'nombre': 'Compartiendo arte',
                'categorias': ['Música','Libros','Artistas']
            }
        ]
        
        for seccion_info in secciones_data:
            seccion, created = Seccion.objects.get_or_create(nombre=seccion_info['nombre'])
            if created:
                self.stdout.write(self.style.SUCCESS(f'Sección creada: {seccion.nombre}'))
            
            for categoria_nombre in seccion_info['categorias']:
                categoria, created = Categoria.objects.get_or_create(
                    nombre=categoria_nombre,
                    seccion=seccion
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Categoría creada: {categoria.nombre} en {seccion.nombre}'))
        
        self.stdout.write(self.style.SUCCESS('Datos iniciales cargados correctamente'))