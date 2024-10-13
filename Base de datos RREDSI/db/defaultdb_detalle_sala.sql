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
-- Table structure for table `detalle_sala`
--

DROP TABLE IF EXISTS `detalle_sala`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_sala` (
  `id_sala` int NOT NULL,
  `id_proyecto_convocatoria` int NOT NULL,
  `fecha` date DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL,
  PRIMARY KEY (`id_sala`,`id_proyecto_convocatoria`),
  KEY `id_proyecto_convocatoria` (`id_proyecto_convocatoria`),
  CONSTRAINT `detalle_sala_ibfk_1` FOREIGN KEY (`id_sala`) REFERENCES `salas` (`id_sala`),
  CONSTRAINT `detalle_sala_ibfk_2` FOREIGN KEY (`id_proyecto_convocatoria`) REFERENCES `proyectos_convocatoria` (`id_proyecto_convocatoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_sala`
--

LOCK TABLES `detalle_sala` WRITE;
/*!40000 ALTER TABLE `detalle_sala` DISABLE KEYS */;
INSERT INTO `detalle_sala` VALUES (1,8,'2024-10-20','09:00:00','11:30:00'),(1,10,'2024-09-10','06:00:00','06:30:00'),(6,22,'2024-09-10','07:00:00','07:30:00'),(6,24,'2024-09-10','07:30:00','09:00:00'),(6,133,'2024-09-11','15:30:00','16:00:00'),(22,40,'2024-10-20','08:00:00','08:30:00'),(22,42,'2024-10-20','07:00:00','07:30:00'),(24,26,'2024-09-10','11:30:00','12:00:00'),(24,28,'2024-10-20','12:00:00','12:30:00'),(24,134,'2024-09-11','07:00:00','07:30:00'),(24,135,'2024-09-11','07:30:00','08:00:00'),(25,30,'2024-09-11','12:30:00','13:00:00'),(25,34,'2024-09-11','13:00:00','13:30:00'),(25,136,'2024-09-11','08:00:00','08:30:00'),(25,137,'2024-09-11','17:00:00','17:30:00'),(28,36,'2024-09-11','13:30:00','14:00:00'),(28,38,'2024-09-11','14:00:00','14:30:00'),(41,44,'2024-09-11','14:30:00','15:00:00');
/*!40000 ALTER TABLE `detalle_sala` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:56:26
