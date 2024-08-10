-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-08-2024 a las 19:11:00
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_rredsi`
--
CREATE DATABASE IF NOT EXISTS `db_rredsi` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_rredsi`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `areas_conocimiento`
--

CREATE TABLE `areas_conocimiento` (
  `id_area_conocimiento` int(11) NOT NULL,
  `nombre` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistentes`
--

CREATE TABLE `asistentes` (
  `id_asistente` int(11) NOT NULL,
  `id_detalles_personales` int(11) DEFAULT NULL,
  `asistencia` tinyint(4) DEFAULT 0,
  `tipo_asistente` enum('evaluador','delegado','ponente','externos') DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `url_comprobante_pago` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autores`
--

CREATE TABLE `autores` (
  `id_autor` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `id_proyecto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `convocatorias`
--

CREATE TABLE `convocatorias` (
  `id_convocatoria` int(11) NOT NULL,
  `nombre` varchar(25) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `estado` enum('en curso','concluida','por publicar') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_personales`
--

CREATE TABLE `detalles_personales` (
  `id_detalle_personal` int(11) NOT NULL,
  `id_tipo_documento` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `documento` varchar(55) NOT NULL,
  `nombres` varchar(25) DEFAULT NULL,
  `apellidos` varchar(25) DEFAULT NULL,
  `celular` varchar(10) NOT NULL,
  `id_institucion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `etapas`
--

CREATE TABLE `etapas` (
  `id_etapa` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fases`
--

CREATE TABLE `fases` (
  `id_fase` int(11) NOT NULL,
  `id_etapa` int(11) DEFAULT NULL,
  `nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_actividades_admin`
--

CREATE TABLE `historial_actividades_admin` (
  `id_actividad` int(11) NOT NULL,
  `accion` enum('Insertar','Actualizar','Eliminar') DEFAULT NULL,
  `id_modulo` int(11) DEFAULT NULL,
  `id_registro` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instituciones`
--

CREATE TABLE `instituciones` (
  `id_institucion` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `items_rubrica`
--

CREATE TABLE `items_rubrica` (
  `id_item_rubrica` int(11) NOT NULL,
  `id_rubrica` int(11) DEFAULT NULL,
  `componente` text DEFAULT NULL,
  `valor_max` float(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modalidades`
--

CREATE TABLE `modalidades` (
  `id_modalidad` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `id_modulo` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participantes_proyecto`
--

CREATE TABLE `participantes_proyecto` (
  `id_participante_proyecto` int(11) NOT NULL,
  `id_datos_personales` int(11) DEFAULT NULL,
  `id_proyecto` int(11) DEFAULT NULL,
  `id_etapa` int(11) DEFAULT NULL,
  `id_proyecto_convocatoria` int(11) DEFAULT NULL,
  `tipo_participante` enum('ponente','tutor','suplente evaluador','suplente ponente','evaluador') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id_modulo` int(11) NOT NULL,
  `id_rol` int(11) NOT NULL,
  `p_insertar` tinyint(4) DEFAULT 0,
  `p_consultar` tinyint(4) DEFAULT 0,
  `p_actualizar` tinyint(4) DEFAULT 0,
  `p_eliminar` tinyint(4) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `postulaciones_evaluadores`
--

CREATE TABLE `postulaciones_evaluadores` (
  `id_convocatoria` int(11) NOT NULL,
  `id_evaluador` int(11) NOT NULL,
  `etapa_virtual` tinyint(4) DEFAULT 0,
  `etapa_presencial` tinyint(4) DEFAULT 0,
  `jornada_manana` tinyint(4) DEFAULT 0,
  `jornada_tarde` tinyint(4) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presentaciones_proyectos`
--

CREATE TABLE `presentaciones_proyectos` (
  `id_presentacion` int(11) NOT NULL,
  `id_proyecto` int(11) DEFAULT NULL,
  `url_presentacion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programacion_fases`
--

CREATE TABLE `programacion_fases` (
  `id_programacion_fase` int(11) NOT NULL,
  `id_fase` int(11) DEFAULT NULL,
  `id_convocatoria` int(11) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos`
--

CREATE TABLE `proyectos` (
  `id_proyecto` int(11) NOT NULL,
  `id_institucion` int(11) DEFAULT NULL,
  `id_modalidad` int(11) DEFAULT NULL,
  `id_area_conocimiento` int(11) DEFAULT NULL,
  `titulo` varchar(200) DEFAULT NULL,
  `programa_academico` varchar(50) DEFAULT NULL,
  `grupo_investigacion` varchar(50) DEFAULT NULL,
  `linea_investigacion` varchar(50) DEFAULT NULL,
  `nombre_semillero` varchar(50) DEFAULT NULL,
  `url_propuesta_escrita` varchar(255) DEFAULT NULL,
  `url_poster` varchar(255) DEFAULT NULL,
  `url_aval` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos_convocatoria`
--

CREATE TABLE `proyectos_convocatoria` (
  `id_proyecto_convocatoria` int(11) NOT NULL,
  `id_proyecto` int(11) DEFAULT NULL,
  `id_convocatoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `respuestas_rubricas`
--

CREATE TABLE `respuestas_rubricas` (
  `id_respuestas_rubrica` int(11) NOT NULL,
  `id_item_rubrica` int(11) DEFAULT NULL,
  `id_rubrica_resultado` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_proyecto_convocatoria` int(11) DEFAULT NULL,
  `observacion` text DEFAULT NULL,
  `calificacion` float(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `nombre` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rubricas`
--

CREATE TABLE `rubricas` (
  `id_rubrica` int(11) NOT NULL,
  `titulo` varchar(40) DEFAULT NULL,
  `id_etapa` int(11) DEFAULT NULL,
  `id_modalidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rubricas_resultados`
--

CREATE TABLE `rubricas_resultados` (
  `id_rubrica_resultado` int(11) NOT NULL,
  `puntaje_aprobacion` float(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salas`
--

CREATE TABLE `salas` (
  `id_sala` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `area_conocimiento` int(11) DEFAULT NULL,
  `numero_sala` varchar(25) DEFAULT NULL,
  `nombre_sala` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salas_asignadas`
--

CREATE TABLE `salas_asignadas` (
  `id_sala` int(11) NOT NULL,
  `id_proyecto_convocatoria` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_documento`
--

CREATE TABLE `tipos_documento` (
  `id_tipo_documento` int(11) NOT NULL,
  `nombre` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `titulos_academicos`
--

CREATE TABLE `titulos_academicos` (
  `id_titulo_academico` int(11) NOT NULL,
  `nivel` enum('pregrado','maestria','especializacion','doctorado') NOT NULL,
  `nombre_titulo` varchar(80) NOT NULL,
  `url_titulo` varchar(255) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `correo` varchar(70) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `estado` enum('activo','inactivo') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `areas_conocimiento`
--
ALTER TABLE `areas_conocimiento`
  ADD PRIMARY KEY (`id_area_conocimiento`);

--
-- Indices de la tabla `asistentes`
--
ALTER TABLE `asistentes`
  ADD PRIMARY KEY (`id_asistente`),
  ADD KEY `id_detalles_personales` (`id_detalles_personales`);

--
-- Indices de la tabla `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`id_autor`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- Indices de la tabla `convocatorias`
--
ALTER TABLE `convocatorias`
  ADD PRIMARY KEY (`id_convocatoria`);

--
-- Indices de la tabla `detalles_personales`
--
ALTER TABLE `detalles_personales`
  ADD PRIMARY KEY (`id_detalle_personal`),
  ADD UNIQUE KEY `documento` (`documento`),
  ADD UNIQUE KEY `celular` (`celular`),
  ADD KEY `id_tipo_documento` (`id_tipo_documento`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_institucion` (`id_institucion`);

--
-- Indices de la tabla `etapas`
--
ALTER TABLE `etapas`
  ADD PRIMARY KEY (`id_etapa`);

--
-- Indices de la tabla `fases`
--
ALTER TABLE `fases`
  ADD PRIMARY KEY (`id_fase`),
  ADD KEY `id_etapa` (`id_etapa`);

--
-- Indices de la tabla `historial_actividades_admin`
--
ALTER TABLE `historial_actividades_admin`
  ADD PRIMARY KEY (`id_actividad`),
  ADD KEY `id_modulo` (`id_modulo`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `instituciones`
--
ALTER TABLE `instituciones`
  ADD PRIMARY KEY (`id_institucion`);

--
-- Indices de la tabla `items_rubrica`
--
ALTER TABLE `items_rubrica`
  ADD PRIMARY KEY (`id_item_rubrica`),
  ADD KEY `id_rubrica` (`id_rubrica`);

--
-- Indices de la tabla `modalidades`
--
ALTER TABLE `modalidades`
  ADD PRIMARY KEY (`id_modalidad`);

--
-- Indices de la tabla `modulos`
--
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`id_modulo`);

--
-- Indices de la tabla `participantes_proyecto`
--
ALTER TABLE `participantes_proyecto`
  ADD PRIMARY KEY (`id_participante_proyecto`),
  ADD KEY `id_datos_personales` (`id_datos_personales`),
  ADD KEY `id_proyecto` (`id_proyecto`),
  ADD KEY `id_etapa` (`id_etapa`),
  ADD KEY `id_proyecto_convocatoria` (`id_proyecto_convocatoria`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id_modulo`,`id_rol`),
  ADD KEY `id_rol` (`id_rol`);

--
-- Indices de la tabla `postulaciones_evaluadores`
--
ALTER TABLE `postulaciones_evaluadores`
  ADD PRIMARY KEY (`id_convocatoria`,`id_evaluador`),
  ADD KEY `id_evaluador` (`id_evaluador`);

--
-- Indices de la tabla `presentaciones_proyectos`
--
ALTER TABLE `presentaciones_proyectos`
  ADD PRIMARY KEY (`id_presentacion`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- Indices de la tabla `programacion_fases`
--
ALTER TABLE `programacion_fases`
  ADD PRIMARY KEY (`id_programacion_fase`),
  ADD KEY `id_fase` (`id_fase`),
  ADD KEY `id_convocatoria` (`id_convocatoria`);

--
-- Indices de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD PRIMARY KEY (`id_proyecto`),
  ADD KEY `id_institucion` (`id_institucion`),
  ADD KEY `id_modalidad` (`id_modalidad`),
  ADD KEY `id_area_conocimiento` (`id_area_conocimiento`);

--
-- Indices de la tabla `proyectos_convocatoria`
--
ALTER TABLE `proyectos_convocatoria`
  ADD PRIMARY KEY (`id_proyecto_convocatoria`),
  ADD KEY `id_proyecto` (`id_proyecto`),
  ADD KEY `id_convocatoria` (`id_convocatoria`);

--
-- Indices de la tabla `respuestas_rubricas`
--
ALTER TABLE `respuestas_rubricas`
  ADD PRIMARY KEY (`id_respuestas_rubrica`),
  ADD KEY `id_item_rubrica` (`id_item_rubrica`),
  ADD KEY `id_rubrica_resultado` (`id_rubrica_resultado`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_proyecto_convocatoria` (`id_proyecto_convocatoria`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `rubricas`
--
ALTER TABLE `rubricas`
  ADD PRIMARY KEY (`id_rubrica`),
  ADD KEY `id_etapa` (`id_etapa`),
  ADD KEY `id_modalidad` (`id_modalidad`);

--
-- Indices de la tabla `rubricas_resultados`
--
ALTER TABLE `rubricas_resultados`
  ADD PRIMARY KEY (`id_rubrica_resultado`);

--
-- Indices de la tabla `salas`
--
ALTER TABLE `salas`
  ADD PRIMARY KEY (`id_sala`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `area_conocimiento` (`area_conocimiento`);

--
-- Indices de la tabla `salas_asignadas`
--
ALTER TABLE `salas_asignadas`
  ADD PRIMARY KEY (`id_sala`,`id_proyecto_convocatoria`),
  ADD KEY `id_proyecto_convocatoria` (`id_proyecto_convocatoria`);

--
-- Indices de la tabla `tipos_documento`
--
ALTER TABLE `tipos_documento`
  ADD PRIMARY KEY (`id_tipo_documento`);

--
-- Indices de la tabla `titulos_academicos`
--
ALTER TABLE `titulos_academicos`
  ADD PRIMARY KEY (`id_titulo_academico`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `areas_conocimiento`
--
ALTER TABLE `areas_conocimiento`
  MODIFY `id_area_conocimiento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `asistentes`
--
ALTER TABLE `asistentes`
  MODIFY `id_asistente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `autores`
--
ALTER TABLE `autores`
  MODIFY `id_autor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `convocatorias`
--
ALTER TABLE `convocatorias`
  MODIFY `id_convocatoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalles_personales`
--
ALTER TABLE `detalles_personales`
  MODIFY `id_detalle_personal` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `etapas`
--
ALTER TABLE `etapas`
  MODIFY `id_etapa` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fases`
--
ALTER TABLE `fases`
  MODIFY `id_fase` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `historial_actividades_admin`
--
ALTER TABLE `historial_actividades_admin`
  MODIFY `id_actividad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `instituciones`
--
ALTER TABLE `instituciones`
  MODIFY `id_institucion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `items_rubrica`
--
ALTER TABLE `items_rubrica`
  MODIFY `id_item_rubrica` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modalidades`
--
ALTER TABLE `modalidades`
  MODIFY `id_modalidad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulos`
--
ALTER TABLE `modulos`
  MODIFY `id_modulo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `participantes_proyecto`
--
ALTER TABLE `participantes_proyecto`
  MODIFY `id_participante_proyecto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id_modulo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `presentaciones_proyectos`
--
ALTER TABLE `presentaciones_proyectos`
  MODIFY `id_presentacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `programacion_fases`
--
ALTER TABLE `programacion_fases`
  MODIFY `id_programacion_fase` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proyectos_convocatoria`
--
ALTER TABLE `proyectos_convocatoria`
  MODIFY `id_proyecto_convocatoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `respuestas_rubricas`
--
ALTER TABLE `respuestas_rubricas`
  MODIFY `id_respuestas_rubrica` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rubricas`
--
ALTER TABLE `rubricas`
  MODIFY `id_rubrica` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rubricas_resultados`
--
ALTER TABLE `rubricas_resultados`
  MODIFY `id_rubrica_resultado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `salas`
--
ALTER TABLE `salas`
  MODIFY `id_sala` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipos_documento`
--
ALTER TABLE `tipos_documento`
  MODIFY `id_tipo_documento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `titulos_academicos`
--
ALTER TABLE `titulos_academicos`
  MODIFY `id_titulo_academico` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistentes`
--
ALTER TABLE `asistentes`
  ADD CONSTRAINT `asistentes_ibfk_1` FOREIGN KEY (`id_detalles_personales`) REFERENCES `detalles_personales` (`id_detalle_personal`);

--
-- Filtros para la tabla `autores`
--
ALTER TABLE `autores`
  ADD CONSTRAINT `autores_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`);

--
-- Filtros para la tabla `detalles_personales`
--
ALTER TABLE `detalles_personales`
  ADD CONSTRAINT `detalles_personales_ibfk_1` FOREIGN KEY (`id_tipo_documento`) REFERENCES `tipos_documento` (`id_tipo_documento`),
  ADD CONSTRAINT `detalles_personales_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `detalles_personales_ibfk_3` FOREIGN KEY (`id_institucion`) REFERENCES `instituciones` (`id_institucion`);

--
-- Filtros para la tabla `fases`
--
ALTER TABLE `fases`
  ADD CONSTRAINT `fases_ibfk_1` FOREIGN KEY (`id_etapa`) REFERENCES `etapas` (`id_etapa`);

--
-- Filtros para la tabla `historial_actividades_admin`
--
ALTER TABLE `historial_actividades_admin`
  ADD CONSTRAINT `historial_actividades_admin_ibfk_1` FOREIGN KEY (`id_modulo`) REFERENCES `modulos` (`id_modulo`),
  ADD CONSTRAINT `historial_actividades_admin_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `items_rubrica`
--
ALTER TABLE `items_rubrica`
  ADD CONSTRAINT `items_rubrica_ibfk_1` FOREIGN KEY (`id_rubrica`) REFERENCES `rubricas` (`id_rubrica`);

--
-- Filtros para la tabla `participantes_proyecto`
--
ALTER TABLE `participantes_proyecto`
  ADD CONSTRAINT `participantes_proyecto_ibfk_1` FOREIGN KEY (`id_datos_personales`) REFERENCES `detalles_personales` (`id_detalle_personal`),
  ADD CONSTRAINT `participantes_proyecto_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`),
  ADD CONSTRAINT `participantes_proyecto_ibfk_3` FOREIGN KEY (`id_etapa`) REFERENCES `etapas` (`id_etapa`),
  ADD CONSTRAINT `participantes_proyecto_ibfk_4` FOREIGN KEY (`id_proyecto_convocatoria`) REFERENCES `proyectos_convocatoria` (`id_proyecto_convocatoria`);

--
-- Filtros para la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD CONSTRAINT `permisos_ibfk_1` FOREIGN KEY (`id_modulo`) REFERENCES `modulos` (`id_modulo`),
  ADD CONSTRAINT `permisos_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`);

--
-- Filtros para la tabla `postulaciones_evaluadores`
--
ALTER TABLE `postulaciones_evaluadores`
  ADD CONSTRAINT `postulaciones_evaluadores_ibfk_1` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatorias` (`id_convocatoria`),
  ADD CONSTRAINT `postulaciones_evaluadores_ibfk_2` FOREIGN KEY (`id_evaluador`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `presentaciones_proyectos`
--
ALTER TABLE `presentaciones_proyectos`
  ADD CONSTRAINT `presentaciones_proyectos_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`);

--
-- Filtros para la tabla `programacion_fases`
--
ALTER TABLE `programacion_fases`
  ADD CONSTRAINT `programacion_fases_ibfk_1` FOREIGN KEY (`id_fase`) REFERENCES `fases` (`id_fase`),
  ADD CONSTRAINT `programacion_fases_ibfk_2` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatorias` (`id_convocatoria`);

--
-- Filtros para la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD CONSTRAINT `proyectos_ibfk_1` FOREIGN KEY (`id_institucion`) REFERENCES `instituciones` (`id_institucion`),
  ADD CONSTRAINT `proyectos_ibfk_2` FOREIGN KEY (`id_modalidad`) REFERENCES `modalidades` (`id_modalidad`),
  ADD CONSTRAINT `proyectos_ibfk_3` FOREIGN KEY (`id_area_conocimiento`) REFERENCES `areas_conocimiento` (`id_area_conocimiento`);

--
-- Filtros para la tabla `proyectos_convocatoria`
--
ALTER TABLE `proyectos_convocatoria`
  ADD CONSTRAINT `proyectos_convocatoria_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`),
  ADD CONSTRAINT `proyectos_convocatoria_ibfk_2` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatorias` (`id_convocatoria`);

--
-- Filtros para la tabla `respuestas_rubricas`
--
ALTER TABLE `respuestas_rubricas`
  ADD CONSTRAINT `respuestas_rubricas_ibfk_1` FOREIGN KEY (`id_item_rubrica`) REFERENCES `items_rubrica` (`id_item_rubrica`),
  ADD CONSTRAINT `respuestas_rubricas_ibfk_2` FOREIGN KEY (`id_rubrica_resultado`) REFERENCES `rubricas_resultados` (`id_rubrica_resultado`),
  ADD CONSTRAINT `respuestas_rubricas_ibfk_3` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `respuestas_rubricas_ibfk_4` FOREIGN KEY (`id_proyecto_convocatoria`) REFERENCES `proyectos_convocatoria` (`id_proyecto_convocatoria`);

--
-- Filtros para la tabla `rubricas`
--
ALTER TABLE `rubricas`
  ADD CONSTRAINT `rubricas_ibfk_1` FOREIGN KEY (`id_etapa`) REFERENCES `etapas` (`id_etapa`),
  ADD CONSTRAINT `rubricas_ibfk_2` FOREIGN KEY (`id_modalidad`) REFERENCES `modalidades` (`id_modalidad`);

--
-- Filtros para la tabla `salas`
--
ALTER TABLE `salas`
  ADD CONSTRAINT `salas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `salas_ibfk_2` FOREIGN KEY (`area_conocimiento`) REFERENCES `areas_conocimiento` (`id_area_conocimiento`);

--
-- Filtros para la tabla `salas_asignadas`
--
ALTER TABLE `salas_asignadas`
  ADD CONSTRAINT `salas_asignadas_ibfk_1` FOREIGN KEY (`id_sala`) REFERENCES `salas` (`id_sala`),
  ADD CONSTRAINT `salas_asignadas_ibfk_2` FOREIGN KEY (`id_proyecto_convocatoria`) REFERENCES `proyectos_convocatoria` (`id_proyecto_convocatoria`);

--
-- Filtros para la tabla `titulos_academicos`
--
ALTER TABLE `titulos_academicos`
  ADD CONSTRAINT `titulos_academicos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
