# Importamos Flask y otras librerías que vamos usar
from flask import Flask, jsonify, abort, render_template, request
import json
import os

# Inicializamos la app de Flask
app = Flask(__name__)

# Esta función abre el archivo JSON que tiene la lista de productos
def cargar_lista_productos():
    ruta = os.path.join(os.path.dirname(__file__), 'productos.json')
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None

# Ruta para devolver los datos de un producto en formato JSON (API)
@app.route('/api/producto', methods=['GET'])
def obtener_producto_api():
    # Busco el parámetro "id" que viene por la URL → ej: /api/producto?id=2
    producto_id = request.args.get('id', default=None, type=int)

    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado.")

    # Acá busco el producto específico con ese ID
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto is None:
        abort(404, description="Producto no encontrado.")

    return jsonify(producto)  # Devuelvo los datos en formato JSON

# Ruta principal → muestra el listado de productos en HTML
@app.route('/', methods=['GET'])
def index():
    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado.")

    # Renderizo el archivo index.html y le paso los productos para que los muestre
    return render_template('index.html', productos=productos)

# Ruta para mostrar la página de detalle de un producto
@app.route('/producto', methods=['GET'])
def detalle_producto():
    # Busco el ID del producto que me pasan por URL → ej: /producto?id=5
    producto_id = request.args.get('id', default=None, type=int)
    if producto_id is None:
        abort(400, description="Parámetro 'id' es requerido.")

    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado.")

    # Acá busco ese producto en particular
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto is None:
        abort(404, description="Producto no encontrado.")

    # Renderizo producto.html enviando los datos del producto
    return render_template('producto.html', producto=producto)

# Esto arranca el servidor Flask si corro el archivo directamente
if __name__ == "__main__":
    app.run(debug=True)
