DROP DATABASE IF EXISTS db_rredsi;
CREATE DATABASE db_rredsi;
USE db_rredsi;

CREATE TABLE Area_of_knowledge (
    id_area_of_knowledge INT PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR(35) NOT NULL
);

CREATE TABLE Institution (
    id_institution INT PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR(50) NOT NULL
);

CREATE TABLE Module (
    id_module INT PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR(50) NOT NULL
);

CREATE TABLE Role (
    id_role INT PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR(30) NOT NULL
);

CREATE TABLE Permissions (
    id_module INT,
    id_role INT,
    p_insert TINYINT DEFAULT 0,
    p_select TINYINT DEFAULT 0,
    p_update TINYINT DEFAULT 0,
    p_delete TINYINT DEFAULT 0,
    PRIMARY KEY (id_module, id_role),
    FOREIGN KEY (id_module) REFERENCES Module(id_module),
    FOREIGN KEY (id_role) REFERENCES Role(id_role)
);

CREATE TABLE Users (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    id_role INT,
    email VARCHAR(70) NOT NULL UNIQUE,
    passwords VARCHAR(255) NOT NULL,
    states ENUM('activo', 'inactivo') NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES Rol(id_rol)
);

CREATE TABLE Stage (
    id_stage INT PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR(20) NOT NULL
);

CREATE TABLE Phase (
    id_phase INT PRIMARY KEY AUTO_INCREMENT,
    id_stage INT,
    names VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_stage) REFERENCES Stage(id_stage)
);

CREATE TABLE Announcement (
    id_announcement INT PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR(25),
    start_dates DATE,
    end_dates DATE,
    states ENUM('en curso', 'concluida', 'por publicar')
);

CREATE TABLE Phase_programming (
    id_'id_phase_programming' INT PRIMARY KEY AUTO_INCREMENT,
    id_phase INT,
    id_announcement INT,
    start_dates DATE,
    end_dates DATE,
    FOREIGN KEY (id_phase) REFERENCES Phase(id_phase),
    FOREIGN KEY (id_announcement) REFERENCES Announcement(id_announcement)
);

CREATE TABLE Evaluators_application(
    id_announcement INT,
    id_evaluator INT,
    etapa_virtual TINYINT DEFAULT 0,
    etapa_presencial TINYINT DEFAULT 0,
    jornada_manana TINYINT DEFAULT 0,
    jornada_tarde TINYINT DEFAULT 0,
    PRIMARY KEY (id_convocatoria, id_evaluador),
    FOREIGN KEY (id_convocatoria) REFERENCES Convocatoria(id_convocatoria),
    FOREIGN KEY (id_evaluador) REFERENCES Usuario(id_usuario)
);

CREATE TABLE Modality (
    id_modality INT PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR(20) NOT NULL
);

CREATE TABLE Rubrica (
    id_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(40),
    id_etapa INT,
    id_modalidad INT,
    FOREIGN KEY (id_etapa) REFERENCES Etapa(id_etapa),
    FOREIGN KEY (id_modalidad) REFERENCES Modalidad(id_modalidad)
);

CREATE TABLE Item_rubrica (
    id_item_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    id_rubrica INT,
    componente TEXT,
    valor_max FLOAT(2, 1),
    FOREIGN KEY (id_rubrica) REFERENCES Rubrica(id_rubrica)
);

CREATE TABLE Proyecto (
    id_proyecto INT PRIMARY KEY,
    id_institucion INT,
    id_modalidad INT,
    id_area_conocimiento INT,
    titulo VARCHAR(200),
    programa_academico VARCHAR(50),
    grupo_investigacion VARCHAR(50),
    linea_investigacion VARCHAR(50),
    nombre_semillero VARCHAR(50),
    url_propuesta_escrita VARCHAR(255),
    url_poster VARCHAR(255),
    url_aval VARCHAR(255),
    FOREIGN KEY (id_institucion) REFERENCES Institucion(id_institucion),
    FOREIGN KEY (id_modalidad) REFERENCES Modalidad(id_modalidad),
    FOREIGN KEY (id_area_conocimiento) REFERENCES Area_conocimiento(id_area_conocimiento)
);

CREATE TABLE Autor (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    id_proyecto INT,
    FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id_proyecto)
);

