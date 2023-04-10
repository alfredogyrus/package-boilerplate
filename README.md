# Boilerplate para paquete software en Python
## Entorno virtual
Lo primero que debes hacer es instalar `pipenv` utilizando `pip`. Ejecuta el comando `pip install pipenv` en tu terminal para instalarlo.

Crear un nuevo entorno virtual. Para crear un nuevo entorno virtual, ejecuta el comando `pipenv --python 3.x`, donde 3.x es la versión de Python que deseas utilizar en tu entorno virtual. Este comando creará automáticamente un nuevo entorno virtual y un archivo Pipfile que contendrá una lista de las dependencias de tu proyecto.

Instalar paquetes. Para instalar paquetes en tu entorno virtual, utiliza el comando `pipenv install paquete`. Este comando instalará el paquete especificado en el entorno virtual y actualizará automáticamente el archivo Pipfile.

Activar el entorno virtual. Para activar el entorno virtual, ejecuta el comando `pipenv shell`. Esto abrirá una nueva terminal con el entorno virtual activado. Todas las dependencias que hayas instalado en el entorno virtual estarán disponibles en esta terminal.

Cuando el paquete software se encuentre listo, recuerda generar el archivo de requisitos. Para generar un archivo de requisitos a partir de tu entorno virtual, utiliza el comando `pipenv lock -r > requirements.txt`. Este comando generará un archivo `requirements.txt` en el directorio actual que contendrá una lista de todas las dependencias instaladas en el entorno virtual junto con sus versiones correspondientes.

Una vez que se ha generado el archivo requirements.txt, es recomendable revisar y editar el archivo según sea necesario. Puedes agregar o eliminar dependencias manualmente según tus necesidades.

Para utilizar el archivo de requisitos en otro entorno virtual o en un servidor de producción, simplemente instala las dependencias del archivo de requisitos utilizando el comando `pip install -r requirements.txt`.

---
## Software
El primer paso para crear un paquete de software es crear una estructura de directorios que contenga los archivos de código fuente y otros recursos necesarios. Para ello, podrías crear una carpeta con el nombre de tu paquete y dentro de ella, crear un archivo `__init__.py` vacío y otra carpeta con el mismo nombre que contendrá el código fuente y otros recursos.

```
package-boilerplate/
└── src/
    └── example_package/
        ├── __init__.py
        └── example.py
```

Dentro de la carpeta de código fuente, escribe el código que conformará tu paquete. Divide el código en módulos y organiza los archivos según su funcionalidad.

```
package-boilerplate/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

---
## Variables de entorno
Instalar el paquete `python-dotenv`. Lo primero que debes hacer es instalar el paquete `python-dotenv` utilizando `pip`. Ejecuta el comando `pip install python-dotenv` en tu terminal para instalarlo.

Crea un archivo llamado `.env` en la raíz de tu proyecto. Este archivo contendrá las variables de entorno que quieras cargar. Puedes agregar una variable de entorno por línea en el formato `NOMBRE_VARIABLE=VALOR_VARIABLE`.

En tu código, puedes cargar las variables de entorno utilizando el paquete `dotenv`. Importa el paquete y llama al método `load_dotenv()` al principio de tu código. Esto cargará automáticamente todas las variables de entorno definidas en el archivo `.env` en el entorno de tu aplicación.

Para acceder a las variables de entorno cargadas, utiliza el método `os.environ.get('NOMBRE_VARIABLE')` en tu código. Esto te devolverá el valor de la variable de entorno especificada.

Es importante agregar el archivo `.env` a tu archivo `.gitignore` o al control de versiones que estés utilizando para evitar que las variables de entorno se compartan accidentalmente con otros desarrolladores.

---

## Fichero de configuración
Instalar la biblioteca `toml`. Antes de poder utilizar toml en tus proyectos de Python, debes instalar la biblioteca `toml`. Puedes instalarlo fácilmente utilizando `pip`. Simplemente ejecuta el comando `pip install toml` en tu terminal para instalarlo.

Crear un archivo `config.toml`. Para utilizar `toml` para la configuración de tu proyecto, crea un archivo `config.toml` en tu proyecto. Este archivo debe contener la configuración para tu proyecto, organizada en secciones y claves. Por ejemplo, un archivo `config.toml` para una aplicación web podría verse así:

```
[server]
host = "0.0.0.0"
port = 8000

