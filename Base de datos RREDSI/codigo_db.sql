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
    correo VARCHAR(70) NOT NULL UNIQUE,
    clave VARCHAR(255) NOT NULL,
    estado ENUM('activo', 'inactivo') NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

INSERT INTO usuarios (id_rol, correo, clave, estado) VALUES
(1, 'evaluador@example.com', 'hashedpassword1', 'activo'),
(2, 'delegado@example.com', 'hashedpassword2', 'activo'),
(3, 'admin@example.com', 'hashedpassword3', 'inactivo'),
(4, 'superadmin@example.com', 'hashedpassword4', 'activo');


CREATE TABLE etapas (
    id_etapa INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL
);

INSERT INTO etapas (nombre) VALUES
('presencial'),
('virtual');


CREATE TABLE fases (
    id_fase INT PRIMARY KEY AUTO_INCREMENT,
    id_etapa INT,
    nombre VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_etapa) REFERENCES etapas(id_etapa)
);

INSERT INTO fases (id_etapa, nombre) VALUES
(1, 'publicación de resultados'),
(1, 'inscripciones abiertas'),
(1, 'asignaciones'),
(1, 'ponencias'),
(1, 'evaluaciones'),
(2, 'publicación de resultados'),
(2, 'inscripciones abiertas'),
(2, 'asignaciones'),
(2, 'ponencias'),
(2, 'evaluaciones');


CREATE TABLE convocatorias (
    id_convocatoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(25),
    fecha_inicio DATE,
    fecha_fin DATE,
    estado ENUM('en curso', 'concluida', 'por publicar')
);

INSERT INTO convocatorias (nombre, fecha_inicio, fecha_fin, estado) VALUES
('Convocatoria 2024 Presencial', '2024-01-01', '2024-02-01', 'en curso'),
('Convocatoria 2024 Virtual', '2024-03-01', '2024-04-01', 'por publicar'),
('Convocatoria 2023 Presencial', '2023-01-01', '2023-02-01', 'concluida'),
('Convocatoria 2023 Virtual', '2023-03-01', '2023-04-01', 'concluida');


CREATE TABLE programacion_fases (
    id_programacion_fase INT PRIMARY KEY AUTO_INCREMENT,
    id_fase INT,
    id_convocatoria INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_fase) REFERENCES fases(id_fase),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria)
);

INSERT INTO programacion_fases (id_fase, id_convocatoria, fecha_inicio, fecha_fin) VALUES
-- Fases para la Convocatoria 2024 Presencial (id_convocatoria = 1)
(1, 1, '2024-01-01', '2024-01-05'),  -- Publicación de resultados
(2, 1, '2024-01-06', '2024-01-10'),  -- Inscripciones abiertas
(3, 1, '2024-01-11', '2024-01-15'),  -- Asignaciones
(4, 1, '2024-01-16', '2024-01-20'),  -- Ponencias
(5, 1, '2024-01-21', '2024-01-25'),  -- Evaluaciones

-- Fases para la Convocatoria 2024 Virtual (id_convocatoria = 2)
(6, 2, '2024-03-01', '2024-03-05'),  -- Publicación de resultados
(7, 2, '2024-03-06', '2024-03-10'),  -- Inscripciones abiertas
(8, 2, '2024-03-11', '2024-03-15'),  -- Asignaciones
(9, 2, '2024-03-16', '2024-03-20'),  -- Ponencias
(10, 2, '2024-03-21', '2024-03-25'); -- Evaluaciones


CREATE TABLE postulaciones_evaluadores (
    id_convocatoria INT,
    id_evaluador INT,
    etapa_virtual TINYINT DEFAULT 0,
    etapa_presencial TINYINT DEFAULT 0,
    jornada_manana TINYINT DEFAULT 0,
    jornada_tarde TINYINT DEFAULT 0,
    PRIMARY KEY (id_convocatoria, id_evaluador),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria),
    FOREIGN KEY (id_evaluador) REFERENCES usuarios(id_usuario)
);

