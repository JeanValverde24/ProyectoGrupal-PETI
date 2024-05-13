# ProyectoGrupal-PETI
## Base de datos
### Diagrama de base de datos del proyecto:

![image](https://github.com/JeanValverde24/ProyectoGrupal-PETI/assets/90206909/62add64e-94c9-420f-8c9c-3c5ad1868b63)

### Scripts parala base de datos:
```sql
USE [PETI-PROYECTO]
GO
/****** Object:  Table [dbo].[AccionesComplementarias]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AccionesComplementarias](
	[IdAcciones] [int] NOT NULL,
	[FkEmpresa] [int] NOT NULL,
	[Accion1] [text] NULL,
	[Accion2] [text] NULL,
	[Accion3] [text] NULL,
	[Accion4] [text] NULL,
	[Accion5] [text] NULL,
	[Accion6] [text] NULL,
	[Accion7] [text] NULL,
	[Accion8] [text] NULL,
	[Accion9] [text] NULL,
	[Accion10] [text] NULL,
	[Accion11] [text] NULL,
	[Accion12] [text] NULL,
	[Accion13] [text] NULL,
	[Accion14] [text] NULL,
	[Accion15] [text] NULL,
	[Accion16] [text] NULL,
 CONSTRAINT [PK_AccionesComplementarias] PRIMARY KEY CLUSTERED 
(
	[IdAcciones] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AnalisisFoda]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AnalisisFoda](
	[idAnalisis] [int] NOT NULL,
	[FkEmpresa] [int] NOT NULL,
	[FkDebilidades] [int] NOT NULL,
	[FkAmenazas] [int] NOT NULL,
	[FkFortalezas] [int] NOT NULL,
	[FkOportunidades] [int] NOT NULL,
 CONSTRAINT [PK_AnalisisFoda] PRIMARY KEY CLUSTERED 
(
	[idAnalisis] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Autodiagnostico]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Autodiagnostico](
	[IdAutodiagnostico] [int] NOT NULL,
	[FkEmpresa] [int] NOT NULL,
	[Resultado] [varchar](5) NOT NULL,
 CONSTRAINT [PK_Autodiagnostico] PRIMARY KEY CLUSTERED 
(
	[IdAutodiagnostico] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CarteraProd]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CarteraProd](
	[IdCarteraProd] [int] NOT NULL,
	[FkPrevisionVentas] [int] NOT NULL,
	[FkTCM] [int] NOT NULL,
	[FkEvo_Dem_Glob_Sec] [int] NOT NULL,
	[FkNiveles_De_Venas] [int] NOT NULL,
 CONSTRAINT [PK_CarteraProd] PRIMARY KEY CLUSTERED 
(
	[IdCarteraProd] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Empresa]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Empresa](
	[IdEmpresa] [int] IDENTITY(1,1) NOT NULL,
	[FkUsuario] [int] NOT NULL,
	[NombreEmpresa] [varchar](150) NOT NULL,
	[Mision] [text] NOT NULL,
	[Vision] [text] NOT NULL,
	[FkValores] [int] NOT NULL,
	[UnidadesEstrategicas] [text] NOT NULL,
	[FkObjetivosEstrategicos] [int] NOT NULL,
	[FkAnálisisFODA] [int] NOT NULL,
	[IdeEstrategicas] [text] NOT NULL,
	[FkAccionesCompetitivas] [int] NOT NULL,
	[Conclusiones] [text] NOT NULL,
 CONSTRAINT [PK_Empresa] PRIMARY KEY CLUSTERED 
(
	[IdEmpresa] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ObjetivosEspecificos]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ObjetivosEspecificos](
	[IdObjEsp] [int] NOT NULL,
	[FkObjetivosGen] [int] NOT NULL,
	[ObjEspecifico1] [text] NOT NULL,
	[ObjEspecifico2] [text] NOT NULL,
	[ObjEspecifico3] [text] NOT NULL,
	[ObjEspecifico4] [text] NOT NULL,
	[ObjEspecifico5] [text] NOT NULL,
	[ObjEspecifico6] [text] NOT NULL,
 CONSTRAINT [PK_ObjetivosEspecificos] PRIMARY KEY CLUSTERED 
(
	[IdObjEsp] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ObjetivosEstrategicos]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ObjetivosEstrategicos](
	[IDobjetivosEst] [int] NOT NULL,
	[FkEmpresa] [int] NOT NULL,
	[FkObjetivosGenerales] [int] NOT NULL,
 CONSTRAINT [PK_ObjetivosEstrategicos] PRIMARY KEY CLUSTERED 
(
	[IDobjetivosEst] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ObjetivosGenerales]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ObjetivosGenerales](
	[idObjGen] [int] NOT NULL,
	[FkObjetivosEst] [int] NOT NULL,
	[ObjGeneral1] [text] NOT NULL,
	[ObjGeneral2] [text] NOT NULL,
	[ObjGeneral3] [text] NOT NULL,
 CONSTRAINT [PK_ObjetivosGenerales] PRIMARY KEY CLUSTERED 
(
	[idObjGen] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PrevisionVentas]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PrevisionVentas](
	[IdPreVentas] [int] NULL,
	[FkCarteraProd] [int] NULL,
	[Producto1] [int] NULL,
	[Producto2] [int] NULL,
	[Producto3] [int] NULL,
	[Producto4] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Usuario]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Usuario](
	[IdUsuario] [int] IDENTITY(1,1) NOT NULL,
	[Usuario] [varchar](150) NOT NULL,
	[Nombres] [varchar](150) NOT NULL,
	[Apellidos] [varchar](150) NOT NULL,
	[Correo] [varchar](250) NOT NULL,
	[Celular] [varchar](9) NOT NULL,
	[Contraseña] [varchar](257) NOT NULL,
 CONSTRAINT [PK_Usuario] PRIMARY KEY CLUSTERED 
(
	[IdUsuario] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Valoracion]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Valoracion](
	[IdValoracion] [int] NOT NULL,
	[FkAutodiagnostico] [int] NOT NULL,
	[Punto0] [char](2) NOT NULL,
	[Punto1] [char](2) NOT NULL,
	[Punto2] [char](2) NOT NULL,
	[Punto3] [char](2) NOT NULL,
	[Punto4] [char](2) NOT NULL,
 CONSTRAINT [PK_Valoracion] PRIMARY KEY CLUSTERED 
(
	[IdValoracion] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Valores]    Script Date: 12-05-2024 23:00:16 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Valores](
	[IdValores] [int] NOT NULL,
	[FkEmpresa] [int] NOT NULL,
	[Valor1] [varchar](50) NOT NULL,
	[Valor2] [varchar](50) NOT NULL,
	[Valor3] [varchar](50) NOT NULL,
	[Valor4] [varchar](50) NULL,
	[Valor5] [varchar](50) NULL,
	[Valor6] [varchar](50) NULL,
 CONSTRAINT [PK_Valores] PRIMARY KEY CLUSTERED 
(
	[IdValores] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[AccionesComplementarias]  WITH CHECK ADD  CONSTRAINT [FK_AccionesComplementarias_Empresa] FOREIGN KEY([FkEmpresa])
REFERENCES [dbo].[Empresa] ([IdEmpresa])
GO
ALTER TABLE [dbo].[AccionesComplementarias] CHECK CONSTRAINT [FK_AccionesComplementarias_Empresa]
GO
ALTER TABLE [dbo].[AnalisisFoda]  WITH CHECK ADD  CONSTRAINT [FK_AnalisisFoda_Empresa] FOREIGN KEY([FkEmpresa])
REFERENCES [dbo].[Empresa] ([IdEmpresa])
GO
ALTER TABLE [dbo].[AnalisisFoda] CHECK CONSTRAINT [FK_AnalisisFoda_Empresa]
GO
ALTER TABLE [dbo].[Empresa]  WITH CHECK ADD  CONSTRAINT [FK_Empresa_AccionesComplementarias] FOREIGN KEY([FkAccionesCompetitivas])
REFERENCES [dbo].[AccionesComplementarias] ([IdAcciones])
GO
ALTER TABLE [dbo].[Empresa] CHECK CONSTRAINT [FK_Empresa_AccionesComplementarias]
GO
ALTER TABLE [dbo].[Empresa]  WITH CHECK ADD  CONSTRAINT [FK_Empresa_AnalisisFoda] FOREIGN KEY([FkAnálisisFODA])
REFERENCES [dbo].[AnalisisFoda] ([idAnalisis])
GO
ALTER TABLE [dbo].[Empresa] CHECK CONSTRAINT [FK_Empresa_AnalisisFoda]
GO
ALTER TABLE [dbo].[Empresa]  WITH CHECK ADD  CONSTRAINT [FK_Empresa_ObjetivosEstrategicos] FOREIGN KEY([FkObjetivosEstrategicos])
REFERENCES [dbo].[ObjetivosEstrategicos] ([IDobjetivosEst])
GO
ALTER TABLE [dbo].[Empresa] CHECK CONSTRAINT [FK_Empresa_ObjetivosEstrategicos]
GO
ALTER TABLE [dbo].[Empresa]  WITH CHECK ADD  CONSTRAINT [FK_Empresa_Usuario] FOREIGN KEY([FkUsuario])
REFERENCES [dbo].[Usuario] ([IdUsuario])
GO
ALTER TABLE [dbo].[Empresa] CHECK CONSTRAINT [FK_Empresa_Usuario]
GO
ALTER TABLE [dbo].[Empresa]  WITH CHECK ADD  CONSTRAINT [FK_Empresa_Valores] FOREIGN KEY([FkValores])
REFERENCES [dbo].[Valores] ([IdValores])
GO
ALTER TABLE [dbo].[Empresa] CHECK CONSTRAINT [FK_Empresa_Valores]
GO
ALTER TABLE [dbo].[ObjetivosEspecificos]  WITH CHECK ADD  CONSTRAINT [FK_ObjetivosEspecificos_ObjetivosGenerales] FOREIGN KEY([FkObjetivosGen])
REFERENCES [dbo].[ObjetivosGenerales] ([idObjGen])
GO
ALTER TABLE [dbo].[ObjetivosEspecificos] CHECK CONSTRAINT [FK_ObjetivosEspecificos_ObjetivosGenerales]
GO
ALTER TABLE [dbo].[ObjetivosEstrategicos]  WITH CHECK ADD  CONSTRAINT [FK_ObjetivosEstrategicos_Empresa] FOREIGN KEY([FkEmpresa])
REFERENCES [dbo].[Empresa] ([IdEmpresa])
GO
ALTER TABLE [dbo].[ObjetivosEstrategicos] CHECK CONSTRAINT [FK_ObjetivosEstrategicos_Empresa]
GO
ALTER TABLE [dbo].[ObjetivosEstrategicos]  WITH CHECK ADD  CONSTRAINT [FK_ObjetivosEstrategicos_ObjetivosGenerales] FOREIGN KEY([FkObjetivosGenerales])
REFERENCES [dbo].[ObjetivosGenerales] ([idObjGen])
GO
ALTER TABLE [dbo].[ObjetivosEstrategicos] CHECK CONSTRAINT [FK_ObjetivosEstrategicos_ObjetivosGenerales]
GO
ALTER TABLE [dbo].[ObjetivosGenerales]  WITH CHECK ADD  CONSTRAINT [FK_ObjetivosGenerales_ObjetivosEstrategicos] FOREIGN KEY([FkObjetivosEst])
REFERENCES [dbo].[ObjetivosEstrategicos] ([IDobjetivosEst])
GO
ALTER TABLE [dbo].[ObjetivosGenerales] CHECK CONSTRAINT [FK_ObjetivosGenerales_ObjetivosEstrategicos]
GO
ALTER TABLE [dbo].[Valoracion]  WITH CHECK ADD  CONSTRAINT [FK_Valoracion_Autodiagnostico] FOREIGN KEY([FkAutodiagnostico])
REFERENCES [dbo].[Autodiagnostico] ([IdAutodiagnostico])
GO
ALTER TABLE [dbo].[Valoracion] CHECK CONSTRAINT [FK_Valoracion_Autodiagnostico]
GO
ALTER TABLE [dbo].[Valores]  WITH CHECK ADD  CONSTRAINT [FK_Valores_Empresa] FOREIGN KEY([FkEmpresa])
REFERENCES [dbo].[Empresa] ([IdEmpresa])
GO
ALTER TABLE [dbo].[Valores] CHECK CONSTRAINT [FK_Valores_Empresa]
GO
```
- *Esta es una base de datos de prueba, el modelo seguira siendo el mismo pero el motor de base de datos va a variar*

