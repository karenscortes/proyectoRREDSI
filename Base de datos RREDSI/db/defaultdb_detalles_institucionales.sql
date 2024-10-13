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

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '5a48c052-6577-11ef-97d4-0625cdb2278d:1-3163';

--
-- Table structure for table `detalles_institucionales`
--

DROP TABLE IF EXISTS `detalles_institucionales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles_institucionales` (
  `id_detalle_institucional` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_institucion` int DEFAULT NULL,
  `semillero` varchar(35) DEFAULT NULL,
  `grupo_investigacion` varchar(35) DEFAULT NULL,
  `id_primera_area_conocimiento` int DEFAULT NULL,
  `id_segunda_area_conocimiento` int DEFAULT NULL,
  PRIMARY KEY (`id_detalle_institucional`,`id_usuario`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_institucion` (`id_institucion`),
  KEY `id_primera_area_conocimiento` (`id_primera_area_conocimiento`),
  KEY `id_segunda_area_conocimiento` (`id_segunda_area_conocimiento`),
  CONSTRAINT `detalles_institucionales_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `detalles_institucionales_ibfk_2` FOREIGN KEY (`id_institucion`) REFERENCES `instituciones` (`id_institucion`),
  CONSTRAINT `detalles_institucionales_ibfk_3` FOREIGN KEY (`id_primera_area_conocimiento`) REFERENCES `areas_conocimiento` (`id_area_conocimiento`),
  CONSTRAINT `detalles_institucionales_ibfk_4` FOREIGN KEY (`id_segunda_area_conocimiento`) REFERENCES `areas_conocimiento` (`id_area_conocimiento`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles_institucionales`
--

LOCK TABLES `detalles_institucionales` WRITE;
/*!40000 ALTER TABLE `detalles_institucionales` DISABLE KEYS */;
INSERT INTO `detalles_institucionales` VALUES (2,557550,1,'Semillero B','Grupo B',1,2),(3,979779,1,'Semillero C','Grupo C',1,2),(5,691430,1,'Semillero de Tecnología','Grupo de Innovación',2,16),(11,979762,5,'Semillero de Robótica','Grupo de Automatización',10,15),(12,979763,7,'Semillero de Ciencias de Datos','Grupo de Big Data',8,12),(13,979764,9,'Semillero de IA','Grupo de IA Aplicada',5,14),(14,979765,3,'Semillero de Energías Renovables','Grupo de Energía Sostenible',3,7),(15,979766,4,'Semillero de Biotecnología','Grupo de Innovación Biotecnológica',2,6),(16,979770,2,'Semillero de Desarrollo Web','Grupo de Información',4,8),(17,979771,6,'Semillero de Blockchain','Grupo de Criptoactivos',9,13),(18,979772,8,'Semillero de Realidad Virtual','Grupo Inmersivo',7,11),(19,979776,1,'Semillero de Nanotecnología','Grupo de Materiales Avanzados',6,10),(20,979777,3,'Semillero de Ciberseguridad','Grupo de Seguridad Informática',12,18),(21,979778,5,'Semillero de Economía Digital','Grupo de Innovación Financiera',14,19),(62,83791,1,'Semillero A','Grupo Investigacion A',5,10),(63,415621,2,'Semillero B','Grupo Investigacion B',8,12),(64,133686,3,'Semillero C','Grupo Investigacion C',3,7),(65,725812,4,'Semillero D','Grupo Investigacion D',6,14),(69,123654,1,'Semillero de AGRO','Grupo de Gestión de Agropecuarios',1,3),(72,423636,1,'Semillero de Tecnología','Grupo de Innovación',1,2),(73,52760,1,'Semillero de Arquitectura','Grupo de Innovación',1,4),(74,961804,2,'Semillero de Gestion Empresarial','Grupo de Inteligencia de Negocios',3,5),(75,962846,3,'Semillero K','Grupo de Sociopatas',3,6),(77,825363,1,'Semillero de Tecnología','Grupo de Innovación',1,2),(92,744081,5,'Semillero de Tecnología','Grupo de Innovación',1,2);
/*!40000 ALTER TABLE `detalles_institucionales` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:54:33
