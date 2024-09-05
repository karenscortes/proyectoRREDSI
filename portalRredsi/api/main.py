from fastapi import FastAPI
from appv1.routers import usuarios, rol
from appv1.routers.delegado import delegados
from appv1.routers.evaluador import evaluadores
from appv1.routers.superadmin import superadmin
from db.database import test_db_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(usuarios.router_user, prefix="/users", tags=["Usuarios"])
app.include_router(rol.router_rol, prefix="/roles", tags=["Roles"])
app.include_router(evaluadores.routerCalificarProyectos, prefix="/proyectos", tags=["Evaluadores"])
app.include_router(delegados.router_delegado, prefix="/salas", tags=["Delegado"])




app.include_router(superadmin.router_superadmin, prefix="/superadmin", tags=["SuperAdmin"])


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
