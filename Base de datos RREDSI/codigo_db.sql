DROP DATABASE IF EXISTS defaultdb;
CREATE DATABASE defaultdb;
USE defaultdb;

CREATE TABLE areas_conocimiento (
    id_area_conocimiento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(35) NOT NULL
);

INSERT INTO areas_conocimiento (nombre) VALUES 
('Matemáticas'),
('Física'),
('Química'),
('Biología'),
('Informática'),
('Economía'),
('Psicología'),
('Derecho'),
('Medicina'),
('Ingeniería Civil'),
('Filosofía'),
('Historia'),
('Literatura'),
('Sociología'),
('Pedagogía'),
('Administración'),
('Arquitectura'),
('Ciencias Políticas'),
('Antropología'),
('Geografía');


CREATE TABLE instituciones (
    id_institucion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO instituciones (nombre) VALUES 
('Universidad de los Andes'),
('Universidad Nacional de Colombia'),
('Pontificia Universidad Javeriana'),
('Universidad de Antioquia'),
('Universidad del Valle'),
('Universidad Industrial de Santander'),
('Universidad del Norte'),
('Universidad del Rosario'),
('Universidad EAFIT'),
('Universidad de La Sabana');

CREATE TABLE tipos_documento (
    id_tipo_documento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(10) NOT NULL
);

INSERT INTO tipos_documento (nombre) VALUES 
('Cédula'),
('Pasaporte'),
('TI');

CREATE TABLE modulos (
    id_modulo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL
);

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


CREATE TABLE roles (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(35) NOT NULL
);

INSERT INTO roles (nombre) VALUES 
('Evaluador'),
('Delegado'),
('Admin'),
('Tutor'),
('Ponente'),
('SuperAdmin');

CREATE TABLE permisos (
    id_modulo INT AUTO_INCREMENT,
    id_rol INT,
    p_insertar TINYINT DEFAULT 0,
    p_consultar TINYINT DEFAULT 0,
    p_actualizar TINYINT DEFAULT 0,
    p_eliminar TINYINT DEFAULT 0,
    PRIMARY KEY (id_modulo, id_rol),
    FOREIGN KEY (id_modulo) REFERENCES modulos(id_modulo),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    id_rol INT,
    id_tipo_documento INT,
    documento VARCHAR(55) UNIQUE NOT NULL,
    nombres VARCHAR(25),
    apellidos VARCHAR(25),
    celular VARCHAR(12) UNIQUE NOT NULL,
    correo VARCHAR(70) NOT NULL UNIQUE,
    clave VARCHAR(255) NOT NULL,
    estado ENUM('activo', 'inactivo') NOT NULL,
    FOREIGN KEY (id_tipo_documento) REFERENCES tipos_documento(id_tipo_documento),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

INSERT INTO usuarios (id_rol, id_tipo_documento, documento, nombres, apellidos, celular, correo, clave, estado)
VALUES
(1, 1, '123456789', 'Juan', 'Pérez', '3001234567', 'evaluador@example.com', '12345', 'activo'),
(2, 2, '987654321', 'Ana', 'Gómez', '3007654321', 'delegado@example.com', '12345', 'activo'),
(3, 1, '112233445', 'Carlos', 'Rodríguez', '3001122334', 'admin@example.com', '12345', 'activo'),
(4, 2, '556677889', 'María', 'López', '3005566778', 'superadmin@example.com', '12345', 'inactivo');


CREATE TABLE etapas (
    id_etapa INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL
);

INSERT INTO etapas (nombre)
VALUES 
('Presencial'),
('Virtual');


CREATE TABLE fases (
    id_fase INT PRIMARY KEY AUTO_INCREMENT,
    id_etapa INT,
    nombre VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_etapa) REFERENCES etapas(id_etapa)
);

INSERT INTO fases (id_etapa, nombre)
VALUES
(1, 'Publicación de resultados'),
(1, 'Inscripciones abiertas'),
(2, 'Asignaciones'),
(2, 'Ponencias'),
(2, 'Evaluaciones');


CREATE TABLE convocatorias (
    id_convocatoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(25),
    fecha_inicio DATE,
    fecha_fin DATE,
    estado ENUM('en curso', 'concluida', 'por publicar')
);

INSERT INTO convocatorias (nombre, fecha_inicio, fecha_fin, estado)
VALUES
('Convo 2024', '2024-01-01', '2024-06-30', 'en curso'),
('Convo 2023', '2023-01-01', '2023-06-30', 'concluida'),
('Convo 2025', '2025-01-01', '2025-06-30', 'por publicar');


CREATE TABLE programacion_fases (
    id_programacion_fase INT PRIMARY KEY AUTO_INCREMENT,
    id_fase INT,
    id_convocatoria INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    id_etspa INT,
    FOREIGN KEY (id_fase) REFERENCES fases(id_fase),
    FOREIGN KEY (id_etapa) REFERENCES etapas(id_etapa),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria)
);

