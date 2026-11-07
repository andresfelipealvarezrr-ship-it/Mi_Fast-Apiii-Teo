# Mini-API de Catálogo (Reto 3.4)

API de **solo lectura** para consultar un catálogo de productos de comercio electrónico. Los datos son una lista en memoria; no usa base de datos.

## Requisitos previos
Python 3.10+, VS Code (o cualquier terminal) y, opcionalmente, Git para clonar.

## Instalación y ejecución (PowerShell, Windows)
```powershell
git clone <URL-DEL-REPOSITORIO>
cd Guia_1_FastAPI_SENA\reto_3_4
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn main:app --reload
```
Si PowerShell bloquea la activación: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`.
Detener el servidor: `Ctrl+C`.

URLs: http://127.0.0.1:8000 · http://127.0.0.1:8000/docs · http://127.0.0.1:8000/redoc

## Endpoints
| Ruta | Parámetros | Respuesta |
|---|---|---|
| `GET /` | — | `{"mensaje": "Bienvenido a la Mini-API de Catalogo"}` |
| `GET /productos` | — | Lista con los 3 productos |
| `GET /productos/{producto_id}` | ruta, `int` | `/productos/2` → Mouse gamer; id inexistente → 404 `{"detail": "Producto no encontrado"}`; id no entero → 422 |
| `GET /categorias` | — | `["Perifericos", "Pantallas"]` |
| `GET /buscar` | consulta: `nombre` (str, **obligatorio**) | `?nombre=mouse` → lista con Mouse gamer; sin coincidencias → `[]`. No distingue mayúsculas |

## Pruebas
Probados desde `/docs` con *Try it out → Execute*. Capturas en `evidencias/capturas/3_4/`.
