-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 16, 2019 at 06:18 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `btresources`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add cart', 1, 'add_cart'),
(2, 'Can change cart', 1, 'change_cart'),
(3, 'Can delete cart', 1, 'delete_cart'),
(4, 'Can view cart', 1, 'view_cart'),
(5, 'Can add member', 2, 'add_member'),
(6, 'Can change member', 2, 'change_member'),
(7, 'Can delete member', 2, 'delete_member'),
(8, 'Can view member', 2, 'view_member'),
(9, 'Can add product', 3, 'add_product'),
(10, 'Can change product', 3, 'change_product'),
(11, 'Can delete product', 3, 'delete_product'),
(12, 'Can view product', 3, 'view_product'),
(13, 'Can add product catergory', 4, 'add_productcatergory'),
(14, 'Can change product catergory', 4, 'change_productcatergory'),
(15, 'Can delete product catergory', 4, 'delete_productcatergory'),
(16, 'Can view product catergory', 4, 'view_productcatergory'),
(17, 'Can add product company', 5, 'add_productcompany'),
(18, 'Can change product company', 5, 'change_productcompany'),
(19, 'Can delete product company', 5, 'delete_productcompany'),
(20, 'Can view product company', 5, 'view_productcompany'),
(21, 'Can add user session', 6, 'add_usersession'),
(22, 'Can change user session', 6, 'change_usersession'),
(23, 'Can delete user session', 6, 'delete_usersession'),
(24, 'Can view user session', 6, 'view_usersession'),
(25, 'Can add log entry', 7, 'add_logentry'),
(26, 'Can change log entry', 7, 'change_logentry'),
(27, 'Can delete log entry', 7, 'delete_logentry'),
(28, 'Can view log entry', 7, 'view_logentry'),
(29, 'Can add permission', 8, 'add_permission'),
(30, 'Can change permission', 8, 'change_permission'),
(31, 'Can delete permission', 8, 'delete_permission'),
(32, 'Can view permission', 8, 'view_permission'),
(33, 'Can add group', 9, 'add_group'),
(34, 'Can change group', 9, 'change_group'),
(35, 'Can delete group', 9, 'delete_group'),
(36, 'Can view group', 9, 'view_group'),
(37, 'Can add user', 10, 'add_user'),
(38, 'Can change user', 10, 'change_user'),
(39, 'Can delete user', 10, 'delete_user'),
(40, 'Can view user', 10, 'view_user'),
(41, 'Can add content type', 11, 'add_contenttype'),
(42, 'Can change content type', 11, 'change_contenttype'),
(43, 'Can delete content type', 11, 'delete_contenttype'),
(44, 'Can view content type', 11, 'view_contenttype'),
(45, 'Can add session', 12, 'add_session'),
(46, 'Can change session', 12, 'change_session'),
(47, 'Can delete session', 12, 'delete_session'),
(48, 'Can view session', 12, 'view_session'),
(49, 'Can add product catergory', 13, 'add_productcatergory'),
(50, 'Can change product catergory', 13, 'change_productcatergory'),
(51, 'Can delete product catergory', 13, 'delete_productcatergory'),
(52, 'Can view product catergory', 13, 'view_productcatergory'),
(53, 'Can add product', 14, 'add_product'),
(54, 'Can change product', 14, 'change_product'),
(55, 'Can delete product', 14, 'delete_product'),
(56, 'Can view product', 14, 'view_product'),
(57, 'Can add product', 15, 'add_product'),
(58, 'Can change product', 15, 'change_product'),
(59, 'Can delete product', 15, 'delete_product'),
(60, 'Can view product', 15, 'view_product'),
(61, 'Can add product catergory', 16, 'add_productcatergory'),
(62, 'Can change product catergory', 16, 'change_productcatergory'),
(63, 'Can delete product catergory', 16, 'delete_productcatergory'),
(64, 'Can view product catergory', 16, 'view_productcatergory'),
(65, 'Can add product', 17, 'add_product'),
(66, 'Can change product', 17, 'change_product'),
(67, 'Can delete product', 17, 'delete_product'),
(68, 'Can view product', 17, 'view_product'),
(69, 'Can add product catergory', 18, 'add_productcatergory'),
(70, 'Can change product catergory', 18, 'change_productcatergory'),
(71, 'Can delete product catergory', 18, 'delete_productcatergory'),
(72, 'Can view product catergory', 18, 'view_productcatergory'),
(73, 'Can add user session', 19, 'add_usersession'),
(74, 'Can change user session', 19, 'change_usersession'),
(75, 'Can delete user session', 19, 'delete_usersession'),
(76, 'Can view user session', 19, 'view_usersession'),
(77, 'Can add users', 20, 'add_users'),
(78, 'Can change users', 20, 'change_users'),
(79, 'Can delete users', 20, 'delete_users'),
(80, 'Can view users', 20, 'view_users'),
(81, 'Can add biotech orders', 21, 'add_biotechorders'),
(82, 'Can change biotech orders', 21, 'change_biotechorders'),
(83, 'Can delete biotech orders', 21, 'delete_biotechorders'),
(84, 'Can view biotech orders', 21, 'view_biotechorders'),
(85, 'Can add flintwood orders', 22, 'add_flintwoodorders'),
(86, 'Can change flintwood orders', 22, 'change_flintwoodorders'),
(87, 'Can delete flintwood orders', 22, 'delete_flintwoodorders'),
(88, 'Can view flintwood orders', 22, 'view_flintwoodorders'),
(89, 'Can add tktitan orders', 23, 'add_tktitanorders'),
(90, 'Can change tktitan orders', 23, 'change_tktitanorders'),
(91, 'Can delete tktitan orders', 23, 'delete_tktitanorders'),
(92, 'Can view tktitan orders', 23, 'view_tktitanorders'),
(93, 'Can add employee', 24, 'add_employee'),
(94, 'Can change employee', 24, 'change_employee'),
(95, 'Can delete employee', 24, 'delete_employee'),
(96, 'Can view employee', 24, 'view_employee'),
(97, 'Can add client session', 25, 'add_clientsession'),
(98, 'Can change client session', 25, 'change_clientsession'),
(99, 'Can delete client session', 25, 'delete_clientsession'),
(100, 'Can view client session', 25, 'view_clientsession'),
(101, 'Can add client', 26, 'add_client'),
(102, 'Can change client', 26, 'change_client'),
(103, 'Can delete client', 26, 'delete_client'),
(104, 'Can view client', 26, 'view_client'),
(105, 'Can add cart', 27, 'add_cart'),
(106, 'Can change cart', 27, 'change_cart'),
(107, 'Can delete cart', 27, 'delete_cart'),
(108, 'Can view cart', 27, 'view_cart'),
(109, 'Can add flint cart', 28, 'add_flintcart'),
(110, 'Can change flint cart', 28, 'change_flintcart'),
(111, 'Can delete flint cart', 28, 'delete_flintcart'),
(112, 'Can view flint cart', 28, 'view_flintcart'),
(113, 'Can add tk cart', 29, 'add_tkcart'),
(114, 'Can change tk cart', 29, 'change_tkcart'),
(115, 'Can delete tk cart', 29, 'delete_tkcart'),
(116, 'Can view tk cart', 29, 'view_tkcart');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$120000$FbB4lvj3TH0x$2iPiAhsLibz0Tt0QXabE71AxCZhZo/oYKC4WBvoJOE0=', '2019-06-07 11:57:43.137458', 1, 'papijames', '', '', 'muema31jk@gmail.com', 1, 1, '2019-05-21 05:25:09.065852'),
(2, 'pbkdf2_sha256$120000$Srp4wGK4mcmP$bPH6Xs3+4nS/aQel4G5B4+YOpZmggWrWQM75Us6/VEs=', '2019-05-23 09:38:44.397561', 0, 'mue', 'James', 'Kennedy', 'muema31jkmue@gmail.com', 0, 1, '2019-05-21 05:38:37.137909'),
(3, 'pbkdf2_sha256$120000$N3w1Y3SD2weH$tSrHf5uMOCgXMRuODIGaDcJxk+1WxxyYFdctYK+YnlM=', '2019-05-21 10:03:27.734379', 0, 'wetre', 'James', 'Kennedy', 'muema31jktre@gmail.com', 0, 1, '2019-05-21 10:03:26.569899'),
(4, 'pbkdf2_sha256$120000$AbOCLGCllkEk$SgGR1YR5YS6WjZBN+jLLFMzJkv/rdiO0qHx+2vOmCsI=', '2019-05-22 11:12:50.041759', 0, 'muej4', 'James', 'Kennedy', 'muema321jk@gmail.com', 0, 1, '2019-05-22 11:12:48.647953'),
(5, 'pbkdf2_sha256$120000$NbTagYZrkmfe$D9nRhJHBuoRf/uRLc3B8Odz/dRkzEY6MfsjDB29Ig/0=', '2019-05-25 10:33:58.891129', 0, 'user', 'James', 'Kennedy', 'muema3123jk@gmail.com', 0, 1, '2019-05-23 11:26:43.752310'),
(6, 'pbkdf2_sha256$120000$SKDz0hGNEFTB$Zok2gpbRSqBcWHmS9TEU8vj9kaILmHxxncq3dUXx75U=', '2019-05-26 09:17:39.249014', 0, 'greenmile', 'James', 'Kennedy', 'muema31qwjk@gmail.com', 0, 1, '2019-05-26 09:17:37.805874'),
(7, 'pbkdf2_sha256$120000$sQNUHQDpmdGH$FI4Qf2JUwYnTMoMfQ0EWrdzL0uIftPF0iqJ188Aze0Y=', '2019-05-26 09:19:39.084409', 0, 'greenmile3', 'James', 'Kennedy', 'muema31qw1jk@gmail.com', 0, 1, '2019-05-26 09:19:37.878589'),
(8, 'pbkdf2_sha256$120000$Ynll4X6PaQug$ss2omy3kP+e/WnUXPOPu7BXHNiROH/tGn5R5/aXGcs0=', '2019-05-26 09:21:01.320460', 0, 'greenmile14', 'James', 'Kennedy', 'muema31qw14jk@gmail.com', 0, 1, '2019-05-26 09:21:00.192867'),
(9, 'pbkdf2_sha256$120000$JW43H3z6YnB7$MPQ6wHYsqqx4NqRidDBQ5FhVqHjjHT1/PJTvbCIb1nY=', '2019-05-26 09:21:40.614754', 0, 'greenmile1445', 'James', 'Kennedy', 'muema31qw1445jk@gmail.com', 0, 1, '2019-05-26 09:21:39.704786'),
(10, 'pbkdf2_sha256$120000$CTjQ57AEZ8SX$l6LCWvu7HIfc402pRvtra+rJmDntRznF+hodMXAKCCg=', '2019-06-07 11:57:18.961669', 0, 'greenmile1446', 'James', 'Kennedy', 'muema31jkdf@gmail.com', 0, 1, '2019-05-26 09:23:11.347847');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `biotech_cart`
--