[database]
url = "sqlite:///database.sqlite"
```

Para leer la configuración desde el archivo `config.toml`, utiliza la biblioteca `toml`. Puedes leer el archivo utilizando el siguiente código Python:
```python
import toml

with open('config.toml', 'r') as f:
    config = toml.load(f)

print(config)
```

Este código abrirá el archivo `config.toml`, lo leerá y lo almacenará en un diccionario de Python. Puedes acceder a los valores de configuración individuales utilizando la sintaxis de diccionario de Python. Por ejemplo, para acceder al valor de configuración `host` en la sección server, utiliza el siguiente código:

```
host = config['server']['host']
```

---
## Documentación
Es importante incluir una documentación clara y completa en tu paquete para que otros desarrolladores puedan entender cómo usar tu software. Puedes utilizar herramientas como Sphinx para generar documentación a partir de tus docstrings.

```
def my_sum(x, y):     
    """calculates the sum of x and y.     
    Parameters:     
       x (int): a number
       y (int): another number    
    Returns:     
       int: sum of x and y
    """      
   
   return x+y
```

Lo primero que debes hacer es instalar Sphinx utilizando `pip`. Ejecuta el comando `pip install sphinx` en tu terminal para instalarlo.

Iniciar el proyecto de Sphinx. Ejecuta el comando `sphinx-quickstart` en tu terminal para iniciar el proyecto de Sphinx. Este comando te guiará a través de la configuración inicial, donde podrás especificar la ubicación de la documentación, el nombre del proyecto, el autor, etc.

Configurar el archivo `conf.py`. El archivo `conf.py` es el archivo de configuración principal de Sphinx. Abre este archivo y configura los valores necesarios, como el nombre del proyecto, el autor, la versión, la extensión de archivos de origen, etc. También puedes agregar extensiones adicionales de Sphinx, como `sphinx.ext.autodoc` para generar automáticamente la documentación de tus funciones y clases.

Crea la estructura básica de la documentación utilizando los comandos de Sphinx, como `sphinx-apidoc` para generar la documentación de tus módulos y make html para generar el HTML de la documentación. Puedes organizar tu documentación utilizando secciones y subsecciones para hacerla fácil de seguir.

Una vez que hayas creado la estructura básica de la documentación, es hora de escribir la documentación en sí. Puedes agregar documentación a tus módulos, funciones, clases y métodos utilizando el formato de `reStructuredText` (reST) de Sphinx.

Una vez que hayas escrito la documentación, utiliza el comando `make html` en tu terminal para generar la documentación en formato HTML. Este comando generará un directorio `_build/html` que contendrá la documentación HTML.

Abre la documentación HTML generada en un navegador web y revisa la documentación para asegurarte de que esté completa y precisa.

---

## Distribuir paquete
Crear un archivo `setup.py`. El archivo `setup.py` es un script de Python que define cómo se debe instalar y distribuir tu paquete. Debes incluir información como el nombre del paquete, la versión, la descripción, los requisitos y las dependencias.

Generar distribuciones: Una vez que hayas escrito el código y creado el archivo `setup.py`, es hora de generar distribuciones de tu paquete. Puedes hacerlo utilizando la herramienta setuptools. Para generar una distribución, ejecuta el comando `python setup.py sdist` en tu terminal. Esto creará un archivo tarball de tu paquete.

---

## Licencia
Como tu código está a punto de ser público, deberías adjuntarle una licencia que explique a los demás cómo deben usar tu código. Probablemente querrás usar una licencia común como la *Licencia MIT* o la *Licencia Apache 2.0*. GitHub te ayudará a elegir una al hacer clic en la opción de Licencia, y agregará un nuevo archivo llamado `LICENSE` a tu paquete. Si prefieres no usar GitHub, puedes agregar el archivo manualmente.

---

## Publicar paquete
Si deseas hacer que tu paquete esté disponible para otros desarrolladores y usuarios, puedes publicarlo en el repositorio público de paquetes de Python, PyPI. Para publicar tu paquete, debes registrarte en PyPI y luego utilizar la herramienta `twine`. Ejecuta el comando `twine upload dist/*` para subir la distribución de tu paquete a PyPI.

---


# Instalación
```
python -m example_package 2 2
```