DROP DATABASE IF EXISTS db_rredsi;
CREATE DATABASE db_rredsi;
USE db_rredsi;

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

CREATE TABLE etapas (
    id_etapa INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL
);

CREATE TABLE fases (
    id_fase INT PRIMARY KEY AUTO_INCREMENT,
    id_etapa INT,
    nombre VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_etapa) REFERENCES etapas(id_etapa)
);

CREATE TABLE convocatorias (
    id_convocatoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(25),
    fecha_inicio DATE,
    fecha_fin DATE,
    estado ENUM('en curso', 'concluida', 'por publicar')
);

CREATE TABLE programacion_fases (
    id_programacion_fase INT PRIMARY KEY AUTO_INCREMENT,
    id_fase INT,
    id_convocatoria INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_fase) REFERENCES fases(id_fase),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria)
);

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

CREATE TABLE items_rubrica (
    id_item_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    id_rubrica INT,
    componente TEXT,
    valor_max FLOAT(2, 1),
    FOREIGN KEY (id_rubrica) REFERENCES rubricas(id_rubrica)
);

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

CREATE TABLE autores (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    id_proyecto INT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);

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
    FOREIGN KEY (id_tipo_documento) REFERENCES tipos_documento(id_tipo_documento),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_institucion) REFERENCES instituciones(id_institucion)
);


CREATE TABLE asistentes (
    id_asistente INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_detalles_personales INT,
    asistencia TINYINT DEFAULT 0,
    tipo_asistente ENUM('evaluador', 'delegado', 'ponente', 'externos'),
    fecha TIMESTAMP,
    url_comprobante_pago VARCHAR(255),
    FOREIGN KEY (id_detalles_personales) REFERENCES detalles_personales(id_detalle_personal)
);

CREATE TABLE proyectos_convocatoria (
    id_proyecto_convocatoria INT PRIMARY KEY AUTO_INCREMENT,
    id_proyecto INT,
    id_convocatoria INT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto),
    FOREIGN KEY (id_convocatoria) REFERENCES convocatorias(id_convocatoria)
);

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

CREATE TABLE rubricas_resultados (
    id_rubrica_resultado INT PRIMARY KEY AUTO_INCREMENT,
    estado_proyecto ENUM('pendiente', 'calificado'),
    puntaje_aprobacion FLOAT(2, 1)
);

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

CREATE TABLE salas (
    id_sala INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    area_conocimiento INT,
    numero_sala VARCHAR(25),
    nombre_sala VARCHAR(25),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (area_conocimiento) REFERENCES areas_conocimiento(id_area_conocimiento)
);


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

CREATE TABLE presentaciones_proyectos (
    id_presentacion INT PRIMARY KEY AUTO_INCREMENT,
    id_proyecto INT,
    url_presentacion TEXT,
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto)
);

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