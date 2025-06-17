from flask import Flask, jsonify, abort, render_template, request
import json
import os

app = Flask(__name__)

def cargar_datos_producto():
    ruta = os.path.join(os.path.dirname(__file__), 'producto.json')
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def cargar_lista_productos():
    ruta = os.path.join(os.path.dirname(__file__), 'productos.json')  # ← Precisa criar esse arquivo
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

@app.route('/api/producto', methods=['GET'])
def obtener_producto():
    producto_id = request.args.get('id', default=None, type=int)
    
    if producto_id is None:
        # Retorna o produto único de producto.json (mantendo compatibilidade)
        producto = cargar_datos_producto()
        if producto is None:
            abort(500, description="Error: archivo de datos no encontrado.")
        return jsonify(producto)
    else:
        # Retorna produto específico de productos.json pelo ID
        productos = cargar_lista_productos()
        producto = next((p for p in productos if p["id"] == producto_id), None)
        if producto is None:
            abort(404, description="Producto no encontrado.")
        return jsonify(producto)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def error_servidor(error):
    return jsonify({'error': error.description}), 500

if __name__ == '__main__':
    app.run(debug=True)
