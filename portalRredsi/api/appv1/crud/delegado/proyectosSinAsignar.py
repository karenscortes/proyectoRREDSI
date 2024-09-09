from sqlalchemy.orm import Session
from sqlalchemy import text

def get_unassigned_projects(db: Session):

        sql = text(
        """
                SELECT  proyectos.titulo,
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
        """
        )
    
        result = db.execute(sql).fetchall()
        return result

def get_all_authors(db: Session,  id_proyecto:int):
    sql = text("SELECT nombre FROM autores WHERE id_proyecto = :id_proyecto")
    result = db.execute(sql, {"id_proyecto": id_proyecto}).fetchall()
    return result