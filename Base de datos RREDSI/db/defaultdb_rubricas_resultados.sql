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
-- Table structure for table `rubricas_resultados`
--

DROP TABLE IF EXISTS `rubricas_resultados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rubricas_resultados` (
  `id_rubrica_resultado` int NOT NULL AUTO_INCREMENT,
  `estado_proyecto` enum('aprobado','reprobado') DEFAULT NULL,
  `puntaje_aprobacion` float(4,1) DEFAULT NULL,
  PRIMARY KEY (`id_rubrica_resultado`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rubricas_resultados`
--

LOCK TABLES `rubricas_resultados` WRITE;
/*!40000 ALTER TABLE `rubricas_resultados` DISABLE KEYS */;
INSERT INTO `rubricas_resultados` VALUES (1,'reprobado',7.5),(2,'aprobado',8.0),(3,'aprobado',100.0),(4,'reprobado',73.8),(5,'reprobado',69.0),(6,'reprobado',46.0),(7,'aprobado',85.9),(8,'reprobado',22.0),(9,'reprobado',20.0),(13,'reprobado',46.0),(14,'aprobado',100.0),(15,'aprobado',100.0),(16,'reprobado',30.0),(17,'aprobado',95.0),(18,'reprobado',67.0),(19,'aprobado',100.0),(20,'aprobado',79.0),(21,'aprobado',91.0),(22,'aprobado',100.0),(23,'aprobado',100.0),(24,'reprobado',54.0),(25,'reprobado',73.0),(26,'aprobado',100.0),(27,'reprobado',62.0),(28,'aprobado',100.0);
/*!40000 ALTER TABLE `rubricas_resultados` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:56:42
