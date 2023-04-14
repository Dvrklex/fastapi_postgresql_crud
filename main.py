import datetime
import os
import uuid
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext

import databases
import sqlalchemy

from models import *


# Load virtual env
load_dotenv(".env")

# Utiliza las variables de entorno
DATABASE_URL = os.getenv('DATABASE_URL')

# Inicializa la aplicación
app = FastAPI()

# Configuración de Passlib
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Conexión a la base de datos
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)

# Define la tabla de usuarios
users = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("usuario", sqlalchemy.String),
    sqlalchemy.Column("contrasenia", sqlalchemy.String),
    sqlalchemy.Column("nombre", sqlalchemy.String),
    sqlalchemy.Column("apellido", sqlalchemy.String),
    sqlalchemy.Column("genero", sqlalchemy.CHAR),
    sqlalchemy.Column("creado", sqlalchemy.String),
    sqlalchemy.Column("estado", sqlalchemy.CHAR),
)

metadata.create_all(engine)

# Manejadores de eventos
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect() 

# CRUD de usuarios
@app.get("/users", response_model=list[UserList])
async def find_all_users():
    query = users.select()
    return await database.fetch_all(query) 

@app.post('/users', response_model=UserList)
async def create_user(user: UserEntry):
    getID = str(uuid.uuid1())
    getDate = str(datetime.datetime.now())
    query = users.insert().values(
        id= getID,
        usuario= user.usuario,
        contrasenia=pwd_context.hash(user.contrasenia),
        nombre= user.nombre,
        apellido=user.apellido,
        genero = user.genero,
        creado = getDate,
        estado = "1"
    )
    await database.execute(query)
    return {
        "id": getID,
        **user.dict(),
        "creado":getDate,
        "estado":"1"
    }
    
@app.get('/users/{id}', response_model=UserList)
async def find_user_by_id(id: str):
    query = users.select().where(users.c.id == id)
    user = await database.fetch_one(query)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put('/users', response_model=UserList)
async def update_user(user: UserUpdate):
    getDate = str(datetime.datetime.now())
    query = users.update().where(users.c.id == user.id).values(
        nombre = user.nombre,
        apellido = user.apellido,
        genero = user.genero,
        estado = user.estado,
        creado = getDate
    )
    await database.execute(query)
    return await find_user_by_id(user.id)

@app.delete("/users/{id}")
async def delete_user(id: str):
    query = users.delete().where(users.c.id == id)
    await database.execute(query)
    return {
        "status": True,
        "mensaje": "Usuario eliminado correctamente."
    }


# uvicorn main:app --reload