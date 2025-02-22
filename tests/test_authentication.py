import sys
import os
import pytest

# Agregar src/ al PYTHONPATH manualmente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar la funcionalidad que estamos probando
from authentication import autenticar_usuario, bloquear_usuario, registrar_usuario, cargar_usuarios, guardar_usuarios

def test_registro_exitoso():
    email = "nuevo_usuario@example.com"

    # Cargar los usuarios y eliminar el usuario de prueba si ya existe
    usuarios = cargar_usuarios()
    if email in usuarios:
        del usuarios[email]  # Eliminar usuario si ya estaba registrado
        guardar_usuarios(usuarios)  # Guardar cambios

    # Intentar registrar el usuario nuevamente
    resultado = registrar_usuario(email, "password123")

    assert resultado is True  # Debe permitir el registro

def test_registro_fallido():
    email = "usuario_incompleto@example.com"
    resultado = registrar_usuario(email, "")  # Intentar registrar sin contraseña
    assert resultado is False  # Debe fallar el registro

def test_login_exitoso():
    email = "usuario_verificado@example.com"

    # Crear usuario y verificarlo antes de iniciar sesión
    registrar_usuario(email, "password123")
    usuarios = cargar_usuarios()
    usuarios[email]["verificado"] = True  # Marcar usuario como verificado
    guardar_usuarios(usuarios)

    # Intentar autenticación
    resultado = autenticar_usuario(email, "password123")
    assert resultado is True  # Debe permitir autenticación

def test_bloqueo_cuenta():
    email = "usuario_bloqueado@example.com"
    registrar_usuario(email, "password123")  # Crear usuario
    resultado = bloquear_usuario(email)  # Intentar bloquear la cuenta
    assert resultado is True  # La cuenta debe ser bloqueada correctamente