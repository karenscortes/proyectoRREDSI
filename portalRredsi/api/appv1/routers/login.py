from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.crud.permissions import get_all_permissions
from appv1.crud.usuarios import create_user_sql, get_user_by_email, get_user_by_id, update_password
from appv1.schemas.usuario import ChangePassword, ResponseLoggin, UserCreate, UserLoggin
from core.security import create_access_token, verify_password, verify_token
from db.database import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/access/token")

async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    user = await verify_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_db = get_user_by_id(db, user)
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not user_db.user_status:
        raise HTTPException(status_code=403, detail="User Deleted, Not authorized")
    return user_db

def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_email(db, username)
    if not user:
        return False
    if not verify_password(password, user.passhash):
        return False
    return user

@router.post("/token", response_model=ResponseLoggin)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Datos Incorrectos en email o password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.user_id, "rol":user.user_role}
    )

    permisos = get_all_permissions(db, user.user_role)

    return ResponseLoggin(
        user=UserLoggin(
            user_id=user.user_id,
            full_name=user.full_name,
            mail=user.mail,
            user_role=user.user_role
        ),
        permissions=permisos,
        access_token=access_token
    )

@router.post("/register")
async def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    user.user_role = 'Cliente'
    respuesta = create_user_sql(db, user)
    if respuesta:
        return {"mensaje":"usuario registrado con éxito"}


# Ejemplo Completo recordar contraseña
# usa código que expira en 2 minutos
# usa servicio API de mailersend
# instalar pip install requests Es ampliamente utilizada para interactuar con servicios web, APIs 

import random
import string
import time
import requests

# almacen de códigos de verificación.
verification_codes = {}

# función que genera el código alfanumerico de 6 digitos
def generate_code(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_email(to_email: str, subject: str, body: str):
    url = "https://api.mailersend.com/v1/email"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer mlsn.1c6857b7db7c6cb3155af4607e0ccae43c62007dddd3bc2fec2d90c86fd126f8"
    }
    data = {
        "from": {
            "email": "MS_OsYbwy@trial-x2p0347wwnklzdrn.mlsender.net"
        },
        "to": [
            {
                "email": to_email
            }
        ],
        "subject": subject,
        "text": body,
        "html": body
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Esto genera una excepción si el código de estado es 4xx o 5xx

        # Verificar si la respuesta tiene contenido antes de intentar convertirla en JSON
        if response.content and response.headers.get('Content-Type') == 'application/json':
            return response.json()  # Intentar convertir la respuesta en JSON
        else:
            print(f"Respuesta sin contenido JSON: {response.status_code} - {response.text}")
            return {"message": "Email enviado, pero no se recibió una respuesta JSON válida"}

    except requests.HTTPError as e:
        if e.response is not None:
            print(f"Error al enviar email: {e.response.status_code} - {e.response.text}")
        else:
            print("Error al enviar email: No se recibió respuesta del servidor.")
        raise HTTPException(status_code=500, detail="Error al enviar email")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        raise HTTPException(status_code=500, detail="Error inesperado al procesar el correo")


@router.post("/request-reset-code")
async def request_reset_code(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Email no registrado")

    code = generate_code()
    verification_codes[email] = {'code': code, 'expires_at': time.time() + 1200}

    try:
        send_email(
            to_email=email,
            subject="Código para modificar tu contraseña",
            body=f"El código de verificación es: {code}"
        )
    except requests.HTTPError as e:
        print(f"Error al enviar email: {e.response.text}")
        raise HTTPException(status_code=500, detail="Error al enviar email")

    return {"message": "Código enviado, vefificar email"}


@router.post("/change-password")
async def change_password(data: ChangePassword, db: Session = Depends(get_db)):
    # Verificar código
    code_info = verification_codes.get(data.email)
    if not code_info or code_info['code'] != data.code or time.time() > code_info['expires_at']:
        raise HTTPException(status_code=400, detail="Código Invalido o ya expiró")

    # Cambiar la contraseña
    user = get_user_by_email(db, data.email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualiza la contraseña del usuario
    success = update_password(db, data.email, data.new_password)

    # Eliminar código de verificación (opcional)
    del verification_codes[data.email]

    return {"message": "Password actualizado correctamente"}