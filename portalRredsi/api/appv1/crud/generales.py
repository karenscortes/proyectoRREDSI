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
