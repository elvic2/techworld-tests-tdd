# TechWorld - Pruebas Automatizadas con TDD en Python

## 📌 Descripción del Proyecto  
Este proyecto implementa pruebas automatizadas para la plataforma **TechWorld**, un e-commerce de productos electrónicos. Se ha seguido el enfoque **TDD (Test-Driven Development)** con `pytest`, asegurando que el código sea probado antes de su implementación.

## 📌 Funcionalidades Probadas  
Se han definido y ejecutado pruebas automatizadas para validar las siguientes funcionalidades:  
- **Autenticación de Usuarios** (Registro, Inicio de sesión, Bloqueo por intentos fallidos).  
- **Seguimiento de Pedidos** (Estado de pedidos, cambios de estado, notificaciones).  
- **Gestión del Carrito y Wishlist** (Agregar, modificar productos, stock).  
- **Gestión de Productos** (Creación, edición, activación en la tienda).  

## 📌 Tecnologías Utilizadas  
- **Python 3.x** - Lenguaje de programación.  
- **pytest** - Framework de pruebas unitarias.  
- **JSON** - Emulación de base de datos para pruebas.  
- **Git y GitHub** - Control de versiones.  

## 📌 Enfoque TDD  
Las pruebas se han desarrollado siguiendo el ciclo clásico de **TDD**:  
1. **Escribir una prueba que falle** → Se define la prueba en `tests/`.  
2. **Escribir el código mínimo para que pase** → Se implementa en `src/`.  
3. **Refactorizar** → Se optimiza el código sin cambiar su funcionalidad.  

## 📌 Resultados de las Pruebas  
Todas las pruebas han sido ejecutadas con éxito, validando el correcto funcionamiento de las funcionalidades clave de la plataforma.  

## 📌 Instalación y Configuración  
### 1️⃣ **Clonar el Repositorio**  
```bash
git clone https://github.com/elvic2/techworld-tests-tdd.git
cd techworld-tests-tdd
```

### 2️⃣ **Crear y Activar el Entorno Virtual**
```bash
python3 -m venv venv
source venv/bin/activate   # En macOS/Linux
venv\Scripts\activate      # En Windows
```
### 3️⃣ **Instalar Dependencias**
```bash
pip install -r requirements.txt
```
### 4️⃣ **Ejecutar las Pruebas**
```bash
pytest -v
```
📌 Contacto
[victorh.vargasf@autonoma.edu.co]
