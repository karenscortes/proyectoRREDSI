-- ACTUALIZAR ESTADO_ASIGNACIÓN Y CALIFICACIÓN 

DELIMITER //
CREATE TRIGGER actualizar_estados_proyectos AFTER UPDATE ON rubricas_resultados
FOR EACH ROW
    BEGIN
        -- Se obtiene la fecha fin de publicación en etapa 1
        SET publication_dueDate  = SELECT programacion_fases.fecha_fin FROM programacion_fases JOIN fases ON (programacion_fases.id_fase = fases.id_fase) WHERE fases.nombre = 'publicacion de resultados' AND fases.id_etapa = 2;

        -- Si continuamos en etapa 1, se actualzará el estado dependiendo de si el proyecto fué abrobado o no
        IF ( CURDATE() <= publication_dueDate ) THEN

            IF(NEW.estado_proyecto = 'aprobado') THEN

                UPDATE proyectos SET estado_asignacion = 'pendiente', estado_calificacion = 'C_virtual'
                WHERE id_proyecto = (
                    SELECT DISTINCT proyectos_convocatoria.id_proyecto FROM proyectos_convocatoria 
                        JOIN respuestas_rubricas ON (proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria)
                    WHERE respuestas_rubricas.id_rubrica_resultado = OLD.id_rubrica_resultado
                );

            ELSE

                UPDATE proyectos SET estado_asignacion = 'archivado', estado_calificacion = 'C_virtual'
                WHERE id_proyecto = (
                    SELECT DISTINCT proyectos_convocatoria.id_proyecto FROM proyectos_convocatoria 
                        JOIN respuestas_rubricas ON (proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria)
                    WHERE respuestas_rubricas.id_rubrica_resultado = OLD.id_rubrica_resultado
                );

            END IF;

        -- Si ya estamos en la etapa dos, el proyecto se archivara solo si ya tiene los dos resultados
        ELSE

            SET total_results = SELECT COUNT( DISTINCT rubricas_resultados.id_rubrica_resultado) FROM rubricas_resultados
                                    JOIN respuestas_rubricas ON (rubricas_resultados.id_rubrica_resultado = respuestas_rubricas.id_rubrica_resultado)
                                WHERE respuestas_rubricas.id_proyecto_convocatoria = (
                                    SELECT id_proyecto_convocatoria 
                                    FROM respuestas_rubricas
                                    WHERE id_rubrica_resultado = OLD.id_rubrica_resultado
                                    LIMIT 1
                                );

            IF(total_results = 2) THEN

                UPDATE proyectos SET estado_asignacion = 'archivado', estado_calificacion = 'C_presencial'
                WHERE id_proyecto = (
                    SELECT proyectos_convocatoria.id_proyecto FROM proyectos_convocatoria 
                        JOIN respuestas_rubricas ON (proyectos_convocatoria.id_proyecto_convocatoria = respuestas_rubricas.id_proyecto_convocatoria)
                    WHERE respuestas_rubricas.id_rubrica_resultado = 1
                    lIMIT 1
                );

            END IF;

        END IF;

    END;
//
DELIMITER ;

-- ACTUALIZAR ROL DE USUARIO DE EXTERNO A SUSTITUTO EVALUADOR O ESTADO_CALIFICACIÓN A P_presencial
DELIMITER //
CREATE TRIGGER actualizar_estado_o_rol AFTER INSERT ON participantes_proyectos
FOR EACH ROW
    BEGIN

        SET id_rol = SELECT id_rol FROM usuarios WHERE id_usuario = NEW.id_usuario;

        IF(NEW.id_etapa = 1 AND id_rol = 1) THEN
            SET total_evaluators =  SELECT COUNT(id_usuario) FROM participantes_proyecto 
                                        JOIN usuarios ON (participantes_proyecto.id_usuario = usuarios.id_usuario )
                                    WHERE id_etapa = 1 AND usuarios.id_rol = 1 AND participantes_proyecto.id_proyecto = NEW.id_proyecto;
            
            IF(total_evaluators = 2) THEN

                UPDATE proyectos SET estado_calificacion = 'P_presencial' WHERE id_proyecto = NEW.id_proyecto;
            
            END IF;
        
        ELSE IF(NEW.id_etapa = 1 AND id_rol = 7) THEN
           
            UPDATE usuarios SET id_rol = 8 WHERE id_usuario = NEW.id_usuario;
        
        END IF;
    END;
//
DELIMITER ;

-- INSERTAR A HISTORIAL_ACTIVIDADES_ADMIN


