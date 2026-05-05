from pydantic import BaseModel

class Usuario:
    def __init__(self,username,password,role="user"):
        self.username = username
        self._password = password
        self._logueado = False
        self.role = role
        
    def verificar_password(self,password):
        return self._password == password
    
    def login(self):
        self._logueado = True
    
    def logout(self):
        self._logueado = False
    
    @property
    def esta_logueado(self):
        return self._logueado
    
    
    
class RegistroData(BaseModel):
    username: str
    password: str
    role: str = "user"

class LoginData(BaseModel):
    username: str
    password: str
   
   