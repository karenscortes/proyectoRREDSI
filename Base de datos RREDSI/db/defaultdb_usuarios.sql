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
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `id_rol` int DEFAULT NULL,
  `id_tipo_documento` int DEFAULT NULL,
  `documento` varchar(55) NOT NULL,
  `nombres` varchar(25) DEFAULT NULL,
  `apellidos` varchar(25) DEFAULT NULL,
  `celular` varchar(12) NOT NULL,
  `correo` varchar(70) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `estado` enum('activo','inactivo') NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `documento` (`documento`),
  UNIQUE KEY `celular` (`celular`),
  UNIQUE KEY `correo` (`correo`),
  KEY `id_tipo_documento` (`id_tipo_documento`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_tipo_documento`) REFERENCES `tipos_documento` (`id_tipo_documento`),
  CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=998797 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (52760,1,2,'5000006','Celestine','Grayson','3045678901','celestine@example.com','$2b$12$3c/9cv6EhMc6YXJkf7M5Pen2FosOR998a5QLHjYLxi93poeiF3KpO','activo'),(78265,3,1,'6000006','Luis Carlos','Hernandez','302202215','miguelh@example.com','$2b$12$yqm6YwNdR36WHlA0Vjvnc.S1bMXfcNH0Uk5rxOqQyNbcVu9ctxr6W','activo'),(83791,3,2,'1234567','Luis','Marin','12345678787','luis@example.com','$2b$12$FQndrxxPLwLIeT4JPkHS/OFCYxiepG9vqmReE/X6cRpmrWAbpJECe','activo'),(123654,1,1,'5000003','Orion','Fitzgerald','30128','orion.fitzgerald@example.com','$2b$12$pA4z7gQ6LkB2Amqp/IZfyu/JpfzCp3FSXPAtAvzJSs2thrJIp1cyy','activo'),(133182,1,1,'1088258094','Miguel Ángel','Alzate Lozano','3008914563','miguelangel4817@gmail.com','$2b$12$SwABYgeUnrItS9FKNI5wbe8nM66GCHvasJnS7ORNnB.E/g3R8WV2G','activo'),(133686,1,1,'1232345','Juana','Gomez','23456','Juana@example.com','$2b$12$xy.rsKwvZEa1bTw/vweo4e.GJCXdjsTfYCHIX.lrM7ACkp7Pi1Moa','activo'),(186898,1,1,'123434654','eale','lastname','3214568796','examplr@gmail.com','$2b$12$TMcdH6JezySAjZUctMW3UeNhsYr.pCMiozg7DFSHTDUMUYmjcx02u','activo'),(196723,7,1,'985744','Elvis','Ramirez','3201000201','Elvira@example.com','$2b$12$1hD4ewSG2KbZ6U.FCIuzb.a/FUsrilXAZFcNCDxpS53jZ//0glIfy','inactivo'),(237216,3,1,'567890','Miguel','Cervantes','21135','miguelc@example.com','$2b$12$5ZM.S.okhzqTzBKyHti2zOLJIJmgj0iQ3oMvqXt.T//J8.J/nFGwa','activo'),(240303,3,1,'5000002','Isolde','MacArthur','30054321','isolde.macarthur@example.com','$2b$12$KinsvLWVwXEisyHY0xjg8u2.XQU2MPOPn5hRS.3h.JfAE7Ye7bUJK','activo'),(245056,2,1,'78769','Gregorio','Marin','323456656','Gregorio@gmail.com','$2b$12$IYt6MGCis36HNey/U/vAOupLsFYnW/gfT6gD26LVFL9dV0JrMhF1q','activo'),(258547,2,2,'1098','Juliana','Lopera','32565898','juli@gmail.com','$2b$12$j4i8Vr5SCykalzGxfBTcwuo6PM5M5iLmIisZJ5OcRgZKMJDyKQ8My','activo'),(275467,1,1,'852369','INTERFAZ','INTERFAZ','258963','interfaz@gmail.com','$2b$12$GAEifRDASCRSkRGfCsWS9OhZRT9D3dZXUYLYj/4SIp2b8GiwROooq','activo'),(326278,1,3,'1004686920','Juliana ','Estupiñan','1088258093','sebastianmoralesrodas@gmail.com','$2b$12$2j7ECRjGBi9qvE5NxjBQ5uaLdYivwrNd8lrCIsRzHHpN7l3EGDv0S','activo'),(345676,3,1,'2345678','Lucia','Marin','322134567','admin1@example.com','$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(400231,3,1,'3000002','Alberto','Torres','354545454','alberto@example.com','$2b$12$KWOX/G6XqD5rvGGJXcvjIu5iQfzAQNElnc54WhmjVXHVo7l5j5oE.','activo'),(415621,2,2,'23456','Juan Delegado','Perez','3456787890','juan@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(423636,1,1,'5000010','Evangeline','Hawthorne','3089012345','evangeline.hawthorne@example.com','$2b$12$p7GjOfFdeWaF64xGH3/QQO3NvwRnrhGo1macgUAsSJ1A9cgfSYfqa','activo'),(505547,2,1,'12345677667','Pedro','Linares','324567888','Pedrito@gmail.com','$2b$12$vBC5e4jmVLpCMxq84I10h.HNKIJSfCi.8H/6/LsSX3GjHNaoApg2u','activo'),(511068,7,3,'111895468','Johana','Bolaños','315442056','bolahana@gmail.com','$2b$12$cNJIUNGC24WVB7TNiujKcuymQUcJZro423Rx9nyA7/Ay4tk2NfqTO','inactivo'),(531044,4,1,'121334573','karen','cortes','3134543544','kscprtewqwe@gmail.com','2VSa2efCfXPlEVaPCNYmx6QzmUZMbn','inactivo'),(557550,2,1,'9999','Carlos','Triana','32457887','Carlos@example.com','$2b$12$/ArIX5O5eeIZT1EfryHwaOsQeoqqac7WT6reH0bk6RYxwWflXEDu2','activo'),(584219,2,1,'5000005','Laura Isabel','Fernandez','325456555','lauraf@example.com','$2b$12$8/WD9wBWK2eaA/BVGV9lrOUYLc1W0dACis/A3EHbiOxCxxMhCdH3.','activo'),(596937,2,1,'1100011','Mariana Sofia','Castro','32154545','marianac@example.com','$2b$12$B2wFLsdhKmvO.FPlsri5GOlcGLlSMx9H9malhAN2ICs9yj9mbIjRC','activo'),(610916,3,1,'2000001','Ana Lucia','Torres','3215444','analu@example.com','$2b$12$tM0R82vnEJ1FhWl0fnDBBObi3GDE3V2a0rLGwM0dDfNXma9SNxDAK','activo'),(615313,7,1,'2001','Markus','Picolini','3201077201','Picolini@example.com','$2b$12$NKNAtMI8RhZKqNDIBbASo.gVnV8hNYvFTLvaGC/1r6SYTN.8OFQSi','inactivo'),(644083,2,1,'1234455','Juliana','Marin','3255456789','Juliana@gmail.com','$2b$12$7t4JbNukjNaRsBlXANoiqednDczLPWXKwH1QroGDj97WeFhxtRFjO','activo'),(655438,2,1,'4000004','David Julian','Gonzalez','659365','davidg@example.com','$2b$12$Q3qyG5/kl5D2hqna5Ac67uAfvb1t/Etnvefpa06rj7WucuXIq9ZNC','activo'),(656575,3,1,'12345','Julian','Gomez','2134567','Juli@example.com','$2b$12$GDfNfA8X45AwxA1boOsBYeCF/oJGxVnHUnUTPyieB6.JlV9GB0tHu','activo'),(691430,1,1,'123455','Sancho','Sanchez','Sancho','Sancho@example.com','$2b$12$sa6O2tkOmDTdzNMyzwaiRu/5MqwAszF1HUUJQjOM6d.mzBx.RAnpS','activo'),(725812,1,1,'9870','Miguel','Romero','302123456','migue@example.com','$2b$12$p1HwscXw6RV0yAfbftZLUe5nwk5.hp3EBeH.rNqw8cfVFSIxoJ.ke','activo'),(744081,1,1,'2345698','Lupe','Mendez','123456776','lup@example.com','$2b$12$lB7iKrx4P2vPQHQxbYXEuew.o.Yqx/ag40ZhKVLiKSkNGM07iyfSq','activo'),(766606,3,1,'30000045','Sofia Maria','Ramirez','Sofia Maria','sofiar@example.com','$2b$12$5aNqtpfOKSzqdGkHMXbqbuuwnwA6xFlOzZnhHn06InxpCtBujbu2m','activo'),(767543,2,1,'2334','Paula','Garzon','12345564','paula@example.com','$2b$12$Et9Oe6.DsKtyDKpXeibrTOTqLViEqlJqg3ORR18M.N2CgyNkygvli','activo'),(768731,5,1,'2346775349','nose','nose ','3245575656','nose@gamil.com','FJpMd9ZJh2uAN7MBGXrTwAxaGZ0ZTt','inactivo'),(810564,3,1,'1200012','Ricardo Jose','Mendoza','321545','ricardom@example.com','$2b$12$2uh1ngG38.5DaHQciV3yr.GHoBXel7cjkkcflwLolaPM/dzOrnYdC','activo'),(825363,1,1,'11376775335','bellacat','ni idea','3233450976','bellis@example.com','$2b$12$xZztav.Lz/xWzebpsKRpROMgblMtwg1NDpJI.saobzX7XM8OS9Qna','activo'),(896895,3,1,'5000004','Seraphina','Blake','301289878','seraphina.blake@example.com','$2b$12$Rx9NAvRJ.MXFLwkkE.7KzeqWSkEAni8fb4olz3b0ZDtxPiXsv7XIK','activo'),(900403,2,2,'2345677','Nicolas','Mendez','3242345678','Nicolas9@gmail.com','$2b$12$HhOjtCw7/xBS1OFcDdQnW.P/POZBKEt.NHg.XyZaJYrELxlNloW2y','activo'),(946124,1,1,'645654654','jbkjbkj','kjbkjb','355555','bkjbkb@gmail.com','$2b$12$rcAE9J.39wLodYql/afRMupT5xtLSgsFXVjJgMSVnwqh2RoDneOGO','activo'),(961804,1,3,'5000008','Ophelia','Wellington','3067890123','Ophelia@example.com','$2b$12$Y6qJR8Ay9OEkEYjotOTjtuvOI9Tx40T.B8TEWjO1xwupwLsvPlT.a','activo'),(962846,1,1,'5000007','Balthazar','Knight','3056789012','balthazar@example.com','$2b$12$mg0bx.X5uL7AQJIk7oIB5.XyEGJs01ROUSmGJjL99VIJ98FAK5tGm','activo'),(968758,2,1,'8000008','Juan Pablo','Rodriguez','3234544','juanr@example.com','$2b$12$jE.Qo.4sXfD4n8f2NMEWn.9u9X77DJxbkvYomoeg6/Hypt1x5.3cS','activo'),(979760,6,1,'51515','Prueba','Melo','Prueba','superadmin@correo.com','$2b$12$RDI1SjbmoeOfMerfH2T0aOV0JZIkQ0zjw3W4OImuKsKd.a7gTLWTy','activo'),(979761,1,1,'1112221110','Katie','Cardona','3001234568','evaluador2@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','inactivo'),(979762,1,1,'2122212220','Zeus','Olivander','3001234569','evaluador3@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979763,1,1,'2415204196','Nate','Sanchez','3001234570','evaluador4@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979764,1,1,'1067492522','Orlando','Castaño','3001234110','evaluador5@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979765,1,2,'A025BC','Thalia','Gomez','3001234120','evaluador6@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979766,1,1,'2014253849','Liliana','Romero','3001234130','evaluador7@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979770,1,1,'1614443217','Carlos','González','3001234140','evaluador8@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979771,1,2,'B103CD','Lucía','Martínez','3001234150','evaluador9@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979772,1,1,'2649875269','Mario','Fernández','3001234160','evaluador10@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979776,1,1,'987654190','Ana','Rodríguez','3101234567','evaluador11@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979777,1,1,'1234567200','Jorge','Calderon','3119876543','evaluador12@example.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979778,1,1,'A4567DE','string','string','string','user@gmail.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979779,2,1,'2345453','camila','perez','43234633','camila@gmail.com','$2b$12$9IaF5VESa.QjxCrcI3NBOujF8FmWaY/v593tdB59Uz5QIVLiSS4Gq','activo'),(979782,6,1,'181818','Pepito','Perez','30978654','asistente1@example.com','clave1encriptada','inactivo'),(979783,7,1,'23451','Paulo','Neruda','3124566789','neruda@example.com','clave3encriptada','inactivo'),(979784,7,1,'897868','Oliverio','Girondo','45678934','oli@example.com','clave5encriptada','inactivo'),(979785,7,1,'656768','Anais','Ninn','675380999','ani@example.com','clave6encriptada','activo'),(979788,5,1,'10882365','Luisa Fernanda','Patiño ','1475623','soyunponente1@example.com','12345','inactivo'),(979789,5,1,'1088236','Yohan','Sanchez','432673','soyunponente2@example.com','12345','inactivo'),(979790,5,1,'346347345','Miguel Angel','Alzate','300125345','miguelacho1234@example.com','12345','inactivo'),(979791,5,1,'7432756762','Miguel Angel','Alzate','732857','132157@example.com','12345','inactivo'),(979792,5,1,'4554893','Lucia Marques','Sucre','76327','17843@example.com','12345','inactivo'),(979793,1,1,'454545','Alejandra','Pizarnik','31125647897','ale@example.com','12345','activo'),(979798,7,1,'2023456789','Sofía Alejandra','Torres Díaz','3201234568','sofia.torres@example.com','$2b$12$MBUn9LwqhEsThOjSn4/.HO1fgVTpKG7IazJnS2BeODeI1QZuavZBy','inactivo'),(979799,7,2,'P234567890','Andrés Felipe','Gutiérrez Rojas','3109876503','andres.gutierrez@example.com','$2b$12$a/GW9WE/8cbM/irAwWyuweA85wud9TYTTD2DLUEnR6gK77riTDQka','inactivo'),(979800,7,1,'9988776655','Valentina Lucía','Castro Peña','3108765462','valentina.castro@example.com','$2b$12$YymLs7wzR3EWAc2g.GEt9ucBxj6NbM1GNiUj1Vzqzlwq1lfkwSn4m','inactivo'),(979801,7,1,'2023456721',' Alejandra','Torres Díaz','3201234511','alejandra.torres@example.com','$2b$12$CazE1bhZP7D3btKeZMD6Z.leW4lPcLYdkGW8TiKcVvEFXZ8K0XeI2','inactivo'),(979802,7,1,'2021456333','Christian','Hernandez','3201234201','chris.chris@example.com','$2b$12$ehvcJEfAFTBwo/vDG3Ot0.E6a80VFRbTbOk/gV332Hk2gcYLpenLe','inactivo'),(990926,1,1,'166666','Francisco','Gomez','3284387438','fran@gmail.com','$2b$12$MCP3yeuXigQqxhqRNVGVWuvTeD4SR9wlF1Aqd1G6oxDoFG08l5O2G','activo');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
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

-- Dump completed on 2024-10-12 21:56:03
