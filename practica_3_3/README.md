# Práctica 3.3 — Primera API con FastAPI

Endpoints de la práctica guiada (solo GET, sin base de datos).

## Ejecutar (PowerShell, Windows)
```powershell
cd practica_3_3
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```
Si PowerShell bloquea la activación: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` y volver a activar.
Detener el servidor: `Ctrl+C`.

URLs: http://127.0.0.1:8000 · http://127.0.0.1:8000/docs · http://127.0.0.1:8000/redoc

## Endpoints
| Ruta | Parámetros | Respuesta de ejemplo |
|---|---|---|
| `GET /` | — | `{"mensaje": "Mi primera API con FastAPI"}` |
| `GET /productos/{producto_id}` | ruta, `int` | `/productos/5` → `{"producto_id": 5, "mensaje": "Producto solicitado"}`; `/productos/abc` → 422 |
| `GET /buscar` | consulta: `nombre` (str, opcional), `precio_max` (float, opcional) | `/buscar?nombre=teclado&precio_max=150000` → `{"buscando": "teclado", "precio_maximo": 150000.0}` |
| `GET /categorias/{categoria_id}` | ruta, `int` | `{"categoria_id": 2, "mensaje": "Categoria solicitada"}` |
| `GET /saludo/{nombre}` | ruta, `str` | `/saludo/Ana` → `{"saludo": "Hola, Ana"}` |
| `GET /filtrar` | consulta: `categoria` (str), `disponible` (bool), ambos obligatorios | `{"categoria": "Perifericos", "disponible": true}` |

Parámetro de ruta: va dentro de la URL y identifica un recurso. Parámetro de consulta: va después de `?` y es opcional si tiene valor por defecto.

Capturas: `evidencias/capturas/3_3/`.
