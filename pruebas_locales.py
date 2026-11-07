from fastapi.testclient import TestClient
import importlib.util, sys

def cargar(ruta):
    spec = importlib.util.spec_from_file_location("m", ruta)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return TestClient(m.app)

p = cargar("practica_3_3/main.py")
r = cargar("reto_3_4/main.py")
casos = [
 (p, "/", 200), (p, "/productos/5", 200), (p, "/productos/abc", 422),
 (p, "/buscar", 200), (p, "/buscar?nombre=teclado", 200),
 (p, "/buscar?nombre=teclado&precio_max=150000", 200),
 (p, "/categorias/2", 200), (p, "/saludo/Ana", 200),
 (p, "/filtrar?categoria=Perifericos&disponible=true", 200),
 (p, "/filtrar?categoria=Perifericos&disponible=false", 200),
 (p, "/filtrar?categoria=Perifericos&disponible=quizas", 422),
 (p, "/filtrar", 422),
 (r, "/", 200), (r, "/productos", 200), (r, "/productos/2", 200),
 (r, "/productos/999", 404), (r, "/productos/abc", 422),
 (r, "/categorias", 200), (r, "/buscar?nombre=mouse", 200),
 (r, "/buscar?nombre=TECLADO", 200), (r, "/buscar?nombre=inexistente", 200),
]
fallos = 0
for c, url, esp in casos:
    resp = c.get(url)
    ok = resp.status_code == esp
    fallos += not ok
    print("OK " if ok else "FAIL", resp.status_code, url, str(resp.json())[:90])
print("fallos:", fallos)
sys.exit(fallos)
