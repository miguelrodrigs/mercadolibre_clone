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

# Ruta para crear un nuevo producto
@app.route('/nuevo-producto', methods=['GET', 'POST'])
def nuevo_producto():
    # Si el usuario envía el formulario (método POST)
    if request.method == 'POST':
        # Cargamos la lista actual de productos desde el archivo JSON
        productos = cargar_lista_productos()

        # Generamos un nuevo ID para el producto sumando 1 al ID más alto actual
        # Si no hay productos, empezamos desde 1
        nuevo_id = max([p['id'] for p in productos], default=0) + 1

        # Creamos un nuevo diccionario con la información del producto, tomando los datos del formulario
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

        # Agregamos el nuevo producto a la lista de productos existente
        productos.append(nuevo)

        # Guardamos la lista actualizada en el archivo JSON
        guardar_lista_productos(productos)

        # Redireccionamos al usuario a la página del detalle del producto recién creado
        return redirect(url_for('detalle_producto', id=nuevo_id))

    # Si es una solicitud GET, simplemente mostramos el formulario para crear un nuevo producto
    return render_template('nuevo_producto.html')


# API para obtener un producto por id o la lista completa si no se pasa el id
@app.route('/api/productos')
def obtener_productos():
    producto_id = request.args.get('id', type=int)

    productos = cargar_lista_productos()

    if producto_id is not None:
        # Buscar el producto con el id especificado
        producto = next((p for p in productos if p["id"] == producto_id), None)
        if producto is None:
            abort(404, description="Producto no encontrado.")
        return jsonify(producto)
    
    # Si no se pasa id, devuelve la lista completa
    return jsonify(productos)

@app.route('/api/productos')
def actualizar_productos():
    producto_id = request.args.get('id', type=int)

    productos = cargar_lista_productos()

    if producto_id is not None:
        # Buscar el producto con el id especificado
        producto = next((p for p in productos if p["id"] == producto_id), None)
        if producto is None:
            abort(404, description="Producto no encontrado.")
        return jsonify(producto)
    
    # Si no se pasa id, devuelve la lista completa
    return jsonify(productos)

@app.route('/descuento')
def aplicar_descuento_simple():
    producto_id = request.args.get('id', type=int)
    porcentaje = request.args.get('porcentaje', type=float)

    if producto_id is None or porcentaje is None:
        return "Faltan parámetros 'id' y 'porcentaje'.", 400

    productos = cargar_lista_productos()
    producto = next((p for p in productos if p["id"] == producto_id), None)

    if producto is None:
        return "Producto no encontrado.", 404

    # Calculamos el nuevo precio con descuento
    precio_original = producto['price']
    nuevo_precio = precio_original * (1 - porcentaje / 100)
    producto['price'] = round(nuevo_precio, 2)

    guardar_lista_productos(productos)

    return f"Descuento aplicado ✅ Producto: {producto['title']} - Precio anterior: ${precio_original} - Nuevo precio: ${producto['price']}"

if __name__ == '__main__':
    app.run(debug=True)
