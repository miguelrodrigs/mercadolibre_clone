Documentación del Proyecto: Detalle de Producto - Mercado Libre (Prototipo)

1. Descripción General

Este proyecto es un prototipo funcional inspirado en la página de detalle de producto de Mercado Libre. Incluye una interfaz web (frontend) y una API backend desarrollada en Python (FastAPI) que proporciona los datos del producto.

El enfoque principal fue mostrar conocimientos de desarrollo backend y procesamiento de datos, integrando el consumo de una API con renderización dinámica en el frontend.

2. Tecnologías utilizadas

Backend:

Python 3.11

FastAPI

Uvicorn

Persistencia local en archivo JSON (sin base de datos)

Frontend:

HTML + CSS (Bootstrap)

JavaScript (para fetch de datos desde la API)

3. Estructura del Proyecto

mercadolibre_clone/
├── main.py          # API FastAPI
├── products.json    # Datos de productos (mock)
├── index.html       # Página principal (frontend)
├── run.md           # Instrucciones para ejecutar
└── README.md        # Documentación (este archivo)

4. Endpoints de la API

Método

Endpoint

Descripción

GET

/api/product/{product_id}

Obtiene detalles de producto

Ejemplo:

GET http://127.0.0.1:8000/api/product/iphone14pro

5. Persistencia de Datos

Los datos están almacenados en products.json. La estructura es sencilla, lo que permite fácil mantenimiento o ampliación.

6. ¿Por qué FastAPI?

Rápida de implementar.

Excelente soporte para documentación automática.

Muy útil para proyectos orientados a APIs REST.

7. Desafíos

Sincronización de datos entre API y frontend (resuelto con JavaScript async/await).

Diseño responsivo similar a Mercado Libre (resuelto utilizando Bootstrap 5).

8. ¿Por qué énfasis en Ingeniería de Datos?

Uso de persistencia local (JSON).

Manipulación estructurada de datos.

Desarrollo de APIs RESTful eficientes.

Separación clara entre capa de datos (API) y presentación (Frontend).

9. ¿Cómo correr el proyecto?

Backend:

pip install fastapi uvicorn
uvicorn main:app --reload

Frontend:

Simplemente abre el archivo index.html en el navegador.

10. Próximos pasos (Mejoras sugeridas)

Incorporar autenticación.

Agregar endpoint de múltiples productos.

Añadir tests unitarios para cobertura.

Persistencia con base de datos relacional o NoSQL.

Autor: Miguel CazemiroPropósito: Prueba técnica - Mercado Libre (Async Work)

