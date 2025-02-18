import sys
import os
import pytest

# Agregar src/ al PYTHONPATH manualmente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar la funcionalidad que estamos probando
from cart import cargar_carrito, guardar_carrito, agregar_producto_carrito, modificar_cantidad_producto

def test_agregar_producto_carrito():
    carrito = cargar_carrito()
    producto_id = "PROD123"

    # Agregar un producto de prueba si no existe
    if producto_id not in carrito:
        resultado = agregar_producto_carrito(producto_id, "Laptop Gamer", 1500, 1)

    # Verificar que se pueda agregar correctamente
    carrito_actualizado = cargar_carrito()
    assert resultado is True
    assert producto_id in carrito_actualizado

def test_modificar_cantidad_producto():
    producto_id = "PROD456"
    carrito = cargar_carrito()

    # Agregar producto de prueba si no existe
    if producto_id not in carrito:
        agregar_producto_carrito(producto_id, "Monitor 4K", 500, 1)
    
    # Modificar cantidad
    resultado = modificar_cantidad_producto(producto_id, 2)

    # Verificar actualización de cantidad
    carrito_actualizado = cargar_carrito()
    assert resultado is True
    assert carrito_actualizado[producto_id]["cantidad"] == 2

def test_agregar_producto_existente():
    producto_id = "PROD789"
    carrito = cargar_carrito()

    # Agregar el producto dos veces
    agregar_producto_carrito(producto_id, "Teclado Mecánico", 100, 1)
    resultado = agregar_producto_carrito(producto_id, "Teclado Mecánico", 100, 1)

    # Verificar que solo se haya aumentado la cantidad en lugar de duplicarlo
    carrito_actualizado = cargar_carrito()
    assert resultado is True
    assert carrito_actualizado[producto_id]["cantidad"] == 2