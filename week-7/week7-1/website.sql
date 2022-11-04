-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'快龍','dragonite','dragonite',337347,'2022-07-09 15:10:44'),(2,'皮卡丘','pikachu','pikachu',859847,'2022-02-18 10:12:30'),(3,'寶貝龍','bagon','bagon',174684,'2022-09-22 22:22:26'),(4,'夢幻','mew','mew',10434947,'2022-08-04 21:18:09'),(5,'拉魯拉絲','ralts','ralts',73688,'2022-05-01 14:01:20'),(6,'可達鴨','psyduck','psyduck',478378,'2022-10-01 19:09:28'),(7,'洛奇亞','lugia','lugia',6987324,'2022-03-17 08:06:47'),(8,'喵喵','meowth','meowth',6373,'2022-06-09 05:23:43'),(9,'急凍鳥','articuno','articuno',963543649,'2022-01-16 04:30:37'),(10,'幸福蛋','blissey','blissey',934786,'2022-06-30 10:06:28'),(11,'卡比獸','snorlax','snorlax',929487,'2022-02-07 07:56:18'),(12,'果然翁','wobbuffet','wobbuffet',82738,'2022-01-13 17:34:09'),(13,'波克比','togepi','togepi',596836,'2022-04-27 01:02:23'),(14,'胖丁','jigglypuff','jigglypuff',860489,'2022-08-05 20:17:04');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,10,'魔法閃耀',27326375,'2022-07-10 20:16:30'),(2,4,'精神強念',723954247,'2022-09-26 17:35:20'),(3,6,'意念頭錘',8364,'2022-10-23 01:35:22'),(4,2,'千萬伏特',2532689,'2022-08-30 07:24:36'),(5,11,'破壞光線',4456777,'2022-07-24 06:17:35'),(6,1,'龍息',29835743,'2022-10-02 22:25:08'),(7,12,'鏡面反射',98645,'2022-07-06 14:34:56'),(8,7,'氣旋攻擊',32397465,'2022-08-13 09:10:34'),(9,3,'噴射火焰',3847,'2022-10-22 18:06:01'),(10,13,'魔法閃耀',27375,'2022-06-30 03:27:08'),(11,8,'欺詐',8465,'2022-06-25 12:36:38'),(12,5,'精神衝擊',1464264,'2022-09-03 10:16:18'),(13,14,'嬉鬧',26624,'2022-08-19 06:22:29'),(14,9,'冰凍光束',627483647,'2022-09-24 16:04:48');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-05  2:54:16
