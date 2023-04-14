##Models 
from pydantic import BaseModel, Field
class UserList(BaseModel):
    id: str
    usuario: str
    contrasenia: str
    nombre: str
    apellido: str
    genero: str
    creado: str
    estado: str 
 
class UserEntry(BaseModel):   
    id: str = Field(...,example="plumita")
    usuario: str = Field(...,example="plumita")
    contrasenia: str = Field(..., example="Plumi")
    nombre: str = Field(..., example="IO")
    apellido: str = Field(..., example="Perico")
    genero: str = Field(...,example="F")
    
class UserUpdate(BaseModel):
    id: str = Field(...,example="Ingresa tu ID")
    nombre: str = Field(..., example="IO")
    apellido: str = Field(..., example="Perico")
    genero: str = Field(...,example="F")
    estado: str = Field(...,example="1")


class UserDelete(BaseModel):
    id: str = Field(..., example='Ingresa tu id')

    