CREATE TABLE Document_type (
    id_document_type INT PRIMARY KEY AUTO_INCREMENT,
    names VARCHAR(10) NOT NULL
);

CREATE TABLE Titulos_academicos (
    id_titulos_academicos INT PRIMARY KEY AUTO_INCREMENT,
    nivel ENUM('pregrado', 'maestria', 'especializacion', 'doctorado') NOT NULL,
    nombre_titulo VARCHAR(80) NOT NULL,
    url_titulo VARCHAR(255) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

CREATE TABLE  id_personal_detail (
    id_personal_detail INT PRIMARY KEY AUTO_INCREMENT,
    id_document_type INT,
    id_user INT,
    document VARCHAR(55) UNIQUE NOT NULL,
    names VARCHAR(25),
    last_names VARCHAR(25),
    cell_phone VARCHAR(12) UNIQUE NOT NULL,
    id_institution INT,
    FOREIGN KEY (id_document_type) REFERENCES Document_type(id_document_type),
    FOREIGN KEY (id_user) REFERENCES Users(id_user),
    FOREIGN KEY (id_institution) REFERENCES Institucion(id_institution)
);

CREATE TABLE Asistentes (
    id_asistente INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_detalles_personales INT,
    asistencia TINYINT DEFAULT 0,
    tipo_asistente ENUM('evaluador', 'delegado', 'ponente', 'externos'),
    fecha TIMESTAMP,
    url_comprobante_pago VARCHAR(255),
    FOREIGN KEY (id_detalles_personales) REFERENCES Detalle_personal(id_detalles_personales)
);

CREATE TABLE Proyecto_convocatoria (
    id_proyecto_convocatoria INT PRIMARY KEY AUTO_INCREMENT,
    id_proyecto INT,
    id_convocatoria INT,
    FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id_proyecto),
    FOREIGN KEY (id_convocatoria) REFERENCES Convocatoria(id_convocatoria)
);

CREATE TABLE Participante_proyecto (
    id_participante_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    id_datos_personales INT,
    id_proyecto INT,
    id_etapa INT,
    id_proyecto_convocatoria INT,
    tipo_participante ENUM('ponente', 'tutor', 'suplente evaluador', 'suplente ponente', 'evaluador'),
    FOREIGN KEY (id_datos_personales) REFERENCES Detalle_personal(id_detalles_personales),
    FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id_proyecto),
    FOREIGN KEY (id_etapa) REFERENCES Etapa(id_etapa),
    FOREIGN KEY (id_proyecto_convocatoria) REFERENCES Proyecto_convocatoria(id_proyecto_convocatoria)
);

CREATE TABLE Rubrica_resultado (
    id_rubrica_resultado INT PRIMARY KEY AUTO_INCREMENT,
    puntaje_aprobacion FLOAT(2, 1)
);

CREATE TABLE Respuestas_rubrica (
    id_respuestas_rubrica INT PRIMARY KEY AUTO_INCREMENT,
    id_item_rubrica INT,
    id_rubrica_resultado INT,
    id_usuario INT,
    id_proyecto_convocatoria INT,
    observacion TEXT,
    calificacion FLOAT(2, 1),
    FOREIGN KEY (id_item_rubrica) REFERENCES Item_rubrica(id_item_rubrica),
    FOREIGN KEY (id_rubrica_resultado) REFERENCES Rubrica_resultado(id_rubrica_resultado),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_proyecto_convocatoria) REFERENCES Proyecto_convocatoria(id_proyecto_convocatoria)
);

CREATE TABLE Sala (
    id_sala INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    area_conocimiento INT,
    numero_sala VARCHAR(25),
    nombre_sala VARCHAR(25),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (area_conocimiento) REFERENCES Area_conocimiento(id_area_conocimiento)
);

CREATE TABLE Sala_asignada (
    id_sala INT,
    id_proyecto_convocatoria INT,
    fecha DATE,
    hora_inicio TIME,
    hora_fin TIME,
    PRIMARY KEY (id_sala, id_proyecto_convocatoria),
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala),
    FOREIGN KEY (id_proyecto_convocatoria) REFERENCES Proyecto_convocatoria(id_proyecto_convocatoria)
);