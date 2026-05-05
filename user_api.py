from fastapi import Depends, APIRouter
from models import Usuario
from auth import get_usuario_actual, requiere_admin

print("USER API CARGADO")

router = APIRouter()

@router.get("/perfil")
def perfil(usuario: Usuario = Depends(get_usuario_actual)):
    return {
        "username": usuario.username,
        "role": usuario.role
    }

@router.get("/admin")
def admin_panel(usuario: Usuario = Depends(requiere_admin)):
    return {
        "mensaje": f"Bienvenido admin {usuario.username}"
    }
    