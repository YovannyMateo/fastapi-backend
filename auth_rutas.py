from fastapi import APIRouter, HTTPException,Header
from models import RegistroData,LoginData,Usuario
from database import usuarios_db,tokens_db


router = APIRouter()

@router.post("/registro")
def registrar_usuario(data: RegistroData):
    if data.username in usuarios_db:
        raise HTTPException(status_code=400, detail= "usuario existente")

   

    nuevo_usuario = Usuario(
    username=data.username,
    password=data.password,
    role=data.role
    )
    usuarios_db[data.username] = nuevo_usuario
    
    return {"mensaje": "usuario creado correctamente"}



@router.post("/login")
def login(data: LoginData):
    
    usuario = usuarios_db.get(data.username)
    
    if not usuario:
        raise HTTPException(status_code=404, detail="usuario no existe")
    
    if not usuario.verificar_password(data.password):
        raise HTTPException(status_code=401,detail="contrasena incorrecta")
    
    if  usuario.esta_logueado:
        raise HTTPException(status_code=400,detail="usuario ya esta logueado")
    
    
    usuario.login()
    
    token = "token_" + data.username
    tokens_db[token] = data.username
    
    return {"token": token}
    
    
    
@router.post("/logout")
def logout(token: str = Header(...)):
    
    
    username = tokens_db.get(token)
    
    if not username:
        raise HTTPException(status_code=401, detail="token invalido")
    
    
    usuario = usuarios_db.get(username)
    
    if not usuario:
        raise HTTPException(status_code=401, detail="usuario no existe")
    
    usuario.logout()
    
    del tokens_db[token]
    
    return{"mensaje": "usuario deslogueado exitosamente"}
    
    

    
    
    



    
    
    

    
    
    
    
    
    

    
    
    
    
   

