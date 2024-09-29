# Crear un usuario
from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def leer_convocatorias(db:Session):
    try:
        sql = text("SELECT nombre, fecha_inicio, fecha_fin, estado FROM convocatorias")
        result = db.execute(sql).fetchall()
        return result
    except SQLAlchemyError as e:
        print(f"Error al buscar usuario por email: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario por email")

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
                estado,
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