CREATE TABLE `biotech_cart` (
  `id` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  `Product_name` varchar(254) NOT NULL,
  `Product_description` longtext NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date_created` date NOT NULL,
  `last_modified` date NOT NULL,
  `ProductID_id` int(11) NOT NULL,
  `User_ID_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `biotech_product`
--

CREATE TABLE `biotech_product` (
  `pid` int(11) NOT NULL,
  `name` varchar(254) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `Product_Catergory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `biotech_product`
--

INSERT INTO `biotech_product` (`pid`, `name`, `description`, `price`, `image`, `stock`, `Product_Catergory_id`) VALUES
(2, 'Fabu-Metronidazole susp. 100ml', 'METRONIDAZOLE SUSPENSION 200MG/5ML', '8.00', 'product_images/WhatsApp_Image_2019-05-28_at_10.55.49.jpeg', 100, 1),
(3, 'Fabupharm ascorbic tabs 250mg chew', 'ASCORBIC ACID TABLETS 250MG (CHEWABLE WITH SWEET TASTE)', '108.00', 'product_images/WhatsApp_Image_2019-05-28_at_10.55.51.jpeg', 1000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `biotech_productcatergory`
--

CREATE TABLE `biotech_productcatergory` (
  `id` int(11) NOT NULL,
  `Catergory` varchar(200) NOT NULL,
  `Catergory_summary` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `biotech_productcatergory`
--

INSERT INTO `biotech_productcatergory` (`id`, `Catergory`, `Catergory_summary`) VALUES
(1, 'Medicine', 'The drug provides are quality');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-05-21 05:27:08.515556', '1', 'ProductCompany object (1)', 1, '[{\"added\": {}}]', 5, 1),
(2, '2019-05-21 05:27:18.609266', '1', 'ProductCompany object (1)', 2, '[{\"changed\": {\"fields\": [\"Company\"]}}]', 5, 1),
(3, '2019-05-21 05:27:28.593148', '1', 'ProductCompany object (1)', 2, '[{\"changed\": {\"fields\": [\"Company\"]}}]', 5, 1),
(4, '2019-05-21 05:27:33.935105', '1', 'ProductCompany object (1)', 2, '[]', 5, 1),
(5, '2019-05-21 05:27:40.768527', '1', 'ProductCompany object (1)', 2, '[]', 5, 1),
(6, '2019-05-21 05:27:51.330706', '1', 'ProductCompany object (1)', 2, '[]', 5, 1),
(7, '2019-05-21 05:28:05.538309', '2', 'ProductCompany object (2)', 1, '[{\"added\": {}}]', 5, 1),
(8, '2019-05-21 05:28:18.198494', '3', 'ProductCompany object (3)', 1, '[{\"added\": {}}]', 5, 1),
(9, '2019-05-21 05:28:42.829938', '1', 'ProductCatergory object (1)', 1, '[{\"added\": {}}]', 4, 1),
(10, '2019-05-21 05:28:55.136319', '2', 'ProductCatergory object (2)', 1, '[{\"added\": {}}]', 4, 1),
(11, '2019-05-21 05:29:32.142980', '3', 'ProductCatergory object (3)', 1, '[{\"added\": {}}]', 4, 1),
(12, '2019-05-21 05:29:46.463749', '4', 'ProductCatergory object (4)', 1, '[{\"added\": {}}]', 4, 1),
(13, '2019-05-21 05:35:17.809712', '1', 'green grams', 1, '[{\"added\": {}}]', 3, 1),
(14, '2019-05-21 05:35:52.271789', '2', 'avocado', 1, '[{\"added\": {}}]', 3, 1),
(15, '2019-05-24 16:03:19.771519', '4', 'Copper', 1, '[{\"added\": {}}]', 3, 1),
(16, '2019-05-26 10:34:02.493302', '1', 'ProductCatergory object (1)', 1, '[{\"added\": {}}]', 16, 1),
(17, '2019-05-26 10:35:04.780469', '1', 'Paracetamols', 1, '[{\"added\": {}}]', 15, 1),
(18, '2019-05-26 20:43:23.379821', '1', 'ProductCatergory object (1)', 1, '[{\"added\": {}}]', 13, 1),
(19, '2019-05-26 20:44:22.467372', '1', 'green grams', 1, '[{\"added\": {}}]', 14, 1),
(20, '2019-05-26 21:58:06.635785', '1', 'ProductCatergory object (1)', 1, '[{\"added\": {}}]', 18, 1),
(21, '2019-05-26 21:58:43.440313', '1', 'Copper', 1, '[{\"added\": {}}]', 17, 1),
(22, '2019-05-26 22:14:00.005709', '1', 'Client object (1)', 2, '[]', 26, 1),
(23, '2019-06-01 05:22:28.285108', '2', 'ProductCatergory object (2)', 1, '[{\"added\": {}}]', 18, 1),
(24, '2019-06-01 05:22:44.006779', '2', 'ProductCatergory object (2)', 2, '[{\"changed\": {\"fields\": [\"Catergory\", \"Catergory_summary\"]}}]', 18, 1),
(25, '2019-06-01 05:22:54.769187', '1', 'ProductCatergory object (1)', 2, '[]', 18, 1),
(26, '2019-06-01 05:23:18.145302', '3', 'ProductCatergory object (3)', 1, '[{\"added\": {}}]', 18, 1),
(27, '2019-06-01 05:23:59.496950', '2', 'ProductCatergory object (2)', 1, '[{\"added\": {}}]', 13, 1),
(28, '2019-06-01 05:26:15.464927', '3', 'pineapples', 1, '[{\"added\": {}}]', 14, 1),
(29, '2019-06-01 05:27:29.708876', '4', 'Avocados', 1, '[{\"added\": {}}]', 14, 1),
(30, '2019-06-07 11:37:25.266269', '2', 'Fabu-Metronidazole susp. 100ml', 1, '[{\"added\": {}}]', 15, 1),
(31, '2019-06-07 11:47:59.733466', '3', 'Fabupharm ascorbic tabs 250mg chew', 1, '[{\"added\": {}}]', 15, 1),
(35, '2019-06-07 12:01:55.186178', '1', 'Paracetamols', 3, '', 15, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'admin', 'logentry'),
(9, 'auth', 'group'),
(8, 'auth', 'permission'),
(10, 'auth', 'user'),
(27, 'Biotech', 'cart'),
(15, 'Biotech', 'product'),
(16, 'Biotech', 'productcatergory'),
(11, 'contenttypes', 'contenttype'),
(1, 'ecommerce', 'cart'),
(2, 'ecommerce', 'member'),
(3, 'ecommerce', 'product'),
(4, 'ecommerce', 'productcatergory'),
(5, 'ecommerce', 'productcompany'),
(6, 'ecommerce', 'usersession'),
(28, 'Flintwood', 'flintcart'),
(14, 'Flintwood', 'product'),
(13, 'Flintwood', 'productcatergory'),
(21, 'orders', 'biotechorders'),
(22, 'orders', 'flintwoodorders'),
(23, 'orders', 'tktitanorders'),
(12, 'sessions', 'session'),
(17, 'TKTitan', 'product'),
(18, 'TKTitan', 'productcatergory'),
(29, 'TKTitan', 'tkcart'),
(26, 'Users', 'client'),
(25, 'Users', 'clientsession'),
(24, 'Users', 'employee'),
(20, 'Users', 'users'),
(19, 'Users', 'usersession');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-05-21 05:22:35.484285'),
(2, 'auth', '0001_initial', '2019-05-21 05:22:38.286634'),
(3, 'admin', '0001_initial', '2019-05-21 05:22:38.745373'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-05-21 05:22:38.780362'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-05-21 05:22:38.814335'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-05-21 05:22:39.278070'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-05-21 05:22:39.420987'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-05-21 05:22:39.573900'),
(9, 'auth', '0004_alter_user_username_opts', '2019-05-21 05:22:39.607881'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-05-21 05:22:39.742804'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-05-21 05:22:39.751801'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-05-21 05:22:39.780781'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-05-21 05:22:39.993334'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-05-21 05:22:40.211700'),
(15, 'ecommerce', '0001_initial', '2019-05-21 05:22:41.645003'),
(16, 'sessions', '0001_initial', '2019-05-21 05:22:41.716023'),
(17, 'ecommerce', '0002_auto_20190521_0914', '2019-05-21 06:14:19.719505'),
(18, 'Biotech', '0001_initial', '2019-05-25 18:00:09.797319'),
(19, 'Flintwood', '0001_initial', '2019-05-25 18:00:10.421961'),
(20, 'TKTitan', '0001_initial', '2019-05-25 18:00:11.026618'),
(21, 'Users', '0001_initial', '2019-05-25 18:00:11.298462'),
(22, 'orders', '0001_initial', '2019-05-25 18:01:11.477506'),
(23, 'Users', '0002_auto_20190526_1111', '2019-05-26 08:12:20.238424'),
(24, 'Users', '0003_auto_20190526_1135', '2019-05-26 08:35:12.461136'),
(25, 'Users', '0004_client_alternate_phonenumber', '2019-05-26 09:14:35.432591'),
(26, 'Users', '0005_auto_20190526_1222', '2019-05-26 09:22:29.189943'),
(27, 'Users', '0006_auto_20190526_1222', '2019-05-26 09:22:29.511963'),
(28, 'Biotech', '0002_cart', '2019-05-26 18:42:15.084634'),
(29, 'Flintwood', '0002_flintcart', '2019-05-26 20:39:05.011520'),
(30, 'TKTitan', '0002_tkcart', '2019-05-26 20:39:05.667469'),
(31, 'orders', '0002_auto_20190527_1418', '2019-05-27 11:18:35.635875'),
(32, 'orders', '0003_auto_20190531_1102', '2019-05-31 08:02:55.738550'),
(33, 'Users', '0007_auto_20190607_1233', '2019-06-07 09:33:31.022481');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('35243lc7a8lj0w3fv0nhf7lqgbracl6l', 'MDQxMjk0YmU5YTMzYzMyMjU0M2E4YzQ2MjRjNjQxNGNmYzQ3ODBmZDp7InVzZXJJRCI6IiJ9', '2019-06-09 09:17:39.210067'),
('524krm9dl9xt9p45m4p0mbs0t6g08b9p', 'NmUxZWQxZjhjYmZhYzcwOTc1ZGIwOGFhYWNmZjExNjkzMzI1YTQ4Yjp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzJkOWM0MzM3Yzk0M2RiM2MwZWViOTA1OWExOTU0Yzg0YmVkYmY0OCIsInVzZXJJRCI6MTAsIlVzZXJuIjoiZ3JlZW5taWxlMTQ0NiJ9', '2019-06-21 12:02:01.488349'),
('8q4lp51b42x7i1qdjpf8gkjz0l25wjd2', 'MzYxNDY2YzI5ZTIyY2JmNDQ4OWE3MjFjOWRmYWFhNWEyZjg1MDRjYjp7InVzZXJJRCI6MywiX2F1dGhfdXNlcl9pZCI6IjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZjNGVhZmJhYmY5MjEwN2VkNGEzNDcxNzc5OGVkOTI3OTcyNzEwZDUifQ==', '2019-06-04 10:03:27.774035'),
('fisoi7vilns5of2f4tqdx4kvdbbrn410', 'MDQxMjk0YmU5YTMzYzMyMjU0M2E4YzQ2MjRjNjQxNGNmYzQ3ODBmZDp7InVzZXJJRCI6IiJ9', '2019-06-09 09:19:39.030133'),
('njxe2bh591d7qahajqvstt7hd9sr7s81', 'MDQxMjk0YmU5YTMzYzMyMjU0M2E4YzQ2MjRjNjQxNGNmYzQ3ODBmZDp7InVzZXJJRCI6IiJ9', '2019-06-09 09:21:01.315466'),
('ptig2pfmf2p2rf22sjgodecf65dl4t51', 'NmFjYzMwNzEyMTlhMjg2ZTJkOGRiYmFkODk3ODFlMzczOTdhZGFiOTp7fQ==', '2019-06-09 12:28:46.735446'),
('u2db2ja9ehdrrkp6xpbv3ing1kzjlybq', 'MDQxMjk0YmU5YTMzYzMyMjU0M2E4YzQ2MjRjNjQxNGNmYzQ3ODBmZDp7InVzZXJJRCI6IiJ9', '2019-06-09 09:21:40.601916'),
('ukbtj1o23we6l3wedi2g1z02wuhhjfci', 'NmFjYzMwNzEyMTlhMjg2ZTJkOGRiYmFkODk3ODFlMzczOTdhZGFiOTp7fQ==', '2019-06-09 09:25:35.454340'),
('w0ln6vkf1pi6ru2p8r1v9opuu1ooy6g1', 'M2I0YTgwZDg3ODBjMmU1OGUxN2U5ZWZiODk5NDAwZmNiYTI3OTE0Yjp7InVzZXJJRCI6NCwiX2F1dGhfdXNlcl9pZCI6IjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImZkNjMyNjFhM2YyYTUyMzk5ZTU4NmNhMGY0OGJmN2VhYjA3MmNkZTkiLCJVc2VybiI6Im11ZWo0In0=', '2019-06-05 11:12:50.080737'),
('x19tzil9zxaox5a05bw7i7xslngj8wbj', 'M2MyZWJhNmRlNTM1MTEyNDlkNjE0OGI2OTljOWNiMTE5MGY2Mzc4ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiOGU2MDZlZjQ4M2ZjODc4NjBiMjI0YjlhMTZkMjM0OTZjZjkyMGFkIn0=', '2019-06-21 11:57:43.210450'),
('yrsl2c0lo84ew6dn4ylgbbgyrb38zuz7', 'NmUxZWQxZjhjYmZhYzcwOTc1ZGIwOGFhYWNmZjExNjkzMzI1YTQ4Yjp7Il9hdXRoX3VzZXJfaWQiOiIxMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzJkOWM0MzM3Yzk0M2RiM2MwZWViOTA1OWExOTU0Yzg0YmVkYmY0OCIsInVzZXJJRCI6MTAsIlVzZXJuIjoiZ3JlZW5taWxlMTQ0NiJ9', '2019-06-15 05:59:06.673607');

-- --------------------------------------------------------

--
-- Table structure for table `ecommerce_cart`
--

CREATE TABLE `ecommerce_cart` (
  `id` int(11) NOT NULL,
  `Cart_slug` varchar(50) NOT NULL,
  `count` int(11) NOT NULL,
  `date_created` date NOT NULL,
  `last_modified` date NOT NULL,
  `Member_ID_id` int(11) NOT NULL,
  `ProductID_id` int(11) NOT NULL,
  `Product_description` longtext NOT NULL,
  `Product_name` varchar(254) NOT NULL,
  `price` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `ecommerce_member`
--

CREATE TABLE `ecommerce_member` (
  `id` int(11) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `country` varchar(200) NOT NULL,
  `physical_address` varchar(200) NOT NULL,
  `privilege` varchar(10) NOT NULL,
  `Userid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ecommerce_member`
--

INSERT INTO `ecommerce_member` (`id`, `phone_number`, `country`, `physical_address`, `privilege`, `Userid_id`) VALUES
(1, '731416316', 'Namibia', 'ERF 26,Rendsburger street', 'Customer', 1),
(2, '731416316', 'Namibia', 'ERF 26,Rendsburger street', 'Customer', 3),
(3, '731416316', 'Namibia', 'ERF 26,Rendsburger street', 'Customer', 4),
(4, '731416316', 'Namibia', 'ERF 26,Rendsburger street', 'Customer', 5);

-- --------------------------------------------------------

--
-- Table structure for table `ecommerce_product`
--

CREATE TABLE `ecommerce_product` (
  `pid` int(11) NOT NULL,
  `name` varchar(254) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `Product_Catergory_id` int(11) NOT NULL,
  `Product_Company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ecommerce_product`
--

INSERT INTO `ecommerce_product` (`pid`, `name`, `description`, `price`, `image`, `stock`, `Product_Catergory_id`, `Product_Company_id`) VALUES
(1, 'green grams', '2\r\n\r\nWhenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-', '120.00', 'product_images/2783a4b3628445825ac553829ab142a0.jpg', 112, 2, 1),
(2, 'avocado', '2\r\n\r\nWhenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-', '34.00', 'product_images/c975139816f7d275f665e5f9dd03cc1c.jpg', 34, 4, 1),
(4, 'Copper', 'this is copper from congo', '400.00', 'product_images/6A0B9143-8C83-471A-AB48-CD4962EB6F0CL0001.jpg', 15, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `ecommerce_productcatergory`
--

CREATE TABLE `ecommerce_productcatergory` (
  `id` int(11) NOT NULL,
  `Catergory` varchar(200) NOT NULL,
  `Catergory_summary` longtext NOT NULL,
  `Product_company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ecommerce_productcatergory`
--

INSERT INTO `ecommerce_productcatergory` (`id`, `Catergory`, `Catergory_summary`, `Product_company_id`) VALUES
(1, 'Vegetables', 'Whenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-', 1),
(2, 'Minerals', '2\r\n\r\nWhenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-', 2),
(3, 'fruits', '2\r\n\r\nWhenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-', 3),
(4, 'Medicine', '2\r\n\r\nWhenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-', 1);

-- --------------------------------------------------------

--
-- Table structure for table `ecommerce_productcompany`
--

CREATE TABLE `ecommerce_productcompany` (
  `id` int(11) NOT NULL,
  `Company` varchar(200) NOT NULL,
  `Company_summary` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ecommerce_productcompany`
--

INSERT INTO `ecommerce_productcompany` (`id`, `Company`, `Company_summary`) VALUES
(1, 'Tk Titan', 'Whenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-'),
(2, 'Biotech', '2\r\n\r\nWhenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-'),
(3, 'Flintwood', '2\r\n\r\nWhenever you update or create anything in the table contains foreign Key you need to pass the object of primary key instead of passing real value.So you have to call the get query to primary key value table then pass that obj to foreign key column as a value.\r\n\r\nExample :-\r\n\r\nSuppose I have two model as follows:-');

-- --------------------------------------------------------

--
-- Table structure for table `ecommerce_usersession`
--

CREATE TABLE `ecommerce_usersession` (
  `id` int(11) NOT NULL,
  `ip_address` varchar(220) DEFAULT NULL,
  `session_key` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `ended` tinyint(1) NOT NULL,
  `Activeuser_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ecommerce_usersession`
--

INSERT INTO `ecommerce_usersession` (`id`, `ip_address`, `session_key`, `timestamp`, `active`, `ended`, `Activeuser_id`) VALUES
(1, '14.14', 'lq23s6lcfhoiac02z7ddb2s5pk1rrf6x', '2019-05-21 05:38:38.254298', 1, 0, 2),
(2, '14.14', 'pdkv4yrucb0mxh7mf002plopr1qj2nds', '2019-05-21 06:42:30.957448', 1, 0, 2),
(3, '14.14', '8q4lp51b42x7i1qdjpf8gkjz0l25wjd2', '2019-05-21 10:03:27.748855', 1, 0, 3),
(4, '14.14', 'w0ln6vkf1pi6ru2p8r1v9opuu1ooy6g1', '2019-05-22 11:12:50.049756', 1, 0, 4),
(5, '14.14', 'wsjw4bf7ivp9fj75o7q4gak4qfzdeir2', '2019-05-23 09:38:44.417559', 1, 0, 2),
(6, '14.14', 'yvcst8b5nq7ggwxmn51ogyq6jq6200ea', '2019-05-23 11:26:45.121730', 1, 0, 5),
(7, '14.14', 'umys09e4saod9i2hzg6ix87kkhuet99m', '2019-05-23 11:29:24.706902', 1, 0, 5),
(8, '14.14', 'vr9t9tp9i88mwr3uns3tg6cd2d2i57lq', '2019-05-23 11:30:30.554666', 1, 0, 5),
(9, '14.14', 'oce7ub63wz07i92uue0vsd0vwlkyg84f', '2019-05-23 11:32:42.234388', 1, 0, 5),
(10, '14.14', '3c0m9a3gr1vsqlibobk0ifbvx08wnxhm', '2019-05-24 17:46:49.379216', 1, 0, 5),
(11, '14.14', '92y9aau95jxfahwm0u6vuk41gf1j4fek', '2019-05-25 10:07:54.763259', 1, 0, 5),
(12, '14.14', 'ky2k31l553vexk6767l6ty51jzka8o45', '2019-05-25 10:33:58.915476', 1, 0, 5);

-- --------------------------------------------------------

--
-- Table structure for table `flintwood_flintcart`
--

CREATE TABLE `flintwood_flintcart` (
  `id` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  `Product_name` varchar(254) NOT NULL,
  `Product_description` longtext NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date_created` date NOT NULL,
  `last_modified` date NOT NULL,
  `ProductID_id` int(11) NOT NULL,
  `User_ID_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `flintwood_product`
--

CREATE TABLE `flintwood_product` (
  `pid` int(11) NOT NULL,
  `name` varchar(254) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `Product_Catergory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `flintwood_product`
--

INSERT INTO `flintwood_product` (`pid`, `name`, `description`, `price`, `image`, `stock`, `Product_Catergory_id`) VALUES
(3, 'pineapples', 'pineapples from the coast of kenya', '50.00', 'product_images/pineapples.jpg', 70, 2),
(4, 'Avocados', 'Avocados from bungoma', '20.00', 'product_images/avocados.jpg', 300, 1);

-- --------------------------------------------------------

--
-- Table structure for table `flintwood_productcatergory`
--

CREATE TABLE `flintwood_productcatergory` (
  `id` int(11) NOT NULL,
  `Catergory` varchar(200) NOT NULL,
  `Catergory_summary` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `flintwood_productcatergory`
--

INSERT INTO `flintwood_productcatergory` (`id`, `Catergory`, `Catergory_summary`) VALUES
(1, 'Vegetables', 'Green photosynthesis blooded living things'),
(2, 'Fruits', 'Fruits taken from Uganda');

-- --------------------------------------------------------

--
-- Table structure for table `orders_biotechorders`
--

CREATE TABLE `orders_biotechorders` (
  `OrderID` varchar(100) NOT NULL,
  `OrderDate` date NOT NULL,
  `OrderList` varchar(2000) NOT NULL,
  `Order_Payment` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `orders_flintwoodorders`
--

CREATE TABLE `orders_flintwoodorders` (
  `OrderID` varchar(100) NOT NULL,
  `OrderDate` date NOT NULL,
  `OrderList` varchar(2000) NOT NULL,
  `Order_Payment` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders_flintwoodorders`
--

INSERT INTO `orders_flintwoodorders` (`OrderID`, `OrderDate`, `OrderList`, `Order_Payment`, `user_id`) VALUES
('6eH5tqqDtGY', '2019-05-28', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),', 0, 10),
('dIHkfeOrVpMY', '2019-05-28', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),', 0, 10),
('edOmMkKoTzp', '2019-05-28', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),', 0, 10),
('fCJQ0wwU0eH', '2019-05-28', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),', 0, 10),
('iFmXdh27bBK', '2019-05-31', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),6).green grams(1),7).green grams(1),', 0, 10),
('lZAUjGwP6Hi', '2019-05-28', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),', 0, 10),
('mAnvwJJv3dK5', '2019-05-28', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),', 0, 10),
('u2ptrGFUQg', '2019-05-28', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),', 0, 10),
('ZGjVixB4W7IL', '2019-05-28', '1).green grams(1),2).green grams(1),3).green grams(1),4).green grams(1),5).green grams(1),', 0, 10);

-- --------------------------------------------------------

--
-- Table structure for table `orders_tktitanorders`
--

CREATE TABLE `orders_tktitanorders` (
  `OrderID` varchar(100) NOT NULL,
  `OrderDate` date NOT NULL,
  `OrderList` varchar(2000) NOT NULL,
  `Order_Payment` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders_tktitanorders`
--

INSERT INTO `orders_tktitanorders` (`OrderID`, `OrderDate`, `OrderList`, `Order_Payment`, `user_id`) VALUES
('2gtlZZtw2b', '2019-06-07', '1).Copper(1),', 0, 10);

-- --------------------------------------------------------

--
-- Table structure for table `tktitan_product`
--

CREATE TABLE `tktitan_product` (
  `pid` int(11) NOT NULL,
  `name` varchar(254) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `image` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `Product_Catergory_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tktitan_productcatergory`
--

CREATE TABLE `tktitan_productcatergory` (
  `id` int(11) NOT NULL,
  `Catergory` varchar(200) NOT NULL,
  `Catergory_summary` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tktitan_productcatergory`
--

INSERT INTO `tktitan_productcatergory` (`id`, `Catergory`, `Catergory_summary`) VALUES
(1, 'Minerals', 'Vitu from the earth'),
(2, 'Vegetabes', 'Vegetables taken from kenya'),
(3, 'Fruits', 'Fruits taken from uganda');

-- --------------------------------------------------------

--
-- Table structure for table `tktitan_tkcart`
--

CREATE TABLE `tktitan_tkcart` (
  `id` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  `Product_name` varchar(254) NOT NULL,
  `Product_description` longtext NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date_created` date NOT NULL,
  `last_modified` date NOT NULL,
  `ProductID_id` int(11) NOT NULL,
  `User_ID_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users_client`
--

CREATE TABLE `users_client` (
  `id` int(11) NOT NULL,
  `physical_address` varchar(200) NOT NULL,
  `privilege` varchar(10) NOT NULL,
  `Country` varchar(200) NOT NULL,
  `phonenumber` varchar(15) NOT NULL,
  `user_id` int(11) NOT NULL,
  `Alternate_phonenumber` varchar(15) NOT NULL,
  `Skype` varchar(15) NOT NULL,
  `WeChat` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users_client`
--

INSERT INTO `users_client` (`id`, `physical_address`, `privilege`, `Country`, `phonenumber`, `user_id`, `Alternate_phonenumber`, `Skype`, `WeChat`) VALUES
(1, 'ERF 27,Rendsburger street', 'all', 'Namibia', '731416316', 10, '0731416317', 'none', 'none');

-- --------------------------------------------------------

--
-- Table structure for table `users_clientsession`
--

CREATE TABLE `users_clientsession` (
  `id` int(11) NOT NULL,
  `ip_address` varchar(220) DEFAULT NULL,
  `session_key` varchar(100) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `ended` tinyint(1) NOT NULL,
  `Activeclient_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users_employee`
--

CREATE TABLE `users_employee` (
  `id` int(11) NOT NULL,
  `physical_address` varchar(200) NOT NULL,
  `privilege` varchar(10) NOT NULL,
  `Country` varchar(200) NOT NULL,
  `phonenumber` varchar(15) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `biotech_cart`
--
ALTER TABLE `biotech_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Biotech_cart_ProductID_id_2df66ab7_fk_Biotech_product_pid` (`ProductID_id`),
  ADD KEY `Biotech_cart_User_ID_id_737006f0_fk_auth_user_id` (`User_ID_id`);

--
-- Indexes for table `biotech_product`
--
ALTER TABLE `biotech_product`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `Biotech_product_Product_Catergory_id_894d8768_fk_Biotech_p` (`Product_Catergory_id`);

--
-- Indexes for table `biotech_productcatergory`
--
ALTER TABLE `biotech_productcatergory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `ecommerce_cart`
--
ALTER TABLE `ecommerce_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ecommerce_cart_Cart_slug_76c68214` (`Cart_slug`),
  ADD KEY `ecommerce_cart_Member_ID_id_3cd94e56_fk_ecommerce_member_id` (`Member_ID_id`),
  ADD KEY `ecommerce_cart_ProductID_id_0f9418dc_fk_ecommerce_product_pid` (`ProductID_id`);

--
-- Indexes for table `ecommerce_member`
--
ALTER TABLE `ecommerce_member`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ecommerce_member_Userid_id_a91d3b86_fk_auth_user_id` (`Userid_id`);

--
-- Indexes for table `ecommerce_product`
--
ALTER TABLE `ecommerce_product`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `ecommerce_product_Product_Catergory_id_ace33c5f_fk_ecommerce` (`Product_Catergory_id`),
  ADD KEY `ecommerce_product_Product_Company_id_3b313e01_fk_ecommerce` (`Product_Company_id`);

--
-- Indexes for table `ecommerce_productcatergory`
--
ALTER TABLE `ecommerce_productcatergory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ecommerce_productcat_Product_company_id_d38a0979_fk_ecommerce` (`Product_company_id`);

--
-- Indexes for table `ecommerce_productcompany`
--
ALTER TABLE `ecommerce_productcompany`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ecommerce_usersession`
--
ALTER TABLE `ecommerce_usersession`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ecommerce_usersession_Activeuser_id_054672ea_fk_auth_user_id` (`Activeuser_id`);

--
-- Indexes for table `flintwood_flintcart`
--
ALTER TABLE `flintwood_flintcart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Flintwood_flintcart_ProductID_id_2d4e3545_fk_Flintwood` (`ProductID_id`),
  ADD KEY `Flintwood_flintcart_User_ID_id_325f7da6_fk_auth_user_id` (`User_ID_id`);

--
-- Indexes for table `flintwood_product`
--
ALTER TABLE `flintwood_product`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `Flintwood_product_Product_Catergory_id_e37df36a_fk_Flintwood` (`Product_Catergory_id`);

--
-- Indexes for table `flintwood_productcatergory`
--
ALTER TABLE `flintwood_productcatergory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders_biotechorders`
--
ALTER TABLE `orders_biotechorders`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `orders_biotechorders_user_id_d3ad8ba5_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `orders_flintwoodorders`
--
ALTER TABLE `orders_flintwoodorders`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `orders_flintwoodorders_user_id_ff22e8b7_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `orders_tktitanorders`
--
ALTER TABLE `orders_tktitanorders`
  ADD PRIMARY KEY (`OrderID`),
  ADD KEY `orders_tktitanorders_user_id_562a5c88_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `tktitan_product`
--
ALTER TABLE `tktitan_product`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `TKTitan_product_Product_Catergory_id_cc049fe9_fk_TKTitan_p` (`Product_Catergory_id`);

--
-- Indexes for table `tktitan_productcatergory`
--
ALTER TABLE `tktitan_productcatergory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tktitan_tkcart`
--
ALTER TABLE `tktitan_tkcart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `TKTitan_tkcart_ProductID_id_dcc09c70_fk_TKTitan_product_pid` (`ProductID_id`),
  ADD KEY `TKTitan_tkcart_User_ID_id_c6ceef0a_fk_auth_user_id` (`User_ID_id`);

--
-- Indexes for table `users_client`
--
ALTER TABLE `users_client`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `users_clientsession`
--
ALTER TABLE `users_clientsession`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Activeclient_id` (`Activeclient_id`);

--
-- Indexes for table `users_employee`
--
ALTER TABLE `users_employee`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `biotech_cart`
--
ALTER TABLE `biotech_cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `biotech_productcatergory`
--
ALTER TABLE `biotech_productcatergory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `ecommerce_cart`
--
ALTER TABLE `ecommerce_cart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ecommerce_member`
--
ALTER TABLE `ecommerce_member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `ecommerce_productcatergory`
--
ALTER TABLE `ecommerce_productcatergory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `ecommerce_productcompany`
--
ALTER TABLE `ecommerce_productcompany`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `ecommerce_usersession`
--
ALTER TABLE `ecommerce_usersession`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `flintwood_flintcart`
--
ALTER TABLE `flintwood_flintcart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `flintwood_productcatergory`
--
ALTER TABLE `flintwood_productcatergory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tktitan_productcatergory`
--
ALTER TABLE `tktitan_productcatergory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tktitan_tkcart`
--
ALTER TABLE `tktitan_tkcart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_client`
--
ALTER TABLE `users_client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users_clientsession`
--
ALTER TABLE `users_clientsession`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_employee`
--
ALTER TABLE `users_employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `biotech_cart`
--
ALTER TABLE `biotech_cart`
  ADD CONSTRAINT `Biotech_cart_ProductID_id_2df66ab7_fk_Biotech_product_pid` FOREIGN KEY (`ProductID_id`) REFERENCES `biotech_product` (`pid`),
  ADD CONSTRAINT `Biotech_cart_User_ID_id_737006f0_fk_auth_user_id` FOREIGN KEY (`User_ID_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `biotech_product`
--
ALTER TABLE `biotech_product`
  ADD CONSTRAINT `Biotech_product_Product_Catergory_id_894d8768_fk_Biotech_p` FOREIGN KEY (`Product_Catergory_id`) REFERENCES `biotech_productcatergory` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `ecommerce_cart`
--
ALTER TABLE `ecommerce_cart`
  ADD CONSTRAINT `ecommerce_cart_Member_ID_id_3cd94e56_fk_ecommerce_member_id` FOREIGN KEY (`Member_ID_id`) REFERENCES `ecommerce_member` (`id`),
  ADD CONSTRAINT `ecommerce_cart_ProductID_id_0f9418dc_fk_ecommerce_product_pid` FOREIGN KEY (`ProductID_id`) REFERENCES `ecommerce_product` (`pid`);

--
-- Constraints for table `ecommerce_member`
--
ALTER TABLE `ecommerce_member`
  ADD CONSTRAINT `ecommerce_member_Userid_id_a91d3b86_fk_auth_user_id` FOREIGN KEY (`Userid_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `ecommerce_product`
--
ALTER TABLE `ecommerce_product`
  ADD CONSTRAINT `ecommerce_product_Product_Catergory_id_ace33c5f_fk_ecommerce` FOREIGN KEY (`Product_Catergory_id`) REFERENCES `ecommerce_productcatergory` (`id`),
  ADD CONSTRAINT `ecommerce_product_Product_Company_id_3b313e01_fk_ecommerce` FOREIGN KEY (`Product_Company_id`) REFERENCES `ecommerce_productcompany` (`id`);

--
-- Constraints for table `ecommerce_productcatergory`
--
ALTER TABLE `ecommerce_productcatergory`
  ADD CONSTRAINT `ecommerce_productcat_Product_company_id_d38a0979_fk_ecommerce` FOREIGN KEY (`Product_company_id`) REFERENCES `ecommerce_productcompany` (`id`);

--
-- Constraints for table `ecommerce_usersession`
--
ALTER TABLE `ecommerce_usersession`
  ADD CONSTRAINT `ecommerce_usersession_Activeuser_id_054672ea_fk_auth_user_id` FOREIGN KEY (`Activeuser_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `flintwood_flintcart`
--
ALTER TABLE `flintwood_flintcart`
  ADD CONSTRAINT `Flintwood_flintcart_ProductID_id_2d4e3545_fk_Flintwood` FOREIGN KEY (`ProductID_id`) REFERENCES `flintwood_product` (`pid`),
  ADD CONSTRAINT `Flintwood_flintcart_User_ID_id_325f7da6_fk_auth_user_id` FOREIGN KEY (`User_ID_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `flintwood_product`
--
ALTER TABLE `flintwood_product`
  ADD CONSTRAINT `Flintwood_product_Product_Catergory_id_e37df36a_fk_Flintwood` FOREIGN KEY (`Product_Catergory_id`) REFERENCES `flintwood_productcatergory` (`id`);

--
-- Constraints for table `orders_biotechorders`
--
ALTER TABLE `orders_biotechorders`
  ADD CONSTRAINT `orders_biotechorders_user_id_d3ad8ba5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `orders_flintwoodorders`
--
ALTER TABLE `orders_flintwoodorders`
  ADD CONSTRAINT `orders_flintwoodorders_user_id_ff22e8b7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `orders_tktitanorders`
--
ALTER TABLE `orders_tktitanorders`
  ADD CONSTRAINT `orders_tktitanorders_user_id_562a5c88_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tktitan_product`
--
ALTER TABLE `tktitan_product`
  ADD CONSTRAINT `TKTitan_product_Product_Catergory_id_cc049fe9_fk_TKTitan_p` FOREIGN KEY (`Product_Catergory_id`) REFERENCES `tktitan_productcatergory` (`id`);

--
-- Constraints for table `tktitan_tkcart`
--
ALTER TABLE `tktitan_tkcart`
  ADD CONSTRAINT `TKTitan_tkcart_ProductID_id_dcc09c70_fk_TKTitan_product_pid` FOREIGN KEY (`ProductID_id`) REFERENCES `tktitan_product` (`pid`),
  ADD CONSTRAINT `TKTitan_tkcart_User_ID_id_c6ceef0a_fk_auth_user_id` FOREIGN KEY (`User_ID_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_client`
--
ALTER TABLE `users_client`
  ADD CONSTRAINT `Users_client_user_id_a6526b81_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_clientsession`
--
ALTER TABLE `users_clientsession`
  ADD CONSTRAINT `Users_clientsession_Activeclient_id_d4f97200_fk_auth_user_id` FOREIGN KEY (`Activeclient_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_employee`
--
ALTER TABLE `users_employee`
  ADD CONSTRAINT `Users_employee_user_id_c6be762a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
