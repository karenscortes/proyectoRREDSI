from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List, Optional
from fastapi import HTTPException
from appv1.schemas.rubricasCalificadas import ProyectoRubricasResponse, RubricaCalificada, ItemRubrica, Evaluador

def get_rubricas_calificadas(db: Session, id_tutor: Optional[int] = None, id_proyecto: Optional[int] = None) -> ProyectoRubricasResponse:
    try:
        # Verificar si se recibe al menos uno de los dos parámetros
        if not id_tutor and not id_proyecto:
            raise HTTPException(status_code=400, detail="Debe proporcionar un id de tutor o un id de proyecto.")
        
        # Consulta para obtener el título del proyecto y la universidad
        proyecto_result = db.execute(text("""
            SELECT p.titulo AS titulo_proyecto, inst.nombre AS universidad_proyecto
            FROM proyectos p
            JOIN instituciones inst ON p.id_institucion = inst.id_institucion
            WHERE p.id_proyecto = :id_proyecto
        """), {"id_proyecto": id_proyecto}).fetchone()

        if not proyecto_result:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")

        # Consulta para obtener los tutores y ponentes
        participantes_result = db.execute(text("""
            SELECT
                GROUP_CONCAT(DISTINCT CASE
                    WHEN u.id_rol = 4 THEN CONCAT(u.nombres, ' ', u.apellidos)
                END SEPARATOR ', ') AS tutores,
                GROUP_CONCAT(DISTINCT CASE
                    WHEN u.id_rol = 5 THEN CONCAT(u.nombres, ' ', u.apellidos)
                END SEPARATOR ', ') AS ponentes
            FROM participantes_proyecto pp
            JOIN usuarios u ON pp.id_usuario = u.id_usuario
            WHERE pp.id_proyecto = :id_proyecto
        """), {"id_proyecto": id_proyecto}).fetchone()

        # Consulta para obtener todas las rúbricas calificadas
        rubricas_result = db.execute(text("""
            SELECT
                r.id_rubrica,
                r.titulo AS titulo_rubrica,
                rr_result.estado_proyecto,
                rr_result.puntaje_aprobacion,
                ir.id_item_rubrica,
                ir.titulo AS titulo_item,
                ir.componente AS item_componente,
                ir.valor_max,
                rr.calificacion,
                rr.observacion,
                u.nombres AS nombre_evaluador,
                u.apellidos AS apellidos_evaluador,
                u.documento AS cedula_evaluador,
                inst.nombre AS universidad_evaluador,
                u.correo AS email_evaluador,
                u.celular AS celular_evaluador
            FROM respuestas_rubricas rr
            JOIN items_rubrica ir ON rr.id_item_rubrica = ir.id_item_rubrica
            JOIN rubricas r ON ir.id_rubrica = r.id_rubrica
            JOIN rubricas_resultados rr_result ON rr.id_rubrica_resultado = rr_result.id_rubrica_resultado
            JOIN proyectos_convocatoria pc ON rr.id_proyecto_convocatoria = pc.id_proyecto_convocatoria
            JOIN usuarios u ON rr.id_usuario = u.id_usuario
            JOIN detalles_institucionales di ON u.id_usuario = di.id_usuario
            JOIN instituciones inst ON di.id_institucion = inst.id_institucion
            WHERE pc.id_proyecto = :id_proyecto
            AND (:id_tutor IS NULL OR u.id_usuario = :id_tutor)
        """), {"id_proyecto": id_proyecto, "id_tutor": id_tutor}).fetchall()

        if not rubricas_result:
            raise HTTPException(status_code=404, detail="No se encontraron rúbricas calificadas para el proyecto")

        # Diccionario para agrupar las rúbricas por ID de rúbrica y evaluador
        rubricas_dict = {}

        # Iterar sobre cada fila y agrupar por rúbrica y evaluador
        for row in rubricas_result:
            rubrica_key = (row.id_rubrica, row.cedula_evaluador)  # Clave única por rúbrica y evaluador
            if rubrica_key not in rubricas_dict:
                # Si la rúbrica aún no está en el diccionario, agregarla
                rubricas_dict[rubrica_key] = {
                    "id_rubrica": row.id_rubrica,
                    "titulo_rubrica": row.titulo_rubrica,
                    "estado_proyecto": row.estado_proyecto,
                    "puntaje_aprobacion": row.puntaje_aprobacion,
                    "evaluador": {
                        "nombre_evaluador": f"{row.nombre_evaluador} {row.apellidos_evaluador}" if row.nombre_evaluador else "Evaluador no especificado",
                        "cedula_evaluador": row.cedula_evaluador or "No especificado",
                        "universidad_evaluador": row.universidad_evaluador or "No especificado",
                        "email_evaluador": row.email_evaluador or "No especificado",
                        "celular_evaluador": row.celular_evaluador or "No especificado"
                    },
                    "items_rubrica": []
                }

            # Añadir cada ítem de la rúbrica
            rubricas_dict[rubrica_key]["items_rubrica"].append({
                "id_item_rubrica": row.id_item_rubrica,
                "titulo_item": row.titulo_item or "No especificado",
                "item_componente": row.item_componente or "No especificado",
                "valor_max": row.valor_max or 0.0,
                "calificacion": row.calificacion or 0.0,
                "observacion": row.observacion or "No hay observaciones"
            })

        # Convertir el diccionario de rúbricas a una lista
        rubricas_calificadas_list = [
            RubricaCalificada(
                id_rubrica=r["id_rubrica"],
                titulo_rubrica=r["titulo_rubrica"],
                estado_proyecto=r["estado_proyecto"],
                puntaje_aprobacion=r["puntaje_aprobacion"],
                items_rubrica=[ItemRubrica(**item) for item in r["items_rubrica"]],
                evaluador=Evaluador(**r["evaluador"])
            ) for r in rubricas_dict.values()
        ]

        # Armar la respuesta final con todas las rúbricas calificadas
        return ProyectoRubricasResponse(
            titulo_proyecto=proyecto_result.titulo_proyecto,
            universidad_proyecto=proyecto_result.universidad_proyecto,
            tutores=participantes_result.tutores or "No especificado",
            ponentes=participantes_result.ponentes or "No especificado",
            rubricas_calificadas=rubricas_calificadas_list
        )

    except Exception as e:
        print(f"Error detectado: {e}")
        raise HTTPException(status_code=500, detail=f"Error al obtener rúbricas calificadas: {str(e)}")
