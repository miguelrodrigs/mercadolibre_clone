from flask import Flask, jsonify, abort, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Ruta del archivo
RUTA_PRODUCTOS = os.path.join(os.path.dirname(__file__), 'productos.json')

# Función para cargar la lista completa de productos
def cargar_lista_productos():
    try:
        with open(RUTA_PRODUCTOS, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Retorna lista vacía si no existe o está corrupto
        return []

# Función para guardar la lista actualizada de productos
def guardar_lista_productos(productos):
    with open(RUTA_PRODUCTOS, 'w', encoding='utf-8') as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)

# Página principal que muestra todos los productos
@app.route('/')
def index():
    productos = cargar_lista_productos()
    return render_template('index.html', productos=productos)

# Página de detalle de producto según id
@app.route('/producto')
def detalle_producto():
    producto_id = request.args.get('id', type=int)
    if producto_id is None:
        abort(400, description="Parámetro 'id' es requerido.")

    productos = cargar_lista_productos()
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto is None:
        abort(404, description="Producto no encontrado.")

    return render_template('producto.html', producto=producto)

# Página para agregar nuevo producto (GET muestra formulario, POST procesa)
@app.route('/nuevo-producto', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        productos = cargar_lista_productos()

        # Generar nuevo id incremental
        nuevo_id = max([p['id'] for p in productos], default=0) + 1

        nuevo = {
        "id": nuevo_id,
        "title": request.form['titulo'],          
        "description": request.form['descripcion'],
        "price": float(request.form['precio']),    
        "images": [request.form['imagen']],        
        "reviews": 0,                             
        "seller": {
            "name": "Vendedor Ejemplo",           
            "reputation": "Nuevo"                 
        },
        "rating": 0.0,                             
        "stock": int(request.form['stock']),
        "payment_methods": [
            "Tarjeta de crédito",
            "Mercado Pago",
            "Transferencia bancaria"
        ],
        "especificaciones": {
            "Condición": "Nuevo",
            "Garantía": "6 meses"
            }
        }
        productos.append(nuevo)
        guardar_lista_productos(productos)

        return redirect(url_for('detalle_producto', id=nuevo_id))

    return render_template('nuevo_producto.html')

# API para obtener producto en JSON por id
@app.route('/api/producto')
def obtener_producto_api():
    producto_id = request.args.get('id', type=int)
    if producto_id is None:
        abort(400, description="Parámetro 'id' es requerido.")

    productos = cargar_lista_productos()
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if producto is None:
        abort(404, description="Producto no encontrado.")

    return jsonify(producto)

if __name__ == '__main__':
    app.run(debug=True)
