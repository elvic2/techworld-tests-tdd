import sys
import os
import pytest

# Agregar src/ al PYTHONPATH manualmente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar la funcionalidad que estamos probando
from orders import cargar_pedidos, guardar_pedidos, consultar_pedido, actualizar_estado_pedido

def test_consultar_pedido_existente():
    pedidos = cargar_pedidos()
    pedido_id = "PED12345"

    # Agregar un pedido de prueba si no existe
    if pedido_id not in pedidos:
        pedidos[pedido_id] = {"estado": "Enviado", "fecha_entrega": "2024-06-15"}
        guardar_pedidos(pedidos)

    # Verificar que se pueda consultar correctamente
    resultado = consultar_pedido(pedido_id)
    assert resultado is not None
    assert resultado["estado"] == "Enviado"

def test_consultar_pedido_inexistente():
    resultado = consultar_pedido("PED00000")  # Pedido que no existe
    assert resultado is None  # Debe devolver None

def test_actualizar_estado_pedido():
    pedido_id = "PED67890"
    pedidos = cargar_pedidos()

    # Agregar pedido de prueba si no existe
    if pedido_id not in pedidos:
        pedidos[pedido_id] = {"estado": "Pendiente", "fecha_entrega": "2024-06-20"}
        guardar_pedidos(pedidos)

    # Actualizar estado a "En tránsito"
    resultado = actualizar_estado_pedido(pedido_id, "En tránsito")
    
    # Verificar que el estado fue actualizado correctamente
    assert resultado is True
    pedidos_actualizados = cargar_pedidos()
    assert pedidos_actualizados[pedido_id]["estado"] == "En tránsito"

def test_actualizar_pedido_inexistente():
    resultado = actualizar_estado_pedido("PED00000", "En tránsito")  # Pedido que no existe
    assert resultado is False  # Debe devolver False