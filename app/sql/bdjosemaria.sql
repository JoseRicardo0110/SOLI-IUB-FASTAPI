-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-04-2024 a las 05:37:20
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdjosemaria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `IdArea` int(11) NOT NULL,
  `Facultad` text NOT NULL,
  `Programa` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `area`
--

INSERT INTO `area` (`IdArea`, `Facultad`, `Programa`) VALUES
(1, 'ingenieria', 'telematica'),
(2, 'ingenieria', 'tecnico electromecanico'),
(3, 'Ciencia económicas y administrativas', 'Administración de empresas'),
(4, 'Ciencias económicas y administrativas', 'Administración de negocios internacionales');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributo`
--

CREATE TABLE `atributo` (
  `id` int(11) NOT NULL,
  `nombre` text NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `atributo`
--

INSERT INTO `atributo` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Dirección', 'La dirección de vivienda del estudiante '),
(2, 'Solicitudes asignadas', 'es una cantidad variable que indica la cantidad de solicitudes que tiene la persona asignada en el momento, eso puede aumentar y disminuir dependiendo las solicitudes que responda o si se quita la asignación a una solicitud');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributoxusuario`
--

CREATE TABLE `atributoxusuario` (
  `id` int(11) NOT NULL,
  `idusuario` int(11) NOT NULL,
  `idatributo` int(11) NOT NULL,
  `valor` text NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `atributoxusuario`
--

INSERT INTO `atributoxusuario` (`id`, `idusuario`, `idatributo`, `valor`, `descripcion`) VALUES
(1, 1, 1, 'carrera 17 #20-10', 'Barranquilla cerca de la parroquia Fátima ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `respuesta`
--

CREATE TABLE `respuesta` (
  `idRespuesta` int(11) NOT NULL,
  `idSolicitud` int(20) NOT NULL,
  `DescripcionRespuesta` text NOT NULL,
  `FechaRespuesta` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `IdRol` int(20) NOT NULL,
  `NombreRol` text NOT NULL,
  `DescripcionRol` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`IdRol`, `NombreRol`, `DescripcionRol`) VALUES
(1, 'administrador', 'administrador del software'),
(2, 'solicitante', 'usuario limitado exclusivamente a la creación de solicitudes y seguimiento del estado de las que el mismo ha creado'),
(3, 'líder', 'persona a cargo de asignar las solicitudes'),
(4, 'consejero', 'persona a cargo de darle resolución a las solicitudes');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rolxusuario`
--

CREATE TABLE `rolxusuario` (
  `Id` int(11) NOT NULL,
  `IdXUsuario` int(11) NOT NULL,
  `IdRol` int(11) NOT NULL,
  `ValorRolXUsuario` text NOT NULL,
  `DescripcionRolXUsuario` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rolxusuario`
--

INSERT INTO `rolxusuario` (`Id`, `IdXUsuario`, `IdRol`, `ValorRolXUsuario`, `DescripcionRolXUsuario`) VALUES
(1, 1, 1, 'Líder de proyecto ', 'persona a cargo de desarrollar el proyecto'),
(2, 2, 2, 'Estudiante técnico ', 'el estudiante con nombre amartinez con el Id(2) capaz de general solicitudes '),
(3, 3, 3, 'Lider de area', 'lider de areaa de ingenieria telematica, puede resolver solicitudes y asignarlas '),
(4, 5, 1, 'desarrolladora del software', 'se encarga de desarrollar lo relacionado a la vista del programa'),
(5, 4, 2, 'estudiante tecnólogo', 'estudiante tecnológico'),
(6, 7, 4, 'consejero de ingenieria telematica', 'consejero del area de ingenieria telematica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitud`
--

CREATE TABLE `solicitud` (
  `idSolicitud` int(11) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `IdTipoSolicitud` int(11) NOT NULL,
  `idpersonaAsignada` int(11) NOT NULL,
  `Archivos` text NOT NULL,
  `Asunto` text NOT NULL,
  `nota` text NOT NULL,
  `FechaCreacion` varchar(20) NOT NULL,
  `FechaUltimaModificacion` varchar(20) NOT NULL,
  `estado` text NOT NULL,
  `prioridad` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `solicitud`
--

INSERT INTO `solicitud` (`idSolicitud`, `idUsuario`, `IdTipoSolicitud`, `idpersonaAsignada`, `Archivos`, `Asunto`, `nota`, `FechaCreacion`, `FechaUltimaModificacion`, `estado`, `prioridad`) VALUES
(1, 1, 1, 7, '', 'solicito creditos unicos para programacion I', '', '', '', 'finalizada', ''),
(2, 4, 5, 0, '', 'no me gusta la profe lourdes prefiero a bryan ', '', '', '', 'sin asignar', ''),
(3, 2, 3, 0, '', 'No me deja matricular :( aparecen créditos en 0', '', '', '', 'sin asignar', ''),
(4, 4, 6, 0, '', 'Me quedo grande programación, quiero pasarme a diseño grafico ', '', '', '', 'finalizada', ''),
(5, 6, 5, 6, '', 'necesito cambiar a un grupo que sea los martes del modulo de catedra de la paz quedo atenta a cualquier observación ', '', '', '', 'pendiente', ''),
(9, 1, 4, 0, '', 'Necesito retirar programacion I porque me quedo grande señores:(', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiposolicitud`
--

CREATE TABLE `tiposolicitud` (
  `IDTipoSolicitud` int(11) NOT NULL,
  `valor` text NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tiposolicitud`
--

INSERT INTO `tiposolicitud` (`IDTipoSolicitud`, `valor`, `descripcion`) VALUES
(1, 'Créditos únicos', 'Son aquellos que solicita el estudiante cuando desea matricular módulos que sumen hasta siete (7) créditos en el periodo académico.'),
(2, 'Créditos adicionales', 'son aquellos en donde “Los estudiantes que necesiten cursar un número de créditos por fuera de los límites indicados sólo podrán hacerlo previa autorización del Director de Programa o quien haga sus veces, sin que se exceda en ningún caso, el veinte por ciento (20%) de los créditos establecidos institucionalmente por período, y no haya interferencia de horarios” (Parágrafo 5 del artículo 51 - Reglamento Estudiantil).'),
(3, 'Matricula', 'tipo de solicitud relacionada a los problemas al matricular'),
(4, 'retiro de modulos ', 'tipo de solicitud relacionada a que la persona necesita retirar un modulo que matriculo'),
(5, 'Cambio de grupo', 'solicitud relacionada con que un estudiante necesita cambiar un modulo por otro'),
(6, 'Transferencia internas', 'Solicitud relacionada a que una persona quiere cambiar de programa internamente en la universidad');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `IdArea` int(11) NOT NULL,
  `usuario` text NOT NULL,
  `contrasena` text NOT NULL,
  `nombre` text NOT NULL,
  `apellido` text NOT NULL,
  `documento` text NOT NULL,
  `teléfono` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `IdArea`, `usuario`, `contrasena`, `nombre`, `apellido`, `documento`, `teléfono`) VALUES
(1, 1, 'jangelricardo', '12345', 'Jose Angel', 'Ricardo Hernandez', '102030467', '3209902456'),
(2, 1, 'amartinez', '54321', 'Ana Maria', 'Martinez Villa', '1021456789', '3205106678'),
(3, 1, 'Bsuarezpeña', '123456', 'benito suarez', 'peña nieto', '1000258741', '018003000444'),
(4, 4, 'jmiguelramirez', '123456', 'José miguel ', 'Ramirez prado', '10001542584', '3012525634'),
(5, 2, 'mfernandezsalcedo', '123456', 'maria fernanda', 'salcedo de la rosa', '1003345658', '3022167894'),
(6, 1, 'iflorez', '098765', 'isabella', 'florez fulleda', '1021433687', '3014901080'),
(7, 1, 'spaez', '129012', 'Samuel David', 'Paez Cogollo', '72405087', '323570890');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`IdArea`);

--
-- Indices de la tabla `atributo`
--
ALTER TABLE `atributo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `atributoxusuario`
--
ALTER TABLE `atributoxusuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idusuario` (`idusuario`,`idatributo`),
  ADD KEY `idatributo` (`idatributo`);

--
-- Indices de la tabla `respuesta`
--
ALTER TABLE `respuesta`
  ADD PRIMARY KEY (`idRespuesta`),
  ADD KEY `idSolicitud` (`idSolicitud`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`IdRol`);

--
-- Indices de la tabla `rolxusuario`
--
ALTER TABLE `rolxusuario`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `IdXUsuario` (`IdXUsuario`),
  ADD KEY `IdRol` (`IdRol`);

--
-- Indices de la tabla `solicitud`
--
ALTER TABLE `solicitud`
  ADD PRIMARY KEY (`idSolicitud`),
  ADD KEY `idUsuario` (`idUsuario`),
  ADD KEY `IdTipoSolicitud` (`IdTipoSolicitud`),
  ADD KEY `idpersonaAsignada` (`idpersonaAsignada`);

--
-- Indices de la tabla `tiposolicitud`
--
ALTER TABLE `tiposolicitud`
  ADD PRIMARY KEY (`IDTipoSolicitud`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IdArea` (`IdArea`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `atributo`
--
ALTER TABLE `atributo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `atributoxusuario`
--
ALTER TABLE `atributoxusuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `respuesta`
--
ALTER TABLE `respuesta`
  MODIFY `idRespuesta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `atributoxusuario`
--
ALTER TABLE `atributoxusuario`
  ADD CONSTRAINT `atributoxusuario_ibfk_1` FOREIGN KEY (`idatributo`) REFERENCES `atributo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `atributoxusuario_ibfk_2` FOREIGN KEY (`idusuario`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `rolxusuario`
--
ALTER TABLE `rolxusuario`
  ADD CONSTRAINT `rolxusuario_ibfk_2` FOREIGN KEY (`IdRol`) REFERENCES `rol` (`IdRol`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rolxusuario_ibfk_3` FOREIGN KEY (`IdXUsuario`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `solicitud`
--
ALTER TABLE `solicitud`
  ADD CONSTRAINT `solicitud_ibfk_2` FOREIGN KEY (`idUsuario`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `solicitud_ibfk_3` FOREIGN KEY (`IdTipoSolicitud`) REFERENCES `tiposolicitud` (`IDTipoSolicitud`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`IdArea`) REFERENCES `area` (`IdArea`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