INSERT INTO postulaciones_evaluadores (id_convocatoria, id_evaluador, etapa_virtual, etapa_presencial, jornada_manana, jornada_tarde) VALUES
-- Suponiendo que los ID de las convocatorias son 1 y 2, y los ID de los evaluadores son 1, 2, 3 y 4
(1, 1, 1, 0, 1, 0),  -- Evaluador 1 postulado para Convocatoria 2024 Presencial, etapa virtual y jornada mañana
(1, 2, 0, 1, 1, 1),  -- Evaluador 2 postulado para Convocatoria 2024 Presencial, etapa presencial y jornadas mañana y tarde
(2, 3, 1, 0, 0, 1),  -- Evaluador 3 postulado para Convocatoria 2024 Virtual, etapa virtual y jornada tarde
(2, 4, 1, 1, 1, 0);  -- Evaluador 4 postulado para Convocatoria 2024 Virtual, etapa virtual y presencial, jornada mañana

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

INSERT INTO rubricas (titulo, id_etapa, id_modalidad) VALUES 
('Rúbrica 1', 1, 1), -- Presencial, Poster
('Rúbrica 2', 2, 2), -- Virtual, Finalizado
('Rúbrica 3', 1, 3); -- Presencial, En curso


CREATE TABLE items_rubrica (
    id_item_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    id_rubrica INT,
    titulo VARCHAR(100)
    descripcion TEXT,
    valor_max FLOAT(3, 1),
    FOREIGN KEY (id_rubrica) REFERENCES rubricas(id_rubrica)
);

INSERT INTO items_rubrica (id_rubrica, componente, valor_max) VALUES 
(1, 'Originalidad', 10.0),  -- Rúbrica 1
(1, 'Claridad en la presentación', 8.0),  -- Rúbrica 1
(2, 'Cumplimiento de objetivos', 9.5),  -- Rúbrica 2
(2, 'Calidad de los resultados', 9.0),  -- Rúbrica 2
(3, 'Nivel de detalle', 8.5),  -- Rúbrica 3
(3, 'Innovación', 7.5);  -- Rúbrica 3


CREATE TABLE proyectos (
    id_proyecto INT PRIMARY KEY,
    id_institucion INT,
    id_modalidad INT,
    id_area_conocimiento INT,
    titulo VARCHAR(200),
    estado ENUM('pendiente', 'asignado') NOT NULL,
    programa_academico VARCHAR(50),
    grupo_investigacion VARCHAR(50),
    linea_investigacion VARCHAR(50),
    nombre_semillero VARCHAR(50),
    url_propuesta_escrita VARCHAR(255),
    url_poster VARCHAR(255),
    url_aval VARCHAR(255),
    FOREIGN KEY (id_institucion) REFERENCES instituciones(id_institucion),
    FOREIGN KEY (id_modalidad) REFERENCES modalidades(id_modalidad),
    FOREIGN KEY (id_area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento)
);

INSERT INTO proyectos (id_proyecto, id_institucion, id_modalidad, id_area_conocimiento, titulo, estado, programa_academico, grupo_investigacion, linea_investigacion, nombre_semillero, url_propuesta_escrita, url_poster, url_aval) VALUES 
(1, 1, 1, 1, 'Proyecto de Investigación 1', 'pendiente', 'Ingeniería de Sistemas', 'Grupo A', 'Línea A', 'Semillero A', 'http://propuesta1.com', 'http://poster1.com', 'http://aval1.com'),
(2, 2, 2, 2, 'Proyecto de Investigación 2', 'asignado', 'Ciencias Sociales', 'Grupo B', 'Línea B', 'Semillero B', 'http://propuesta2.com', 'http://poster2.com', 'http://aval2.com'),
(3, 1, 3, 3, 'Proyecto de Investigación 3', 'pendiente', 'Ingeniería Industrial', 'Grupo C', 'Línea C', 'Semillero C', 'http://propuesta3.com', 'http://poster3.com', 'http://aval3.com');


CREATE TABLE autores (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    id_proyecto INT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);
INSERT INTO autores (nombre, id_proyecto) VALUES 
('Juan Pérez', 1),
('María García', 2),
('Carlos López', 1),
('Ana Martínez', 3);


CREATE TABLE tipos_documento (
    id_tipo_documento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(10) NOT NULL
);

