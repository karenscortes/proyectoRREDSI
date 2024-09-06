# # Crear un usuario
# """ from sqlalchemy import func
# from sqlalchemy.orm import Session
# from datetime import datetime
# from appv1.models.rubrica import Rubrica


        
# def get_delegados_activos(db: Session):
#     try:
#         sql = text("""
#         SELECT roles.id_rol, roles.nombre, usuarios.id_usuario, usuarios.correo,
#         usuarios.clave, usuarios.estado, detalles_personales.id_detalle_personal, detalles_personales.documento, 
#         detalles_personales.nombres, detalles_personales.apellidos, detalles_personales.celular, 
#         detalles_personales.id_institucion, detalles_personales.semillero, detalles_personales.grupo_investigacion,
#         detalles_personales.id_area_conocimiento, titulos_academicos.id_titulo_academico, titulos_academicos.nivel,
#         titulos_academicos.nombre_titulo, titulos_academicos.url_titulo FROM roles JOIN usuarios ON roles.id_rol = usuarios.id_rol
#         JOIN detalles_personales ON usuarios.id_usuario = detalles_personales.id_usuario
#         JOIN titulos_academicos ON usuarios.id_usuario = titulos_academicos.id_usuario
#         WHERE usuarios.estado = 'activo' AND roles.nombre = 'Delegado';
#         """)
#         result = db.execute(sql).fetchall()
        
# return db.query(Rubrica).filter(User.user_role == user_role, User.created_at >= start_date, User.created_at <= end_date).all()
        
#     except SQLAlchemyError as e:
#         print(f"Error al buscar los delegados: {e}")
#         raise HTTPException(status_code=500, detail="Error al buscar los delegados")

#  """

