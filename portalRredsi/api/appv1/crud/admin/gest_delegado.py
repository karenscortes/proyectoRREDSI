# Crear un usuario
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
      
from sqlalchemy import text


def get_delegados_activos(db: Session):
    try:
        sql = text("""
            SELECT * from usuarios JOIN roles ON usuarios.id_rol = roles.id_rol  
            JOIN detalles_institucionales ON usuarios.id_usuario = detalles_institucionales.id_usuario
            JOIN titulos_academicos ON usuarios.id_usuario = titulos_academicos.id_usuario
            WHERE roles.nombre = 'Delegado' AND usuarios.estado = 'activo';
        """)
        result = db.execute(sql).fetchall() 
        return result     
    except SQLAlchemyError as e:
        print(f"Error al buscar los delegados: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar los delegados")


