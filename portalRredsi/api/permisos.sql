--Roles del sistema
INSERT INTO rol(nombre) VALUES ('SuperAdmin');
INSERT INTO rol(nombre) VALUES ('Administrador');
INSERT INTO rol(nombre) VALUES ('Delegado');
INSERT INTO rol(nombre) VALUES ('Evaluador');

--Modulos de los usuarios del sistema
INSERT INTO modulo(nombre) VALUES ('areas_conocimiento'); -- id: 1
INSERT INTO modulo(nombre) VALUES ('instituciones'); -- id: 2
INSERT INTO modulo(nombre) VALUES ('roles'); -- id: 3
INSERT INTO modulo(nombre) VALUES ('usuarios'); -- id: 4
INSERT INTO modulo(nombre) VALUES ('etapas'); -- id: 5
INSERT INTO modulo(nombre) VALUES ('fases'); -- id: 6
INSERT INTO modulo(nombre) VALUES ('convocatorias'); -- id: 7
INSERT INTO modulo(nombre) VALUES ('programacion_fases'); -- id: 8
INSERT INTO modulo(nombre) VALUES ('postulaciones_evaluadores'); -- id: 9
INSERT INTO modulo(nombre) VALUES ('modalidades'); -- id: 10
INSERT INTO modulo(nombre) VALUES ('rubricas'); -- id: 11
INSERT INTO modulo(nombre) VALUES ('items_rubrica'); -- id: 12
INSERT INTO modulo(nombre) VALUES ('proyectos'); -- id: 13
INSERT INTO modulo(nombre) VALUES ('autores'); -- id: 14
INSERT INTO modulo(nombre) VALUES ('titulos_academicos'); -- id: 15
INSERT INTO modulo(nombre) VALUES ('detalles_personales'); -- id: 16
INSERT INTO modulo(nombre) VALUES ('asistentes'); -- id: 17
INSERT INTO modulo(nombre) VALUES ('participantes_proyecto'); -- id: 18
INSERT INTO modulo(nombre) VALUES ('rubricas_resultados'); -- id: 19
INSERT INTO modulo(nombre) VALUES ('respuestas_rubricas'); -- id: 20
INSERT INTO modulo(nombre) VALUES ('salas'); -- id: 21
INSERT INTO modulo(nombre) VALUES ('salas_asignadas'); -- id: 22
INSERT INTO modulo(nombre) VALUES ('presentaciones_proyectos'); -- id: 23
INSERT INTO modulo(nombre) VALUES ('historial_actividades_admin'); -- id: 24


-- Permisos para el módulo "areas_conocimiento"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "instituciones"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "roles"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 3, 0, 0, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "usuarios"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "etapas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (5, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (5, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (5, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (5, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "fases"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (6, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (6, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (6, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (6, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "convocatorias"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (7, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (7, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (7, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (7, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "programacion_fases"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (8, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (8, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (8, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (8, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "postulaciones_evaluadores"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (9, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (9, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (9, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (9, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "modalidades"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (10, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (10, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (10, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (10, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "rubricas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (11, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (11, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (11, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (11, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "items_rubrica"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (12, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (12, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (12, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (12, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "proyectos"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (13, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (13, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (13, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (13, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "autores"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (14, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (14, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (14, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (14, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "titulos_academicos"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (15, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (15, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (15, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (15, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "detalles_personales"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (16, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (16, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (16, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (16, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "asistentes"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (17, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (17, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (17, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (17, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "participantes_proyecto"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (18, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (18, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (18, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (18, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "rubricas_resultados"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (19, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (19, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (19, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (19, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "respuestas_rubricas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (20, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (20, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (20, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (20, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "salas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (21, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (21, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (21, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (21, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "salas_asignadas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (22, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (22, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (22, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (22, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "presentaciones_proyectos"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (23, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (23, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (23, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (23, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "historial_actividades_admin"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (24, 1, 1, 1, 1, 1); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (24, 2, 1, 1, 1, 1); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (24, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (24, 4, 0, 1, 0, 0); -- Evaluador
