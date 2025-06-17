# Proyecto MercadoLibre Clone - Backend y Frontend

Este proyecto es un clon simple de una página de detalle de producto tipo MercadoLibre.

## Backend

- Implementado con Flask.
- Lee los datos del producto desde un archivo JSON (`producto.json`).
- Expone un endpoint `/api/producto` para entregar la información del producto.
- Maneja errores 404 y 500 con respuestas JSON.
- Documentación y comentarios en español para facilitar la comprensión.

## Frontend

- Página en `templates/index.html` que consume la API con fetch para mostrar los datos dinámicamente.
- Usa Bootstrap 5 para estilo y responsividad.
- Muestra imágenes, título, precio, vendedor, stock, métodos de pago, descripción y características.

## Cómo ejecutar

1. Instalar dependencias:

```
pip install Flask
```

2. Ejecutar la aplicación:

```
python app.py
```

3. Abrir el navegador en:

```
http://localhost:5000/
```

## Desafíos y soluciones

- Optamos por persistir datos en JSON para evitar base de datos real, según requisitos.
- Separación clara entre frontend y backend para facilitar mantenimiento.
- Manejo básico de errores para mejor experiencia y robustez.
- Documentación y comentarios para claridad del código.