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
-- Table structure for table `participantes_proyecto`
--

DROP TABLE IF EXISTS `participantes_proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `participantes_proyecto` (
  `id_participante_proyecto` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `id_etapa` int DEFAULT NULL,
  `id_proyecto` int DEFAULT NULL,
  `id_proyectos_convocatoria` int DEFAULT NULL,
  `tipo_usuario` enum('evaluador','suplenteEvaluador','ponente','suplentePonente','tutor') DEFAULT NULL,
  PRIMARY KEY (`id_participante_proyecto`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_etapa` (`id_etapa`),
  KEY `id_proyectos_convocatoria` (`id_proyectos_convocatoria`),
  KEY `participantes_proyecto_ibfk_3` (`id_proyecto`),
  CONSTRAINT `participantes_proyecto_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `participantes_proyecto_ibfk_2` FOREIGN KEY (`id_etapa`) REFERENCES `etapas` (`id_etapa`),
  CONSTRAINT `participantes_proyecto_ibfk_3` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`),
  CONSTRAINT `participantes_proyecto_ibfk_4` FOREIGN KEY (`id_proyectos_convocatoria`) REFERENCES `proyectos_convocatoria` (`id_proyecto_convocatoria`)
) ENGINE=InnoDB AUTO_INCREMENT=213 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participantes_proyecto`
--

LOCK TABLES `participantes_proyecto` WRITE;
/*!40000 ALTER TABLE `participantes_proyecto` DISABLE KEYS */;
INSERT INTO `participantes_proyecto` VALUES (8,83791,1,3,10,NULL),(9,415621,2,3,10,NULL),(10,133686,2,4,11,NULL),(11,725812,2,4,11,NULL),(12,83791,1,3,10,NULL),(13,415621,2,3,10,NULL),(14,133686,2,4,11,NULL),(15,415621,2,4,11,NULL),(16,725812,1,101,22,NULL),(17,725812,2,102,23,NULL),(18,725812,1,103,24,NULL),(19,725812,2,104,25,NULL),(20,725812,1,105,26,NULL),(21,725812,2,106,27,NULL),(22,725812,1,107,28,NULL),(23,725812,2,108,29,NULL),(24,725812,1,109,30,NULL),(25,725812,2,110,31,NULL),(27,725812,2,112,33,NULL),(28,725812,1,113,34,NULL),(29,725812,2,114,35,NULL),(30,725812,1,115,36,NULL),(31,725812,2,116,37,NULL),(32,725812,1,117,38,NULL),(33,725812,2,118,39,NULL),(34,725812,1,119,40,NULL),(35,725812,2,120,41,NULL),(36,725812,1,121,42,NULL),(37,725812,2,122,43,NULL),(38,725812,1,123,44,NULL),(39,725812,2,124,45,NULL),(43,979779,2,120,45,NULL),(44,979779,2,120,45,NULL),(45,979779,2,120,45,NULL),(48,123654,1,121,42,NULL),(49,123654,1,101,22,NULL),(50,123654,1,105,26,NULL),(51,123654,1,107,28,NULL),(52,123654,1,109,30,NULL),(53,123654,2,121,42,NULL),(54,123654,2,125,133,NULL),(57,123654,1,125,133,NULL),(96,725812,2,4,11,NULL),(98,979762,2,5,12,NULL),(99,725812,2,109,30,NULL),(101,825363,2,9,16,NULL),(102,123654,2,126,134,NULL),(103,725812,1,126,134,NULL),(104,744081,1,126,134,NULL),(105,725812,2,128,136,NULL),(106,744081,2,127,135,NULL),(107,725812,1,128,136,NULL),(108,744081,1,128,136,NULL),(132,123654,1,113,34,NULL),(133,123654,1,123,44,NULL),(141,123654,2,129,137,NULL),(142,979788,2,129,137,NULL),(143,979789,2,129,137,NULL),(144,123654,1,129,137,NULL),(145,725812,1,129,137,NULL),(146,725812,2,130,138,NULL),(147,979789,2,130,138,NULL),(148,979788,2,130,138,NULL),(178,979785,1,125,133,'suplentePonente'),(179,133686,1,125,133,'suplentePonente'),(180,133686,1,128,136,'suplenteEvaluador'),(212,979793,1,129,137,'suplenteEvaluador');
/*!40000 ALTER TABLE `participantes_proyecto` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:54:57