INSERT INTO programacion_fases (id_fase, id_convocatoria, fecha_inicio, fecha_fin)
VALUES
(1, 1, '2024-01-05', '2024-01-10'),
(2, 1, '2024-01-11', '2024-02-15'),
(3, 1, '2024-02-16', '2024-03-15'),
(4, 1, '2024-03-16', '2024-04-15'),
(5, 1, '2024-04-16', '2024-06-30');

CREATE TABLE postulaciones_evaluadores (
    id_convocatoria INT,
    id_evaluador INT,
    estado_postulacion ENUM('pendiente', 'aceptada', 'rechazada') NOT NULL DEFAULT 'pendiente', 
    etapa_virtual TINYINT DEFAULT 0,
    etapa_presencial TINYINT DEFAULT 0,
    jornada_manana TINYINT DEFAULT 0,
    jornada_tarde TINYINT DEFAULT 0,
    PRIMARY KEY (id_convocatoria, id_evaluador),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria),
    FOREIGN KEY (id_evaluador) REFERENCES usuarios(id_usuario)
);

INSERT INTO postulaciones_evaluadores (id_convocatoria, id_evaluador, estado_postulacion, etapa_virtual, etapa_presencial, jornada_manana, jornada_tarde)
VALUES
(1, 1, 'pendiente', 1, 0, 1, 0),  -- Evaluador para la convocatoria 2024, solo en la etapa virtual y en la jornada de mañana
(1, 2, 'pendiente', 0, 1, 0, 1),  -- Evaluador para la convocatoria 2024, solo en la etapa presencial y en la jornada de tarde
(2, 1, 'aceptada', 1, 1, 1, 0),   -- Evaluador para la convocatoria 2023, en ambas etapas y solo en la jornada de mañana
(3, 3, 'rechazada', 0, 1, 0, 1);  -- Evaluador para la convocatoria 2025, solo en la etapa presencial y en la jornada de tarde


CREATE TABLE modalidades (
    id_modalidad INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL
);

INSERT INTO modalidades (nombre) VALUES 
('Poster'),
('Finalizado'),
('En curso');

CREATE TABLE rubricas (
    id_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(40),
    id_etapa INT,
    id_modalidad INT,
    FOREIGN KEY (id_etapa) REFERENCES etapas(id_etapa),
    FOREIGN KEY (id_modalidad) REFERENCES modalidades(id_modalidad)
);

INSERT INTO rubricas (titulo, id_etapa, id_modalidad)
VALUES
('Presencial-Poster', 1, 1),
('Virtual-Finalizado', 2, 2);


CREATE TABLE items_rubrica (
    id_item_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    id_rubrica INT,
    titulo VARCHAR(50),
    componente TEXT,
    valor_max FLOAT(3, 1),
    FOREIGN KEY (id_rubrica) REFERENCES rubricas(id_rubrica)
);

INSERT INTO items_rubrica (id_rubrica, titulo ,componente, valor_max)
VALUES
(1, 'titulo','Originalidad del proyecto', 10.0),
(1, 'redaccion','Claridad de la presentación', 9.5),
(2, 'originalidad','Innovación tecnológica', 10.0),
(2, 'Social','Impacto social', 9.0);

CREATE TABLE proyectos (
    id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    id_institucion INT,
    id_modalidad INT,
    id_area_conocimiento INT,
    titulo VARCHAR(200),
    estado_asignacion ENUM('pendiente', 'asignado') NOT NULL,
    estado_calificacion ENUM('P_virtual', 'C_virtual','P_presencial','C_presencial') NOT NULL,
    programa_academico VARCHAR(50),
    grupo_investigacion VARCHAR(50),
    linea_investigacion VARCHAR(50),
    nombre_semillero VARCHAR(50),
    url_propuesta_escrita VARCHAR(255),
    url_aval VARCHAR(255),
    FOREIGN KEY (id_institucion) REFERENCES instituciones(id_institucion),
    FOREIGN KEY (id_modalidad) REFERENCES modalidades(id_modalidad),
    FOREIGN KEY (id_area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento)
);

-- triger que inserte los participantes proyectos de tutor y ponente proeycto convocatoria registar autores

INSERT INTO proyectos (id_proyecto, id_institucion, id_modalidad, id_area_conocimiento, titulo, estado, programa_academico, grupo_investigacion, linea_investigacion, nombre_semillero, url_propuesta_escrita, url_aval)
VALUES
(1, 1, 1, 1, 'Innovación en Energías Renovables', 'pendiente', 'Ingeniería Eléctrica', 'Grupo de Energías Renovables', 'Energía Solar', 'Semillero de Energía', 'https://propuestas.com/energia_renovable','https://avales.com/energia_renovable'),
(2, 2, 2, 2, 'Desarrollo de Software Educativo', 'asignado', 'Ingeniería de Sistemas', 'Grupo de Tecnologías Educativas', 'Software Educativo', 'Semillero de Tecnología', 'https://propuestas.com/software_educativo', 'https://avales.com/software_educativo');

