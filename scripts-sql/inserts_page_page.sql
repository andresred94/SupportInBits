-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-04-2025 a las 17:03:53
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `supportinbits`
--
USE supportinbits;
--
-- Volcado de datos para la tabla `page_page`
--

INSERT INTO `page_page` (`id`, `titulo`, `m_descri`, `m_handF`, `m_mobileOp`, `m_robots`) VALUES
(1, 'Support In Bits | Inicio', 'Web desarrollada para fomentar la creación de aplicaciones web usables y accesibles', 'true', 'width', 'index'),
(2, 'Support In Bits | Política de cookies', 'Página web con toda la información relacionada sobre qué hacemos con sus datos en Support In Bits', 'true', 'width', 'noindex'),
(3, 'Support In Bits | Quien soy', 'En esta página web se describe al creador de la web', 'true', 'width', 'noindex'),
(4, 'Support In Bits | Políticas de privacidad', 'En esta página se muestra las políticas de privacidad de Support In Bits', 'true', 'width', 'noindex'),
(5, 'Support In Bits | Preguntas frecuentes', 'En esta página encontrarás las respuestas a tus preguntas de c¾mo desarrollar una web accesible', 'true', 'width', 'index');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
