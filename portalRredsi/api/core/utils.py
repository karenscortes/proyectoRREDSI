import secrets
import string
from fastapi import HTTPException
import uuid
import os
from fastapi import UploadFile
import shutil
from core.config import settings

from fastapi import HTTPException, UploadFile 

def generate_Contraseña(length=30):
    # Caracteres posibles para el ID aleatorio
    characters = string.ascii_letters + string.digits
    # Genera un ID aleatorio de la longitud deseada
    random_id = ''.join(secrets.choice(characters) for _ in range(length))

    return random_id

def generate_project_id(length=5):
    characters = string.digits 

    random_id = ''.join(secrets.choice(characters) for _ in range(length))
    return random_id


def generate_user_id(length=11): 
    # Caracteres posibles para el ID aleatorio
    characters = string.ascii_letters + string.digits 

    # Genera un ID aleatorio de la longitud deseada
    random_id = ''.join(secrets.choice(characters) for _ in range(length))
    return random_id

def generate_user_id_int(length=6): 
    characters = string.digits 

    random_id = ''.join(secrets.choice(characters) for _ in range(length))
    return random_id



# Para subir archivos

# Configuración del directorio de subida se asigna en .env
# UPLOAD_FOLDER = "static/files"
os.makedirs(settings.UPLOAD_FOLDER, exist_ok=True)

# Tipos de archivos permitidos
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx", "xls", "xlsx"}

# Verifica si el archivo tiene una extensión permitida.
def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Guarda el archivo en el directorio de subida y devuelve la ruta completa del archivo.
def save_file(file: UploadFile) -> str:
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Invalid file type. Allowed types: pdf, doc, docx, xls, xlsx")
    
    file_extension = file.filename.rsplit('.', 1)[1].lower()
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_location = os.path.join(settings.UPLOAD_FOLDER, unique_filename)
    
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)  # alamacena el archivo
    
    return file_location  # Devuelve la ruta completa del archivo