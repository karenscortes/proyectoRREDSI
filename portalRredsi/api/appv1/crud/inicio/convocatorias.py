# Crear un usuario
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Consultar administradores con paginación
def get_all_convocatorias(db: Session, page: int = 1, page_size: int = 5):
    try:
        # Calcular el offset basado en el número de página y el tamaño de página
        offset = (page - 1) * page_size

        # Consulta SQL con paginación, incluyendo todos los campos requeridos
        sql = text("""
            SELECT
                id_convocatoria,   
                nombre,
                fecha_inicio,
                fecha_fin,
                estado
                FROM convocatorias          
            LIMIT :page_size OFFSET :offset;
        """)
        params = {
            "page_size": page_size,
            "offset": offset
        }
        result = db.execute(sql, params).mappings().all()

        # Obtener el número total de convocatorias activos
        count_sql = text("""
            SELECT COUNT(id_convocatoria)
            FROM convocatorias;
        """)
        total_convocatorias = db.execute(count_sql).scalar()

        # Calcular el número total de páginas
        total_pages = (total_convocatorias + page_size - 1) // page_size

        # Verificar si se encontraron administradores
        if not result:
            raise HTTPException(status_code=404, detail="No se encontraron convocatorias")

        return result, total_pages

    except SQLAlchemyError as e:
        print(f"Error al buscar convocatorias: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar convocatorias")
    

def get_programacion_fases_activa(db: Session, page: int = 1, page_size: int = 5):
    try:
        # Calcular el offset basado en el número de página y el tamaño de página
        offset = (page - 1) * page_size

        # Consulta SQL simplificada para obtener la programación de fases de la convocatoria activa
        sql = text(""" 
            SELECT
                programacion_fases.id_programacion_fase,
                convocatorias.id_convocatoria,  -- Asegúrate de incluir este campo
                fases.id_fase,  -- Asegúrate de incluir este campo
                convocatorias.nombre AS convocatoria_nombre,
                fases.nombre AS fase_nombre,
                etapas.nombre AS etapa_nombre,
                programacion_fases.fecha_inicio,
                programacion_fases.fecha_fin
            FROM programacion_fases
            JOIN convocatorias ON programacion_fases.id_convocatoria = convocatorias.id_convocatoria
            JOIN fases ON programacion_fases.id_fase = fases.id_fase
            JOIN etapas ON fases.id_etapa = etapas.id_etapa
            WHERE convocatorias.estado = 'en curso'
            LIMIT :page_size OFFSET :offset;
        """)

        params = {
            "page_size": page_size,
            "offset": offset
        }

        # Ejecutar la consulta
        result = db.execute(sql, params).mappings().all()

        # Obtener el número total de programaciones
        count_sql = text("""
            SELECT COUNT(id_programacion_fase)  -- Asegúrate de contar las programaciones
            FROM programacion_fases
            JOIN convocatorias ON programacion_fases.id_convocatoria = convocatorias.id_convocatoria
            WHERE convocatorias.estado = 'en curso';
        """)
        total_programacion = db.execute(count_sql).scalar()

        # Calcular el número total de páginas
        total_pages = (total_programacion + page_size - 1) // page_size

        # Verificar si no hay resultados
        if not result:
            raise HTTPException(status_code=404, detail="No se encontró programación para la convocatoria activa")

        return {
            "programacion_fases": result,
            "total_pages": total_pages,
            "current_page": page,
            "page_size": page_size
        }

    except SQLAlchemyError as e:
        print(f"Error al buscar la programación de fases: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar la programación de fases")




    