from fastapi import FastAPI, HTTPException

app = FastAPI(title="Mini-API de Catalogo")

# Datos temporales en memoria (sin base de datos, solo lectura)
productos = [
    {"id": 1, "nombre": "Teclado mecanico", "precio": 120000, "categoria": "Perifericos"},
    {"id": 2, "nombre": "Mouse gamer", "precio": 85000, "categoria": "Perifericos"},
    {"id": 3, "nombre": "Monitor 24", "precio": 650000, "categoria": "Pantallas"},
]


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la Mini-API de Catalogo"}


@app.get("/productos")
def listar_productos():
    return productos


@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.get("/categorias")
def listar_categorias():
    categorias = []
    for producto in productos:
        if producto["categoria"] not in categorias:
            categorias.append(producto["categoria"])
    return categorias


# `nombre` es obligatorio; la busqueda no distingue mayusculas/minusculas
@app.get("/buscar")
def buscar_productos(nombre: str):
    texto = nombre.lower()
    return [p for p in productos if texto in p["nombre"].lower()]
