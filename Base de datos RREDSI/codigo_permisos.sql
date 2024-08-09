--Roles del sistema
INSERT INTO rol(nombre) VALUES ('SuperAdmin');
INSERT INTO rol(nombre) VALUES ('Admin');
INSERT INTO rol(nombre) VALUES ('Delegado');
INSERT INTO rol(nombre) VALUES ('Evaluador');

--Modulos de los usuarios del sistema
INSERT INTO modulo(nombre) VALUES ('Usuario SuperAdmin');
INSERT INTO modulo(nombre) VALUES ('Usuario Admin');
INSERT INTO modulo(nombre) VALUES ('Usuario Delegado');
INSERT INTO modulo(nombre) VALUES ('Usuario Evaluador');

--Permisos de Super Admin hacia otros Usuarios
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 1, 0, 0, 0, 0);
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 1, 0, 1, 1, 0);
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 1, 0, 1, 1, 0);
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 1, 0, 0, 0, 0);

--Permisos de Admin hacia otros Usuarios
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (1, 2, 0, 0, 0, 0);
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (2, 2, 0, 0, 0, 0);
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (3, 2, 1, 1, 1, 0);
INSERT INTO permisos(id_modulo, id_rol, p_insertar, p_consultar, p_actualizar, p_eliminar) VALUES (4, 2, 0, 0, 0, 0);