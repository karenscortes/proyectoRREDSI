from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

def get_unassigned_projects(db: Session, page: int = 1, page_size: int = 10):
        try:
                offset = (page - 1) * page_size

                sql = text(
                """
                        SELECT  DISTINCT proyectos.id_proyecto,
                                         proyectos.titulo,
                                         modalidades.nombre        AS modalidad,
                                         instituciones.nombre      AS institucion,
                                         areas_conocimiento.nombre AS area_conocimiento
                        FROM proyectos
                                INNER JOIN modalidades ON (proyectos.id_modalidad = modalidades.id_modalidad)
                                INNER JOIN instituciones ON (proyectos.id_institucion = instituciones.id_institucion)
                                INNER JOIN areas_conocimiento ON (proyectos.id_area_conocimiento = areas_conocimiento.id_area_conocimiento)
                                INNER JOIN proyectos_convocatoria ON (proyectos.id_proyecto = proyectos_convocatoria.id_proyecto)              
                        WHERE proyectos.estado_asignacion= 'pendiente'
                        AND proyectos_convocatoria.id_convocatoria = (
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

                count_sql = text("SELECT COUNT(proyectos.id_proyecto) AS cantidad_proyectos FROM proyectos JOIN proyectos_convocatoria ON (proyectos.id_proyecto = proyectos_convocatoria.id_proyecto) WHERE proyectos_convocatoria.id_convocatoria IN (SELECT id_convocatoria FROM convocatorias WHERE estado = 'en curso') AND proyectos.estado_asignacion = 'pendiente'")

                total_proyectos = db.execute(count_sql).scalar()

                total_pages = (total_proyectos + page_size - 1) // page_size

                return result,total_pages
        except SQLAlchemyError as e:
                print(f"Error al obtener proyectos no asignados: {e}")
                raise HTTPException(status_code=500, detail="Error al obtener todos los proyectos no asignados")

def get_all_authors(db: Session,  id_proyecto:int):
    try:    
        sql = text("SELECT nombre FROM autores WHERE id_proyecto = :id_proyecto")
        result = db.execute(sql, {"id_proyecto": id_proyecto}).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener autores del proyecto: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener autores del proyecto")
    
def get_assignment_dates(db: Session):
    try:    
        first_sql = text(
             """SELECT programacion_fases.fecha_inicio, programacion_fases.fecha_fin 
                FROM programacion_fases JOIN fases ON (programacion_fases.id_fase = fases.id_fase) 
                WHERE fases.id_etapa = 2 
                AND fases.nombre = 'Asignaciones' 
                AND programacion_fases.id_convocatoria = (
                                SELECT id_convocatoria
                                FROM convocatorias
                                WHERE estado = 'en curso'
                )"""
        )
        first_dates = db.execute(first_sql).fetchone()

        second_sql = text(
             """SELECT programacion_fases.fecha_inicio, programacion_fases.fecha_fin 
                FROM programacion_fases JOIN fases ON (programacion_fases.id_fase = fases.id_fase) 
                WHERE fases.id_etapa = 1 
                AND fases.nombre = 'Asignaciones' 
                AND programacion_fases.id_convocatoria = (
                                SELECT id_convocatoria
                                FROM convocatorias
                                WHERE estado = 'en curso'
                )"""
        )

        second_dates = db.execute(second_sql).fetchone()

        if not first_dates or not second_dates:
            raise HTTPException(status_code=404, detail="No se encontraron fechas para las fases de asignaciones")

        return first_dates,second_dates
    except SQLAlchemyError as e:
        print(f"Error al obtener las fechas de asignación: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener las fechas")