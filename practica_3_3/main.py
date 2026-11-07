from fastapi import FastAPI

app = FastAPI()


# Paso 3: endpoint raíz
@app.get("/")
def inicio():
    return {"mensaje": "Mi primera API con FastAPI"}


# Paso 6: parámetro de ruta (producto_id se valida como entero)
@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    return {"producto_id": producto_id, "mensaje": "Producto solicitado"}


# Paso 7: parámetros de consulta opcionales (tienen valor por defecto)
@app.get("/buscar")
def buscar_productos(nombre: str = "", precio_max: float = 0):
    return {"buscando": nombre, "precio_maximo": precio_max}


# Ejercicio 1: parámetro de ruta entero
@app.get("/categorias/{categoria_id}")
def obtener_categoria(categoria_id: int):
    return {"categoria_id": categoria_id, "mensaje": "Categoria solicitada"}


# Ejercicio 2: parámetro de ruta de texto
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}"}


# Ejercicio 3: parámetros de consulta obligatorios (sin valor por defecto)
@app.get("/filtrar")
def filtrar(categoria: str, disponible: bool):
    return {"categoria": categoria, "disponible": disponible}
