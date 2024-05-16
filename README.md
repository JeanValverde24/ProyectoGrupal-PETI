# ProyectoGrupal-PETI

#Creacion de  bd Mysql 

#Jose Luis Jarro C.


```
msql

CREATE DATABASE IF NOT EXISTS `PETI-PROYECTO`;
USE `PETI-PROYECTO`;

CREATE TABLE `AccionesComplementarias` (
  `IdAcciones` int NOT NULL,
  `FkEmpresa` int NOT NULL,
  `Accion1` text,
  `Accion2` text,
  `Accion3` text,
  `Accion4` text,
  `Accion5` text,
  `Accion6` text,
  `Accion7` text,
  `Accion8` text,
  `Accion9` text,
  `Accion10` text,
  `Accion11` text,
  `Accion12` text,
  `Accion13` text,
  `Accion14` text,
  `Accion15` text,
  `Accion16` text,
  PRIMARY KEY (`IdAcciones`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `AnalisisFoda` (
  `idAnalisis` int NOT NULL,
  `FkEmpresa` int NOT NULL,
  `FkDebilidades` int NOT NULL,
  `FkAmenazas` int NOT NULL,
  `FkFortalezas` int NOT NULL,
  `FkOportunidades` int NOT NULL,
  PRIMARY KEY (`idAnalisis`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Autodiagnostico` (
  `IdAutodiagnostico` int NOT NULL,
  `FkEmpresa` int NOT NULL,
  `Resultado` varchar(5) NOT NULL,
  PRIMARY KEY (`IdAutodiagnostico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `CarteraProd` (
  `IdCarteraProd` int NOT NULL,
  `FkPrevisionVentas` int NOT NULL,
  `FkTCM` int NOT NULL,
  `FkEvo_Dem_Glob_Sec` int NOT NULL,
  `FkNiveles_De_Venas` int NOT NULL,
  PRIMARY KEY (`IdCarteraProd`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Empresa` (
  `IdEmpresa` int NOT NULL AUTO_INCREMENT,
  `FkUsuario` int NOT NULL,
  `NombreEmpresa` varchar(150) NOT NULL,
  `Mision` text NOT NULL,
  `Vision` text NOT NULL,
  `FkValores` int NOT NULL,
  `UnidadesEstrategicas` text NOT NULL,
  `FkObjetivosEstrategicos` int NOT NULL,
  `FkAnálisisFODA` int NOT NULL,
  `IdeEstrategicas` text NOT NULL,
  `FkAccionesCompetitivas` int NOT NULL,
  `Conclusiones` text NOT NULL,
  PRIMARY KEY (`IdEmpresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `ObjetivosEspecificos` (
  `IdObjEsp` int NOT NULL,
  `FkObjetivosGen` int NOT NULL,
  `ObjEspecifico1` text NOT NULL,
  `ObjEspecifico2` text NOT NULL,
  `ObjEspecifico3` text NOT NULL,
  `ObjEspecifico4` text NOT NULL,
  `ObjEspecifico5` text NOT NULL,
  `ObjEspecifico6` text NOT NULL,
  PRIMARY KEY (`IdObjEsp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `ObjetivosEstrategicos` (
  `IDobjetivosEst` int NOT NULL,
  `FkEmpresa` int NOT NULL,
  `FkObjetivosGenerales` int NOT NULL,
  PRIMARY KEY (`IDobjetivosEst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `ObjetivosGenerales` (
  `idObjGen` int NOT NULL,
  `FkObjetivosEst` int NOT NULL,
  `ObjGeneral1` text NOT NULL,
  `ObjGeneral2` text NOT NULL,
  `ObjGeneral3` text NOT NULL,
  PRIMARY KEY (`idObjGen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `PrevisionVentas` (
  `IdPreVentas` int DEFAULT NULL,
  `FkCarteraProd` int DEFAULT NULL,
  `Producto1` int DEFAULT NULL,
  `Producto2` int DEFAULT NULL,
  `Producto3` int DEFAULT NULL,
  `Producto4` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Usuario` (
  `IdUsuario` int NOT NULL AUTO_INCREMENT,
  `Usuario` varchar(150) NOT NULL,
  `Nombres` varchar(150) NOT NULL,
  `Apellidos` varchar(150) NOT NULL,
  `Correo` varchar(250) NOT NULL,
  `Celular` varchar(9) NOT NULL,
  `Contraseña` varchar(257) NOT NULL,
  PRIMARY KEY (`IdUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Valoracion` (
  `IdValoracion` int NOT NULL,
  `FkAutodiagnostico` int NOT NULL,
  `Punto0` char(2) NOT NULL,
  `Punto1` char(2) NOT NULL,
  `Punto2` char(2) NOT NULL,
  `Punto3` char(2) NOT NULL,
  `Punto4` char(2) NOT NULL,
  PRIMARY KEY (`IdValoracion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Valores` (
  `IdValores` int NOT NULL,
  `FkEmpresa` int NOT NULL,
  `Valor1` varchar(50) NOT NULL,
  `Valor2` varchar(50) NOT NULL,
  `Valor3` varchar(50) NOT NULL,
  `Valor4` varchar(50) DEFAULT NULL,
  `Valor5` varchar(50) DEFAULT NULL,
  `Valor6` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`IdValores`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `AccionesComplementarias`
ADD CONSTRAINT `FK_AccionesComplementarias_Empresa` FOREIGN KEY (`FkEmpresa`) REFERENCES `Empresa` (`IdEmpresa`);

ALTER TABLE `AnalisisFoda`
ADD CONSTRAINT `FK_AnalisisFoda_Empresa` FOREIGN KEY (`FkEmpresa`) REFERENCES `Empresa` (`IdEmpresa`);

ALTER TABLE `Empresa`
ADD CONSTRAINT `FK_Empresa_AccionesComplementarias` FOREIGN KEY (`FkAccionesCompetitivas`) REFERENCES `AccionesComplementarias` (`IdAcciones`),
ADD CONSTRAINT `FK_Empresa_AnalisisFoda` FOREIGN KEY (`FkAnálisisFODA`) REFERENCES `AnalisisFoda` (`idAnalisis`),
ADD CONSTRAINT `FK_Empresa_ObjetivosEstrategicos` FOREIGN KEY (`FkObjetivosEstrategicos`) REFERENCES `ObjetivosEstrategicos` (`IDobjetivosEst`),
ADD CONSTRAINT `FK_Empresa_Usuario` FOREIGN KEY (`FkUsuario`) REFERENCES `Usuario` (`IdUsuario`),
ADD CONSTRAINT `FK_Empresa_Valores` FOREIGN KEY (`FkValores`) REFERENCES `Valores` (`IdValores`);

ALTER TABLE `ObjetivosEspecificos`
ADD CONSTRAINT `FK_ObjetivosEspecificos_ObjetivosGenerales` FOREIGN KEY (`FkObjetivosGen`) REFERENCES `ObjetivosGenerales` (`idObjGen`);

ALTER TABLE `ObjetivosEstrategicos`
ADD CONSTRAINT `FK_ObjetivosEstrategicos_Empresa` FOREIGN KEY (`FkEmpresa`) REFERENCES `Empresa` (`IdEmpresa`),
ADD CONSTRAINT `FK_ObjetivosEstrategicos_ObjetivosGenerales` FOREIGN KEY (`FkObjetivosGenerales`) REFERENCES `ObjetivosGenerales` (`idObjGen`);

ALTER TABLE `ObjetivosGenerales`
ADD CONSTRAINT `FK_ObjetivosGenerales_ObjetivosEstrategicos` FOREIGN KEY (`FkObjetivosEst`) REFERENCES `ObjetivosEstrategicos` (`IDobjetivosEst`);

ALTER TABLE `Valoracion`
ADD CONSTRAINT `FK_Valoracion_Autodiagnostico` FOREIGN KEY (`FkAutodiagnostico`) REFERENCES `Autodiagnostico` (`IdAutodiagnostico`);

ALTER TABLE `Valores`
ADD CONSTRAINT `FK_Valores_Empresa` FOREIGN KEY (`FkEmpresa`) REFERENCES `Empresa` (`IdEmpresa`);
```
