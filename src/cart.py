import json
import os

CART_FILE = "data/cart.json"

def cargar_carrito():
    """ Carga los productos del carrito desde el archivo JSON. """
    if os.path.exists(CART_FILE):
        with open(CART_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_carrito(data):
    """ Guarda los productos en el archivo JSON del carrito. """
    with open(CART_FILE, "w") as file:
        json.dump(data, file, indent=4)

def agregar_producto_carrito(producto_id, nombre, precio, cantidad):
    """ Agrega un producto al carrito. Si ya existe, aumenta la cantidad. """
    carrito = cargar_carrito()

    if producto_id in carrito:
        carrito[producto_id]["cantidad"] += cantidad
    else:
        carrito[producto_id] = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

    guardar_carrito(carrito)
    return True

def modificar_cantidad_producto(producto_id, nueva_cantidad):
    """ Modifica la cantidad de un producto en el carrito. """
    carrito = cargar_carrito()

    if producto_id in carrito and nueva_cantidad > 0:
        carrito[producto_id]["cantidad"] = nueva_cantidad
        guardar_carrito(carrito)
        return True

    return False