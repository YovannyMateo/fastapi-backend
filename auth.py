from fastapi import HTTPException, Depends, Header
from models import Usuario
from database import usuarios_db, tokens_db

def get_usuario_actual(token: str = Header(...)):
    username = tokens_db.get(token)

    if not username:
        raise HTTPException(status_code=401, detail="Token invalido")

    usuario = usuarios_db.get(username)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no existe")

    if not usuario.esta_logueado:
        raise HTTPException(status_code=403, detail="No autorizado")

    return usuario


def requiere_admin(usuario: Usuario = Depends(get_usuario_actual)):
    if usuario.role != "admin":
        raise HTTPException(status_code=403, detail="Acceso denegado")

    return usuario
