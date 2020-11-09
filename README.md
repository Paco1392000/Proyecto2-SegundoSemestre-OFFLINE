# Introducción
Un servidor web que permite manejar usuarios y crear recetas que persisten solo durante la ejecución. Está realizado en el lenguaje de programación Python y utiliza el framework Flask para servir distintas páginas, así como W3.CSS para agregar estilos. Las páginas logran interactuar con el servidor utilizando dos protocolos diferentes y presentar datos de entre dos lenguajes distintos.

# Uso
Para utilizar el servidor, solo es necesario ejecutar el archivo `main.py`
```
$ python main.py
```

## Requerimientos para generar PDFs
Agregar el builtpack para la librería:
```
heroku buildpacks:add https://github.com/dscout/wkhtmltopdf-buildpack.git
```

Agregar variable de entorno de Heroku:
```
heroku config:set WKHTMLTOPDF_BINARY=wkhtmltopdf-pack
```

Agregar a "requirements.txt":
```
pdfkit==0.6.1
git+git://github.com/johnfraney/wkhtmltopdf-pack.git
```

# TODO
- ~~Agregar navegación y manejo de parámetros por rutas.~~
- ~~Integrar carga de archivos.~~
- ~~Descarga de reportes.~~
- ~~Despliegue en la nube.~~