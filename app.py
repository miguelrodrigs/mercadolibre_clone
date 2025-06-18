from flask import Flask, jsonify, abort, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Función para cargar la lista de productos desde el archivo JSON
def cargar_lista_productos():
    ruta = os.path.join(os.path.dirname(__file__), 'productos.json')
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Retorna None si el archivo no existe
        return None
    except json.JSONDecodeError:
        # Retorna None si el archivo está corrupto o mal formateado
        return None

# API para obtener un producto específico por ID en formato JSON
@app.route('/api/producto', methods=['GET'])
def obtener_producto_api():
    producto_id = request.args.get('id', default=None, type=int)

    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado o corrupto.")

    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto is None:
        abort(404, description="Producto no encontrado.")

    return jsonify(producto)

# Ruta principal que muestra un producto guardado localmente (data/product.json)
@app.route('/')
def mostrar_producto():
    try:
        with open('data/product.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return render_template('producto.html', producto=datos['producto'])
    except FileNotFoundError:
        return "⚠️ Archivo 'product.json' no encontrado.", 404
    except json.JSONDecodeError:
        return "⚠️ Error al leer 'product.json'.", 500
    except Exception as e:
        return f"⚠️ Error inesperado: {str(e)}", 500

# Ruta para agregar un nuevo producto con formulario GET/POST
@app.route('/nuevo-producto', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        try:
            nuevo = {
                "titulo": request.form['titulo'],
                "descripcion": request.form['descripcion'],
                "precio": float(request.form['precio']),
                "imagen": request.form['imagen'],
                "stock": int(request.form['stock']),
                "valoraciones": []
            }
            with open('data/product.json', 'w', encoding='utf-8') as archivo:
                json.dump({"producto": nuevo}, archivo, ensure_ascii=False, indent=4)

            return redirect(url_for('mostrar_producto'))
        except Exception as e:
            # Manejo de errores al guardar producto
            return f"⚠️ Error al guardar producto: {str(e)}", 500

    # GET: Mostrar formulario
    return render_template('nuevo_producto.html')

# Ruta para mostrar listado de productos desde productos.json
@app.route('/', methods=['GET'])
def index():
    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado o corrupto.")
    return render_template('index.html', productos=productos)

# Ruta para mostrar detalle de producto específico
@app.route('/producto', methods=['GET'])
def detalle_producto():
    producto_id = request.args.get('id', default=None, type=int)
    if producto_id is None:
        abort(400, description="Parámetro 'id' es requerido.")

    productos = cargar_lista_productos()
    if productos is None:
        abort(500, description="Error: archivo de datos no encontrado o corrupto.")

    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto is None:
        abort(404, description="Producto no encontrado.")

    return render_template('producto.html', producto=producto)

if __name__ == "__main__":
    app.run(debug=True)