INSERT INTO tipos_documento (nombre) VALUES 
('Cédula'),
('Pasaporte'),
('TI');


CREATE TABLE titulos_academicos (
    id_titulo_academico INT PRIMARY KEY AUTO_INCREMENT,
    nivel ENUM('pregrado', 'maestria', 'especializacion', 'doctorado') NOT NULL,
    nombre_titulo VARCHAR(80) NOT NULL,
    url_titulo VARCHAR(255) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

INSERT INTO titulos_academicos (nivel, nombre_titulo, url_titulo, id_usuario) VALUES
('pregrado', 'Ingeniería de Sistemas', 'http://example.com/titulo1.pdf', 1),
('maestria', 'Maestría en Ciencias', 'http://example.com/titulo2.pdf', 2),
('doctorado', 'Doctorado en Filosofía', 'http://example.com/titulo3.pdf', 3),
('especializacion', 'Especialización en Gerencia de Proyectos', 'http://example.com/titulo4.pdf', 4);


CREATE TABLE detalles_personales (
    id_detalle_personal INT PRIMARY KEY AUTO_INCREMENT,
    id_tipo_documento INT,
    id_usuario INT,
    documento VARCHAR(55) UNIQUE NOT NULL,
    nombres VARCHAR(25),
    apellidos VARCHAR(25),
    celular VARCHAR(10) UNIQUE NOT NULL,
    id_institucion INT,
    semillero VARCHAR(25),
    grupo_investigacion VARCHAR(25),
    id_area_conocimiento INT,
    FOREIGN KEY (id_tipo_documento) REFERENCES tipos_documento(id_tipo_documento),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_institucion) REFERENCES instituciones(id_institucion),
    FOREIGN KEY (id_area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento)
);

INSERT INTO detalles_personales (id_tipo_documento, id_usuario, documento, nombres, apellidos, celular, id_institucion, semillero, grupo_investigacion) VALUES
(1, 1, '123456789', 'Juan', 'Pérez', '3001234567', 1, 'Semillero A', 'Grupo Investigación X'),
(2, 2, '987654321', 'María', 'González', '3009876543', 2, 'Semillero B', 'Grupo Investigación Y'),
(3, 3, '123789456', 'Carlos', 'López', '3012345678', 3, 'Semillero C', 'Grupo Investigación Z'),
(4, 4, '789456123', 'Ana', 'Ramírez', '3098765432', 4, 'Semillero D', 'Grupo Investigación W');



CREATE TABLE asistentes (
    id_asistente INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_detalles_personales INT,
    asistencia TINYINT DEFAULT 0,
    tipo_asistente ENUM('evaluador', 'delegado', 'ponente', 'externos'),
    fecha TIMESTAMP,
    url_comprobante_pago VARCHAR(255),
    FOREIGN KEY (id_detalles_personales) REFERENCES detalles_personales(id_detalle_personal)
);
INSERT INTO asistentes (id_detalles_personales, asistencia, tipo_asistente, fecha, url_comprobante_pago) VALUES 
(1, 1, 'evaluador', '2024-09-01 10:00:00', 'http://comprobante1.com'),
(2, 0, 'delegado', '2024-09-02 11:00:00', 'http://comprobante2.com'),
(3, 1, 'ponente', '2024-09-03 12:00:00', 'http://comprobante3.com'),
(4, 0, 'externos', '2024-09-04 13:00:00', 'http://comprobante4.com');

CREATE TABLE proyectos_convocatoria (
    id_proyecto_convocatoria INT PRIMARY KEY AUTO_INCREMENT,
    id_proyecto INT,
    id_convocatoria INT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria)
);
INSERT INTO proyectos_convocatoria (id_proyecto, id_convocatoria) VALUES 
(1, 1),
(2, 1),
(3, 2),
(1, 3);

