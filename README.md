# FastAPI Backend Auth System

Este es un backend desarrollado con FastAPI que implementa un sistema básico de autenticación.

##  Funcionalidades

- Registro de usuarios
- Login con token
- Logout
- Protección de rutas con Depends
- Sistema de roles (user / admin)

##  Endpoints

### Auth
- POST /auth/registro
- POST /auth/login
- POST /auth/logout

### Usuario
- GET /perfil
- GET /admin (solo admin)

##  Tecnologías usadas

- Python
- FastAPI
- Pydantic

##  Cómo ejecutar

```bash
uvicorn main:app --reload
http://127.0.0.1:8000/docs

Notas

Este proyecto usa almacenamiento en memoria (diccionarios), no base de datos.

 Autor

Yovanny Mateo
