from sys import prefix
from fastapi import FastAPI
from appv1.routers import login, usuarios, rol
from appv1.routers.admin import admin
from appv1.routers.delegado import asignarProyectoEtapaVirtual, asistencia, listaEvaluadores, postulaciones, proyectosSinAsignar, salas
from appv1.routers.evaluador import evaluadores

from appv1.routers.superadmin import superadmin
from db.database import test_db_connection
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# USUARIOS
app.include_router(usuarios.router_user, prefix="/users", tags=["Usuarios"])

# ROLES 
app.include_router(rol.router_rol, prefix="/roles", tags=["Roles"])

# LOGIN
app.include_router(login.router, prefix="/access", tags=["access"])

# EVALUADORES 
app.include_router(evaluadores.routerObtenerProyectos, prefix="/obtenerProyectosEvaluador", tags=["Evaluadores"])
app.include_router(evaluadores.routerInsertarPostulacionEvaluador, prefix="/postulacionEvaluador", tags=["Evaluadores"])
app.include_router(evaluadores.routerInsetarCalificacionRubrica, prefix="/calificacionRubrica", tags=["Evaluadores"])
app.include_router(evaluadores.routerObtenerHorarioEvaluador, prefix="/obtenerHorarioEvaluador", tags=["Evaluadores"])

# DELEGADO
app.include_router(asignarProyectoEtapaVirtual.router_proyecto_etapa_uno, prefix="/asignarProyectoEtapaVirtual", tags=["Delegado"])
app.include_router(salas.router_sala, prefix="/salas", tags=["Delegado"])
app.include_router(postulaciones.router_postulaciones, prefix="/postulaciones", tags=["Delegado - Lista Postulaciones"])
app.include_router(listaEvaluadores.router_evaluadores, prefix="/listaEvaluadores", tags=["Delegado - Lista Evaluadores"])
app.include_router(proyectosSinAsignar.router_proyectosSinAsignar, prefix="/proyectosSinAsignar", tags=["Delegado - Lista Proyectos sin Asignar"])
app.include_router(asistencia.router_asistencia,prefix="/asistencia", tags=["Delegado - Asistencia"])

# ADMIN 
app.include_router(admin.router_admin, prefix="/admin", tags=["Administrador"])

#SUPERADMIN
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