CREATE TABLE autores (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    id_proyecto INT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);
INSERT INTO autores (nombre, id_proyecto)
VALUES
('Juan Pérez', 1),
('Ana Gómez', 1),
('Carlos López', 2),
('María Rodríguez', 2);

CREATE TABLE titulos_academicos (
    id_titulo_academico INT PRIMARY KEY AUTO_INCREMENT,
    nivel ENUM('pregrado', 'maestria', 'especializacion', 'doctorado') NOT NULL,
    nombre_titulo VARCHAR(80) NOT NULL,
    url_titulo VARCHAR(255) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

INSERT INTO titulos_academicos (nivel, nombre_titulo, url_titulo, id_usuario)
VALUES
('pregrado', 'Ingeniería Eléctrica', 'https://titulos.com/ingenieria_electrica', 1),
('maestria', 'Maestría en Educación', 'https://titulos.com/maestria_educacion', 2),
('especializacion', 'Especialización en Gestión de Proyectos', 'https://titulos.com/especializacion_proyectos', 3),
('doctorado', 'Doctorado en Física', 'https://titulos.com/doctorado_fisica', 4);

CREATE TABLE detalles_institucionales (
    id_detalle_institucional INT AUTO_INCREMENT,
    id_usuario INT UNIQUE,
    id_institucion INT,
    semillero VARCHAR(35),
    grupo_investigacion VARCHAR(35),
    id_primera_area_conocimiento INT,
    id_segunda_area_conocimiento INT,
    PRIMARY KEY (id_detalle_institucional, id_usuario),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_institucion) REFERENCES instituciones(id_institucion),
    FOREIGN KEY (id_primera_area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento),
    FOREIGN KEY (id_segunda_area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento)
);

INSERT INTO detalles_institucionales (id_usuario, id_institucion, semillero, grupo_investigacion, id_primera_area_conocimiento, id_segunda_area_conocimiento)
VALUES
(1, 1, 'Semillero de Tecnología', 'Grupo de Innovación', 1, 2),
(2, 2, 'Semillero de IA', 'Grupo de Inteligencia Artificial', 3, 4),
(3, 3, 'Semillero de Gestión', 'Grupo de Gestión de Proyectos', 5, 6),
(4, 4, 'Semillero de Sostenibilidad', 'Grupo de Ciencias Ambientales', 7, 8);

CREATE TABLE asistentes (
    id_asistente INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    asistencia TINYINT DEFAULT 0,
    fecha TIMESTAMP,
    url_comprobante_pago VARCHAR(255),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

INSERT INTO asistentes (id_usuario, asistencia, tipo_asistente, fecha, url_comprobante_pago)
VALUES
(1, 1,  '2024-09-10 09:00:00', 'https://comprobantes.com/pago_juan'),
(2, 0,  '2024-09-11 10:00:00', 'https://comprobantes.com/pago_ana'),
(3, 1,  '2024-09-12 11:00:00', 'https://comprobantes.com/pago_carlos'),
(4, 1,  '2024-09-13 12:00:00', 'https://comprobantes.com/pago_maria');

CREATE TABLE proyectos_convocatoria (
    id_proyecto_convocatoria INT PRIMARY KEY AUTO_INCREMENT,
    id_proyecto INT,
    id_convocatoria INT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria) 
);

INSERT INTO proyectos_convocatoria (id_proyecto, id_convocatoria)
VALUES
(1, 1),  -- Proyecto 1 para Convocatoria 1
(2, 2),  -- Proyecto 2 para Convocatoria 2
(3, 1),  -- Proyecto 3 para Convocatoria 1
(4, 3);  -- Proyecto 4 para Convocatoria 3

CREATE TABLE participantes_proyecto (
    id_participante_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_etapa INT,
    id_proyecto INT,
    id_proyectos_convocatoria INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_etapa) REFERENCES etapas(id_etapa),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto),
    FOREIGN KEY (id_proyectos_convocatoria) REFERENCES proyectos_convocatoria(id_proyecto_convocatoria)
);

INSERT INTO participantes_proyecto (id_usuario, id_etapa, id_proyecto, tipo_participante)
VALUES
(1, 1, 1, 1, 'ponente'),           
(2, 2, 2, 2, 'tutor'),             
(3, 3, 3, 3, 'ponente'),         
(4, 4, 4, 4, 'suplente evaluador'); 

CREATE TABLE rubricas_resultados (
    id_rubrica_resultado INT PRIMARY KEY AUTO_INCREMENT,
    puntaje_aprobacion FLOAT(10, 1)
);

