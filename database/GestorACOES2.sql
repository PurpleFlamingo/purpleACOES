-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: GestorACOES2
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

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
-- Table structure for table `apadrinamiento`
--

DROP TABLE IF EXISTS `apadrinamiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apadrinamiento` (
  `id_apadrinamiento` int(11) NOT NULL,
  `joven` int(11) NOT NULL,
  `socio` int(11) NOT NULL,
  `agente` int(11) NOT NULL,
  `fecha_de_inicio` date NOT NULL,
  `fecha_de_baja` date DEFAULT NULL,
  PRIMARY KEY (`joven`,`socio`),
  UNIQUE KEY `idApadrinamiento_UNIQUE` (`id_apadrinamiento`),
  KEY `fk_apadrinamiento_joven1_idx` (`joven`),
  KEY `fk_apadrinamiento_socio1_idx` (`socio`),
  KEY `fk_apadrinamiento_voluntario1_idx` (`agente`),
  CONSTRAINT `fk_apadrinamiento_joven1` FOREIGN KEY (`joven`) REFERENCES `joven` (`id_joven`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_apadrinamiento_socio1` FOREIGN KEY (`socio`) REFERENCES `socio` (`usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_apadrinamiento_voluntario1` FOREIGN KEY (`agente`) REFERENCES `voluntario` (`usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apadrinamiento`
--

LOCK TABLES `apadrinamiento` WRITE;
/*!40000 ALTER TABLE `apadrinamiento` DISABLE KEYS */;
INSERT INTO `apadrinamiento` VALUES (1,1,1,11,'2016-12-12',NULL),(2,2,2,11,'2017-11-11','2018-02-02'),(3,3,1,11,'2010-10-10','2010-12-12'),(4,4,2,11,'2016-09-09',NULL);
/*!40000 ALTER TABLE `apadrinamiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colegio`
--

DROP TABLE IF EXISTS `colegio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `colegio` (
  `id_colegio` int(11) NOT NULL,
  `asociado_ACOES` tinyint(1) DEFAULT NULL,
  `nombre_colegio` varchar(45) DEFAULT NULL,
  `colonia` int(11) NOT NULL,
  PRIMARY KEY (`id_colegio`),
  KEY `fk_colegio_colonia1_idx` (`colonia`),
  CONSTRAINT `fk_colegio_colonia1` FOREIGN KEY (`colonia`) REFERENCES `colonia` (`id_colonia`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colegio`
--

LOCK TABLES `colegio` WRITE;
/*!40000 ALTER TABLE `colegio` DISABLE KEYS */;
INSERT INTO `colegio` VALUES (1,0,'Central Vicente Caceres',3),(2,0,'Marcos Efrain Aguirre Lara de Copán',5),(3,1,'San Marcos',7),(4,1,'Primero de Mayo',3);
/*!40000 ALTER TABLE `colegio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colonia`
--

DROP TABLE IF EXISTS `colonia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `colonia` (
  `id_colonia` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `numero_de_habitantes` int(11) NOT NULL,
  `descripcion` longtext,
  PRIMARY KEY (`id_colonia`),
  UNIQUE KEY `nombre_UNIQUE` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colonia`
--

LOCK TABLES `colonia` WRITE;
/*!40000 ALTER TABLE `colonia` DISABLE KEYS */;
INSERT INTO `colonia` VALUES (1,'Alicante',999999,'Localidad de España'),(2,'Málaga',999999,'Localidad de España'),(3,'Tegucigalpa',9999,'Localidad de Honduras'),(4,'Cordoba',999999,'Localidad de España'),(5,'La Ceiba',9999,'Localidad de Honduras'),(6,'Sevilla',999999,'Localidad de España'),(7,'San Pedro Sula',9999,'Localidad de Honduras'),(8,'3',1,NULL);
/*!40000 ALTER TABLE `colonia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `envios`
--

DROP TABLE IF EXISTS `envios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `envios` (
  `id_envios` int(11) NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `eviado_por_socio` tinyint(1) DEFAULT NULL,
  `recibido` tinyint(1) DEFAULT NULL,
  `respuestaA` int(11) DEFAULT NULL,
  `apadrinamiento` int(11) NOT NULL,
  PRIMARY KEY (`id_envios`),
  KEY `fk_envios_envios1_idx` (`respuestaA`),
  KEY `fk_envios_apadrinamiento1_idx` (`apadrinamiento`),
  CONSTRAINT `fk_envios_apadrinamiento1` FOREIGN KEY (`apadrinamiento`) REFERENCES `apadrinamiento` (`id_apadrinamiento`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_envios_envios1` FOREIGN KEY (`respuestaA`) REFERENCES `envios` (`id_envios`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `envios`
--

LOCK TABLES `envios` WRITE;
/*!40000 ALTER TABLE `envios` DISABLE KEYS */;
/*!40000 ALTER TABLE `envios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `joven`
--

DROP TABLE IF EXISTS `joven`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `joven` (
  `id_joven` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellidos` varchar(45) NOT NULL,
  `nombre_del_padre` varchar(45) DEFAULT NULL,
  `nombre_de_la_madre` varchar(45) DEFAULT NULL,
  `estado` varchar(45) DEFAULT NULL,
  `url_foto` varchar(200) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `fecha_de_alta_acoes` date NOT NULL,
  `fecha_de_alta` date DEFAULT NULL,
  `fecha_de_salida_acoes` date DEFAULT NULL,
  `grado` varchar(45) DEFAULT NULL,
  `historial` longtext,
  `observaciones` longtext,
  `colonia_nacimiento` int(11) NOT NULL,
  `colonia_residencia` int(11) NOT NULL,
  `colegio` int(11) NOT NULL,
  PRIMARY KEY (`id_joven`),
  KEY `fk_joven_colonia1_idx` (`colonia_nacimiento`),
  KEY `fk_joven_colonia2_idx` (`colonia_residencia`),
  KEY `fk_joven_colegio1_idx` (`colegio`),
  CONSTRAINT `fk_joven_colegio1` FOREIGN KEY (`colegio`) REFERENCES `colegio` (`id_colegio`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_joven_colonia1` FOREIGN KEY (`colonia_nacimiento`) REFERENCES `colonia` (`id_colonia`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_joven_colonia2` FOREIGN KEY (`colonia_residencia`) REFERENCES `colonia` (`id_colonia`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joven`
--

LOCK TABLES `joven` WRITE;
/*!40000 ALTER TABLE `joven` DISABLE KEYS */;
INSERT INTO `joven` VALUES (1,'Pepito','Alba','Pepe','Pepa','Honduras',NULL,'2000-01-01','2010-01-01',NULL,NULL,NULL,NULL,NULL,3,3,1),(2,'Rafa','Benitez','Rafael','Rafaela','Honduras',NULL,'2000-02-02','2010-02-02',NULL,NULL,NULL,NULL,NULL,5,5,2),(3,'Sera','Arturez','Serafin','Sara','Honduras',NULL,'2000-03-03','2010-03-03',NULL,NULL,NULL,NULL,NULL,5,7,3),(4,'Carlos','Flamenco','Carlo','Carla','Honduras',NULL,'2000-04-04','2010-04-04',NULL,NULL,NULL,NULL,NULL,7,3,4);
/*!40000 ALTER TABLE `joven` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permiso`
--

DROP TABLE IF EXISTS `permiso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permiso` (
  `permiso` varchar(50) NOT NULL,
  `alcance` varchar(45) NOT NULL,
  `descripcion_del_alcance` longtext NOT NULL,
  PRIMARY KEY (`permiso`),
  UNIQUE KEY `permiso_UNIQUE` (`permiso`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permiso`
--

LOCK TABLES `permiso` WRITE;
/*!40000 ALTER TABLE `permiso` DISABLE KEYS */;
INSERT INTO `permiso` VALUES ('Alicante','La localidad de Alicante','Acceso de lectura y escritura a todos los datos de dicha localidad'),('Cordoba','La localidad de Cordoba','Acceso de lectura y escritura a todos los datos de dicha localidad'),('General','General','Permiso absoluto'),('La Ceiba','La localidad de La Ceiba','Acceso de lectura y escritura a todos los datos de dicha localidad'),('Málaga','La localidad de Málaga','Acceso de lectura y escritura a todos los datos de dicha localidad'),('San Pedro Sula','La localidad de San Pedro Sula','Acceso de lectura y escritura a todos los datos de dicha localidad'),('Sevilla','La localidad de Sevilla','Acceso de lectura y escritura a todos los datos de dicha localidad'),('Socio','Socio','Consulta'),('Tegucigalpa','La localidad de Tegucigalpa','Acceso de lectura y escritura a todos los datos de dicha localidad');
/*!40000 ALTER TABLE `permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pertenecer_proyecto`
--

DROP TABLE IF EXISTS `pertenecer_proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pertenecer_proyecto` (
  `joven` int(11) NOT NULL,
  `proyecto` int(11) NOT NULL,
  `fecha_de_alta` date NOT NULL,
  `fecha_de_baja` date DEFAULT NULL,
  PRIMARY KEY (`joven`,`proyecto`),
  KEY `fk_joven_has_proyecto_proyecto1_idx` (`proyecto`),
  KEY `fk_joven_has_proyecto_joven1_idx` (`joven`),
  CONSTRAINT `fk_joven_has_proyecto_joven1` FOREIGN KEY (`joven`) REFERENCES `joven` (`id_joven`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_joven_has_proyecto_proyecto1` FOREIGN KEY (`proyecto`) REFERENCES `proyecto` (`id_proyecto`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pertenecer_proyecto`
--

LOCK TABLES `pertenecer_proyecto` WRITE;
/*!40000 ALTER TABLE `pertenecer_proyecto` DISABLE KEYS */;
INSERT INTO `pertenecer_proyecto` VALUES (1,1,'2010-01-01',NULL),(2,2,'2010-02-02','2015-05-05'),(3,3,'2011-01-11',NULL);
/*!40000 ALTER TABLE `pertenecer_proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyecto`
--

DROP TABLE IF EXISTS `proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proyecto` (
  `id_proyecto` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `requisitos_participacion` longtext,
  `descripcion` longtext,
  `tipo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_proyecto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyecto`
--

LOCK TABLES `proyecto` WRITE;
/*!40000 ALTER TABLE `proyecto` DISABLE KEYS */;
INSERT INTO `proyecto` VALUES (1,'Casa Central Vicente Caceres','Ingreso anual menor que el salario minimo interprofesional','Casa Populorum','Casa Populorum'),(2,'Casa Tegucigalpa Norte','Ingreso anual menor que el salario minimo interprofesional','Casa Populorum','Casa Populorum'),(3,'Residencia Primero de Mayo','Expediente academico decente','Residencia','Residencia');
/*!40000 ALTER TABLE `proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rol` (
  `rol_name` varchar(45) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `modificacion` tinyint(1) NOT NULL,
  PRIMARY KEY (`rol_name`),
  UNIQUE KEY `rol_name_UNIQUE` (`rol_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES ('Agente Local','Agente encaragado de apadrinamientos de una localidad en ACOES',1),('Coordinador de Proyecto','Coordinador de un proyecto en Honduras en ACOES',1),('Coordinador General','Coordinador general en ACOES',1),('Coordinador Local','Coordinador de una localidad en Espana en ACOES',1),('Responsable Economico de Proyecto','Responsable economico de un proyecto en Honduras en ACOES',1),('Responsable Economico General','Responsable economico general en ACOES',1),('Socio','Socio de ACOES',0);
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socio`
--

DROP TABLE IF EXISTS `socio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `socio` (
  `usuario` int(11) NOT NULL,
  `nombre_pila` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) NOT NULL,
  `nif` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) DEFAULT NULL,
  `poblacion` varchar(45) DEFAULT NULL,
  `codigo_postal` varchar(45) DEFAULT NULL,
  `provincia` varchar(45) DEFAULT NULL,
  `estado` varchar(45) DEFAULT NULL,
  `telefono1` varchar(45) DEFAULT NULL,
  `telefono2` varchar(45) DEFAULT NULL,
  `correo_electronico` varchar(45) DEFAULT NULL,
  `relacion` varchar(45) DEFAULT NULL,
  `certificado` tinyint(4) DEFAULT NULL,
  `sector` varchar(45) DEFAULT NULL,
  `fecha_de_alta` date NOT NULL,
  `fecha_de_baja` date DEFAULT NULL,
  `observaciones` longtext,
  `cuota` int(11) DEFAULT '0',
  PRIMARY KEY (`usuario`),
  KEY `fk_socio_usuario1_idx` (`usuario`),
  CONSTRAINT `fk_socio_usuario1` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socio`
--

LOCK TABLES `socio` WRITE;
/*!40000 ALTER TABLE `socio` DISABLE KEYS */;
INSERT INTO `socio` VALUES (1,'Pepe','Martinez','A1234B','Calle Abc','Malaga','29001','Malaga','España','987654321','','pepe@gg.com','1',0,'','2018-06-05',NULL,NULL,0),(2,'Miriam','Gala','G2564H','Carril Ghio','Sevilla','27001','Sevilla','España','987562431','','miriam@uu.com','No',1,'','2017-11-01',NULL,NULL,25),(71,'a','a','a','a','a','a','a','España','a','a','','a',0,'a','2019-01-20',NULL,'a',0),(74,'das','asd','asd','sad','asdsad','asd','sd','España','','','','',0,'','2019-01-20',NULL,'',0),(75,'a','a','a','a','a','a','a','España','','','','',0,'','2019-01-20',NULL,'',0);
/*!40000 ALTER TABLE `socio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaccion`
--

DROP TABLE IF EXISTS `transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaccion` (
  `id_transaccion` int(11) NOT NULL,
  `gasto` tinyint(1) NOT NULL,
  `fechaEmision` date NOT NULL,
  `cuantia` int(11) NOT NULL,
  `moneda` varchar(45) NOT NULL,
  `destino` varchar(45) DEFAULT NULL,
  `formaDePago` varchar(45) DEFAULT NULL,
  `motivo` varchar(45) DEFAULT NULL,
  `proyecto` int(11) DEFAULT NULL,
  `apadrinamiento` int(11) DEFAULT NULL,
  `beneficiario` varchar(45) DEFAULT NULL,
  `partida` varchar(45) NOT NULL,
  PRIMARY KEY (`id_transaccion`),
  KEY `fk_transaccion_proyecto1_idx` (`proyecto`),
  KEY `fk_transaccion_apadrinamiento1_idx` (`apadrinamiento`),
  CONSTRAINT `fk_transaccion_apadrinamiento1` FOREIGN KEY (`apadrinamiento`) REFERENCES `apadrinamiento` (`id_apadrinamiento`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_transaccion_proyecto1` FOREIGN KEY (`proyecto`) REFERENCES `proyecto` (`id_proyecto`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaccion`
--

LOCK TABLES `transaccion` WRITE;
/*!40000 ALTER TABLE `transaccion` DISABLE KEYS */;
INSERT INTO `transaccion` VALUES (1,0,'2017-01-01',10,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(2,0,'2017-01-01',15,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(3,0,'2017-01-01',20,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(4,0,'2017-01-01',25,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(5,0,'2017-01-01',30,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(6,0,'2017-01-01',10,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(7,0,'2017-01-01',15,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,1,'ACOES','Mensualidad socio'),(8,0,'2017-01-01',20,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,4,'ACOES','Mensualidad socio'),(9,0,'2017-01-01',25,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(10,0,'2017-01-02',30,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(11,1,'2017-01-02',10,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(12,1,'2017-01-02',15,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(13,1,'2017-01-02',20,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(14,1,'2017-01-02',25,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(15,1,'2017-01-02',30,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(16,1,'2017-01-02',10,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(17,1,'2017-01-02',15,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(18,1,'2017-01-02',20,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(19,1,'2017-01-02',25,'Lempiras','ACOES','Efectivo','Gastos material escolar',3,NULL,'ACOES','Gastos material escolar'),(20,0,'2017-01-02',30,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,1,'ACOES','Mensualidad socio'),(21,0,'2017-01-03',35,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,4,'ACOES','Mensualidad socio'),(22,0,'2017-01-03',40,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio'),(23,0,'2017-01-03',45,'Euros','ACOES','Efectivo','Mensualidad socio',NULL,NULL,'ACOES','Mensualidad socio');
/*!40000 ALTER TABLE `transaccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `clave` varchar(16) NOT NULL,
  `rol` varchar(45) NOT NULL,
  `permiso` varchar(50) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `identificacion_UNIQUE` (`id_usuario`),
  UNIQUE KEY `nombre_UNIQUE` (`nombre`),
  KEY `rol_usuario_idx` (`rol`),
  KEY `fk_usuario_permiso1_idx` (`permiso`),
  CONSTRAINT `fk_usuario_permiso1` FOREIGN KEY (`permiso`) REFERENCES `permiso` (`permiso`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `rol_usuario` FOREIGN KEY (`rol`) REFERENCES `rol` (`rol_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'pepe','pepe','Socio','Socio'),(2,'miriam','miriam','Socio','Socio'),(11,'cristian','cristian','Agente Local','Málaga'),(21,'serafin','serafin','Coordinador de Proyecto','Tegucigalpa'),(41,'pablo','pablo','Responsable Economico General','General'),(51,'marta','marta','Coordinador General','General'),(52,'pedro','pedro','Coordinador General','General'),(70,'usuario','clave','Socio','Socio'),(71,'a','a','Socio','Socio'),(72,'b','b','Agente Local','Sevilla'),(73,'c','2','Agente Local','Sevilla'),(74,'d','c','Socio','Socio'),(75,'33','a','Socio','Socio');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voluntario`
--

DROP TABLE IF EXISTS `voluntario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `voluntario` (
  `usuario` int(11) NOT NULL,
  `nombre_pila` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) NOT NULL,
  `nif` varchar(45) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `fecha_alta` date NOT NULL,
  `correo_electronico` varchar(45) DEFAULT NULL,
  `telefono_contacto` varchar(45) DEFAULT NULL,
  `direccion` varchar(45) NOT NULL,
  `codigo_postal` varchar(45) NOT NULL,
  `provincia` varchar(45) NOT NULL,
  `estado` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`usuario`),
  UNIQUE KEY `nif_UNIQUE` (`nif`),
  KEY `fk_voluntario_usuario1_idx` (`usuario`),
  CONSTRAINT `fk_voluntario_usuario1` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voluntario`
--

LOCK TABLES `voluntario` WRITE;
/*!40000 ALTER TABLE `voluntario` DISABLE KEYS */;
INSERT INTO `voluntario` VALUES (11,'Cristian','Garcia','B258D','1989-12-11','2015-01-02','cristian@dd.es','654789321','Avenida Roma','29010','Malaga','España'),(21,'Serefin','Lozano','G23156D','1990-01-02','2010-02-06','serafin@teg.hd','97845632','Calle Pelaez','15892','Tegucigalpa','Honduras'),(41,'Pablo','Clavos','H5646D','1992-02-03','2010-02-08','clavito@ho.dd','648984321','Calle Principal','16001','Tegucigalpa','Honduras'),(51,'Marta','Gala','T215S','1993-08-11','2015-06-01','marta@gg.es','985423215','Alameda Secundaria','270001','Sevilla','España'),(52,'Pedro','Carpintero','G8876T','1970-01-11','2006-07-09','pedro@ww.hd','5465321','Calle Central','16002','Tegucigalpa','Honduras'),(73,'w','w','w','2019-01-19','2019-01-20','','','w','w','w','w');
/*!40000 ALTER TABLE `voluntario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-22  7:43:04
