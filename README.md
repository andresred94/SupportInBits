# SuppportInBits - TFG 2º DAW.

**autor: Andres Martin Bravo Castro**

**version(Pre-Alfa): 0.0.0**

Este fichero es una guía detallada de cómo instalar las herramientas necesarias para instalar, desarrollar y desplegar una aplicación web hecha con el framework Django de Python.

# Índice

- ## [Instalación](#install)
  - ### [Requisitos previos](#require-prev)
    - #### [Instalación de requisitos previos](#install-req)
- ## [Despliegue de app](#deploy)
- ## [Desarrollo de la app](#dev)
  - ### [placeholder](#placeholder)
    - #### [placeholder](#placeholder)
      - ##### [placeholder](#placeholder)
        - ###### [placeholder](#placeholder)
- ## [Webgrafia](#docs)

<div id='install' />

## Instalación

<div id='require-prev' />

### Requisitos previos

Para poder crear cualquier proyecto usando Django y Python primero tenemos que intalar python para ello en la
[documentación oficial de Python](https://wiki.python.org/moin/BeginnersGuide/Download) se encuentran las
guías detalladas de cómo instalar python dependiendo de tu sistema operativo.

**NOTA: cuando instales python asegurate de marcar la opción "anádir al PAth"**

<div id='install-req' />

#### Instalación de requisitos previos

Para la instalación de los modulos necesarios abre una terminal en la **carpeta**
**raíz del proyecto** y ejecuta el comando `pip install -r .\app\requirements.txt` en caso de Linux es **pip3** 
Dentro del fichero se encuentran todos los modulos necesarios para que esta aplicación funcione.
Esta instalación de los modulos es necesaria tanto en desarrollo como producción de la aplicación.

---

<div id='dev' />

## Ejecutar la aplicación en modo desarrollo
Para ejecutar esta aplicación en modo de desarrollo simplemente tenemos que ejecutar el siguiente comando:

En Windows `py manage.py runserver `
En Linux `python3 manage.py runserver `

---

<div id='deploy' />

## Despliegue de la aplicación en AWS
Para desplegar la aplicación web en AWD tenemos que tener una instancia de
EC2 en nuestra cuenta de AWS. Una vez que tengamos acceso y podamos acceder al servidor en remoto podemos empezar a desplegar la web. 

--- 

<div id='docs' />

## Webgrafía

- [Guía para principiantes de Python](https://wiki.python.org/moin/BeginnersGuide)
- [Guía de instalación de Django](https://docs.djangoproject.com/en/5.1/)
- []()
