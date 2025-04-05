import json
from django.core.management.commands.dumpdata import Command as DumpDataCommand
from django.core.serializers.json import DjangoJSONEncoder

class Command(DumpDataCommand):
    def handle(self, *args, **options):
        # Obtener los datos como diccionario
        data = super().handle(*args, **options)
        
        # Configurar el archivo de salida
        output_file = options.get('output')
        indent = options.get('indent')
        
        # Escribir en UTF-8 sin BOM
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, cls=DjangoJSONEncoder, indent=indent, ensure_ascii=False)