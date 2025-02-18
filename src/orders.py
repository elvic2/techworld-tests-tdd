import json
import os

ORDERS_FILE = "data/orders.json"

def cargar_pedidos():
    """ Carga los pedidos desde el archivo JSON. """
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_pedidos(data):
    """ Guarda los pedidos en el archivo JSON. """
    with open(ORDERS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def consultar_pedido(pedido_id):
    """ Devuelve la información de un pedido si existe, o None si no existe. """
    pedidos = cargar_pedidos()
    return pedidos.get(pedido_id, None)

def actualizar_estado_pedido(pedido_id, nuevo_estado):
    """ Actualiza el estado de un pedido si existe, y devuelve True si se actualizó. """
    pedidos = cargar_pedidos()

    if pedido_id in pedidos:
        pedidos[pedido_id]["estado"] = nuevo_estado
        guardar_pedidos(pedidos)
        return True  # Se actualizó correctamente
    
    return False  # El pedido no existe