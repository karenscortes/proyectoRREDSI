from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.admin.gest_asistentes_externos import existing_email, existing_record, existing_user
from appv1.crud.usuarios import create_institutional_data, create_user_sql, get_institutional_details,  get_user_by_email, get_user_by_id, update_institutional_data, update_password, update_user
from appv1.routers.login import get_current_user
from appv1.schemas.detalle_institucional import DetalleInstitucional, DetalleInstitucionalUpdate
from appv1.schemas.usuario import ResponseLoggin, UserCreate, UserResponse, UserUpdate, resetPassword
from core.security import get_hashed_password, verify_password
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

# Obtener info actual de la persona logueada
@router_user.get("/me/get_institutional_details/", response_model=Optional[DetalleInstitucional])
def read_current_user(
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)# Obtener el usuario autenticado desde el token
):
    information = get_institutional_details(db,current_user.id_usuario)
    return information

#Actualizar datos personales
    
@router_user.put("/update/{user_id}/", response_model=UserUpdate)
def update_user_info(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    
    if user_id != current_user.id_usuario:
        permisos = get_permissions(db, current_user.id_rol, MODULE)
        if not permisos.p_actualizar:
            raise HTTPException(status_code=401, detail="No está autorizado a actualizar este usuario")
    
    verify_user = existing_user(db, user_id)
    if verify_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user.correo and user.correo != current_user.correo: 
        verify_new_email = existing_email(db, user.correo)

        if verify_new_email:
            raise HTTPException(status_code=400, detail="El email ya está registrado por otro usuario")
    
    db_user = update_user(db, user_id, user)
    
    
    if user.clave:  
        hashed_password = get_hashed_password(user.clave)  
        update_password(db, user_id, hashed_password)  

    if db_user:

        updated_user=existing_user(db, user_id)

        user = UserUpdate(
            id_tipo_documento= updated_user.id_tipo_documento,
            documento= updated_user.documento,
            nombres=updated_user.nombres,
            apellidos=updated_user.apellidos,
            celular=updated_user.celular,
            correo=updated_user.correo
        )

        return user
    else:
        raise HTTPException(status_code=500, detail="Error al actualizar el usuario")


@router_user.put("/update-password/")
def update_pass(
    data:resetPassword,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    if data.email != current_user.correo:
        permisos = get_permissions(db, current_user.id_rol, MODULE)
        if not permisos.p_actualizar:
            raise HTTPException(status_code=401, detail="No está autorizado para actualizar este usuario")
        
    user = existing_email(db, data.email)

    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not verify_password(data.current_password,user.clave):
        raise HTTPException(status_code=401, detail="Contraseña Incorrecta")
    isUpdated = update_password(db, data.email, data.new_password)
    if not isUpdated:
        raise HTTPException(status_code=500, detail="Error al actualizar el usuario")
    

# Actcualizar detalle institucional
@router_user.put("/update-institutional-data/{user_id}/")
def update_institutional_info(
    user_id: int,
    data: DetalleInstitucionalUpdate,
    db: Session = Depends(get_db),
):
        
    verify_record = existing_record(db, user_id)
    if verify_record is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    
    db_data = update_institutional_data(db,user_id, data)

    if not db_data:
        raise HTTPException(status_code=500, detail="Error al actualizar los datos institucionales")
    return db_data

# Crear Detalle Institucional
@router_user.post("/create-institutional-data/")
async def insert_institutional_data(
    data: DetalleInstitucional, 
    db: Session = Depends(get_db),    
):
    respuesta = create_institutional_data(db, data)
    if respuesta:
        return {"mensaje":"Datos institucionales ingresados exitosamente"}
    else:
        raise HTTPException(status_code=500, detail="Error al ingresar datos institucionales")
        
