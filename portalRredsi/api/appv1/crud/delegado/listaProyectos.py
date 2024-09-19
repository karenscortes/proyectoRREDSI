from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

def get_all_projects(db: Session, page: int = 1, page_size: int = 10):
        try:
                offset = (page - 1) * page_size

                sql = text(
                """
                        SELECT  proyectos.id_proyecto,
                                proyectos.titulo,
                                proyectos.estado,
                                instituciones.nombre  AS institucion       
                        FROM proyectos
                                JOIN instituciones ON (proyectos.id_institucion = instituciones.id_institucion)             
                        LIMIT :page_size OFFSET :offset
                """
                )

                params = {
                "page_size": page_size,
                "offset": offset
                }
        
                result = db.execute(sql, params).mappings().all()
                count_sql = text(""" SELECT  COUNT(*)       
                        FROM proyectos
                        JOIN instituciones ON (proyectos.id_institucion = instituciones.id_institucion)                 
                        """)
                total_proyectos = db.execute(count_sql).scalar()
                total_pages = (total_proyectos + page_size - 1) // page_size

                return result,total_pages
        except SQLAlchemyError as e:
                print(f"Error al obtener proyectos  {e}")
                raise HTTPException(status_code=500, detail="Error al obtener todos los proyectos")
