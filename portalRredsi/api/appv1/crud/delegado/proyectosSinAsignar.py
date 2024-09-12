from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

def get_unassigned_projects(db: Session, page: int = 1, page_size: int = 10):
        try:
                offset = (page - 1) * page_size

                sql = text(
                """
                        SELECT  proyectos.id_proyecto,
                                proyectos.titulo,
                                modalidades.nombre        AS modalidad,
                                instituciones.nombre      AS institucion,
                                areas_conocimiento.nombre AS area_conocimiento
                        FROM proyectos
                                INNER JOIN modalidades ON (proyectos.id_modalidad = modalidades.id_modalidad)
                                INNER JOIN instituciones ON (proyectos.id_institucion = instituciones.id_institucion)
                                INNER JOIN areas_conocimiento ON (proyectos.id_area_conocimiento = areas_conocimiento.id_area_conocimiento)
                                INNER JOIN proyectos_convocatoria ON (proyectos.id_proyecto = proyectos_convocatoria.id_proyecto)              
                        WHERE proyectos.estado = 'pendiente'
                        AND proyectos_convocatoria.id_convocatoria IN (
                                SELECT id_convocatoria
                                FROM convocatorias
                                WHERE estado = 'en curso'
                        ) 
                        LIMIT :page_size OFFSET :offset
                """
                )

                params = {
                "page_size": page_size,
                "offset": offset
                }
        
                result = db.execute(sql, params).mappings().all()

                count_sql = text("SELECT COUNT(proyectos.id_proyecto) AS cantidad_proyectos FROM proyectos JOIN proyectos_convocatoria ON (proyectos.id_proyecto = proyectos_convocatoria.id_proyecto) WHERE proyectos_convocatoria.id_convocatoria IN (SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso') AND proyectos.estado = 'pendiente'")

                total_proyectos = db.execute(count_sql).scalar()

                total_pages = (total_proyectos + page_size - 1) // page_size

                return result,total_pages
        except SQLAlchemyError as e:
                print(f"Error al obtener proyectos no asignados: {e}")
                raise HTTPException(status_code=500, detail="Error al obtener todos los proyectos no asignados")

def get_all_authors(db: Session,  id_proyecto:int):
    sql = text("SELECT nombre FROM autores WHERE id_proyecto = :id_proyecto")
    result = db.execute(sql, {"id_proyecto": id_proyecto}).fetchall()
    return result