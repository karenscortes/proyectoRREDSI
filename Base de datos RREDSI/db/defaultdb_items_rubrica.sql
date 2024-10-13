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
-- Table structure for table `items_rubrica`
--

DROP TABLE IF EXISTS `items_rubrica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items_rubrica` (
  `id_item_rubrica` int NOT NULL AUTO_INCREMENT,
  `id_rubrica` int DEFAULT NULL,
  `titulo` varchar(50) DEFAULT NULL,
  `componente` text,
  `valor_max` float(3,1) DEFAULT NULL,
  `estado` enum('activo','inactivo') NOT NULL DEFAULT 'activo',
  PRIMARY KEY (`id_item_rubrica`),
  KEY `id_rubrica` (`id_rubrica`),
  CONSTRAINT `items_rubrica_ibfk_1` FOREIGN KEY (`id_rubrica`) REFERENCES `rubricas` (`id_rubrica`)
) ENGINE=InnoDB AUTO_INCREMENT=234 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items_rubrica`
--

LOCK TABLES `items_rubrica` WRITE;
/*!40000 ALTER TABLE `items_rubrica` DISABLE KEYS */;
INSERT INTO `items_rubrica` VALUES (142,3,'Título','Nombre del proyecto e imagen alusiva.',5.0,'activo'),(143,3,'Resumen','Debe contener una exposición clara y concisa de la propuesta de investigación (máximo 120 palabras) y Palabras Claves.',5.0,'activo'),(144,3,'Problema y Justificación','Planteamiento, formulación de la pregunta, justificación del problema.',10.0,'activo'),(145,3,'Referente Teórico','Mínimo dos autores con una pequeña contextualización del aporte teórico a la propuesta de investigación.',10.0,'activo'),(146,3,'Objetivos','Precisos y coherentes con el problema.',10.0,'activo'),(147,3,'Metodología','Coherencia con marco teórico y referencial. Deben estar todas las referencias en el texto. ',15.0,'activo'),(148,3,'Resultados esperados: ','productos de investigación o pertinencia de los resultados esperados con los objetivos propuestos.',15.0,'activo'),(149,3,'Impactos','Social, económico y ambiental.',10.0,'activo'),(150,3,'Diseño','Calidad y pertinencia.',10.0,'activo'),(151,3,'Bibliografía','Coherencia con marco teórico y referencial. Deben estar todas las referencias en el texto.',10.0,'activo'),(152,4,'Coherencia','Claridad y coherencia entre los diferentes puntos de la propuesta.',10.0,'activo'),(153,4,'Título','Es coherente con el contenido desarrollado.',5.0,'activo'),(154,4,'Resumen y Palabras Claves','',5.0,'activo'),(155,4,'Problema y Justificación','Planteamiento, formulación de la pregunta, justificación del problema.',15.0,'activo'),(156,4,'Objetivos','Precisos y coherentes con el problema.',10.0,'activo'),(157,4,'Referente teórico','Acorde con la temática y está construido de acuerdo a documentos de referencia en la materia.',15.0,'activo'),(158,4,'Metodología','Especifica el Tipo de investigación, presenta de manera clara la metodología que se está empleando para lograr los objetivos planteados.',10.0,'activo'),(159,4,'Avances de los resultados','Los datos parciales recolectados son pertinentes con los objetivos de la investigación',10.0,'activo'),(160,4,'Impactos','Social, económico y ambiental.',10.0,'activo'),(161,4,'Bibliografía','Se presentan referencias bibliográficas pertinentes y actualizadas relacionadas directamente con la temática de investigación.',10.0,'activo'),(163,5,'Coherencia','Claridad y coherencia entre los diferentes puntos de la propuesta.',10.0,'activo'),(164,5,'Título','Es coherente con el contenido desarrollado.',5.0,'activo'),(165,5,'Resumen y Palabras Claves','',5.0,'activo'),(166,5,'Problema y Justificación','Planteamiento, formulación de la pregunta, justificación del problema.',10.0,'activo'),(167,5,'Objetivos','Precisos y coherentes con el problema.',10.0,'activo'),(168,5,'Referente teórico','Acorde con la temática y está construido de acuerdo a documentos de referencia en la materia.',10.0,'activo'),(169,5,'Metodología','Especifica el Tipo de investigación, presenta de manera clara la metodología que se está empleando para lograr los objetivos planteados.',10.0,'activo'),(170,5,'Avances de los resultados','Los datos parciales recolectados son pertinentes con los objetivos de la investigación',10.0,'activo'),(171,5,'Impactos','Social, económico y ambiental.',5.0,'activo'),(172,5,'Bibliografía','Se presentan referencias bibliográficas pertinentes y actualizadas relacionadas directamente con la temática de investigación.',5.0,'activo'),(173,5,'Dominio temático','El ponente muestra Seguridad y conocimiento sobre el tema que trabaja',5.0,'activo'),(174,5,'Conversatorio y conclusiones de la sala','se resaltan las posibles alianzas o redes que se pueden tejer entre los participantes a partir de punto de interés comunes.',15.0,'activo'),(175,6,'Coherencia','Claridad y coherencia entre los diferentes puntos de la propuesta.',10.0,'activo'),(176,6,'Título','Es coherente con el contenido desarrollado.',5.0,'activo'),(177,6,'Resumen y Palabras Claves','',5.0,'activo'),(178,6,'Problema y Justificación','Planteamiento, formulación de la pregunta, justificación del problema.',10.0,'activo'),(179,6,'Objetivos','Precisos y coherentes con el problema.',10.0,'activo'),(180,6,'Referente teórico','Acorde con la temática y está construido de acuerdo a documentos de referencia en la materia.',10.0,'activo'),(181,6,'Metodología','Especifica el Tipo de investigación, presenta de manera clara la metodología que se está empleando para lograr los objetivos planteados.',10.0,'activo'),(182,6,'Resultados y discusión','Coherencia. Presenta de manera clara el análisis de los hallazgos obtenidos. El desarrollo del trabajo y sus resultados responden a los objetivos planteados.',5.0,'activo'),(183,6,'Impactos','Social, económico y ambiental.',5.0,'activo'),(184,6,'Conclusiones','Descripción precisa de los aspectos más relevantes obtenidos en la investigación.',5.0,'activo'),(185,6,'Bibliografía','Se presentan referencias bibliográficas pertinentes y actualizadas relacionadas directamente con la temática de investigación.',5.0,'activo'),(186,6,'Dominio temático','El ponente muestra Seguridad y conocimiento sobre el tema que trabaja',5.0,'activo'),(187,6,'Conversatorio y conclusiones de la sala','se resaltan las posibles alianzas o redes que se pueden tejer entre los participantes a partir de punto de interés comunes.',15.0,'activo'),(201,1,'Título','Nombre del proyecto e imagen alusiva.',6.0,'activo'),(202,1,'Resumen','Debe contener una exposición clara y concisa de la propuesta de investigación (mo 120 palabras) y Palabras Claves. ',5.0,'activo'),(203,1,'Problema y Justificación','Planteamiento, formulación de la pregunta, justificación del problema...',10.0,'activo'),(204,1,'Referente Teórico','Mínimo dos autores con una pequeña contextualización del aporte teórico a la propuesta de investigación.',10.0,'activo'),(205,1,'Objetivos','Precisos y coherentes con el problema.',10.0,'activo'),(206,1,'Metodología','Tipo de investigación e instrumentos de recolección.',15.0,'activo'),(207,1,'Resultados esperados','productos de investigación o pertinencia de los resultados esperados con los objetivos propuestos.',15.0,'activo'),(208,1,'Impactos','Social, económico y ambiental',10.0,'activo'),(209,1,'Diseño','Calidad y pertinencia.',10.0,'activo'),(210,1,'Bibliografía','Coherencia con marco teórico y referencial. Deben estar todas las referencias en el texto.',10.0,'activo'),(219,2,'Coherencia','Claridad y coherencia entre los diferentes puntos de la propuesta.',10.0,'activo'),(220,2,'Título','Es coherente con el contenido desarrollado.',5.0,'activo'),(221,2,'Resumen y Palabras Claves','',5.0,'activo'),(222,2,'Problema y Justificación','Planteamiento, formulación de la pregunta, justificación del problema.',10.0,'activo'),(223,2,'Objetivos','Precisos y coherentes con el problema.',10.0,'activo'),(224,2,'Referente teórico','Acorde con la temática y está construido de acuerdo a documentos de referencia en la materia.',10.0,'activo'),(225,2,'Metodología','Especifica el Tipo de investigación, presenta de manera clara la metodología utilizada para lograr los objetivos planteados.',10.0,'activo'),(226,2,'Resultados y discusión','Coherencia. Presenta de manera clara el análisis de los hallazgos obtenidos. El desarrollo del trabajo y sus resultados responden a los objetivos planteados.',10.0,'activo'),(227,2,'Impactos','Social, económico y ambiental.',10.0,'activo'),(228,2,'Conclusiones','Descripción precisa de los aspectos más relevantes obtenidos en la investigación.',10.0,'activo'),(229,2,'Bibliografía','Se presentan referencias bibliográficas pertinentes y actualizadas relacionadas directamente con la temática de investigación.',10.0,'activo'),(230,1,'Prueba ','Esto es una prueba',1.0,'activo'),(231,1,'Prueba2','Esto una prueba 2 ',1.0,'inactivo'),(232,1,'Prueba2','Esto es otra prueba',5.0,'activo'),(233,1,'Prueba3','Esto es prueba 3.',5.0,'activo');
/*!40000 ALTER TABLE `items_rubrica` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:56:51
