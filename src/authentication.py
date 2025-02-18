import json
import os

DB_FILE = "data/users.json"

def cargar_usuarios():
    """ Carga los usuarios desde el archivo JSON. """
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_usuarios(data):
    """ Guarda los usuarios en el archivo JSON. """
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

def registrar_usuario(email, password):
    """ Registra un usuario solo si tiene una contraseña válida y no existe ya en la base de datos. """
    usuarios = cargar_usuarios()

    if email in usuarios or not password.strip():
        return False  # Retorna False si el usuario ya existe o la contraseña está vacía
    
    usuarios[email] = {"password": password, "verificado": False}
    guardar_usuarios(usuarios)
    return True  # Retorna True si el registro fue exitoso

def autenticar_usuario(email, password):
    """ Permite el inicio de sesión solo si el usuario está registrado y su contraseña es correcta. """
    usuarios = cargar_usuarios()
    
    if email in usuarios and usuarios[email]["password"] == password and usuarios[email].get("verificado", False):
        return True  # Usuario autenticado con éxito
    
    return False  # Autenticación fallida

def bloquear_usuario(email):
    """ Bloquea una cuenta de usuario si está en la base de datos. """
    usuarios = cargar_usuarios()
    
    if email in usuarios:
        usuarios[email]["bloqueado"] = True
        guardar_usuarios(usuarios)
        return True  # La cuenta ha sido bloqueada con éxito
    
    return False  # El usuario no existe y no se puede bloquear