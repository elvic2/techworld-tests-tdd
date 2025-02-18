import sys
import os
import pytest

# Agregar src/ al PYTHONPATH manualmente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar la funcionalidad que estamos probando
from products import cargar_productos, guardar_productos, crear_producto, editar_producto, activar_producto

def test_crear_producto():
    productos = cargar_productos()
    producto_id = "PROD100"

    # Crear un nuevo producto de prueba
    resultado = crear_producto(producto_id, "Mouse Inalámbrico", "Mouse ergonómico con sensor óptico", 50, 30, "Periféricos")

    # Verificar que el producto fue creado
    productos_actualizados = cargar_productos()
    assert resultado is True
    assert producto_id in productos_actualizados

def test_editar_producto():
    producto_id = "PROD200"
    
    # Crear el producto antes de editarlo si no existe
    crear_producto(producto_id, "Teclado", "Teclado estándar", 25, 20, "Periféricos")

    # Modificar la descripción y el precio del producto
    resultado = editar_producto(producto_id, "Teclado Mecánico RGB", 80)

    # Verificar que los cambios se reflejaron
    productos_actualizados = cargar_productos()
    assert resultado is True
    assert productos_actualizados[producto_id]["descripcion"] == "Teclado Mecánico RGB"
    assert productos_actualizados[producto_id]["precio"] == 80

def test_activar_producto():
    producto_id = "PROD300"

    # Crear el producto antes de activarlo
    crear_producto(producto_id, "Monitor Full HD", "Monitor 24 pulgadas", 200, 10, "Monitores")

    # Activar el producto
    resultado = activar_producto(producto_id)

    # Verificar que el producto está activo
    productos_actualizados = cargar_productos()
    assert resultado is True
    assert productos_actualizados[producto_id]["estado"] == "activo"

def test_crear_producto_sin_datos():
    # Intentar crear un producto sin nombre
    resultado = crear_producto("PROD400", "", "Descripción vacía", 0, 0, "Accesorios")

    # Verificar que no se permite la creación
    assert resultado is False