INSERT INTO rubricas_resultados (estado_proyecto, puntaje_aprobacion)
VALUES
('pendiente', 7.5),  -- Resultado pendiente con un puntaje de aprobación de 7.5
('calificado', 8.0),  -- Proyecto calificado con un puntaje de aprobación de 8.0
('pendiente', 6.5);   -- Resultado pendiente con un puntaje de aprobación de 6.5


CREATE TABLE respuestas_rubricas (
    id_respuestas_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    id_item_rubrica INT,
    id_rubrica_resultado INT,
    id_usuario INT,
    id_proyecto_convocatoria INT,
    observacion TEXT,
    calificacion FLOAT(3, 1),
    FOREIGN KEY (id_item_rubrica) REFERENCES items_rubrica(id_item_rubrica),
    FOREIGN KEY (id_rubrica_resultado) REFERENCES rubricas_resultados(id_rubrica_resultado),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_proyecto_convocatoria) REFERENCES proyectos_convocatoria(id_proyecto_convocatoria)
);

INSERT INTO respuestas_rubricas (id_item_rubrica, id_rubrica_resultado, id_usuario, id_proyecto_convocatoria, observacion, calificacion)
VALUES
(1, 1, 2, 1, 'Buen desarrollo del proyecto', 8.0),  -- Respuesta para el primer ítem de la rúbrica, pendiente de calificación
(2, 2, 3, 2, 'Algunas mejoras necesarias', 7.0),   -- Calificación asignada para el segundo ítem
(3, 1, 4, 3, 'Excepcional trabajo', 9.0);          -- Respuesta para el tercer ítem con calificación alta


CREATE TABLE salas (
    id_sala INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_area_conocimiento INT,
    id_convocatoria INT,
    numero_sala VARCHAR(25),
    nombre_sala VARCHAR(25),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria)
);

INSERT INTO salas (id_usuario, area_conocimiento, numero_sala, nombre_sala)
VALUES
(1, 2, '101', 'Sala Innovación'),          -- Sala asignada al usuario 1, con un área de conocimiento 2
(2, 3, '202', 'Sala Tecnología'),          -- Sala asignada al usuario 2, con un área de conocimiento 3
(3, 4, '303', 'Sala Ciencias Ambientales');-- Sala asignada al usuario 3, con un área de conocimiento 4

CREATE TABLE detalle_sala (
    id_sala INT,
    id_proyecto_convocatoria INT,
    fecha DATE,
    hora_inicio TIME,
    hora_fin TIME,
    PRIMARY KEY (id_sala, id_proyecto_convocatoria),
    FOREIGN KEY (id_sala) REFERENCES salas(id_sala),
    FOREIGN KEY (id_proyecto_convocatoria) REFERENCES proyectos_convocatoria(id_proyecto_convocatoria)
);

INSERT INTO detalle_sala (id_sala, id_proyecto_convocatoria, fecha, hora_inicio, hora_fin)
VALUES
(1, 1, '2024-09-10', '09:00:00', '11:00:00'),  -- Detalles de la sala 1 para el proyecto 1
(2, 2, '2024-09-11', '13:00:00', '15:00:00'),  -- Detalles de la sala 2 para el proyecto 2
(3, 3, '2024-09-12', '10:00:00', '12:00:00');  -- Detalles de la sala 3 para el proyecto 3

CREATE TABLE presentaciones_proyectos (
    id_presentacion INT PRIMARY KEY AUTO_INCREMENT,
    id_proyecto INT,
    url_presentacion TEXT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);

INSERT INTO presentaciones_proyectos (id_proyecto, url_presentacion)
VALUES
(1, 'http://example.com/presentacion_proyecto1.pdf'),  -- Presentación para el proyecto 1
(2, 'http://example.com/presentacion_proyecto2.pdf'),  -- Presentación para el proyecto 2
(3, 'http://example.com/presentacion_proyecto3.pdf');  -- Presentación para el proyecto 3

CREATE TABLE historial_actividades_admin (
    id_actividad INT PRIMARY KEY AUTO_INCREMENT,
    accion ENUM('Insertar','Actualizar', 'Eliminar'),
    id_modulo INT,
    id_registro INT,
    id_usuario INT, 
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_modulo) REFERENCES modulos(id_modulo),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

INSERT INTO historial_actividades_admin (accion, id_modulo, id_registro, id_usuario)
VALUES
('Insertar', 1, 101, 1),  -- Acción de insertar en el módulo 1, registro 101, realizada por el usuario 1
('Actualizar', 2, 202, 2),  -- Acción de actualizar en el módulo 2, registro 202, realizada por el usuario 2
('Eliminar', 3, 303, 3);  -- Acción de eliminar en el módulo 3, registro 303, realizada por el usuario 3
