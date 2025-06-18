# Documentación del Proyecto - MercadoLibre Clone

## Objetivo

Este proyecto es un clon simplificado de una página de producto de MercadoLibre, desarrollado como desafío técnico. La aplicación muestra un listado de productos, sus detalles, y permite agregar nuevos productos a través de un formulario.

## Elecciones de diseño

- **Backend:** Python con Flask, elegido por su simplicidad y facilidad para integrar HTML usando Jinja2.  
- **Persistencia de datos:** Los productos se almacenan en un archivo JSON local (`productos.json`), tal como se solicitó en el desafío.  
- **Frontend:** Utilicé HTML con Bootstrap para lograr un diseño responsivo y similar al sitio real de MercadoLibre, especialmente en la paleta de colores amarilla característica.  
- **API RESTful:** Implementé un endpoint `/api/producto` que devuelve los detalles de un producto en formato JSON, lo que facilita futuras integraciones.

## Funcionalidades implementadas

- Página principal con listado de productos (`/`)  
- Página de detalle individual de producto (`/producto?id=<id>`)  
- API RESTful para obtener detalles de productos (`/api/producto?id=<id>`)  
- Formulario para agregar nuevos productos (`/nuevo-producto`), con generación automática de IDs  
- Inclusión de métodos de pago y especificaciones en los datos del producto  
- Manejo de errores adecuados para códigos 400, 404 y 500  
- Documentación de uso incluida (`run.md`)

## Dificultades enfrentadas

Mi mayor desafío estuvo en el **frontend (HTML y CSS)**, ya que mi experiencia está más enfocada en ingeniería de datos y desarrollo backend. El diseño responsivo y la estructura visual requirieron un poco más de investigación y pruebas para lograr una interfaz que resultara aceptable y clara para el usuario. Para resolver esto, utilicé Bootstrap, que me permitió organizar el HTML de forma más rápida y profesional.

En cuanto al backend, la lógica para manejar el archivo JSON, generar IDs automáticamente y organizar las rutas fue más sencilla, gracias a mi experiencia previa en programación y manipulación de datos estructurados.

## Cobertura

El proyecto incluye un manejo adecuado de errores y documentación completa. En cuanto a pruebas unitarias, por limitaciones de tiempo no se implementaron tests automáticos formales, pero el proyecto fue probado manualmente en distintos escenarios, incluyendo la adición y visualización de productos, y manejo de errores 400 y 404.

## Link al repositorio

[https://github.com/miguelrodrigs/mercadolibre_clone](https://github.com/miguelrodrigs/mercadolibre_clone)
