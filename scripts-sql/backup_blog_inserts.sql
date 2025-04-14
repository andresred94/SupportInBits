-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-04-2025 a las 14:36:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

SET FOREIGN_KEY_CHECKS = 0;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `supportinbits`
--

--
-- Volcado de datos para la tabla `blog_categoria`
--
-- TRUNCATE `blog_seccion`;

INSERT INTO `blog_seccion` (`id`, `nombre`, `slug`, `descripcion`) VALUES
(1, 'tutoriales', 'tutoriales-sobre-informatica', 'En esta categoría encontrarás entradas tutoriales sobre cableado de redes, montaje de ordenadores o consejos para mejorar la accesibilidad de tu sitio web.');

-- TRUNCATE 'blog_categoria';

INSERT INTO `blog_categoria` (`id`, `nombre`, `slug`, `descripcion`) VALUES
(1, 'redes', 'todo-sobre-redes', 'En esta categoría se muestran entradas sobre redes locales, desde cómo cablear tu casa para conectar un ordenador o cómo reutilizar un router como punto de acceso.');

--
-- Volcado de datos para la tabla `blog_entrada`
--
-- TRUNCATE 'blog_entrada';

INSERT INTO `blog_entrada` (`id`, `titulo`, `slug`, `contenido`, `resumen`, `fecha_publicacion`, `fecha_actualizacion`, `publicado`, `imagen_portada`, `categoria_id`, `pagina_id`) VALUES
(1, 'Mi primera entrada', 'esto-es-la-primera-entrada', '\r\nThe standard Lorem Ipsum passage, used since the 1500s\r\n\r\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\r\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\r\n\r\n\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"\r\n1914 translation by H. Rackham\r\n\r\n\"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?\"\r\nSection 1.10.33 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\r\n\r\n\"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.\"\r\n1914 translation by H. Rackham\r\n\r\n\"On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains.\"\r\n', '\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\r\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC', '2025-04-11 13:08:05.000000', '2025-04-11 13:08:05.000000', 1, '/staticFiles/supportinbits/img/ambc.jpg', 1, 1);

--
-- Volcado de datos para la tabla `blog_seccion`
--

--
-- Volcado de datos para la tabla `page_page`
--

TRUNCATE `page_page`;

INSERT INTO `page_page` (`id`, `titulo`, `m_descri`, `m_handF`, `m_mobileOp`, `m_robots`) VALUES
(1, 'Support In Bits | Inicio', 'Web desarrollada para fomentar la creación de aplicaciones web usables y accesibles', 'true', 'width', 'index'),
(2, 'Support In Bits | Política de cookies', 'Página web con toda la información relacionada sobre qué hacemos con sus datos en Support In Bits', 'true', 'width', 'noindex'),
(3, 'Support In Bits | Quien soy', 'En esta página web se describe al creador de la web', 'true', 'width', 'noindex'),
(4, 'Support In Bits | Políticas de privacidad', 'En esta página se muestra las políticas de privacidad de Support In Bits', 'true', 'width', 'noindex'),
(5, 'Support In Bits | Preguntas frecuentes', 'En esta página encontrarás las respuestas a tus preguntas de c¾mo desarrollar una web accesible', 'true', 'width', 'index'),
(6, 'Support In Bits | Blog', 'En esta página encontrarás todos las entradas publicadas de diversos temas sobre informática y accesibilidad', 'true', 'width', 'index'),
(7, 'Support In Bits | Crear entrada', 'En esta página puedes crear tu entrada y comprobar que cumple con los requisitos de accesibilidad', 'true', 'width', 'noindex');

SET FOREIGN_KEY_CHECKS = 1;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
