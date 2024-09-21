from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.usuarios import create_user_sql,  get_user_by_email, get_user_by_id, update_password, update_user
from appv1.routers.login import get_current_user
from appv1.schemas.usuario import UserCreate, UserResponse, UserUpdate
from core.security import get_hashed_password
from db.database import get_db
from appv1.crud.permissions import get_permissions


router_user = APIRouter()
MODULE = 3

@router_user.post("/create")
async def insert_user(
    user: UserCreate, 
    db: Session = Depends(get_db),
    current_user : UserResponse =Depends(get_current_user)
    
):

    respuesta = create_user_sql(db, user)
    if respuesta:
        return {"mensaje":"Usuario ingresado exitosamente"}
        
# Verificar si el email ya está registrado
    existing_user = get_user_by_email(db, user.correo)
    if existing_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    respuesta = create_user_sql(db, user)
    if respuesta:
        return {"mensaje":"usuario registrado con éxito"}


# Ruta para obtener un usuario por su ID
@router_user.get("/get-user/{user_id}", response_model=UserResponse)
def read_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(get_current_user)  # Usuario autenticado
):
    # Verificar si el usuario está intentando consultar su propio perfil
    if user_id != current_user.id_usuario:
        # Obtener los permisos del rol del usuario autenticado
        permisos = get_permissions(db, current_user.id_rol, MODULE)
        
        # Verificar si tiene permiso para consultar
        if not permisos.p_consultar:
            raise HTTPException(status_code=401, detail="No está autorizado para consultar este usuario")

    # Si tiene permiso o es su propio perfil, obtener el usuario
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return user

    
@router_user.put("/update/", response_model=dict)
def update_user(
    user: UserUpdate,
    user_id: Optional[int] = None,  # Parámetro opcional, si no se proporciona, actualiza al usuario autenticado
    current_user: UserResponse = Depends(get_current_user),  # Usuario autenticado
    db: Session = Depends(get_db)
):
    # Verificar si está actualizando su propio perfil o el de otro usuario
    if user_id is None:
        user_id = current_user.id_usuario  # Si no se proporciona user_id, actualiza el perfil del usuario autenticado
    
    # Verificar permisos solo si intenta actualizar el perfil de otro usuario
    if user_id != current_user.id_usuario:
        permisos = get_permissions(db, current_user.id_rol, MODULE)
        if not permisos.p_actualizar:
            raise HTTPException(status_code=401, detail="No está autorizado a actualizar este usuario")
    
    # Verificar si el usuario existe
    verify_user = get_user_by_id(db, user_id)
    if verify_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Verificar si el correo ya está registrado por otro usuario
    if user.correo:  # Solo si se proporciona un correo en la actualización
        verify_new_email = get_user_by_email(db, user.correo)
        # Asegurarse de que el correo no esté registrado por otro usuario
        if verify_new_email and verify_new_email.id_usuario != user_id:
            raise HTTPException(status_code=400, detail="El email ya está registrado por otro usuario")
    
    # Actualizar perfil de usuario (propio o de otro, según el caso)
    db_user = update_user(db, user_id, user)
    
    # Si el usuario desea actualizar su contraseña
    if user.clave:  # Si se proporciona una nueva clave, actualizamos
        hashed_password = get_hashed_password(user.clave)  # Asegurarse de tener `get_hashed_password` importado
        update_password(db, user_id, hashed_password)  # Crear esta función en tu CRUD si no existe

    if db_user:
        return {"mensaje": "Información actualizada con éxito"}
    else:
        raise HTTPException(status_code=500, detail="Error al actualizar el usuario")


