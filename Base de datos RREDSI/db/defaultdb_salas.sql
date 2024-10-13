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
-- Table structure for table `salas`
--

DROP TABLE IF EXISTS `salas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salas` (
  `id_sala` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `id_area_conocimiento` int DEFAULT NULL,
  `id_convocatoria` int DEFAULT NULL,
  `numero_sala` varchar(25) DEFAULT NULL,
  `nombre_sala` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_sala`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_area_conocimiento` (`id_area_conocimiento`),
  KEY `id_convocatoria` (`id_convocatoria`),
  CONSTRAINT `salas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `salas_ibfk_2` FOREIGN KEY (`id_area_conocimiento`) REFERENCES `areas_conocimiento` (`id_area_conocimiento`),
  CONSTRAINT `salas_ibfk_3` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatorias` (`id_convocatoria`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salas`
--

LOCK TABLES `salas` WRITE;
/*!40000 ALTER TABLE `salas` DISABLE KEYS */;
INSERT INTO `salas` VALUES (1,415621,3,1,'236','ideagero'),(6,557550,3,1,'99','Sala de ciencias sociales.'),(22,979779,1,1,'100','Sala de Tecnología'),(24,968758,3,1,'305','Sala de Gestión'),(25,596937,3,1,'356','Agro'),(28,584219,1,1,'110','nueva sala'),(41,896895,20,1,'524','SenaSOFT'),(42,979779,1,1,'108','Math'),(43,557550,2,1,'400','Física'),(44,979779,1,1,'403','Math'),(45,655438,2,1,'257','Nueva sala');
/*!40000 ALTER TABLE `salas` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:54:27
