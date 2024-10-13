-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: mysql-24d415ec-diazricostephanie7-b9b4.c.aivencloud.com    Database: defaultdb
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '5a48c052-6577-11ef-97d4-0625cdb2278d:1-3164';

--
-- Table structure for table `postulaciones_evaluadores`
--

DROP TABLE IF EXISTS `postulaciones_evaluadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `postulaciones_evaluadores` (
  `id_convocatoria` int NOT NULL,
  `id_evaluador` int NOT NULL,
  `estado_postulacion` enum('pendiente','aceptada','rechazada') NOT NULL DEFAULT 'pendiente',
  `etapa_virtual` tinyint DEFAULT '0',
  `etapa_presencial` tinyint DEFAULT '0',
  `jornada_manana` tinyint DEFAULT '0',
  `jornada_tarde` tinyint DEFAULT '0',
  PRIMARY KEY (`id_convocatoria`,`id_evaluador`),
  KEY `id_evaluador` (`id_evaluador`),
  CONSTRAINT `postulaciones_evaluadores_ibfk_1` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatorias` (`id_convocatoria`),
  CONSTRAINT `postulaciones_evaluadores_ibfk_2` FOREIGN KEY (`id_evaluador`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postulaciones_evaluadores`
--

LOCK TABLES `postulaciones_evaluadores` WRITE;
/*!40000 ALTER TABLE `postulaciones_evaluadores` DISABLE KEYS */;
INSERT INTO `postulaciones_evaluadores` VALUES (1,52760,'pendiente',0,1,1,1),(1,123654,'pendiente',1,1,1,1),(1,423636,'pendiente',1,1,1,1),(1,725812,'pendiente',1,1,0,1),(1,825363,'pendiente',1,1,1,1),(1,961804,'pendiente',1,1,1,0),(1,962846,'pendiente',1,1,0,1),(1,979762,'pendiente',1,0,0,0),(1,979763,'aceptada',1,1,1,1),(1,979764,'pendiente',1,1,1,0),(1,979765,'pendiente',0,1,0,1),(1,979766,'pendiente',1,1,1,1),(1,979771,'rechazada',0,1,1,0),(1,979772,'rechazada',1,1,0,1),(1,979776,'rechazada',0,1,1,0),(1,979777,'rechazada',0,1,0,1),(1,979778,'aceptada',1,1,0,1),(2,979770,'rechazada',1,1,1,1);
/*!40000 ALTER TABLE `postulaciones_evaluadores` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-12 21:57:35
