from flask import Flask, jsonify, abort, render_template
import json

app = Flask(__name__)

def cargar_datos_producto():
    """
    Carga los datos del producto desde un archivo JSON local.
    Retorna un diccionario con la información del producto.
    """
    try:
        with open('producto.json', 'r', encoding='utf-8') as archivo:
            producto = json.load(archivo)
            return producto
    except FileNotFoundError:
        # Si no se encuentra el archivo JSON, se devuelve None
        return None

@app.route('/api/producto', methods=['GET'])
def obtener_producto():
    """
    Endpoint para obtener los detalles del producto.
    Retorna un JSON con la información del producto.
    """
    producto = cargar_datos_producto()
    if producto is None:
        abort(500, description="Error: archivo de datos no encontrado.")
    return jsonify(producto)

@app.route('/', methods=['GET'])
def index():
    """
    Ruta principal que renderiza el template HTML.
    """
    return render_template('index.html')

@app.errorhandler(404)
def pagina_no_encontrada(error):
    """
    Maneja errores 404 cuando la ruta no existe.
    """
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def error_servidor(error):
    """
    Maneja errores internos del servidor (500).
    """
    return jsonify({'error': error.description}), 500

if __name__ == '__main__':
    app.run(debug=True)