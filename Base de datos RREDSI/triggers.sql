-- ACTUALIZAR ESTADO_ASIGNACIÓN 

DELIMITER //
CREATE TRIGGER actualizar_estado AFTER INSERT ON rubricas_resultados
FOR EACH ROW
    BEGIN
        -- Se obtiene la fecha fin de publicación en etapa 1
        SET publication_dueDate  = SELECT programacion_fases.fecha_fin FROM programacion_fases JOIN fases ON (programacion_fases.id_fase = fases.id_fase) WHERE fases.nombre = 'publicacion de resultados' AND fases.id_etapa = 1;

        IF ( CURDATE() <= publication_dueDate ) THEN
            UPDATE proyectos SET estado_asignacion = 'pendiente'
            WHERE id_proyecto IN (
                SELECT DISTINCT proyectos_convocatoria.id_proyecto FROM proyectos_convocatoria 
                    JOIN respuestas_rubricas ON (proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria)
                    JOIN rubricas_resultados ON (respuestas_rubricas.id_rubrica_resultado = rubricas_resultados.id_rubrica_resultado)
                WHERE rubricas_resultados.estado_proyecto = 'aprobado' 
                AND proyectos_convocatoria.id_convocatoria IN (
                    SELECT id_convocatoria 
                    FROM convocatorias 
                    WHERE estado = 'en curso'
                )
            );

            UPDATE proyectos SET estado_asignacion = 'archivado'
            WHERE id_proyecto IN (
                SELECT DISTINCT proyectos_convocatoria.id_proyecto FROM proyectos_convocatoria 
                    JOIN respuestas_rubricas ON (proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria)
                    JOIN rubricas_resultados ON (respuestas_rubricas.id_rubrica_resultado = rubricas_resultados.id_rubrica_resultado)
                WHERE rubricas_resultados.estado_proyecto = 'reprobado' 
                AND proyectos_convocatoria.id_convocatoria IN (
                    SELECT id_convocatoria 
                    FROM convocatorias 
                    WHERE estado = 'en curso'
                )
            );
        ELSE
            SET total_results = SELECT COUNT( DISTINCT respuestas_rubricas.id_rubrica_resultado) FROM respuestas_rubricas
                                    JOIN rubricas_resultados  ON (rubricas_resultados.id_rubrica_resultado = respuestas_rubricas.id_rubrica_resultado)
                                WHERE id_proyecto_convocatoria = (
                                    SELECT id_proyecto_convocatoria 
                                    FROM respuestas_rubricas
                                    WHERE id_rubrica_resultado = 1
                                    LIMIT 1
                                );

            IF(total_results == 2) THEN

                UPDATE proyectos SET estado_asignacion = 'archivado'
                WHERE id_proyecto IN (
                    SELECT DISTINCT proyectos_convocatoria.id_proyecto FROM proyectos_convocatoria 
                    WHERE proyectos_convocatoria.id_convocatoria IN (
                        SELECT id_convocatoria 
                        FROM convocatorias 
                        WHERE estado = 'en curso'
                    )
                );
            END IF;
        END IF;
    END;
//
DELIMITER ;