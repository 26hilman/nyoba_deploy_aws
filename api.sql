-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: API
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ListBook`
--

DROP TABLE IF EXISTS `ListBook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ListBook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `isbn` varchar(255) DEFAULT NULL,
  `writer` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ListBook`
--

LOCK TABLES `ListBook` WRITE;
/*!40000 ALTER TABLE `ListBook` DISABLE KEYS */;
INSERT INTO `ListBook` VALUES (1,'Judul Buku Sangar','1234','Dr. Who'),(2,'Judul Buku Sangar','1234','Dr. Who'),(3,'Judul Buku Sangar','1234','Dr. Who'),(4,'Judul Buku Sangar','1234','Dr. Who'),(5,'Judul Buku Sangar','1234','Dr. Who'),(6,'Judul Buku Sangar','1234','Dr. Who'),(7,'Judul Buku Sangar','1234','Dr. Who'),(8,'Judul Buku Sangar','1234','Dr. Who'),(9,'Judul Buku Sangar','1234','Dr. Who'),(10,'Judul Buku Sangar','1234','Dr. Who'),(11,'Judul Buku Sangar','1234','Dr. Who'),(12,'Judul Buku Sangar','1234','Dr. Who'),(13,'Judul Buku Sangar','1234','Dr. Who'),(14,'Judul Buku Sangar','1234','Dr. Who'),(15,'Judul Buku Sangar','1234','Dr. Who'),(16,'Judul Buku Sangar','1234','Dr. Who'),(17,'Judul Buku Sangar','1234','Dr. Who'),(18,'Judul Buku Sangar','1234','Dr. Who'),(19,'Judul Buku Sangar','1234','Dr. Who'),(20,'Judul Buku Sangar','1234','Dr. Who'),(21,'Judul Buku Sangar','1234','Dr. Who'),(22,'Judul Buku Sangar','1234','Dr. Who'),(23,'Judul Buku Sangar','1234','Dr. Who'),(24,'Judul Buku Sangar','1234','Dr. Who'),(25,'Judul Buku Sangar','1234','Dr. Who'),(26,'Judul Buku Sangar','1234','Dr. Who'),(27,'Judul Buku Sangar','1234','Dr. Who'),(28,'Judul Buku Sangar','1234','Dr. Who'),(29,'Judul Buku Sangar','1234','Dr. Who'),(30,'Judul Buku Sangar','1234','Dr. Who'),(31,'Judul Buku Sangar','1234','Dr. Who'),(32,'Judul Buku Sangar','1234','Dr. Who'),(33,'Judul Buku Sangar','1234','Dr. Who');
/*!40000 ALTER TABLE `ListBook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ListClient`
--

DROP TABLE IF EXISTS `ListClient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ListClient` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_key` varchar(255) DEFAULT NULL,
  `client_secret` varchar(255) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ListClient`
--

LOCK TABLES `ListClient` WRITE;
/*!40000 ALTER TABLE `ListClient` DISABLE KEYS */;
INSERT INTO `ListClient` VALUES (1,'alterra','masukaja','true'),(3,'altsasafsafsaferra','masukaja','false'),(4,'altsasafsafsaferra','masukaja','false'),(5,NULL,NULL,NULL),(6,NULL,NULL,NULL),(7,NULL,NULL,NULL),(8,NULL,NULL,NULL),(9,'afdgdsfgsfdgdsf','asdfsadf','1'),(10,'afdgdsfgsfdgdsf','asdfsadf','0'),(11,'afdgdsfgsfdgdsf','asdfsadf','0'),(12,'afdgdsfgsfdgdsf','asdfsadf','1'),(13,'afdgdsfgsfdgdsf','asdfsadf','0'),(14,'afdgdsfgsfdgdsf','asdfsadf','0'),(15,'afdgdsfgsfdgdsf','asdfsadf','0'),(16,'afdgdsfgsfdgdsf','asdfsadf','1'),(17,'afdgdsfgsfdgdsf','asdfsadf','0'),(18,'afdgdsfgsfdgdsf','asdfsadf','0');
/*!40000 ALTER TABLE `ListClient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ListRent`
--

DROP TABLE IF EXISTS `ListRent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ListRent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ListRent`
--

LOCK TABLES `ListRent` WRITE;
/*!40000 ALTER TABLE `ListRent` DISABLE KEYS */;
INSERT INTO `ListRent` VALUES (1,2,2),(2,2,2),(3,2,3);
/*!40000 ALTER TABLE `ListRent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ListUser`
--

DROP TABLE IF EXISTS `ListUser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ListUser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `client_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ListUser`
--

LOCK TABLES `ListUser` WRITE;
/*!40000 ALTER TABLE `ListUser` DISABLE KEYS */;
INSERT INTO `ListUser` VALUES (2,'Hilman Yanuar Rahmadi',7,'Male',9999999),(3,'Hilman Yanuar Rahmadi',7,'Male',9999999),(4,'Hilman Yanuar Rahmadi',7,'Male',9999999),(5,'Hilman Yanuar Rahmadi',7,'Male',9999999),(6,'Hilman Yanuar Rahmadi',7,'Male',9999999),(7,'Hilman Yanuar Rahmadi',7,'Male',9999999),(8,'Hilman Yanuar Rahmadi',7,'Male',9999999),(9,'Hilman Yanuar Rahmadi',7,'Male',9999999),(10,'Hilman Yanuar Rahmadi',7,'Male',9999999),(11,'Hilman Yanuar Rahmadi',7,'Male',9999999),(12,'Hilman Yanuar Rahmadi',7,'Male',9999999),(13,'Hilman Yanuar Rahmadi',7,'Male',9999999),(14,'Hilman Yanuar Rahmadi',7,'Male',9999999),(15,'Hilman Yanuar Rahmadi',7,'Male',9999999),(16,'Hilman Yanuar Rahmadi',7,'Male',9999999),(17,'Hilman Yanuar Rahmadi',7,'Male',9999999),(18,'Hilman Yanuar Rahmadi',7,'Male',9999999),(19,'Hilman Yanuar Rahmadi',7,'Male',9999999),(20,'Hilman Yanuar Rahmadi',7,'Male',9999999),(21,'Hilman Yanuar Rahmadi',7,'Male',9999999),(22,'Hilman Yanuar Rahmadi',7,'Male',9999999),(23,'Hilman Yanuar Rahmadi',7,'Male',9999999),(24,'Hilman Yanuar Rahmadi',7,'Male',9999999),(25,'Hilman Yanuar Rahmadi',7,'Male',9999999),(26,'Hilman Yanuar Rahmadi',7,'Male',9999999),(27,'Hilman Yanuar Rahmadi',7,'Male',9999999),(28,'Hilman Yanuar Rahmadi',7,'Male',9999999),(29,'Hilman Yanuar Rahmadi',7,'Male',9999999),(30,'Hilman Yanuar Rahmadi',7,'Male',9999999),(31,'Hilman Yanuar Rahmadi',7,'Male',9999999),(32,'Hilman Yanuar Rahmadi',7,'Male',9999999),(33,'Hilman Yanuar Rahmadi',7,'Male',9999999);
/*!40000 ALTER TABLE `ListUser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-18 22:33:25
