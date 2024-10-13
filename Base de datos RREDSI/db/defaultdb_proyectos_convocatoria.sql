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
-- Table structure for table `proyectos_convocatoria`
--

DROP TABLE IF EXISTS `proyectos_convocatoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyectos_convocatoria` (
  `id_proyecto_convocatoria` int NOT NULL AUTO_INCREMENT,
  `id_proyecto` int DEFAULT NULL,
  `id_convocatoria` int DEFAULT NULL,
  PRIMARY KEY (`id_proyecto_convocatoria`),
  KEY `id_convocatoria` (`id_convocatoria`),
  KEY `proyectos_convocatoria_ibfk_1` (`id_proyecto`),
  CONSTRAINT `proyectos_convocatoria_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`),
  CONSTRAINT `proyectos_convocatoria_ibfk_2` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatorias` (`id_convocatoria`)
) ENGINE=InnoDB AUTO_INCREMENT=192 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyectos_convocatoria`
--

LOCK TABLES `proyectos_convocatoria` WRITE;
/*!40000 ALTER TABLE `proyectos_convocatoria` DISABLE KEYS */;
INSERT INTO `proyectos_convocatoria` VALUES (8,1,1),(9,2,2),(10,3,1),(11,4,1),(12,5,1),(13,6,1),(14,7,1),(15,8,1),(16,9,1),(17,10,1),(18,11,1),(19,12,1),(20,13,1),(21,14,1),(22,101,1),(23,102,1),(24,103,1),(25,104,1),(26,105,1),(27,106,1),(28,107,1),(29,108,1),(30,109,1),(31,110,1),(32,111,1),(33,112,1),(34,113,1),(35,114,1),(36,115,1),(37,116,1),(38,117,1),(39,118,1),(40,119,1),(41,120,1),(42,121,1),(43,122,1),(44,123,1),(45,124,1),(125,1,1),(126,2,1),(127,3,1),(128,4,1),(130,1,1),(131,124,1),(132,121,2),(133,125,1),(134,126,1),(135,127,1),(136,128,1),(137,129,1),(138,130,1);
/*!40000 ALTER TABLE `proyectos_convocatoria` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:55:21
