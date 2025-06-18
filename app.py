from flask import Flask, jsonify, abort, render_template, request
import json
import os

app = Flask(__name__)

# ---------------------- FUNCIONES AUXILIARES ----------------------

def cargar_lista_productos():
    """
    Carga la lista completa de productos desde 'productos.json'.
    Retorna una lista de diccionarios o None si el archivo no existe.
    """
    ruta = os.path.join(os.path.dirname(__file__), 'productos.json')
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None

# ---------------------- RUTAS ----------------------

@app.route('/api/producto', methods=['GET'])
def obtener_producto_api():
    """
    Endpoint API que devuelve información de productos en formato JSON.
    
    Parámetros GET:
      - id (opcional): si se pasa, busca el producto por ID en 'productos.json'.
                       si no se pasa, devuelve la lista completa de productos.
    """
    producto_id = request.args.get('id', default=None, type=int)
    
    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado.")

    if producto_id is None:
        # Si no se especifica ID, se devuelve toda la lista de productos
        return jsonify(productos)
    else:
        # Si se pasa un ID, busca el producto por ID
        producto = next((p for p in productos if p["id"] == producto_id), None)
        if producto is None:
            abort(404, description="Producto no encontrado.")
        return jsonify(producto)

@app.route('/', methods=['GET'])
def index():
    """
    Ruta principal ("/"): muestra la página HTML con el listado de productos.
    Utiliza la plantilla 'index.html'.
    
    Respuesta:
      - Página web con listado de productos.
    """
    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado.")
    return render_template('index.html', productos=productos)

@app.route('/producto', methods=['GET'])
def detalle_producto():
    """
    Ruta para mostrar el detalle individual de un producto.
    
    Parámetros GET:
      - id: ID del producto a mostrar (obligatorio)
      
    """
    producto_id = request.args.get('id', default=None, type=int)
    if producto_id is None:
        abort(400, description="Parámetro 'id' es requerido.")
    
    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado.")
    
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto is None:
        abort(404, description="Producto no encontrado.")
    
    return render_template('producto.html', producto=producto)

# ---------------------- FIN DEL ARCHIVO ----------------------
