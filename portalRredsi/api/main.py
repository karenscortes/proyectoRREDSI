from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from appv1.crud import usuarios
from db.database import test_db_connection

app = FastAPI()

app.include_router(usuarios.router_user, prefix="/users", tags=["Usuarios"])

def on_startup():
    test_db_connection()

# Configuración de CORS para permitir todas las solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir estos métodos HTTP
    allow_headers=["*"],  # Permitir cualquier encabezado en las solicitudes
)
