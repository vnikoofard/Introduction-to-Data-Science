-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: banco
-- ------------------------------------------------------
-- Server version	8.0.26

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

--
-- Table structure for table `lojas`
--

DROP TABLE IF EXISTS `lojas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lojas` (
  `ID_Loja` int DEFAULT NULL,
  `Loja` text,
  `Gerente` text,
  `Endereco` text,
  `Num_Funcionarios` int DEFAULT NULL,
  `Telefone` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lojas`
--

LOCK TABLES `lojas` WRITE;
/*!40000 ALTER TABLE `lojas` DISABLE KEYS */;
INSERT INTO `lojas` VALUES (1,'Rio de Janeiro','Pedro Martins','R. Visc. de Pirajá, 136 - Ipanema, Rio de Janeiro - RJ, 22410-000',23,'(21) 3198-1239'),(2,'Belo Horizonte','Julia Freitas','Av. Barão Homem de Melo, 1389 - Nova Granada, Belo Horizonte - MG, 30431-425',13,'(31) 2891-2394'),(3,'Salvador','Marcelo Castro','Shopping Barra - Av. Centenário, 2992 - Barra, Salvador - BA, 40155-150',19,'(71) 3465-8748'),(4,'Curitiba','Amanda Lima','R. Brasílio Itiberê, 3279 - Água Verde, Curitiba - PR, 80250-160',31,'(41) 2923-2137'),(5,'Fortaleza','Letícia Gomes','Av. Dom Luís, 500 - Aldeota, Fortaleza - CE, 60160-230',12,'(85) 3294-1481'),(6,'São Paulo','Rogério Lopes','R. Teodoro Sampaio, 954 - Pinheiros, São Paulo - SP, 05406-050',33,'(11) 3295-3945'),(7,'Niterói','Matheus Leal','Rua Quinze de Novembro, 8 - Loja 301a Loja 301b - Centro, Niterói - RJ, 24020-125',18,'(21) 3134-7263'),(8,'Goiânia','Carlos Henrique','Av. Goiás Norte, 3.592 - quadra 2.1 - St. Mal. Rondon, Goiânia - GO, 74063-010',11,NULL);
/*!40000 ALTER TABLE `lojas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-25 15:13:58
