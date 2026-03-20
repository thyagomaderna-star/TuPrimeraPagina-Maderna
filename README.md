


# MI Primera Pagina Web - Cine App 

Un proyecto de aplicación web desarrollado con **Python** y el framework **Django**. 

## Características
* Interfaz sencilla y fácil de usar.
* Gestión de entornos virtuales y dependencias mediante `pipenv`.

## Tecnologías Utilizadas
* **Lenguaje:** Python
* **Framework Web:** Django
* **Gestor de Entorno:** Pipenv
* **Base de Datos:** SQLite (por defecto en Django)

## Instalación y Ejecución Local

Si querés clonar este proyecto y correrlo en tu máquina, seguí estos pasos:

1. **Clonar el repositorio:**
* **Abrir terminal** 
Se recomienda utilizar la terminarl Git Bash, aunque puede utilizarse PowerShell o cmd. Abrir la terminal en el directorio donde quiera guardar el repositorio.

* **Ejecución de comandos** 
al tener preparada la ubicación, usaremos los siguientes comandos.

 `git clone https://github.com/thyagomaderna-star/TuPrimeraPagina-Maderna.git`

 luego para entrar al repositorio desde la terminal.

 `cd TuPrimeraPagina-Maderna `

 por ultimo este comando nos abrirá Visual Studio Code.

 `code .`

 2. **Instalar técnologias y frameworks**
 
* **Ejecución de comandos** 
Utilizaremos Python y Django como técnologias principales y Pipenv para nuestra maquina virtual, por lo que necesitaremos instalar las librerias.
En nuestro IDE, abriremos una nueva terminal donde se encuentra nuestro proyecto y usaremos los siguientes comandos:

`pip install python `

 `python -m pip install pipenv `

  `python -m pipenv install django`

Luego de que ejecutemos los comandos para tener las librerias, con el siguiente y ultimo comando, ejecutaremos la aplicación Web.  

 `python -m pipenv run python manage.py runserver`
