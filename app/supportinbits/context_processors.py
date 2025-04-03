from django.urls import resolve, Resolver404
from django.apps import apps

def breadcrumbs(request):
    breadcrumbs = [{'name': 'Inicio', 'url': '/'}]
    
    try:
        resolved = resolve(request.path_info)
        url_name = resolved.url_name
        
        # Mapeo de nombres de URL a nombres amigables
        name_mapping = {
            '/': 'Inicio',
            'cookies': 'Cookies',
            'about': 'Quien soy',
            'politicas': 'Politíca de Privacidad',
            'test': 'Pagina de testeo',
            # Añade más mapeos según necesites
        }
        
        # Si es una URL conocida, usa el nombre mapeado
        if url_name in name_mapping:
            breadcrumbs.append({
                'name': name_mapping[url_name],
                'url': request.path
            })
        else:
            # Lógica genérica para URLs no mapeadas
            path_parts = [p for p in request.path.split('/') if p]
            current_url = ''
            
            for i, part in enumerate(path_parts):
                current_url += f'/{part}'
                breadcrumbs.append({
                    'name': part.replace('-', ' ').title(),
                    'url': current_url if i < len(path_parts)-1 else None
                })
    
    except Resolver404:
        pass
    
    return {'breadcrumbs': breadcrumbs}