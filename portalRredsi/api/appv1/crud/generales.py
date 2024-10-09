from sqlalchemy.orm import Session
from sqlalchemy import text

from appv1.crud.evaluador.proyectos import get_current_convocatoria, get_etapa_actual

def get_areas_conocimiento(db: Session):
    sql = text("SELECT DISTINCT areas_conocimiento.* FROM areas_conocimiento")
    result = db.execute(sql).fetchall()
    return result

def get_proyecto_by_id(db: Session,id_proyecto : int):
    sql = text("""SELECT id_proyecto,id_institucion,id_modalidad,id_area_conocimiento,titulo,programa_academico,grupo_investigacion,linea_investigacion,nombre_semillero,url_propuesta_escrita,estado_calificacion,url_aval
                    FROM proyectos 
                    WHERE id_proyecto = :id_p
            """)
    result = db.execute(sql,{"id_p": id_proyecto}).fetchone()
    return result

# CANTIDAD DE POSTULACIONES PENDIENTES EN UNA CONVOCATORIA EN CURSO
def get_cantidad_postulaciones(db: Session):
    sql = text("""SELECT COUNT(*) FROM postulaciones_evaluadores 
                JOIN convocatorias ON postulaciones_evaluadores.id_convocatoria = convocatorias.id_convocatoria
                WHERE convocatorias.estado = 'en curso'
                AND postulaciones_evaluadores.estado_postulacion = 'pendiente'
            """)
    result = db.execute(sql).scalar()
    return result

# CANTIDAD DE PROYECTOS ASIGNADOS EN LA ETAPA ACTUAL
def get_cantidad_proyectos_asignados(db: Session):
    etapa_actual = get_etapa_actual(db)
    
    sql = text("""SELECT DISTINCT(COUNT(*)) FROM proyectos
                JOIN proyectos_convocatoria ON proyectos_convocatoria.id_proyecto = proyectos.id_proyecto
                JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
                JOIN participantes_proyecto ON proyectos.id_proyecto = participantes_proyecto.id_proyecto
                WHERE proyectos.estado_asignacion = 'asignado'
                AND participantes_proyecto.id_etapa = :etp_actual
                AND convocatorias.estado = 'en curso'
            """)
    result = db.execute(sql,{"etp_actual": etapa_actual["id_etapa"] }).scalar()
    return result

# CANTIDAD DE PROYECTOS INSCRITOS EN UNA CONVOCATORIA EN CURSO
def get_cantidad_proyectos_inscritos(db: Session):
    convocatoria_actual = get_current_convocatoria(db)
    sql = text("""SELECT DISTINCT(COUNT(*)) FROM proyectos 
                JOIN proyectos_convocatoria ON proyectos.id_proyecto = proyectos_convocatoria.id_proyecto
                WHERE proyectos_convocatoria.id_convocatoria = :id_convocatoria
            """)
    result = db.execute(sql,{"id_convocatoria": convocatoria_actual }).scalar()
    return result

# CANTIDAD DE PROYECTOS CALIFICADOS EN UNA ETAPA EN CURSO Y EN UNA CONVOCATORIA EN CURSO
def get_cantidad_proyectos_calificados(db: Session):
    etapa_actual = get_etapa_actual(db)
    
    if(etapa_actual["id_etapa"] == '1'):
        sql = text("""SELECT DISTINCT(COUNT(*)) FROM proyectos
                    JOIN proyectos_convocatoria ON proyectos_convocatoria.id_proyecto = proyectos.id_proyecto
                    JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
                    WHERE proyectos.estado_calificacion = 'C_presencial' AND convocatorias.estado = 'en curso'
                """)
        result = db.execute(sql).scalar()
    else:
        sql = text("""SELECT DISTINCT(COUNT(*)) FROM proyectos
                    JOIN proyectos_convocatoria ON proyectos_convocatoria.id_proyecto = proyectos.id_proyecto
                    JOIN convocatorias ON proyectos_convocatoria.id_convocatoria = convocatorias.id_convocatoria
                    WHERE proyectos.estado_calificacion = 'C_virtual' AND convocatorias.estado = 'en curso'
                """)
        result = db.execute(sql).scalar()
    return result