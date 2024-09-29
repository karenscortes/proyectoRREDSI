from sqlalchemy.orm import Session
from sqlalchemy import text

def get_areas_conocimiento(db: Session):
    sql = text("SELECT * FROM areas_conocimiento")
    result = db.execute(sql).fetchall()
    return result

def get_proyecto_by_id(db: Session,id_proyecto : int):
    sql = text("""SELECT id_proyecto,id_institucion,id_modalidad,id_area_conocimiento,titulo,programa_academico,grupo_investigacion,linea_investigacion,nombre_semillero,url_propuesta_escrita,estado_calificacion,url_aval
                    FROM proyectos 
                    WHERE id_proyecto = :id_p
            """)
    result = db.execute(sql,{"id_p": id_proyecto}).fetchone()
    return result

def get_cantidad_postulaciones(db: Session):
    sql = text("""SELECT COUNT(*) FROM postulaciones_evaluadores 
                JOIN convocatorias ON postulaciones_evaluadores.id_convocatoria = convocatorias.id_convocatoria
                WHERE convocatorias.estado = 'en curso'
                AND postulaciones_evaluadores.estado_postulacion = 'pendiente'
            """)
    result = db.execute(sql).scalar()
    return result

def get_cantidad_proyectos_asignados(db: Session):
    sql = text("""SELECT COUNT(*) FROM proyectos
                JOIN proyectos_convocatoria ON proyectos_convocatoria.id_proyecto = proyectos.id_proyecto
                JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
                WHERE proyectos.estado_asignacion = 'asignado'
            """)
    result = db.execute(sql).scalar()
    return result