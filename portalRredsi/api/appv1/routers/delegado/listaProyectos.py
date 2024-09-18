from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from appv1.routers.login import get_current_user
from appv1.schemas.usuario import UserResponse
from db.database import get_db
from appv1.crud.delegado.asistencia import get_all_projects
from appv1.crud.permissions import get_permissions
