# ProyectoGrupal-PETI
## Base de datos
### Diagrama de base de datos del proyecto:

![image](https://github.com/JeanValverde24/ProyectoGrupal-PETI/assets/90206909/62add64e-94c9-420f-8c9c-3c5ad1868b63)

### Scripts parala base de datos:
```sql
-- Tabla AccionesComplementarias
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
  PRIMARY KEY (`IdAcciones`),
  KEY `FK_AccionesComplementarias_Empresa` (`FkEmpresa`),
  CONSTRAINT `FK_AccionesComplementarias_Empresa` FOREIGN KEY (`FkEmpresa`) REFERENCES `Empresa` (`IdEmpresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla AnalisisFoda
CREATE TABLE `AnalisisFoda` (
  `idAnalisis` int NOT NULL,
  `FkEmpresa` int NOT NULL,
  `FkDebilidades` int NOT NULL,
  `FkAmenazas` int NOT NULL,
  `FkFortalezas` int NOT NULL,
  `FkOportunidades` int NOT NULL,
  PRIMARY KEY (`idAnalisis`),
  KEY `FK_AnalisisFoda_Empresa` (`FkEmpresa`),
  CONSTRAINT `FK_AnalisisFoda_Empresa` FOREIGN KEY (`FkEmpresa`) REFERENCES `Empresa` (`IdEmpresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Tabla Empresa
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
  PRIMARY KEY (`IdEmpresa`),
  KEY `FK_Empresa_Usuario` (`FkUsuario`),
  KEY `FK_Empresa_ObjetivosEstrategicos` (`FkObjetivosEstrategicos`),
  KEY `FK_Empresa_Valores` (`FkValores`),
  KEY `FK_Empresa_AccionesComplementarias` (`FkAccionesCompetitivas`),
  KEY `FK_Empresa_AnalisisFoda` (`FkAnálisisFODA`),
  CONSTRAINT `FK_Empresa_AccionesComplementarias` FOREIGN KEY (`FkAccionesCompetitivas`) REFERENCES `AccionesComplementarias` (`IdAcciones`),
  CONSTRAINT `FK_Empresa_AnalisisFoda` FOREIGN KEY (`FkAnálisisFODA`) REFERENCES `AnalisisFoda` (`idAnalisis`),
  CONSTRAINT `FK_Empresa_ObjetivosEstrategicos` FOREIGN KEY (`FkObjetivosEstrategicos`) REFERENCES `ObjetivosEstrategicos` (`IDobjetivosEst`),
  CONSTRAINT `FK_Empresa_Usuario` FOREIGN KEY (`FkUsuario`) REFERENCES `Usuario` (`IdUsuario`),
  CONSTRAINT `FK_Empresa_Valores` FOREIGN KEY (`FkValores`) REFERENCES `Valores` (`IdValores`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla ObjetivosEspecificos
CREATE TABLE `ObjetivosEspecificos` (
  `IdObjEsp` int NOT NULL,
  `FkObjetivosGen` int NOT NULL,
  `ObjEspecifico1` text NOT NULL,
  `ObjEspecifico2` text NOT NULL,
  `ObjEspecifico3` text NOT NULL,
  `ObjEspecifico4` text NOT NULL,
  `ObjEspecifico5` text NOT NULL,
  `ObjEspecifico6` text NOT NULL,
  PRIMARY KEY (`IdObjEsp`),
  KEY `FK_ObjetivosEspecificos_ObjetivosGenerales` (`FkObjetivosGen`),
  CONSTRAINT `FK_ObjetivosEspecificos_ObjetivosGenerales` FOREIGN KEY (`FkObjetivosGen`) REFERENCES `ObjetivosGenerales` (`idObjGen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla ObjetivosEstrategicos
CREATE TABLE `ObjetivosEstrategicos` (
  `IDobjetivosEst` int NOT NULL,
  `FkEmpresa` int NOT NULL,
  `FkObjetivosGenerales` int NOT NULL,
  PRIMARY KEY (`IDobjetivosEst`),
  KEY `FK_ObjetivosEstrategicos_Empresa` (`FkEmpresa`),
  KEY `FK_ObjetivosEstrategicos_ObjetivosGenerales` (`FkObjetivosGenerales`),
  CONSTRAINT `FK_ObjetivosEstrategicos_Empresa` FOREIGN KEY (`FkEmpresa`) REFERENCES `Empresa` (`IdEmpresa`),
  CONSTRAINT `FK_ObjetivosEstrategicos_ObjetivosGenerales` FOREIGN KEY (`FkObjetivosGenerales`) REFERENCES `ObjetivosGenerales` (`idObjGen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla ObjetivosGenerales
CREATE TABLE `ObjetivosGenerales` (
  `idObjGen` int NOT NULL,
  `FkObjetivosEst` int NOT NULL,
  `ObjGeneral1` text NOT NULL,
  `ObjGeneral2` text NOT NULL,
  `ObjGeneral3` text NOT NULL,
  PRIMARY KEY (`idObjGen`),
  KEY `FK_ObjetivosGenerales_ObjetivosEstrategicos` (`FkObjetivosEst`),
  CONSTRAINT `FK_ObjetivosGenerales_ObjetivosEstrategicos` FOREIGN KEY (`FkObjetivosEst`) REFERENCES `ObjetivosEstrategicos` (`IDobjetivosEst`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Tabla Usuario
CREATE TABLE `Usuario` (
  `IdUsuario` int NOT NULL AUTO_INCREMENT,
  `Usuario` varchar(150) NOT NULL,
  `Nombres` varchar(150) NOT NULL,
  `Apellidos` varchar(150) NOT NULL,
  `Correo` varchar(250) NOT NULL,
  `Celular` varchar(9) NOT NULL,
  `Contraseña` varchar(257) NOT NULL,
  PRIMARY KEY (`IdUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla Valoracion
CREATE TABLE `Valoracion` (
  `IdValoracion` int NOT NULL,
  `FkAutodiagnostico` int NOT NULL,
  `Punto0` char(2) NOT NULL,
  `Punto1` char(2) NOT NULL,
  `Punto2` char(2) NOT NULL,
  `Punto3` char(2) NOT NULL,
  `Punto4` char(2) NOT NULL,
  PRIMARY KEY (`IdValoracion`),
  KEY `FK_Valoracion_Autodiagnostico` (`FkAutodiagnostico`),
  CONSTRAINT `FK_Valoracion_Autodiagnostico` FOREIGN KEY (`FkAutodiagnostico`) REFERENCES `Autodiagnostico` (`IdAutodiagnostico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Tabla Valores
CREATE TABLE `Valores` (
  `IdValores` int NOT NULL,
  `FkEmpresa` int NOT NULL,
  `Valor1` varchar(50) NOT NULL,
  `Valor2` varchar(50) NOT NULL,
  `Valor3` varchar(50) NOT NULL,
  `Valor4` varchar(50) DEFAULT NULL,
  `Valor5` varchar(50) DEFAULT NULL,
  `Valor6` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`IdValores`),
  KEY `FK_Valores_Empresa` (`FkEmpresa`),
  CONSTRAINT `FK_Valores_Empresa` FOREIGN KEY (`FkEmpresa`) REFERENCES `Empresa` (`IdEmpresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```
- *Esta es una base de datos de prueba, el modelo seguira siendo el mismo pero el motor de base de datos va a variar*

