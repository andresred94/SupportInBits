- ## [Comandos utilizados](#all-cmd)
  - ### [Comandos de git](#cmd-git)
  - ### [Comandos de python](#cmd-python)
  - ### [Comandos de ubuntu server](#cmd-server)

--- 

<div id='all-cmd' />

## Comandos utilizados

--- 

<div id='cmd-git' />

### comandos de git

> `git fetch origin` Descarga cambios sin modificar archivos\
> `git merge origin/main` Fusiona cambios en tu rama (reemplaza "main" por tu rama)\
> `git pull origin main` Descarga y fusiona cambios (reemplaza "main" por tu rama)\
> `git status` Comprueba los archivos modificados\
> `git add .` Añade todos los archivos modificados\
> `git commit -m "Descripción breve de los cambios" ` Crea un commit con los archivos añadidos\
> `git branch` Para saber en qué rama estás\
> `git push origin <nombre-de-la-rama> ` Envia los cambios al repo remoto\
> `git branch nombre-de-la-rama` crea una rama\
> `git checkout nombre-de-la-rama` cambia a la rama\
> `git checkout -b nombre-de-la-rama` crea una rama y te cambia a esa rama\
> `git switch -c nombre-de-la-rama` en git > 2.23 cambia a la rama indicada\
> `git checkout nombre-de-la-rama` cambia a la rama indicada\
> `git merge nombre-de-la-rama` fusiona la rama que 

--- 

### comandos de python
<div id='cmd-python' />

> `py manage.py check` comprueba cualquier error en el proyecto\
> `py -m pip install mysql-connector-python` descarga e instala el  conector de MySQL\
> `pip install django-bootstrap-v5` comando para instalar BootStrap con python\
> `pip3 install -r requirements.txt` para instalar dependencias\
> `python manage.py migrate --database=nombre_baseDdatos` Para MongoDB (si usas Djongo)\
> `pip install django-breadcrumbs` instala migas de pan de bootstrap\
> `python manage.py collectstatic` coleccionar archivos estáticos

--- 

### comandos de django
<div id='cmd-python' />

> `python manage.py startapp {nombre de la pp}` crea una app en tu proyecto en Windows\
> `python3 manage.py startapp {nombre de la pp}` crea una app en tu proyecto en Linux\
> `pip install django-cookie-consent` instala el paquete de cookies de django 
> `$ python manage.py createsuperuser` crea un usuario que se añade a la base de datos SQLite3 

--- 

### comandos de ubuntu server
<div id='cmd-server' />

> `sudo systemctl stop nginx.service ` detiene el servidor nginx\
> `sudo systemctl daemon-reload` recarga el daemon de gunicorn\
> `sudo systemctl restart gunicorn` reinicia el servicio\
> `sudo systemctl restart nginx`reinicia el servicio\