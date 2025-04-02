def breadcrumbs(request):
    # Puedes definir tus breadcrumbs basados en la URL
    path = request.path_info.split('/')
    breadcrumbs = [{'name': 'Inicio', 'url': '/'}]
    
    # Lógica para construir breadcrumbs dinámicos
    url_accum = ''
    for part in path[1:-1]:
        if part:
            url_accum += f'/{part}'
            breadcrumbs.append({
                'name': part.replace('-', ' ').title(),
                'url': url_accum
            })
    
    return {'breadcrumbs': breadcrumbs}