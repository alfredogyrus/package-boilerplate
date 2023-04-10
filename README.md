# Boilerplate para paquete software en Python
Un boilerplate es un conjunto de archivos y estructuras de directorios que proporcionan una base sólida para un proyecto de software. En esta receta, se proporcionará una guía paso a paso para crear un boilerplate para un paquete de software en Python, incluyendo la estructura de directorios, los archivos necesarios y las configuraciones recomendadas. Con este boilerplate, podrás comenzar a desarrollar tu paquete de software de manera más eficiente y efectiva.
## 1. Entorno virtual
Lo primero que debes hacer es instalar [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html#) utilizando `pip`. Ejecuta el comando `pip install pipenv` en tu terminal para instalarlo.

Crear un nuevo entorno virtual. Para crear un nuevo entorno virtual, ejecuta el comando `pipenv --python 3.x`, donde 3.x es la versión de Python que deseas utilizar en tu entorno virtual. Este comando creará automáticamente un nuevo entorno virtual y un archivo Pipfile que contendrá una lista de las dependencias de tu proyecto.

Instalar paquetes. Para instalar paquetes en tu entorno virtual, utiliza el comando `pipenv install paquete`. Este comando instalará el paquete especificado en el entorno virtual y actualizará automáticamente el archivo Pipfile.

Activar el entorno virtual. Para activar el entorno virtual, ejecuta el comando `pipenv shell`. Esto abrirá una nueva terminal con el entorno virtual activado. Todas las dependencias que hayas instalado en el entorno virtual estarán disponibles en esta terminal.

Cuando el paquete software se encuentre listo, recuerda generar el archivo de requisitos. Para generar un archivo de requisitos a partir de tu entorno virtual, utiliza el comando `pipenv run pip freeze > requirements.txt`. Este comando generará un archivo `requirements.txt` en el directorio actual que contendrá una lista de todas las dependencias instaladas en el entorno virtual junto con sus versiones correspondientes. Para generar el entorno definitivo de `pipenv` utiliza `pipenv lock`.

Una vez que se ha generado el archivo `requirements.txt`, es recomendable revisar y editar el archivo según sea necesario. Puedes agregar o eliminar dependencias manualmente según tus necesidades.

Para utilizar el archivo de requisitos en otro entorno virtual o en un servidor de producción, simplemente instala las dependencias del archivo de requisitos utilizando el comando `pip install -r requirements.txt` o `pipenv install -r requirements.txt`.

---
## 2. Software
El primer paso para crear un paquete de software es crear [una estructura de directorios](https://docs.python.org/3/tutorial/modules.html#packages) que contenga los archivos de código fuente y otros recursos necesarios. Para ello, podrías crear una carpeta con el nombre de tu paquete y dentro de ella, crear un archivo `__init__.py` vacío y otra carpeta con el mismo nombre que contendrá el código fuente y otros recursos.

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
## 3. Variables de entorno
Instalar el paquete [python-dotenv](https://pypi.org/project/python-dotenv/). Lo primero que debes hacer es instalar el paquete `python-dotenv` utilizando `pipenv`. Ejecuta el comando `pipenv install python-dotenv` en tu terminal para instalarlo.

Crea un archivo llamado `.env` en la raíz de tu proyecto. Este archivo contendrá las variables de entorno que quieras cargar. Puedes agregar una variable de entorno por línea en el formato `NOMBRE_VARIABLE=VALOR_VARIABLE`.

En tu código, puedes cargar las variables de entorno utilizando el paquete `dotenv`. Importa el paquete y llama al método `load_dotenv()` al principio de tu código. Esto cargará automáticamente todas las variables de entorno definidas en el archivo `.env` en el entorno de tu aplicación.

Para acceder a las variables de entorno cargadas, utiliza el método `os.environ.get('NOMBRE_VARIABLE')` en tu código. Esto te devolverá el valor de la variable de entorno especificada.

Es importante agregar el archivo `.env` a tu archivo `.gitignore` o al control de versiones que estés utilizando para evitar que las variables de entorno se compartan accidentalmente con otros desarrolladores.

---

## 4. Fichero de configuración
Instalar la biblioteca [toml](https://toml.io/en/). Antes de poder utilizar toml en tus proyectos de Python, debes instalar la biblioteca `toml`. Puedes instalarlo fácilmente utilizando `pipenv`. Simplemente ejecuta el comando `pipenv install toml` en tu terminal para instalarlo.

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
## 5. Documentación
Es importante incluir una documentación clara y completa en tu paquete para que otros desarrolladores puedan entender cómo usar tu software. Puedes utilizar herramientas como [Sphinx](https://www.sphinx-doc.org/en/master/) para generar documentación a partir de tus docstrings.

Lo primero que debes hacer es instalar Sphinx utilizando `pipenv`. Ejecuta el comando `pipenv install sphinx` en tu terminal para instalarlo.

Iniciar el proyecto de Sphinx. Ejecuta el comando `sphinx-quickstart docs` en tu terminal para iniciar el proyecto de Sphinx. Este comando te guiará a través de la configuración inicial, donde podrás especificar la ubicación de la documentación, el nombre del proyecto, el autor, etc.

Configurar el archivo `conf.py`. El archivo `conf.py` es el archivo de configuración principal de Sphinx. Abre este archivo y configura los valores necesarios, como el nombre del proyecto, el autor, la versión, la extensión de archivos de origen, etc. También puedes agregar extensiones adicionales de Sphinx, como `sphinx.ext.autodoc` para generar automáticamente la documentación de tus funciones y clases.

Crea la estructura básica de la documentación utilizando los comandos de Sphinx, como `sphinx-apidoc -f -o docs/source src/example_package` para generar la documentación de tus módulos. Puedes organizar tu documentación utilizando secciones y subsecciones para hacerla fácil de seguir.

Una vez que hayas creado la estructura básica de la documentación, es hora de escribir la documentación en sí. Puedes agregar documentación a tus módulos, funciones, clases y métodos utilizando el formato de *reStructuredText* (reST) de Sphinx.

Una vez que hayas escrito la documentación, utiliza el comando `sphinx-build -b html docs/source/ docs/build/html` en tu terminal para generar la documentación en formato HTML. Este comando generará un directorio `build/html` que contendrá la documentación HTML.

Abre la documentación HTML generada en un navegador web y revisa la documentación para asegurarte de que esté completa y precisa.

---


## 6. README
Incluir un archivo `README` en un paquete de software con Python es una buena práctica que puede proporcionar información valiosa sobre el paquete y su uso. Un archivo `README` bien escrito puede proporcionar una descripción clara y concisa del proyecto, incluyendo su propósito, características y funcionalidades.

El archivo `README` puede proporcionar información detallada sobre cómo instalar y utilizar el paquete, incluyendo los requisitos del sistema, los comandos de instalación y los ejemplos de uso.

Además, puede incluir información sobre cómo los usuarios pueden colaborar con el proyecto, incluyendo cómo informar errores y enviar solicitudes de extracción.

Finalmente, al incluir una documentación detallada en el archivo `README`, se puede mejorar la documentación general del proyecto y hacer que sea más fácil para los usuarios entender cómo funciona el paquete.

---

## 7. Licencia
Como tu código está a punto de ser público, deberías adjuntarle una licencia que explique a los demás cómo deben usar tu código. Probablemente querrás usar una licencia común como la *Licencia MIT* o la *Licencia Apache 2.0*. GitHub te ayudará a elegir una al hacer clic en la opción de Licencia, y agregará un nuevo archivo llamado `LICENSE` a tu paquete. Si prefieres no usar GitHub, puedes agregar el archivo manualmente.

Por ejemplo, la licencia MIT:
```
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 8. Distribuir paquete
Para realizar la distribución del paquete se deberá construir el `build` utilizando una herramienta para la generación del backend. En este caso, se creará un fichero `pyproject.toml`, el cual contendrá la siguiente información. Nótese que se deberá modificar la información contenida en [project] acordemente.
```
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "example_package_YOUR_USERNAME_HERE"
version = "0.0.1"
authors = [
  { name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/pypa/sampleproject"
"Bug Tracker" = "https://github.com/pypa/sampleproject/issues"
```

El próximo paso será generar los paquetes de distribución del repositorio software. Estos archivos podrían ser subidos a PyPI o finalmente, ser instalados con `pip` utilizando `pip install paquete.whl`.

A continuación, ejecutar los siguientes comandos en el mismo directorio donde se encuentra el fichero `pyproject.toml`.

```
python -m pip install --upgrade build

python -m build
```

Una vez terminado el proceso, el resultado debería ser el siguiente

```
dist/
├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
└── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
```

El archivo `tar.gz` es una distribución de código fuente, mientras que el archivo `.whl` es una distribución compilada. Las versiones más recientes de `pip` instalan preferentemente distribuciones compiladas, pero recurrirán a distribuciones de código fuente si es necesario. Siempre debes subir una distribución de código fuente y proporcionar distribuciones compiladas para las plataformas con las que tu proyecto es compatible. En este caso, nuestro paquete de ejemplo es compatible con Python en cualquier plataforma, por lo que solo se necesita una distribución compilada.

---
## 9. Publicar paquete
Si deseas hacer que tu paquete esté disponible para otros desarrolladores y usuarios, puedes publicarlo en el repositorio público de paquetes de Python, PyPI. Para publicar tu paquete, debes registrarte en PyPI y luego utilizar la herramienta `twine`. Ejecuta el comando `twine check dist/*` y `twine upload dist/*` para subir la distribución de tu paquete a PyPI.

---


# Ejecución paso a paso
```
cd package-boilerplate

pip install pipenv

Windows: set PIPENV_VENV_IN_PROJECT=1
Unix: export PIPENV_VENV_IN_PROJECT=1

pipenv --python 3.9

pipenv shell

pipenv install python-dotenv

pipenv install toml

pipenv install sphinx

sphinx-quickstart docs

pipenv install sphinx-rtd-theme

sphinx-apidoc -f -o docs/source src/example_package

sphinx-build -b html docs/source/ docs/build/html

pipenv lock

pipenv run pip freeze > requirements.txt
```