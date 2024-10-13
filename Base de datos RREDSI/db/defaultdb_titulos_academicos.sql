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
-- Table structure for table `titulos_academicos`
--

DROP TABLE IF EXISTS `titulos_academicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `titulos_academicos` (
  `id_titulo_academico` int NOT NULL AUTO_INCREMENT,
  `nivel` enum('pregrado','maestria','especializacion','doctorado') NOT NULL,
  `nombre_titulo` varchar(80) NOT NULL,
  `url_titulo` varchar(255) NOT NULL,
  `id_usuario` int NOT NULL,
  PRIMARY KEY (`id_titulo_academico`),
  KEY `titulos_academicos_ibfk_1` (`id_usuario`),
  CONSTRAINT `titulos_academicos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `titulos_academicos`
--

LOCK TABLES `titulos_academicos` WRITE;
/*!40000 ALTER TABLE `titulos_academicos` DISABLE KEYS */;
INSERT INTO `titulos_academicos` VALUES (6,'pregrado','Ingeniero en Sistemas','https://colaboracion.dnp.gov.co/CDTI/Oficina%20Informatica/Sistemas%20de%20informaci%C3%B3n/Gu%C3%ADas%20Formatos%20Plantillas/Gu%C3%ADa%20para%20la%20Elaboraci%C3%B3n%20del%20Manual%20del%20Usuario%20del%20Sistema.pdf?',979762),(9,'especializacion','Especialista en Gerencia de Proyectos','https://titulos.com/gerencia_proyectos',979762),(10,'pregrado','Licenciado en Matemáticas','https://titulos.com/licenciatura_matematicas',979763),(11,'maestria','Maestría en Inteligencia Artificial','https://titulos.com/inteligencia_artificial',979763),(12,'pregrado','Ingeniero Fisico','https://titulos.com/fisica_teorica',979764),(13,'pregrado','Administrador de Empresas','https://titulos.com/administracion_empresas',979765),(14,'pregrado','Ingeniería Mecanica','https://titulos.com/mecanica',979766),(15,'pregrado','Licenciatura en Informática','https://titulos.com/informatica',979770),(16,'pregrado','Ingeniería Ambiental','https://titulos.com/ingenieria_ambiental',979771),(17,'pregrado','Ingeniería Civil','https://titulos.com/ingenieria_civil',979772),(18,'pregrado','Arquitectura','https://titulos.com/arquitectura',979776),(19,'pregrado','Licenciatura en Física','https://titulos.com/licenciatura_fisica',979777),(20,'pregrado','Ingeniería en Electrónica','https://titulos.com/ingenieria_electronica',979778),(22,'doctorado','Doctorado en Ingeniería','http://example.com/titulo557550.pdf',557550),(23,'especializacion','Especialización en Gestión de Proyectos','http://example.com/titulo979779.pdf',979779),(24,'pregrado','Ingeniero Electricista','https://noesis.uis.edu.co/server/api/core/bitstreams/dfa93f13-602b-459b-a962-5020b880d4a3/content',52760),(25,'pregrado','Administrador de Empresas','https://noesis.uis.edu.co/server/api/core/bitstreams/dfa93f13-602b-459b-a962-5020b880d4a3/content',961804),(26,'pregrado','Ingeniero Civil','https://noesis.uis.edu.co/server/api/core/bitstreams/dfa93f13-602b-459b-a962-5020b880d4a3/content',962846),(27,'pregrado','Ingeniería Eléctrica','https://colaboracion.dnp.gov.co/CDTI/Oficina%20Informatica/Sistemas%20de%20informaci%C3%B3n/Gu%C3%ADas%20Formatos%20Plantillas/Gu%C3%ADa%20para%20la%20Elaboraci%C3%B3n%20del%20Manual%20del%20Usuario%20del%20Sistema.pdf?',415621),(28,'pregrado','Ingeniero Electricista','https://colaboracion.dnp.gov.co/CDTI/Oficina%20Informatica/Sistemas%20de%20informaci%C3%B3n/Gu%C3%ADas%20Formatos%20Plantillas/Gu%C3%ADa%20para%20la%20Elaboraci%C3%B3n%20del%20Manual%20del%20Usuario%20del%20Sistema.pdf?',725812),(29,'doctorado','Doctorado en Ingeniería','https://noesis.uis.edu.co/server/api/core/bitstreams/dfa93f13-602b-459b-a962-5020b880d4a3/content',123654);
/*!40000 ALTER TABLE `titulos_academicos` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:58:14
