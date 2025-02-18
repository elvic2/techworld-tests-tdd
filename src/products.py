import json
import os

PRODUCTS_FILE = "data/products.json"

def cargar_productos():
    """ Carga los productos desde el archivo JSON. """
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_productos(data):
    """ Guarda los productos en el archivo JSON. """
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def crear_producto(producto_id, nombre, descripcion, precio, stock, categoria):
    """ Crea un nuevo producto si tiene datos válidos y no existe ya en la base de datos. """
    productos = cargar_productos()

    if producto_id in productos or not nombre.strip() or precio <= 0 or stock < 0:
        return False  # Retorna False si el producto ya existe o tiene datos inválidos
    
    productos[producto_id] = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock,
        "categoria": categoria,
        "estado": "inactivo"
    }
    guardar_productos(productos)
    return True  # Retorna True si el producto se creó correctamente

def editar_producto(producto_id, nueva_descripcion, nuevo_precio):
    """ Modifica la descripción y el precio de un producto si existe. """
    productos = cargar_productos()

    if producto_id in productos and nuevo_precio > 0:
        productos[producto_id]["descripcion"] = nueva_descripcion
        productos[producto_id]["precio"] = nuevo_precio
        guardar_productos(productos)
        return True  # Se actualizó correctamente
    
    return False  # El producto no existe o los datos son inválidos

def activar_producto(producto_id):
    """ Activa un producto si existe y tiene stock disponible. """
    productos = cargar_productos()

    if producto_id in productos and productos[producto_id]["stock"] > 0:
        productos[producto_id]["estado"] = "activo"
        guardar_productos(productos)
        return True  # Producto activado correctamente
    
    return False  # Producto no encontrado o sin stock