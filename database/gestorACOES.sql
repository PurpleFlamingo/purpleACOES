-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: jfaldanam.ddns.net    Database: gestorACOES
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
INSERT INTO `apadrinamiento` VALUES (5,2,1,2,'2015-01-01',NULL),(4,2,3,2,'2017-01-01',NULL),(2,3,3,2,'2017-01-01',NULL),(6,4,1,2,'2015-01-01',NULL),(3,4,3,2,'2017-01-01',NULL);
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
INSERT INTO `colegio` VALUES (1,1,'AAA',1),(2,1,'San Benito',1);
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
INSERT INTO `colonia` VALUES (1,'AAA',1,'111'),(2,'El quinto pino',9001,'Es una colonia que tiene más de 9000 habitantes y que queda por el quinto pino'),(3,'Lalala',13,NULL);
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
INSERT INTO `joven` VALUES (2,'B','BBB','B','BBB','AAA',NULL,'2011-10-10','2012-12-12','2011-11-11',NULL,'0',NULL,NULL,1,1,1),(3,'C','CCC','C','CCC','CCC',NULL,'2010-01-01','2013-12-12','2010-12-12',NULL,'1',NULL,NULL,1,1,1),(4,'D','DDD','D','DDD','DDD',NULL,'2009-01-01','2010-05-02','2010-05-06',NULL,NULL,NULL,NULL,1,1,1),(5,'E','EEE','','',NULL,'','2008-01-01','2010-11-12','2010-11-12',NULL,'',NULL,NULL,1,1,1);
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
INSERT INTO `permiso` VALUES ('Alicante','La localidad de Alicante','Acceso de lectura y escritura a todos los datos de dicha localidad'),('BatCountry','La localidad de Bat Country','Acceso de lectura y escritura a toda la informacion de dicha localidad'),('General','Todos los datos','Acceso de lectura y escritura a toda la informcacion'),('Socio','Apadrinados','Solo lectura datos concretos de los jovenes a los que apadrine');
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
INSERT INTO `proyecto` VALUES (1,'Alfa','Ser una prueba','Eres una prueba','Prueba'),(2,'Beta','NO TENIUA NADA ESCRITAAOA','OKOKOK','This is SPARTA'),(3,'Delta','Ser una prueba','Esto es una prueba','Prueba'),(4,'Patata','Hidratos de carbono','Soy una comida','Prueba'),(5,'OMEGA','JEJEJEJEJJEE','JIJIJIIJJ','ULTIMO'),(6,'Submarino','Aguantar altas presiones bajo el agua.','Te permite ver los peces del mar.','Acuatico'),(7,'Warning','Intentar editar sin seleccionar un proyecto','Has pulsado editar sin seleccionar un proyecto','Error');
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
INSERT INTO `socio` VALUES (1,'Carlos','A','1','2','3','3','4','5','6','7','asd','',1,'','2011-01-01',NULL,''),(3,'Pablito Pablo','P','11','1','1','1','1','1','2','','1','',1,'','2012-12-01','2018-01-05',''),(4,'Paco','P','5','6','2','1','4','4','1','4',NULL,'',1,'','2011-01-01',NULL,''),(21,'alez','a','4','6','3','2','4','4','4','5',NULL,'',1,'','2011-01-01',NULL,''),(24,'Name','N','2','5','4','4','4','4','3','6',NULL,'',1,'','2011-01-01',NULL,''),(26,'Pepito','holo','2','4','5','3','4','4','2','7',NULL,'',1,'','2011-01-01',NULL,''),(108,'AUno','Uno','3','4','3','2','4','4','4','8',NULL,'',1,'','2018-11-12',NULL,'');
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
INSERT INTO `transaccion` VALUES (2,1,'2017-01-01',128,'Euros','Honduras','Transferencia','Porque si',NULL,NULL,'Yo'),(4,1,'2018-02-02',128,'Euros','Honduras','Transferencia','Porque si',NULL,NULL,'Yo'),(5,1,'2018-12-31',123123,'Euros','si','yes','no',1,NULL,'si'),(7,1,'2019-12-02',123,'Euros','seee','si','no',1,4,'asas'),(92,0,'2015-01-01',35,'Euros',NULL,'Transferencia bancaria','Cuota mes de Enero',NULL,2,'Joven apadrinado'),(94,0,'2015-02-01',35,'Euros',NULL,'Transferencia bancaria','Cuota mes de Febrero',NULL,2,'Joven apadrinado'),(95,0,'2015-02-01',35,'Euros',NULL,'Transferencia bancaria','Cuota mes de Febrero',NULL,3,'Joven apadrinado'),(96,0,'2015-02-01',35,'Euros',NULL,'Transferencia bancaria','Cuota mes de Febrero',NULL,4,'Joven apadrinado');
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
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Carlo','12345','Socio','Socio'),(2,'Marta','1234','Coordinador General','General'),(3,'Pablo','1234','Socio','Socio'),(4,'Paco','9876','Socio','Socio'),(5,'Juan','5874','Coordinador Local','General'),(6,'Pepito','6345','Responsable Economico General','General'),(7,'Enrique','3456','Responsable Economico de Proyecto','Alicante'),(8,'Coche','2342','Responsable Economico de Proyecto','Alicante'),(9,'Azul','2434','Coordinador General','Alicante'),(10,'MShadow','Nightmare','Responsable Economico General','BatCountry'),(11,'ZackyV','Runaway','Coordinador Local','BatCountry'),(12,'SynysterGaytes','So far away','Responsable Economico General','BatCountry'),(13,'JohnnyChrist','Demons','Agente Local','BatCountry'),(14,'Brooks','The Stage','Coordinador Local','BatCountry'),(15,'TheRev','Fiction','Agente Local','BatCountry'),(16,'python','django','Coordinador Local','Alicante'),(17,'MrGoblikon','TrollsSucks','Coordinador General','Alicante'),(18,'last3','3','Agente Local','Alicante'),(19,'last2','2','Coordinador de Proyecto','Alicante'),(20,'lastOne','1','Agente Local','Alicante'),(21,'alez','1234','Socio','Socio'),(22,'Bond','JamesBond','Agente Local','Alicante'),(23,'ramon','1234','Responsable Economico de Proyecto','Alicante'),(24,'prueba','prueba','Socio','Socio'),(25,'user','pass','Coordinador Local','Alicante'),(26,'PPrez','holo','Socio','Socio'),(27,'Caramelo','candy','Responsable Economico de Proyecto','Alicante'),(101,'c','b','Coordinador General','Alicante'),(108,'A1','123','Socio','Socio');
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
INSERT INTO `voluntario` VALUES (2,'Martilla','Martillo','2','2077-07-17','2012-01-03','martita@marta.mazo','453','calleMODIFICADO','4','prov1prueba','Honduras'),(5,'Juan','Lopez','5','2077-07-17','2012-01-03',NULL,'23423','calle1','2','Alicante','Honduras'),(6,'Pepito','Grillo','6','2077-07-17','2012-01-03','pprez@email.com','423423','calle3','6','Alicante','Honduras'),(7,'Enrique','Kike','7','2077-07-17','2012-01-03',NULL,'5435','calle1','3','Alicante','Honduras'),(8,'Coche','McQueen','8','2077-07-17','2012-01-03',NULL,'645','callef','5','Algeciras','Espana'),(9,'Azul','Color','9','2077-07-17','2012-01-03',NULL,'64564','calleasdad','7','Algeciras','Espana'),(10,'Mister','Shadow','10','2077-07-17','2012-01-03','mshadows@a7x.com','756','calleadsd','8','BatCountry','Espana'),(11,'Zacky','Vengeance','11','2077-07-17','2012-01-03','zackyV@a7x.com','75675','calle5','4','BatCountry','Espana'),(12,'Synyster','Gates','12','2077-07-17','2012-01-03','gates@a7x.com','5675','callers','3','BatCountry','Espana'),(13,'Johnny','Christ','13','2077-07-17','2012-01-03','christ@a7x.com','35435','callersd','5','BatCountry','Espana'),(14,'Brooks','Wackerman','14','2077-07-17','2012-01-03','wackerman@a7x.com','234','callea12343','7','BatCountry','Espana'),(15,'Jimmy','\'The Rev\' Sullivan','15','2077-07-17','2012-01-03','theRev@a7x.com','54353','calle1234','2','BatCountry','Espana'),(16,'python','el lenguage','16','2077-07-17','2012-01-03','python@python.python','123','calledasds','5','Phytonlandia','Espana'),(17,'John','Goblikon','17','2077-07-17','2012-01-03',NULL,'345345','calle13434','8','Goblin Island','Espana'),(18,'last','third','18','2077-07-17','2012-01-03','correo@correo.correo','4566','calle345343','3','Alicante','Honduras'),(19,'last','second','19','2077-07-17','2012-01-03','jfaldanam@gmail.com','345','calleffsdf','6','Alicante','Honduras'),(20,'last','first','20','2077-07-17','2012-01-03','','24324','calle12345','1232','Alicante','Honduras'),(22,'007','Bond, James Bond','1','1978-06-12','1978-06-12','correo@alicante.007','1234','Alicante','35','Alicante','Honduras'),(23,'carlos','asd','123','2017-10-01','2019-12-11','asd','dasdas','asd','adssa','asda','adsads'),(25,'Name','Ape','NIFFF','2001-02-02','2000-01-01',NULL,NULL,'ssi','no','Alicante','España'),(27,'Cara','Melo','','1550-03-03','1550-03-03','','','Piruleta','5528','Alicante','Azucar');
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

-- Dump completed on 2019-01-09 12:39:05