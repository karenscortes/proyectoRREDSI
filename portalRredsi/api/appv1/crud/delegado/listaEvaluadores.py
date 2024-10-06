from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

def get_all_evaluators(db: Session, page: int = 1, page_size: int = 10):
    try:
        offset = (page - 1) * page_size
        sql = text(
        """
            SELECT DISTINCT usuarios.id_usuario,
            usuarios.correo,
            usuarios.estado,
            usuarios.nombres,
            usuarios.apellidos,
            usuarios.documento,
            usuarios.celular,
            instituciones.nombre AS nombre_institucion,
            area1.nombre         AS area_conocimiento,
            area2.nombre         AS otra_area
            FROM usuarios
                INNER JOIN detalles_institucionales ON (usuarios.id_usuario = detalles_institucionales.id_usuario)
                INNER JOIN instituciones ON (detalles_institucionales.id_institucion = instituciones.id_institucion)
                LEFT JOIN areas_conocimiento area1 ON (detalles_institucionales.id_primera_area_conocimiento = area1.id_area_conocimiento)
                LEFT JOIN areas_conocimiento area2 ON (detalles_institucionales.id_segunda_area_conocimiento = area2.id_area_conocimiento)
            WHERE usuarios.id_rol  IN (
                SELECT id_rol
                FROM roles
                WHERE nombre = 'Evaluador'
            )
            LIMIT :page_size OFFSET :offset;

        """ 
        )
        params = {
            "page_size": page_size,
            "offset": offset
        }
        
        result = db.execute(sql,params).mappings().all()
        count_sql = text("""SELECT COUNT(*)
                            FROM usuarios
                                INNER JOIN detalles_institucionales ON (usuarios.id_usuario = detalles_institucionales.id_usuario)
                                INNER JOIN instituciones ON (detalles_institucionales.id_institucion = instituciones.id_institucion)
                                LEFT JOIN areas_conocimiento area1 ON (detalles_institucionales.id_primera_area_conocimiento = area1.id_area_conocimiento)
                                LEFT JOIN areas_conocimiento area2 ON (detalles_institucionales.id_segunda_area_conocimiento = area2.id_area_conocimiento)
                            WHERE usuarios.id_rol  IN (
                                SELECT id_rol
                                FROM roles
                                WHERE nombre = 'Evaluador'
                            ) """)
        total_evaluadores = db.execute(count_sql).scalar()

            # Calcular el número total de páginas
        total_pages = (total_evaluadores + page_size - 1) // page_size

        return result, total_pages
    except SQLAlchemyError as e:
        print(f"Error al obtener los evaluadores: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener todos los evaluadores")

def update_evaluator_status(db: Session, id_usuario:int, estado: str):
    try:
        sql = text("UPDATE usuarios SET estado = :estado WHERE id_usuario = :id_usuario")
        params = {
            "estado": estado,
            "id_usuario": id_usuario
        }
        db.execute(sql, params)
        db.commit()
        return True
    except SQLAlchemyError as e:
        print(f"Error al actualizar estado de evaluador: {e}")
        raise HTTPException(status_code=500, detail="Error al actualizar estado de evaluador")

def get_evaluator_by_document(db: Session, documento: str):
    try:
        sql = text(
        """
            SELECT usuarios.id_usuario,
            usuarios.correo,
            usuarios.estado,
            usuarios.nombres,
            usuarios.apellidos,
            usuarios.documento,
            usuarios.celular,
            instituciones.nombre AS nombre_institucion,
            area1.nombre         AS area_conocimiento,
            area2.nombre         AS otra_area
            FROM usuarios
                INNER JOIN detalles_institucionales ON (usuarios.id_usuario = detalles_institucionales.id_usuario)
                INNER JOIN instituciones ON (detalles_institucionales.id_institucion = instituciones.id_institucion)
                LEFT JOIN areas_conocimiento area1 ON (detalles_institucionales.id_primera_area_conocimiento = area1.id_area_conocimiento)
                LEFT JOIN areas_conocimiento area2 ON (detalles_institucionales.id_segunda_area_conocimiento = area2.id_area_conocimiento)
            WHERE usuarios.documento LIKE :documento OR usuarios.nombres LIKE :documento 
            AND usuarios.id_rol IN (
                SELECT id_rol
                FROM roles
                WHERE nombre = 'Evaluador'
            )
        """
        )

        result = db.execute(sql, {"documento": f"%{documento}%"}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener evaluador por documento: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener evaluador por documento")

def get_evaluator_by_id(db: Session, id_evaluador: int):
    try:
        sql = text(
        """
            SELECT usuarios.id_usuario,
            usuarios.correo,
            usuarios.estado,
            usuarios.nombres,
            usuarios.apellidos,
            usuarios.celular,
            instituciones.nombre AS nombre_institucion,
            area1.nombre         AS area_conocimiento,
            area2.nombre         AS otra_area
            FROM usuarios
                INNER JOIN detalles_institucionales ON (usuarios.id_usuario = detalles_institucionales.id_usuario)
                INNER JOIN instituciones ON (detalles_institucionales.id_institucion = instituciones.id_institucion)
                LEFT JOIN areas_conocimiento area1 ON (detalles_institucionales.id_primera_area_conocimiento = area1.id_area_conocimiento)
                LEFT JOIN areas_conocimiento area2 ON (detalles_institucionales.id_segunda_area_conocimiento = area2.id_area_conocimiento)
            WHERE usuarios.id_usuario = :id_evaluador AND usuarios.id_rol IN (
                SELECT id_rol
                FROM roles
                WHERE nombre = 'Evaluador'
            )
        """
        )

        result = db.execute(sql, {"id_evaluador": id_evaluador}).fetchone()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener evaluador por id: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener evaluador por id")


