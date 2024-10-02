from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Optional, List
from appv1.schemas.rubricasCalificadas import ProyectoRubricasResponse, RubricaCalificada, ItemRubrica, Etapa, Evaluador

def get_rubricas_calificadas(db: Session, id_tutor: Optional[int] = None, id_proyecto: Optional[int] = None) -> List[ProyectoRubricasResponse]:
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

        # Manejo de posibles valores nulos
        tutores = participantes_result.tutores or ""
        ponentes = participantes_result.ponentes or ""

        # Consulta para obtener las rúbricas calificadas
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
                e.nombre AS nombre_etapa,
                e.id_etapa,
                u.id_usuario AS id_evaluador,
                u.nombres AS nombre_evaluador,
                u.documento AS cedula_evaluador,
                inst.nombre AS universidad_evaluador,
                u.correo AS email_evaluador,
                u.celular AS celular_evaluador
            FROM respuestas_rubricas rr
            JOIN items_rubrica ir ON rr.id_item_rubrica = ir.id_item_rubrica
            JOIN rubricas r ON ir.id_rubrica = r.id_rubrica
            JOIN rubricas_resultados rr_result ON rr.id_rubrica_resultado = rr_result.id_rubrica_resultado
            JOIN proyectos_convocatoria pc ON rr.id_proyecto_convocatoria = pc.id_proyecto_convocatoria
            JOIN etapas e ON r.id_etapa = e.id_etapa
            JOIN usuarios u ON rr.id_usuario = u.id_usuario
            JOIN detalles_institucionales di ON u.id_usuario = di.id_usuario
            JOIN instituciones inst ON di.id_institucion = inst.id_institucion
            WHERE pc.id_proyecto = :id_proyecto
        """), {"id_proyecto": id_proyecto}).fetchall()

        if not rubricas_result:
            raise HTTPException(status_code=404, detail="No se encontraron rúbricas calificadas para el proyecto")

        rubricas_calificadas_list = []
        rubricas_dict = {}

        # Iterar sobre cada ítem de la rúbrica
        for row in rubricas_result:
            rubrica_key = (row.id_rubrica, row.id_evaluador)  # Clave única por rúbrica y evaluador
            
            if rubrica_key not in rubricas_dict:
                rubricas_dict[rubrica_key] = {
                    "id_rubrica": row.id_rubrica,
                    "titulo_rubrica": row.titulo_rubrica,
                    "estado_proyecto": row.estado_proyecto,
                    "puntaje_aprobacion": row.puntaje_aprobacion,
                    "etapa": {
                        "nombre_etapa": row.nombre_etapa,
                        "tipo_etapa": "Virtual" if row.id_etapa == 2 else "Presencial"
                    },
                    "evaluador": {
                        "nombre_evaluador": row.nombre_evaluador,
                        "cedula_evaluador": row.cedula_evaluador,
                        "universidad_evaluador": row.universidad_evaluador,
                        "email_evaluador": row.email_evaluador,
                        "celular_evaluador": row.celular_evaluador
                    },
                    "items_rubrica": []
                }

            rubricas_dict[rubrica_key]["items_rubrica"].append({
                "id_item_rubrica": row.id_item_rubrica,
                "titulo_item": row.titulo_item,
                "item_componente": row.item_componente,
                "valor_max": row.valor_max,
                "calificacion": row.calificacion,
                "observacion": row.observacion
            })

        for rubrica in rubricas_dict.values():
            rubricas_calificadas_list.append(rubrica)

        respuesta_final = ProyectoRubricasResponse(
            titulo_proyecto=proyecto_result.titulo_proyecto,
            universidad_proyecto=proyecto_result.universidad_proyecto,
            tutores=tutores,
            ponentes=ponentes,
            rubricas_calificadas=[
                RubricaCalificada(
                    id_rubrica=rubrica["id_rubrica"],
                    titulo_rubrica=rubrica["titulo_rubrica"],
                    estado_proyecto=rubrica["estado_proyecto"],
                    puntaje_aprobacion=rubrica["puntaje_aprobacion"],
                    items_rubrica=[ItemRubrica(**item) for item in rubrica["items_rubrica"]],
                    etapa=Etapa(**rubrica["etapa"]),
                    evaluador=Evaluador(**rubrica["evaluador"])
                ) for rubrica in rubricas_calificadas_list
            ]
        )

        # Convertimos el objeto Pydantic a un diccionario usando .dict() para evitar el error de serialización
        return [respuesta_final.dict()]  # Devolver como un dict en lugar de un objeto Pydantic

    except Exception as e:
        print(f"Error detectado: {e}")
        raise HTTPException(status_code=500, detail=f"Error al obtener rúbricas calificadas: {str(e)}")