CREATE TABLE participantes_proyecto (
    id_participante_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    id_datos_personales INT,
    id_proyecto INT,
    id_etapa INT,
    id_proyecto_convocatoria INT,
    tipo_participante ENUM('ponente', 'tutor', 'suplente evaluador', 'suplente ponente', 'evaluador'),
    FOREIGN KEY (id_datos_personales) REFERENCES detalles_personales(id_detalle_personal),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto),
    FOREIGN KEY (id_etapa) REFERENCES etapas(id_etapa),
    FOREIGN KEY (id_proyecto_convocatoria) REFERENCES proyectos_convocatoria(id_proyecto_convocatoria)
);
INSERT INTO participantes_proyecto (id_datos_personales, id_proyecto, id_etapa, id_proyecto_convocatoria, tipo_participante) VALUES 
(1, 1, 1, 1, 'ponente'),
(2, 1, 2, 2, 'tutor'),
(3, 2, 1, 3, 'suplente evaluador'),
(4, 3, 2, 4, 'evaluador');

CREATE TABLE rubricas_resultados (
    id_rubrica_resultado INT PRIMARY KEY AUTO_INCREMENT,
    estado_proyecto ENUM('pendiente', 'calificado'),

    puntaje_aprobacion FLOAT(2, 1)
);

INSERT INTO rubricas_resultados (estado_proyecto, puntaje_aprobacion) VALUES
('pendiente', 7.5),
('calificado', 8.0);

CREATE TABLE respuestas_rubricas (
    id_respuestas_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    id_item_rubrica INT,
    id_rubrica_resultado INT,
    id_usuario INT,
    id_proyecto_convocatoria INT,
    observacion TEXT,
    calificacion FLOAT(2, 1),
    FOREIGN KEY (id_item_rubrica) REFERENCES items_rubrica(id_item_rubrica),
    FOREIGN KEY (id_rubrica_resultado) REFERENCES rubricas_resultados(id_rubrica_resultado),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_proyecto_convocatoria) REFERENCES proyectos_convocatoria(id_proyecto_convocatoria)
);
INSERT INTO respuestas_rubricas (id_item_rubrica, id_rubrica_resultado, id_usuario, id_proyecto_convocatoria, observacion, calificacion) VALUES
(1, 1, 1, 1, 'Observación sobre la originalidad', 9.0),
(2, 1, 2, 2, 'Observación sobre la claridad en la presentación', 7.5),
(1, 2, 3, 3, 'Observación sobre el cumplimiento de objetivos', 8.0),
(2, 2, 4, 4, 'Observación sobre la calidad de los resultados', 9.0);


CREATE TABLE salas (
    id_sala INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    area_conocimiento INT,
    numero_sala VARCHAR(25),
    nombre_sala VARCHAR(25),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento)
);
INSERT INTO salas (id_usuario, area_conocimiento, numero_sala, nombre_sala) VALUES
(1, 1, 'A101', 'Sala de Conferencias A'),
(2, 2, 'B202', 'Sala de Talleres B'),
(3, 1, 'C303', 'Sala de Reuniones C'),
(4, 3, 'D404', 'Sala de Exposiciones D');


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
INSERT INTO detalle_sala (id_sala, id_proyecto_convocatoria, fecha, hora_inicio, hora_fin) VALUES
(1, 1, '2024-09-10', '09:00:00', '11:00:00'),
(2, 2, '2024-09-11', '10:00:00', '12:00:00'),
(3, 3, '2024-09-12', '13:00:00', '15:00:00'),
(4, 4, '2024-09-13', '14:00:00', '16:00:00');

CREATE TABLE presentaciones_proyectos (
    id_presentacion INT PRIMARY KEY AUTO_INCREMENT,
    id_proyecto INT,
    url_presentacion TEXT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);

INSERT INTO presentaciones_proyectos (id_proyecto, url_presentacion) VALUES
(1, 'http://presentacion1.com'),
(2, 'http://presentacion2.com'),
(3, 'http://presentacion3.com'),
(4, 'http://presentacion4.com');


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
INSERT INTO historial_actividades_admin (accion, id_modulo, id_registro, id_usuario, fecha) VALUES
('Insertar', 1, 101, 1, '2024-09-01 10:00:00'),
('Actualizar', 2, 102, 2, '2024-09-02 11:00:00'),
('Eliminar', 3, 103, 3, '2024-09-03 12:00:00'),
('Insertar', 1, 104, 4, '2024-09-04 13:00:00');

