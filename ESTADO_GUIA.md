# Estado de la guía

Leyenda: [x] hecho y verificado · [~] hecho, verificado solo en el entorno de Claude (TestClient), falta en tu PC · [ ] pendiente

## Reflexión (EV01)
- [x] Documento de ~media página con las 4 respuestas (revisado visualmente, 1 página)
- [ ] Completar nombre, instructor y fecha en la portada

## Conceptos (EV02)
- [x] Cuadro Flask vs FastAPI de 6 filas
- [x] Mapa conceptual con API, HTTP, método, endpoint, JSON y código de estado (revisado visualmente)
- [ ] Completar nombre, instructor y fecha

## Práctica 3.3
- [x] practica_3_3/main.py con los 6 endpoints (raíz, productos/{id}, buscar, categorias/{id}, saludo/{nombre}, filtrar)
- [~] Respuestas correctas, incluidos 422 en /productos/abc y /filtrar inválido (12 casos con TestClient)
- [ ] venv, instalación y servidor en tu PC
- [ ] Try it out en /docs de todos los endpoints
- [ ] Capturas reales en evidencias/capturas/3_3/

## Reto 3.4
- [x] reto_3_4/main.py con los 5 endpoints y los 3 productos originales
- [~] 9 casos probados con TestClient (incluye 404, 422, búsqueda sin coincidencias y sin distinguir mayúsculas)
- [ ] Try it out en /docs de los 5 endpoints en tu PC
- [ ] Capturas reales en evidencias/capturas/3_4/
- [x] README, requirements.txt, .gitignore, README raíz
- [ ] Repositorio en GitHub y enlace real (pendiente de ti)

## Revisión final
- [ ] Capturas reales (no se simularon)
- [ ] No subir venv/ ni .env
