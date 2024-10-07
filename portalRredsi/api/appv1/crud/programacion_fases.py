from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

def get_phase_dates(db: Session):
    try:
        sql = text("""
            SELECT 
                    MIN(pf.fecha_inicio) AS fecha_inicio, 
                    MAX(pf.fecha_fin) AS fecha_fin, 
                    f.nombre AS nombre_fase, 
                    e.nombre AS nombre_etapa
                FROM 
                    programacion_fases pf
                INNER JOIN 
                    fases f ON pf.id_fase = f.id_fase
                INNER JOIN 
                    etapas e ON f.id_etapa = e.id_etapa
                INNER JOIN 
                    convocatorias c ON pf.id_convocatoria = c.id_convocatoria
                WHERE 
                    (f.nombre = 'Inscripciones abiertas' AND e.nombre = 'Virtual') OR
                    (f.nombre = 'Publicación de resultados' AND e.nombre = 'Virtual') OR
                    (f.nombre = 'Evento' AND e.nombre = 'Presencial') OR
                    (f.nombre = 'Publicación de resultados' AND e.nombre = 'Presencial')
                GROUP BY 
                    f.nombre, e.nombre
                HAVING 
                    f.nombre = 'Evento' OR COUNT(*) = 1;

        """)
        result = db.execute(sql).mappings().all()

        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron fases con las fechas solicitadas")

        return result
    except SQLAlchemyError as e:
        print(f"Error al obtener las fechas de las fases: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener las fechas de las fases")
