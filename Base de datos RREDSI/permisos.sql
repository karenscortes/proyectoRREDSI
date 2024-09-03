--Roles del sistema
INSERT INTO rol(nombre) VALUES ('SuperAdmin');
INSERT INTO rol(nombre) VALUES ('Administrador');
INSERT INTO rol(nombre) VALUES ('Delegado');
INSERT INTO rol(nombre) VALUES ('Evaluador');

--Modulos de los usuarios del sistema
INSERT INTO modulos(nombre) VALUES ('areas_conocimiento'); -- id: 1
INSERT INTO modulos(nombre) VALUES ('instituciones'); -- id: 2
INSERT INTO modulos(nombre) VALUES ('usuarios'); -- id: 3
INSERT INTO modulos(nombre) VALUES ('etapas'); -- id: 4
INSERT INTO modulos(nombre) VALUES ('fases'); -- id: 5
INSERT INTO modulos(nombre) VALUES ('convocatorias'); -- id: 6
INSERT INTO modulos(nombre) VALUES ('programacion_fases'); -- id: 7
INSERT INTO modulos(nombre) VALUES ('postulaciones_evaluadores'); -- id: 8
INSERT INTO modulos(nombre) VALUES ('rubricas'); -- id: 9
INSERT INTO modulos(nombre) VALUES ('items_rubrica'); -- id: 10
INSERT INTO modulos(nombre) VALUES ('proyectos'); -- id: 11
INSERT INTO modulos(nombre) VALUES ('asistentes'); -- id: 12
INSERT INTO modulos(nombre) VALUES ('participantes_proyecto'); -- id: 13
INSERT INTO modulos(nombre) VALUES ('respuestas_rubricas'); -- id: 14
INSERT INTO modulos(nombre) VALUES ('salas'); -- id: 15
INSERT INTO modulos(nombre) VALUES ('salas_asignadas'); -- id: 16
INSERT INTO modulos(nombre) VALUES ('presentaciones_proyectos'); -- id: 17
INSERT INTO modulos(nombre) VALUES ('historial_actividades_admin'); -- id: 18

-- Permisos para el módulo "areas_conocimiento"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 1, 0, 1, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 2, 0, 1, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "instituciones"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 1, 0, 1, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 2, 0, 1, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "usuarios"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 1, 0, 1, 1, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 2, 1, 1, 1, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 3, 0, 1, 1, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "etapas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 2, 1, 1, 1, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "tipos de fases"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (5, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (5, 2, 0, 1, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (5, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (5, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "convocatorias"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (6, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (6, 2, 1, 1, 1, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (6, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (6, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "programacion_fases"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (7, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (7, 2, 1, 1, 1, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (7, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (7, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "postulaciones_evaluadores"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (8, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (8, 2, 0, 0, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (8, 3, 0, 1, 1, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (8, 4, 1, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "rubricas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (9, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (9, 2, 0, 1, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (9, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (9, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "items_rubrica"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (10, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (10, 2, 0, 1, 1, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (10, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (10, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "proyectos"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (11, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (11, 2, 0, 0, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (11, 3, 0, 1, 1, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (11, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "asistentes"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (12, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (12, 2, 1, 1, 1, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (12, 3, 0, 1, 1, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (12, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "participantes_proyecto"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (13, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (13, 2, 0, 0, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (13, 3, 1, 1, 1, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (13, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "respuestas_rubricas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (14, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (14, 2, 0, 0, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (14, 3, 1, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (14, 4, 1, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "salas"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (15, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (15, 2, 1, 1, 1, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (15, 3, 0, 1, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (15, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "detalle_sala"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (16, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (16, 2, 0, 0, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (16, 3, 1, 1, 1, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (16, 4, 0, 1, 0, 0); -- Evaluador

-- Permisos para el módulo "presentaciones_proyectos"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (17, 1, 0, 0, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (17, 2, 0, 0, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (17, 3, 1, 1, 1, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (17, 4, 0, 0, 0, 0); -- Evaluador

-- Permisos para el módulo "historial_actividades_admin"
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (18, 1, 0, 1, 0, 0); -- SuperAdmin
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (18, 2, 0, 0, 0, 0); -- Administrador
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (18, 3, 0, 0, 0, 0); -- Delegado
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (18, 4, 0, 0, 0, 0); -- Evaluador
