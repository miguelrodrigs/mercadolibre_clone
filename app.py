from flask import Flask, jsonify, abort, render_template, request
import json
import os

app = Flask(__name__)

def cargar_datos_producto():
    ruta = os.path.join(os.path.dirname(__file__), 'producto.json')
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None

def cargar_lista_productos():
    ruta = os.path.join(os.path.dirname(__file__), 'productos.json')
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None

@app.route('/api/producto', methods=['GET'])
def obtener_producto():
    producto_id = request.args.get('id', default=None, type=int)
    
    if producto_id is None:
        producto = cargar_datos_producto()
        if producto is None:
            abort(500, description="Error: archivo de datos no encontrado.")
        return jsonify(producto)
    else:
        productos = cargar_lista_productos()
        if productos is None:
            abort(500, description="Error: archivo de datos no encontrado.")
        producto = next((p for p in productos if p["id"] == producto_id), None)
        if producto is None:
            abort(404, description="Producto no encontrado.")
        return jsonify(producto)

@app.route('/', methods=['GET'])
def index():
    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado.")
    return render_template('index.html', productos=productos)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def error_servidor(error):
    return jsonify({'error': error.description}), 500

if __name__ == '__main__':
    app.run(debug=True)
