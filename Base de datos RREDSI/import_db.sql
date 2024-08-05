-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-08-2024 a las 16:42:44
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
-- Estructura de tabla para la tabla `area_conocimiento`
--

CREATE TABLE `area_conocimiento` (
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
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `id_autor` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `id_proyecto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `convocatoria`
--

CREATE TABLE `convocatoria` (
  `id_convocatoria` int(11) NOT NULL,
  `nombre` varchar(25) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `estado` enum('en curso','concluida','por publicar') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_personal`
--

CREATE TABLE `detalle_personal` (
  `id_detalles_personales` int(11) NOT NULL,
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
-- Estructura de tabla para la tabla `etapa`
--

CREATE TABLE `etapa` (
  `id_etapa` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fase`
--

CREATE TABLE `fase` (
  `id_fase` int(11) NOT NULL,
  `id_etapa` int(11) DEFAULT NULL,
  `nombre` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `institucion`
--

CREATE TABLE `institucion` (
  `id_institucion` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `item_rubrica`
--

CREATE TABLE `item_rubrica` (
  `id_item_rubrica` int(11) NOT NULL,
  `id_rubrica` int(11) DEFAULT NULL,
  `componente` text DEFAULT NULL,
  `valor_max` float(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modalidad`
--

CREATE TABLE `modalidad` (
  `id_modalidad` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulo`
--

CREATE TABLE `modulo` (
  `id_modulo` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participante_proyecto`
--

CREATE TABLE `participante_proyecto` (
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
-- Estructura de tabla para la tabla `postulacion_evaluadores`
--

CREATE TABLE `postulacion_evaluadores` (
  `id_convocatoria` int(11) NOT NULL,
  `id_evaluador` int(11) NOT NULL,
  `etapa_virtual` tinyint(4) DEFAULT 0,
  `etapa_presencial` tinyint(4) DEFAULT 0,
  `jornada_manana` tinyint(4) DEFAULT 0,
  `jornada_tarde` tinyint(4) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programacion_fase`
--

CREATE TABLE `programacion_fase` (
  `id_programacion_fase` int(11) NOT NULL,
  `id_fase` int(11) DEFAULT NULL,
  `id_convocatoria` int(11) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
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
-- Estructura de tabla para la tabla `proyecto_convocatoria`
--

CREATE TABLE `proyecto_convocatoria` (
  `id_proyecto_convocatoria` int(11) NOT NULL,
  `id_proyecto` int(11) DEFAULT NULL,
  `id_convocatoria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `respuestas_rubrica`
--

CREATE TABLE `respuestas_rubrica` (
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
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id_rol` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rubrica`
--

CREATE TABLE `rubrica` (
  `id_rubrica` int(11) NOT NULL,
  `titulo` varchar(40) DEFAULT NULL,
  `id_etapa` int(11) DEFAULT NULL,
  `id_modalidad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rubrica_resultado`
--

CREATE TABLE `rubrica_resultado` (
  `id_rubrica_resultado` int(11) NOT NULL,
  `puntaje_aprobacion` float(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sala`
--

CREATE TABLE `sala` (
  `id_sala` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `area_conocimiento` int(11) DEFAULT NULL,
  `numero_sala` varchar(25) DEFAULT NULL,
  `nombre_sala` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sala_asignada`
--

CREATE TABLE `sala_asignada` (
  `id_sala` int(11) NOT NULL,
  `id_proyecto_convocatoria` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_documento`
--

CREATE TABLE `tipo_documento` (
  `id_tipo_documento` int(11) NOT NULL,
  `nombre` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `titulos_academicos`
--

CREATE TABLE `titulos_academicos` (
  `id_titulos_academicos` int(11) NOT NULL,
  `nivel` enum('pregrado','maestria','especializacion','doctorado') NOT NULL,
  `nombre_titulo` varchar(80) NOT NULL,
  `url_titulo` varchar(255) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
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
-- Indices de la tabla `area_conocimiento`
--
ALTER TABLE `area_conocimiento`
  ADD PRIMARY KEY (`id_area_conocimiento`);

--
-- Indices de la tabla `asistentes`
--
ALTER TABLE `asistentes`
  ADD PRIMARY KEY (`id_asistente`),
  ADD KEY `id_detalles_personales` (`id_detalles_personales`);

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`id_autor`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- Indices de la tabla `convocatoria`
--
ALTER TABLE `convocatoria`
  ADD PRIMARY KEY (`id_convocatoria`);

--
-- Indices de la tabla `detalle_personal`
--
ALTER TABLE `detalle_personal`
  ADD PRIMARY KEY (`id_detalles_personales`),
  ADD UNIQUE KEY `documento` (`documento`),
  ADD UNIQUE KEY `celular` (`celular`),
  ADD KEY `id_tipo_documento` (`id_tipo_documento`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_institucion` (`id_institucion`);

--
-- Indices de la tabla `etapa`
--
ALTER TABLE `etapa`
  ADD PRIMARY KEY (`id_etapa`);

--
-- Indices de la tabla `fase`
--
ALTER TABLE `fase`
  ADD PRIMARY KEY (`id_fase`),
  ADD KEY `id_etapa` (`id_etapa`);

--
-- Indices de la tabla `institucion`
--
ALTER TABLE `institucion`
  ADD PRIMARY KEY (`id_institucion`);

--
-- Indices de la tabla `item_rubrica`
--
ALTER TABLE `item_rubrica`
  ADD PRIMARY KEY (`id_item_rubrica`),
  ADD KEY `id_rubrica` (`id_rubrica`);

--
-- Indices de la tabla `modalidad`
--
ALTER TABLE `modalidad`
  ADD PRIMARY KEY (`id_modalidad`);

--
-- Indices de la tabla `modulo`
--
ALTER TABLE `modulo`
  ADD PRIMARY KEY (`id_modulo`);

--
-- Indices de la tabla `participante_proyecto`
--
ALTER TABLE `participante_proyecto`
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
-- Indices de la tabla `postulacion_evaluadores`
--
ALTER TABLE `postulacion_evaluadores`
  ADD PRIMARY KEY (`id_convocatoria`,`id_evaluador`),
  ADD KEY `id_evaluador` (`id_evaluador`);

--
-- Indices de la tabla `programacion_fase`
--
ALTER TABLE `programacion_fase`
  ADD PRIMARY KEY (`id_programacion_fase`),
  ADD KEY `id_fase` (`id_fase`),
  ADD KEY `id_convocatoria` (`id_convocatoria`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`id_proyecto`),
  ADD KEY `id_institucion` (`id_institucion`),
  ADD KEY `id_modalidad` (`id_modalidad`),
  ADD KEY `id_area_conocimiento` (`id_area_conocimiento`);

--
-- Indices de la tabla `proyecto_convocatoria`
--
ALTER TABLE `proyecto_convocatoria`
  ADD PRIMARY KEY (`id_proyecto_convocatoria`),
  ADD KEY `id_proyecto` (`id_proyecto`),
  ADD KEY `id_convocatoria` (`id_convocatoria`);

--
-- Indices de la tabla `respuestas_rubrica`
--
ALTER TABLE `respuestas_rubrica`
  ADD PRIMARY KEY (`id_respuestas_rubrica`),
  ADD KEY `id_item_rubrica` (`id_item_rubrica`),
  ADD KEY `id_rubrica_resultado` (`id_rubrica_resultado`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_proyecto_convocatoria` (`id_proyecto_convocatoria`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `rubrica`
--
ALTER TABLE `rubrica`
  ADD PRIMARY KEY (`id_rubrica`),
  ADD KEY `id_etapa` (`id_etapa`),
  ADD KEY `id_modalidad` (`id_modalidad`);

--
-- Indices de la tabla `rubrica_resultado`
--
ALTER TABLE `rubrica_resultado`
  ADD PRIMARY KEY (`id_rubrica_resultado`);

--
-- Indices de la tabla `sala`
--
ALTER TABLE `sala`
  ADD PRIMARY KEY (`id_sala`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `area_conocimiento` (`area_conocimiento`);

--
-- Indices de la tabla `sala_asignada`
--
ALTER TABLE `sala_asignada`
  ADD PRIMARY KEY (`id_sala`,`id_proyecto_convocatoria`),
  ADD KEY `id_proyecto_convocatoria` (`id_proyecto_convocatoria`);

--
-- Indices de la tabla `tipo_documento`
--
ALTER TABLE `tipo_documento`
  ADD PRIMARY KEY (`id_tipo_documento`);

--
-- Indices de la tabla `titulos_academicos`
--
ALTER TABLE `titulos_academicos`
  ADD PRIMARY KEY (`id_titulos_academicos`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD KEY `id_rol` (`id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `area_conocimiento`
--
ALTER TABLE `area_conocimiento`
  MODIFY `id_area_conocimiento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `asistentes`
--
ALTER TABLE `asistentes`
  MODIFY `id_asistente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `id_autor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `convocatoria`
--
ALTER TABLE `convocatoria`
  MODIFY `id_convocatoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_personal`
--
ALTER TABLE `detalle_personal`
  MODIFY `id_detalles_personales` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `etapa`
--
ALTER TABLE `etapa`
  MODIFY `id_etapa` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `fase`
--
ALTER TABLE `fase`
  MODIFY `id_fase` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `institucion`
--
ALTER TABLE `institucion`
  MODIFY `id_institucion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `item_rubrica`
--
ALTER TABLE `item_rubrica`
  MODIFY `id_item_rubrica` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modalidad`
--
ALTER TABLE `modalidad`
  MODIFY `id_modalidad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulo`
--
ALTER TABLE `modulo`
  MODIFY `id_modulo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `participante_proyecto`
--
ALTER TABLE `participante_proyecto`
  MODIFY `id_participante_proyecto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id_modulo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `programacion_fase`
--
ALTER TABLE `programacion_fase`
  MODIFY `id_programacion_fase` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proyecto_convocatoria`
--
ALTER TABLE `proyecto_convocatoria`
  MODIFY `id_proyecto_convocatoria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `respuestas_rubrica`
--
ALTER TABLE `respuestas_rubrica`
  MODIFY `id_respuestas_rubrica` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rubrica`
--
ALTER TABLE `rubrica`
  MODIFY `id_rubrica` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rubrica_resultado`
--
ALTER TABLE `rubrica_resultado`
  MODIFY `id_rubrica_resultado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `sala`
--
ALTER TABLE `sala`
  MODIFY `id_sala` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_documento`
--
ALTER TABLE `tipo_documento`
  MODIFY `id_tipo_documento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `titulos_academicos`
--
ALTER TABLE `titulos_academicos`
  MODIFY `id_titulos_academicos` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistentes`
--
ALTER TABLE `asistentes`
  ADD CONSTRAINT `asistentes_ibfk_1` FOREIGN KEY (`id_detalles_personales`) REFERENCES `detalle_personal` (`id_detalles_personales`);

--
-- Filtros para la tabla `autor`
--
ALTER TABLE `autor`
  ADD CONSTRAINT `autor_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id_proyecto`);

--
-- Filtros para la tabla `detalle_personal`
--
ALTER TABLE `detalle_personal`
  ADD CONSTRAINT `detalle_personal_ibfk_1` FOREIGN KEY (`id_tipo_documento`) REFERENCES `tipo_documento` (`id_tipo_documento`),
  ADD CONSTRAINT `detalle_personal_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  ADD CONSTRAINT `detalle_personal_ibfk_3` FOREIGN KEY (`id_institucion`) REFERENCES `institucion` (`id_institucion`);

--
-- Filtros para la tabla `fase`
--
ALTER TABLE `fase`
  ADD CONSTRAINT `fase_ibfk_1` FOREIGN KEY (`id_etapa`) REFERENCES `etapa` (`id_etapa`);

--
-- Filtros para la tabla `item_rubrica`
--
ALTER TABLE `item_rubrica`
  ADD CONSTRAINT `item_rubrica_ibfk_1` FOREIGN KEY (`id_rubrica`) REFERENCES `rubrica` (`id_rubrica`);

--
-- Filtros para la tabla `participante_proyecto`
--
ALTER TABLE `participante_proyecto`
  ADD CONSTRAINT `participante_proyecto_ibfk_1` FOREIGN KEY (`id_datos_personales`) REFERENCES `detalle_personal` (`id_detalles_personales`),
  ADD CONSTRAINT `participante_proyecto_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id_proyecto`),
  ADD CONSTRAINT `participante_proyecto_ibfk_3` FOREIGN KEY (`id_etapa`) REFERENCES `etapa` (`id_etapa`),
  ADD CONSTRAINT `participante_proyecto_ibfk_4` FOREIGN KEY (`id_proyecto_convocatoria`) REFERENCES `proyecto_convocatoria` (`id_proyecto_convocatoria`);

--
-- Filtros para la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD CONSTRAINT `permisos_ibfk_1` FOREIGN KEY (`id_modulo`) REFERENCES `modulo` (`id_modulo`),
  ADD CONSTRAINT `permisos_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`);

--
-- Filtros para la tabla `postulacion_evaluadores`
--
ALTER TABLE `postulacion_evaluadores`
  ADD CONSTRAINT `postulacion_evaluadores_ibfk_1` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatoria` (`id_convocatoria`),
  ADD CONSTRAINT `postulacion_evaluadores_ibfk_2` FOREIGN KEY (`id_evaluador`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `programacion_fase`
--
ALTER TABLE `programacion_fase`
  ADD CONSTRAINT `programacion_fase_ibfk_1` FOREIGN KEY (`id_fase`) REFERENCES `fase` (`id_fase`),
  ADD CONSTRAINT `programacion_fase_ibfk_2` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatoria` (`id_convocatoria`);

--
-- Filtros para la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD CONSTRAINT `proyecto_ibfk_1` FOREIGN KEY (`id_institucion`) REFERENCES `institucion` (`id_institucion`),
  ADD CONSTRAINT `proyecto_ibfk_2` FOREIGN KEY (`id_modalidad`) REFERENCES `modalidad` (`id_modalidad`),
  ADD CONSTRAINT `proyecto_ibfk_3` FOREIGN KEY (`id_area_conocimiento`) REFERENCES `area_conocimiento` (`id_area_conocimiento`);

--
-- Filtros para la tabla `proyecto_convocatoria`
--
ALTER TABLE `proyecto_convocatoria`
  ADD CONSTRAINT `proyecto_convocatoria_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id_proyecto`),
  ADD CONSTRAINT `proyecto_convocatoria_ibfk_2` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatoria` (`id_convocatoria`);

--
-- Filtros para la tabla `respuestas_rubrica`
--
ALTER TABLE `respuestas_rubrica`
  ADD CONSTRAINT `respuestas_rubrica_ibfk_1` FOREIGN KEY (`id_item_rubrica`) REFERENCES `item_rubrica` (`id_item_rubrica`),
  ADD CONSTRAINT `respuestas_rubrica_ibfk_2` FOREIGN KEY (`id_rubrica_resultado`) REFERENCES `rubrica_resultado` (`id_rubrica_resultado`),
  ADD CONSTRAINT `respuestas_rubrica_ibfk_3` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  ADD CONSTRAINT `respuestas_rubrica_ibfk_4` FOREIGN KEY (`id_proyecto_convocatoria`) REFERENCES `proyecto_convocatoria` (`id_proyecto_convocatoria`);

--
-- Filtros para la tabla `rubrica`
--
ALTER TABLE `rubrica`
  ADD CONSTRAINT `rubrica_ibfk_1` FOREIGN KEY (`id_etapa`) REFERENCES `etapa` (`id_etapa`),
  ADD CONSTRAINT `rubrica_ibfk_2` FOREIGN KEY (`id_modalidad`) REFERENCES `modalidad` (`id_modalidad`);

--
-- Filtros para la tabla `sala`
--
ALTER TABLE `sala`
  ADD CONSTRAINT `sala_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  ADD CONSTRAINT `sala_ibfk_2` FOREIGN KEY (`area_conocimiento`) REFERENCES `area_conocimiento` (`id_area_conocimiento`);

--
-- Filtros para la tabla `sala_asignada`
--
ALTER TABLE `sala_asignada`
  ADD CONSTRAINT `sala_asignada_ibfk_1` FOREIGN KEY (`id_sala`) REFERENCES `sala` (`id_sala`),
  ADD CONSTRAINT `sala_asignada_ibfk_2` FOREIGN KEY (`id_proyecto_convocatoria`) REFERENCES `proyecto_convocatoria` (`id_proyecto_convocatoria`);

--
-- Filtros para la tabla `titulos_academicos`
--
ALTER TABLE `titulos_academicos`
  ADD CONSTRAINT `titulos_academicos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
