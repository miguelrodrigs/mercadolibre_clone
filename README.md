
---

##  `DOCUMENTACION`

```markdown
#  Documentación del Proyecto - MercadoLibre Clone

##  Objetivo

Este proyecto es un clon simplificado de una página de producto de MercadoLibre, desarrollado como desafío técnico. La aplicación muestra un listado de productos, sus detalles, y permite agregar nuevos productos a través de un formulario.

## Elecciones de diseño

- **Stack Backend:** Python con Flask por su simplicidad y facilidad de integración con HTML usando Jinja2.
- **Persistencia de datos:** Productos almacenados en un archivo JSON (`productos.json`) local, como solicitado por el desafío.
- **Frontend:** HTML + Bootstrap para lograr un diseño responsivo y similar al sitio real de MercadoLibre. La paleta de colores fue adaptada al amarillo característico.
- **API RESTful:** Endpoint `/api/producto` que devuelve los detalles de un producto en formato JSON para futuras integraciones.

##  Funcionalidades implementadas

- ✔️ Página de listado de productos (`/`)
- ✔️ Página de detalle por producto (`/producto?id=<id>`)
- ✔️ API RESTful (`/api/producto?id=<id>`)
- ✔️ Formulario para agregar productos (`/nuevo-producto`), con IDs incrementales automáticos
- ✔️ Métodos de pago y especificaciones incluidas
- ✔️ Tratamiento de errores 400, 404 y 500
- ✔️ Documentación de uso (`run.md`)

## Dificultades enfrentadas

Mi mayor desafío fue principalmente en la parte de **Frontend (HTML y CSS)**, ya que mi perfil es más orientado a **Ingeniería de Datos** y desarrollo backend. El diseño responsivo y la estructura visual requirieron más investigación y pruebas para lograr una interfaz aceptable. Para solucionar eso utilicé **Bootstrap**, que permitió estructurar el HTML de forma rápida y más profesional.

En el Backend, la lógica de manejo del archivo JSON, generación automática de IDs y organización de rutas fueron sencillas debido a mi experiencia previa en programación y manipulación de datos estructurados.

## Cobertura

El proyecto cuenta con tratamiento adecuado de errores e implementé documentación completa. A nível de pruebas unitarias, aunque no se implementaron tests automáticos formales por limitación de tiempo, el proyecto fue testeado manualmente en diferentes escenarios (adición, visualización, error 404, error 400).

## 📎 Link al repositorio

https://github.com/miguelrodrigs/mercadolibre_clone
