# FastApi + PostgreSQL 13 CRUD

Este proyecto es una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) construida con FastAPI y PostgreSQL. Permite gestionar usuarios en una base de datos.

### Requisitos
Requisitos
Para poder ejecutar este proyecto, necesitarás tener instalado lo siguiente:

 - Python 3.9.X
 - PostgreSQL 13
 - Pip (gestor de paquetes de Python)

### Instalación
1. Clona el repositorio.
    ```bash
    git clone https://github.com/Dvrklex/fastapi_postgresql_crud.git
    ```
2. Navega a la carpeta del proyecto.
    ```bash
    cd fastapi_postgresql_crud
    ```
3. Crea un entorno virtual.
    En linux o mac:
    ```bash
    python -m venv <nombre_del_entorno>
    ```
    O en windows:
    ```bash
    source <nombre_del_entorno>/bin/activate <nombre_del_entorno>\Scripts\activate
    ```
4. Instala las dependencias.
    ```bash
    pip install -r requirements.txt
    ```
5. Configura las variables de entorno.
    ```bash
    DATABASE_URL=postgresql://usuario:contraseña@localhost:puerto/tu_base_de_datos
    API_KEY=tu_api_key_secreta
    ```
## Ejecuta el proyecto
1. Inicia el servidor de FastAPI.
```bash
uvicorn main:app --reload
```
2. Accede a la API en tu navegador con la siguiente URL: http://localhost:8000/docs
3. Prueba los endpoint de la API con SwaggerUI.
