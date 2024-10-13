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
-- Table structure for table `asistentes`
--

DROP TABLE IF EXISTS `asistentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asistentes` (
  `id_asistente` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `asistencia` tinyint DEFAULT '0',
  `fecha` timestamp NULL DEFAULT NULL,
  `url_comprobante_pago` varchar(255) DEFAULT NULL,
  `id_convocatoria` int NOT NULL,
  PRIMARY KEY (`id_asistente`),
  KEY `id_usuario` (`id_usuario`),
  KEY `fk_id_convocatoria` (`id_convocatoria`),
  CONSTRAINT `asistentes_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `fk_id_convocatoria` FOREIGN KEY (`id_convocatoria`) REFERENCES `convocatorias` (`id_convocatoria`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistentes`
--

LOCK TABLES `asistentes` WRITE;
/*!40000 ALTER TABLE `asistentes` DISABLE KEYS */;
INSERT INTO `asistentes` VALUES (39,83791,0,'2024-09-01 10:00:00','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(40,415621,1,'2024-09-01 11:00:00','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(41,133686,1,'2024-09-01 12:00:00','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(42,725812,1,'2024-09-01 13:00:00','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(46,979783,0,'2024-09-17 11:28:52','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(47,979784,1,'2024-09-17 11:32:05','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(48,979785,1,'2024-09-17 11:32:22','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(49,979793,1,'2024-09-18 02:07:02','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(50,979798,1,'2024-09-27 16:31:30','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(51,979799,0,'2024-09-27 16:31:33','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(52,979800,0,'2024-09-27 16:31:35','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(53,979801,0,'2024-09-27 18:41:20','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(54,979801,0,'2024-09-27 18:45:02','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(55,979802,0,'2024-09-28 18:47:13','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(56,196723,0,'2024-10-02 14:20:51','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(57,511068,0,'2024-10-02 14:20:55','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1),(60,615313,0,'2024-10-12 18:17:50','https://getquipu.com/wp-content/uploads/2021/10/19125745/Modelo-Recibo-de-Pago-1.pdf',1);
/*!40000 ALTER TABLE `asistentes` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:54:02
