-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 23, 2026 at 10:00 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID_Admin` int(11) NOT NULL,
  `Username_Admin` varchar(50) NOT NULL,
  `Password_Admin` varchar(255) NOT NULL,
  `Email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`ID_Admin`, `Username_Admin`, `Password_Admin`, `Email`) VALUES
(1, 'adminfmipa', 'admin123', 'admin@fmipa.ac.id');

-- --------------------------------------------------------

--
-- Table structure for table `bank_soal`
--

CREATE TABLE `bank_soal` (
  `ID_Soal` int(11) NOT NULL,
  `ID_Tes` int(11) NOT NULL,
  `Pertanyaan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bank_soal`
--

INSERT INTO `bank_soal` (`ID_Soal`, `ID_Tes`, `Pertanyaan`) VALUES
(1, 1, 'Jenis kelamin Anda?'),
(2, 1, 'Berapa usia Anda dalam tahun?'),
(3, 1, 'Saya tidak akan pernah mau ikut audisi menjadi peserta kuis di TV.'),
(4, 1, 'Saya bukan orang yang suka menggoda/bercanda dengan lawan jenis.'),
(5, 1, 'Saya perlu mempersiapkan mental dulu sebelum berani menelepon seseorang.'),
(6, 1, 'Saya tidak suka tinggal serumah dengan orang lain (kost/kontrakan bareng).'),
(7, 1, 'Saya lebih banyak mendengarkan daripada berbicara dalam percakapan.'),
(8, 1, 'Saya jarang menceritakan hal-hal pribadi tentang diri saya.'),
(9, 1, 'Saya bisa menghabiskan waktu berjam-jam sendirian melakukan hobi saya.'),
(10, 1, 'Saya lebih suka makan sendirian.'),
(11, 1, 'Saya kesulitan menemukan orang yang ingin saya jadikan teman.'),
(12, 1, 'Saya lebih suka bersosialisasi satu lawan satu daripada dalam kelompok besar.'),
(13, 1, 'Terkadang saya berbicara terlalu pelan hingga orang lain sulit mendengar.'),
(14, 1, 'Saya tidak suka difoto.'),
(15, 1, 'Saya bisa mempertahankan percakapan dengan siapa pun tentang hal apa pun.'),
(16, 1, 'Saya ingin memiliki banyak teman dan pergaulan yang luas.'),
(17, 1, 'Saya suka mengobrol dengan orang lain saat sedang mengantri.'),
(18, 1, 'Saya bisa bersikap liar dan heboh saat sedang santai.'),
(19, 1, 'Saya adalah orang yang ceria dan penuh semangat.'),
(20, 1, 'Saya menyukai hal-hal yang menantang dan seru.'),
(21, 1, 'Saya ingin ikut serta dalam suatu pawai atau karnaval.'),
(22, 1, 'Saya adalah orang yang bersemangat dan ekspresif.'),
(23, 1, 'Saya pandai berbicara di depan umum secara spontan (tanpa persiapan).'),
(24, 1, 'Saya secara alami cenderung menjadi pemimpin dalam kelompok.'),
(25, 1, 'Saya adalah orang yang spontan dan tidak suka terlalu banyak rencana.'),
(26, 1, 'Saya akan menikmati menjadi pelatih tim olahraga.'),
(27, 1, 'Saya memiliki kepribadian yang kuat dan tegas.'),
(28, 1, 'Saya tertarik dengan banyak aktivitas yang berbeda.'),
(29, 1, 'Saya menghabiskan banyak waktu melamun atau membayangkan dunia fantasi.'),
(30, 1, 'Saya sering merasa beruntung dalam hidup.'),
(31, 1, 'Saya tidak melakukan kontak mata saat berbicara dengan orang lain.'),
(32, 1, 'Suara saya cenderung datar (monoton) tidak banyak perubahan nada.'),
(33, 1, 'Saya adalah orang yang suka menyentuh orang lain (misalnya menepuk bahu, berpelukan).'),
(34, 1, 'Saya ingin mencoba bungee jumping (bungee jumping: melompat dari ketinggian dengan tali elastis yang terikat di kaki).'),
(35, 1, 'Saya cenderung dikagumi oleh orang lain.'),
(36, 1, 'Saya membuat gerakan tubuh yang besar saat sedang bersemangat.'),
(37, 1, 'Saya adalah orang yang pemberani.'),
(38, 1, 'Saya selalu hidup di saat ini (tidak terlalu memikirkan masa lalu atau masa depan).'),
(39, 1, 'Saya terlibat aktif dalam kegiatan masyarakat sekitar.'),
(40, 1, 'Saya pandai menghibur anak-anak.'),
(41, 1, 'Saya menyukai acara-acara formal.'),
(42, 1, 'Saya baru akan meminta bantuan jika benar-benar tersesat.'),
(43, 1, 'Saya tidak terlalu peduli dengan olahraga.'),
(44, 1, 'Saya lebih suka olahraga individu daripada olahraga tim.'),
(45, 1, 'Orang tua saya tidak tahu apa-apa tentang kehidupan percintaan saya.'),
(46, 1, 'Saya lebih banyak mendengarkan daripada berbicara dalam percakapan.'),
(47, 1, 'Saya tidak pernah membiarkan pintu kamar saya terbuka.'),
(48, 1, 'Saya banyak menggunakan gerakan tangan saat berbicara.'),
(49, 1, 'Saya suka mengabadikan kegiatan saya dalam bentuk foto.'),
(50, 1, 'Saat kecil, saya suka berpura-pura mengadakan konser atau pertunjukan bersama teman-teman.'),
(51, 1, 'Saya sangat suka menari.'),
(52, 1, 'Saya akan kesulitan menggambarkan diri saya kepada orang lain.'),
(53, 1, 'Kehidupan saya tidak akan menjadi cerita yang menarik untuk diceritakan.'),
(54, 1, 'Saya ragu-ragu dalam memberikan saran atau usulan.'),
(55, 1, 'Saya cepat lelah.'),
(56, 1, 'Saya tidak pernah menceritakan hal-hal penting tentang diri saya kepada orang lain.'),
(57, 1, 'Saya menghindari pergi ke tempat yang tidak saya kenal.'),
(58, 1, 'Pergi ke dokter selalu terasa canggung bagi saya.'),
(59, 1, 'Saya tidak menjaga hubungan dengan teman-teman lama saya selama bertahun-tahun.'),
(60, 1, 'Saya sudah lama tidak merasakan kebahagiaan yang sesungguhnya.'),
(61, 1, 'Saya tidak suka meminta bantuan kepada orang lain.'),
(62, 1, 'Jika saya meninggal, saya tidak ingin ada acara peringatan untuk saya.'),
(63, 1, 'Saya tidak suka berbelanja.'),
(64, 1, 'Saya suka menirukan gaya atau suara orang lain.'),
(65, 1, 'Saya akan merasa senang jika diminta berbicara di acara peringatan seseorang.'),
(66, 1, 'Saya tidak akan pernah pergi ke klub dansa.'),
(67, 1, 'Saya merasa sangat sulit mengatakan kepada seseorang bahwa saya tertarik padanya.'),
(68, 1, 'Saya tidak suka berinteraksi dengan banyak orang.'),
(69, 1, 'Saya dulu adalah orang yang terbuang/asing di sekolah (tidak punya banyak teman).'),
(70, 1, 'Saya akan menikmati pekerjaan sebagai pustakawan.'),
(71, 1, 'Saya biasanya tidak sendiri (sedang menjalin hubungan).'),
(72, 1, 'Saya mampu membela diri sendiri.'),
(73, 1, 'Jika saya tinggal di pantai, saya akan rutin berselancar.'),
(74, 1, 'Saya pernah bercita-cita menjadi pelawak tunggal (stand-up comedian).'),
(75, 1, 'Saya adalah orang yang memiliki status sosial tinggi.'),
(76, 1, 'Saya berolahraga secara teratur.'),
(77, 1, 'Saya sering tertawa.'),
(78, 1, 'Saya suka membuat kejutan iseng (prank).'),
(79, 1, 'Saya bahagia dengan hidup saya saat ini.'),
(80, 1, 'Saya tidak pernah kehabisan kata-kata saat berbicara.'),
(81, 1, 'Saya merasa sehat dan bersemangat hampir sepanjang waktu.'),
(82, 1, 'Saya suka pesta besar dengan banyak orang.'),
(83, 1, 'Saya merasa canggung berada di dekat orang yang tidak dikenal.'),
(84, 1, 'Saya tidak banyak bicara.'),
(85, 1, 'Saya lebih suka berada di belakang layar (tidak tampil di depan).'),
(86, 1, 'Saya tidak suka menarik perhatian orang lain kepada diri saya.'),
(87, 1, 'Saya tidak punya banyak hal untuk dikatakan.'),
(88, 1, 'Saya sering merasa sedih.'),
(89, 1, 'Saya tidak terlalu tertarik dengan orang lain.'),
(90, 1, 'Saya membuat orang lain merasa nyaman berada di dekat saya.'),
(91, 1, 'Saya tidak keberatan menjadi pusat perhatian.'),
(92, 1, 'Saya yang memulai percakapan dengan orang lain.'),
(93, 1, 'Saya berbicara dengan banyak orang yang berbeda saat berada di pesta.');

-- --------------------------------------------------------

--
-- Table structure for table `detail_tes`
--

CREATE TABLE `detail_tes` (
  `ID_Hasil` int(11) NOT NULL,
  `ID_Soal` int(11) NOT NULL,
  `Jawaban_Mahasiswa` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `detail_tes` (jawaban untuk hasil tes mahasiswa)
-- Skala jawaban: 1=Sangat Tidak Setuju, 2=Tidak Setuju, 3=Netral, 4=Setuju, 5=Sangat Setuju
-- Kecuali soal nomor 1 (jenis kelamin) dan nomor 2 (usia)
--

-- =====================================================
-- Hasil Tes 1 (ID_Hasil=1) - I Gede Andhika Pratama (Ekstrovert)
-- =====================================================
INSERT INTO `detail_tes` (`ID_Hasil`, `ID_Soal`, `Jawaban_Mahasiswa`) VALUES
(1, 1, '1'),
(1, 2, '21'),
(1, 3, '1'),
(1, 4, '1'),
(1, 5, '1'),
(1, 6, '2'),
(1, 7, '2'),
(1, 8, '2'),
(1, 9, '2'),
(1, 10, '2'),
(1, 11, '2'),
(1, 12, '2'),
(1, 13, '2'),
(1, 14, '2'),
(1, 15, '5'),
(1, 16, '5'),
(1, 17, '5'),
(1, 18, '4'),
(1, 19, '4'),
(1, 20, '5'),
(1, 21, '4'),
(1, 22, '4'),
(1, 23, '4'),
(1, 24, '4'),
(1, 25, '4'),
(1, 26, '4'),
(1, 27, '4'),
(1, 28, '5'),
(1, 29, '2'),
(1, 30, '4'),
(1, 31, '2'),
(1, 32, '2'),
(1, 33, '4'),
(1, 34, '4'),
(1, 35, '4'),
(1, 36, '4'),
(1, 37, '4'),
(1, 38, '3'),
(1, 39, '4'),
(1, 40, '4'),
(1, 41, '3'),
(1, 42, '2'),
(1, 43, '3'),
(1, 44, '2'),
(1, 45, '2'),
(1, 46, '2'),
(1, 47, '2'),
(1, 48, '4'),
(1, 49, '4'),
(1, 50, '4'),
(1, 51, '4'),
(1, 52, '2'),
(1, 53, '2'),
(1, 54, '2'),
(1, 55, '3'),
(1, 56, '2'),
(1, 57, '2'),
(1, 58, '2'),
(1, 59, '3'),
(1, 60, '2'),
(1, 61, '2'),
(1, 62, '2'),
(1, 63, '3'),
(1, 64, '4'),
(1, 65, '3'),
(1, 66, '2'),
(1, 67, '2'),
(1, 68, '1'),
(1, 69, '3'),
(1, 70, '3'),
(1, 71, '4'),
(1, 72, '4'),
(1, 73, '4'),
(1, 74, '4'),
(1, 75, '4'),
(1, 76, '4'),
(1, 77, '5'),
(1, 78, '4'),
(1, 79, '4'),
(1, 80, '4'),
(1, 81, '4'),
(1, 82, '5'),
(1, 83, '2'),
(1, 84, '2'),
(1, 85, '2'),
(1, 86, '2'),
(1, 87, '2'),
(1, 88, '3'),
(1, 89, '2'),
(1, 90, '4'),
(1, 91, '5'),
(1, 92, '5'),
(1, 93, '5');

-- =====================================================
-- Hasil Tes 2 (ID_Hasil=2) - P. Made Hesa Dharma Putra (Introvert - tes pertama)
-- =====================================================
INSERT INTO `detail_tes` (`ID_Hasil`, `ID_Soal`, `Jawaban_Mahasiswa`) VALUES
(2, 1, '1'),
(2, 2, '20'),
(2, 3, '5'),
(2, 4, '4'),
(2, 5, '5'),
(2, 6, '4'),
(2, 7, '5'),
(2, 8, '4'),
(2, 9, '5'),
(2, 10, '4'),
(2, 11, '4'),
(2, 12, '5'),
(2, 13, '4'),
(2, 14, '5'),
(2, 15, '2'),
(2, 16, '2'),
(2, 17, '1'),
(2, 18, '1'),
(2, 19, '2'),
(2, 20, '2'),
(2, 21, '1'),
(2, 22, '1'),
(2, 23, '2'),
(2, 24, '2'),
(2, 25, '3'),
(2, 26, '2'),
(2, 27, '2'),
(2, 28, '3'),
(2, 29, '4'),
(2, 30, '3'),
(2, 31, '4'),
(2, 32, '4'),
(2, 33, '2'),
(2, 34, '2'),
(2, 35, '2'),
(2, 36, '2'),
(2, 37, '2'),
(2, 38, '3'),
(2, 39, '2'),
(2, 40, '3'),
(2, 41, '3'),
(2, 42, '4'),
(2, 43, '3'),
(2, 44, '4'),
(2, 45, '4'),
(2, 46, '5'),
(2, 47, '4'),
(2, 48, '2'),
(2, 49, '2'),
(2, 50, '2'),
(2, 51, '2'),
(2, 52, '4'),
(2, 53, '4'),
(2, 54, '4'),
(2, 55, '3'),
(2, 56, '4'),
(2, 57, '4'),
(2, 58, '4'),
(2, 59, '3'),
(2, 60, '4'),
(2, 61, '4'),
(2, 62, '4'),
(2, 63, '3'),
(2, 64, '2'),
(2, 65, '2'),
(2, 66, '4'),
(2, 67, '4'),
(2, 68, '2'),
(2, 69, '3'),
(2, 70, '3'),
(2, 71, '3'),
(2, 72, '2'),
(2, 73, '2'),
(2, 74, '1'),
(2, 75, '2'),
(2, 76, '3'),
(2, 77, '3'),
(2, 78, '2'),
(2, 79, '3'),
(2, 80, '2'),
(2, 81, '3'),
(2, 82, '1'),
(2, 83, '4'),
(2, 84, '4'),
(2, 85, '4'),
(2, 86, '4'),
(2, 87, '4'),
(2, 88, '3'),
(2, 89, '2'),
(2, 90, '3'),
(2, 91, '1'),
(2, 92, '2'),
(2, 93, '1');

-- =====================================================
-- Hasil Tes 3 (ID_Hasil=3) - P. Made Hesa Dharma Putra (Ambivert - tes kedua)
-- =====================================================
INSERT INTO `detail_tes` (`ID_Hasil`, `ID_Soal`, `Jawaban_Mahasiswa`) VALUES
(3, 1, '1'),
(3, 2, '20'),
(3, 3, '3'),
(3, 4, '3'),
(3, 5, '3'),
(3, 6, '3'),
(3, 7, '3'),
(3, 8, '3'),
(3, 9, '3'),
(3, 10, '3'),
(3, 11, '3'),
(3, 12, '3'),
(3, 13, '3'),
(3, 14, '3'),
(3, 15, '3'),
(3, 16, '3'),
(3, 17, '3'),
(3, 18, '3'),
(3, 19, '3'),
(3, 20, '3'),
(3, 21, '3'),
(3, 22, '3'),
(3, 23, '3'),
(3, 24, '3'),
(3, 25, '3'),
(3, 26, '3'),
(3, 27, '3'),
(3, 28, '3'),
(3, 29, '3'),
(3, 30, '3'),
(3, 31, '3'),
(3, 32, '3'),
(3, 33, '3'),
(3, 34, '3'),
(3, 35, '3'),
(3, 36, '3'),
(3, 37, '3'),
(3, 38, '3'),
(3, 39, '3'),
(3, 40, '3'),
(3, 41, '3'),
(3, 42, '3'),
(3, 43, '3'),
(3, 44, '3'),
(3, 45, '3'),
(3, 46, '3'),
(3, 47, '3'),
(3, 48, '3'),
(3, 49, '3'),
(3, 50, '3'),
(3, 51, '3'),
(3, 52, '3'),
(3, 53, '3'),
(3, 54, '3'),
(3, 55, '3'),
(3, 56, '3'),
(3, 57, '3'),
(3, 58, '3'),
(3, 59, '3'),
(3, 60, '3'),
(3, 61, '3'),
(3, 62, '3'),
(3, 63, '3'),
(3, 64, '3'),
(3, 65, '3'),
(3, 66, '3'),
(3, 67, '3'),
(3, 68, '3'),
(3, 69, '3'),
(3, 70, '3'),
(3, 71, '3'),
(3, 72, '3'),
(3, 73, '3'),
(3, 74, '3'),
(3, 75, '3'),
(3, 76, '3'),
(3, 77, '3'),
(3, 78, '3'),
(3, 79, '3'),
(3, 80, '3'),
(3, 81, '3'),
(3, 82, '3'),
(3, 83, '3'),
(3, 84, '3'),
(3, 85, '3'),
(3, 86, '3'),
(3, 87, '3'),
(3, 88, '3'),
(3, 89, '3'),
(3, 90, '3'),
(3, 91, '3'),
(3, 92, '3'),
(3, 93, '3');

-- =====================================================
-- Hasil Tes 4 (ID_Hasil=4) - Andi Makarim (Ambivert)
-- =====================================================
INSERT INTO `detail_tes` (`ID_Hasil`, `ID_Soal`, `Jawaban_Mahasiswa`) VALUES
(4, 1, '1'),
(4, 2, '19'),
(4, 3, '3'),
(4, 4, '3'),
(4, 5, '3'),
(4, 6, '2'),
(4, 7, '4'),
(4, 8, '3'),
(4, 9, '4'),
(4, 10, '3'),
(4, 11, '3'),
(4, 12, '4'),
(4, 13, '3'),
(4, 14, '3'),
(4, 15, '4'),
(4, 16, '3'),
(4, 17, '3'),
(4, 18, '3'),
(4, 19, '4'),
(4, 20, '4'),
(4, 21, '2'),
(4, 22, '2'),
(4, 23, '3'),
(4, 24, '3'),
(4, 25, '4'),
(4, 26, '3'),
(4, 27, '3'),
(4, 28, '4'),
(4, 29, '4'),
(4, 30, '3'),
(4, 31, '3'),
(4, 32, '3'),
(4, 33, '4'),
(4, 34, '3'),
(4, 35, '3'),
(4, 36, '3'),
(4, 37, '3'),
(4, 38, '4'),
(4, 39, '3'),
(4, 40, '4'),
(4, 41, '2'),
(4, 42, '3'),
(4, 43, '3'),
(4, 44, '3'),
(4, 45, '4'),
(4, 46, '4'),
(4, 47, '3'),
(4, 48, '3'),
(4, 49, '4'),
(4, 50, '4'),
(4, 51, '3'),
(4, 52, '3'),
(4, 53, '3'),
(4, 54, '3'),
(4, 55, '3'),
(4, 56, '3'),
(4, 57, '3'),
(4, 58, '3'),
(4, 59, '4'),
(4, 60, '3'),
(4, 61, '3'),
(4, 62, '3'),
(4, 63, '3'),
(4, 64, '3'),
(4, 65, '2'),
(4, 66, '3'),
(4, 67, '3'),
(4, 68, '2'),
(4, 69, '3'),
(4, 70, '3'),
(4, 71, '3'),
(4, 72, '4'),
(4, 73, '3'),
(4, 74, '3'),
(4, 75, '3'),
(4, 76, '4'),
(4, 77, '4'),
(4, 78, '3'),
(4, 79, '4'),
(4, 80, '3'),
(4, 81, '4'),
(4, 82, '3'),
(4, 83, '3'),
(4, 84, '3'),
(4, 85, '3'),
(4, 86, '3'),
(4, 87, '3'),
(4, 88, '3'),
(4, 89, '3'),
(4, 90, '4'),
(4, 91, '3'),
(4, 92, '3'),
(4, 93, '3');

-- =====================================================
-- Hasil Tes 5 (ID_Hasil=5) - Sanji Putra (Ekstrovert)
-- =====================================================
INSERT INTO `detail_tes` (`ID_Hasil`, `ID_Soal`, `Jawaban_Mahasiswa`) VALUES
(5, 1, '1'),
(5, 2, '20'),
(5, 3, '1'),
(5, 4, '1'),
(5, 5, '1'),
(5, 6, '2'),
(5, 7, '1'),
(5, 8, '1'),
(5, 9, '2'),
(5, 10, '1'),
(5, 11, '2'),
(5, 12, '1'),
(5, 13, '1'),
(5, 14, '2'),
(5, 15, '5'),
(5, 16, '5'),
(5, 17, '5'),
(5, 18, '5'),
(5, 19, '5'),
(5, 20, '5'),
(5, 21, '5'),
(5, 22, '4'),
(5, 23, '5'),
(5, 24, '5'),
(5, 25, '5'),
(5, 26, '5'),
(5, 27, '4'),
(5, 28, '5'),
(5, 29, '2'),
(5, 30, '4'),
(5, 31, '1'),
(5, 32, '1'),
(5, 33, '5'),
(5, 34, '5'),
(5, 35, '4'),
(5, 36, '5'),
(5, 37, '5'),
(5, 38, '4'),
(5, 39, '5'),
(5, 40, '5'),
(5, 41, '3'),
(5, 42, '1'),
(5, 43, '2'),
(5, 44, '1'),
(5, 45, '1'),
(5, 46, '1'),
(5, 47, '1'),
(5, 48, '5'),
(5, 49, '5'),
(5, 50, '5'),
(5, 51, '5'),
(5, 52, '1'),
(5, 53, '1'),
(5, 54, '1'),
(5, 55, '2'),
(5, 56, '1'),
(5, 57, '1'),
(5, 58, '1'),
(5, 59, '2'),
(5, 60, '1'),
(5, 61, '1'),
(5, 62, '1'),
(5, 63, '2'),
(5, 64, '5'),
(5, 65, '4'),
(5, 66, '1'),
(5, 67, '1'),
(5, 68, '1'),
(5, 69, '2'),
(5, 70, '2'),
(5, 71, '5'),
(5, 72, '5'),
(5, 73, '5'),
(5, 74, '5'),
(5, 75, '4'),
(5, 76, '5'),
(5, 77, '5'),
(5, 78, '5'),
(5, 79, '5'),
(5, 80, '5'),
(5, 81, '5'),
(5, 82, '5'),
(5, 83, '1'),
(5, 84, '1'),
(5, 85, '1'),
(5, 86, '1'),
(5, 87, '1'),
(5, 88, '2'),
(5, 89, '1'),
(5, 90, '5'),
(5, 91, '5'),
(5, 92, '5'),
(5, 93, '5');

-- --------------------------------------------------------

--
-- Table structure for table `hasil_tes`
--

CREATE TABLE `hasil_tes` (
  `ID_Hasil` int(11) NOT NULL,
  `ID_Mahasiswa` int(11) NOT NULL,
  `ID_Tes` int(11) NOT NULL,
  `ID_Jenis` int(11) DEFAULT NULL,
  `Waktu_Mulai_Tes` timestamp NULL DEFAULT NULL,
  `Waktu_Selesai_Tes` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hasil_tes`
--

INSERT INTO `hasil_tes` (`ID_Hasil`, `ID_Mahasiswa`, `ID_Tes`, `ID_Jenis`, `Waktu_Mulai_Tes`, `Waktu_Selesai_Tes`) VALUES
(1, 2, 1, 2, '2026-05-13 14:50:55', '2026-05-13 14:58:55'),
(2, 1, 1, 1, '2026-05-12 14:50:55', '2026-05-12 15:00:55'),
(3, 1, 1, 3, '2026-05-20 09:30:00', '2026-05-20 09:45:00'),
(4, 3, 1, 3, '2026-05-21 10:00:00', '2026-05-21 10:15:00'),
(5, 4, 1, 2, '2026-05-22 11:00:00', '2026-05-22 11:20:00');

-- --------------------------------------------------------

--
-- Table structure for table `jenis_hasil_tes`
--

CREATE TABLE `jenis_hasil_tes` (
  `ID_Jenis` int(11) NOT NULL,
  `Hasil` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jenis_hasil_tes`
--

INSERT INTO `jenis_hasil_tes` (`ID_Jenis`, `Hasil`) VALUES
(1, 'Introvert'),
(2, 'Ekstrovert'),
(3, 'Ambivert');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `ID_Mahasiswa` int(11) NOT NULL,
  `NIM` bigint(20) NOT NULL,
  `Nama_Mahasiswa` varchar(100) NOT NULL,
  `Password_Mahasiswa` varchar(255) NOT NULL,
  `Alamat` text DEFAULT NULL,
  `Nomor_Telepon` varchar(20) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Deskripsi` text DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`ID_Mahasiswa`, `NIM`, `Nama_Mahasiswa`, `Password_Mahasiswa`, `Alamat`, `Nomor_Telepon`, `Email`, `Deskripsi`, `created_by`) VALUES
(1, 2408561131, 'P. Made Hesa Dharma Putra', 'mahasiswa1', 'Jl. Pendidikan No. 123, Denpasar, Bali', '081234567890', 'hesa.putra@student.unud.ac.id', 'Mahasiswa semester 6, aktif dalam organisasi kampus, memiliki minat di bidang teknologi.', 1),
(2, 2408561152, 'I Gede Andhika Pratama', 'mahasiswa2', 'Jl. Merdeka No. 45, Gianyar, Bali', '081298765432', 'andhika.pratama@student.unud.ac.id', 'Mahasiswa semester 6 yang aktif dalam berbagai kegiatan kemahasiswaan.', 1),
(3, 2408561190, 'Andi Makarim', 'mahasiswa3', 'Jl. Sudirman No. 12, Jakarta Selatan', '081234567891', 'andi.makarim@student.unud.ac.id', 'Mahasiswa semester 4, aktif dalam kegiatan sosial dan memiliki minat di bidang seni.', 1),
(4, 2408561198, 'Sanji Putra', 'mahasiswa4', 'Jl. Gatot Subroto No. 88, Surabaya', '081234567892', 'sanji.putra@student.unud.ac.id', 'Mahasiswa semester 4, aktif dalam organisasi kemahasiswaan dan kegiatan olahraga.', 1);

-- --------------------------------------------------------

--
-- Table structure for table `tes`
--

CREATE TABLE `tes` (
  `ID_Tes` int(11) NOT NULL,
  `Nama_Tes` varchar(100) NOT NULL,
  `Jumlah_Soal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tes`
--

INSERT INTO `tes` (`ID_Tes`, `Nama_Tes`, `Jumlah_Soal`) VALUES
(1, 'Tes Kepribadian Introvert Ekstrovert Ambivert', 93);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID_Admin`),
  ADD UNIQUE KEY `Username_Admin` (`Username_Admin`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `bank_soal`
--
ALTER TABLE `bank_soal`
  ADD PRIMARY KEY (`ID_Soal`),
  ADD KEY `ID_Tes` (`ID_Tes`);

--
-- Indexes for table `detail_tes`
--
ALTER TABLE `detail_tes`
  ADD PRIMARY KEY (`ID_Hasil`,`ID_Soal`),
  ADD KEY `ID_Soal` (`ID_Soal`);

--
-- Indexes for table `hasil_tes`
--
ALTER TABLE `hasil_tes`
  ADD PRIMARY KEY (`ID_Hasil`),
  ADD KEY `ID_Mahasiswa` (`ID_Mahasiswa`),
  ADD KEY `ID_Tes` (`ID_Tes`),
  ADD KEY `ID_Jenis` (`ID_Jenis`);

--
-- Indexes for table `jenis_hasil_tes`
--
ALTER TABLE `jenis_hasil_tes`
  ADD PRIMARY KEY (`ID_Jenis`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`ID_Mahasiswa`),
  ADD UNIQUE KEY `NIM` (`NIM`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD KEY `created_by` (`created_by`);

--
-- Indexes for table `tes`
--
ALTER TABLE `tes`
  ADD PRIMARY KEY (`ID_Tes`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID_Admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `bank_soal`
--
ALTER TABLE `bank_soal`
  MODIFY `ID_Soal` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `hasil_tes`
--
ALTER TABLE `hasil_tes`
  MODIFY `ID_Hasil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `jenis_hasil_tes`
--
ALTER TABLE `jenis_hasil_tes`
  MODIFY `ID_Jenis` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `ID_Mahasiswa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tes`
--
ALTER TABLE `tes`
  MODIFY `ID_Tes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bank_soal`
--
ALTER TABLE `bank_soal`
  ADD CONSTRAINT `bank_soal_ibfk_1` FOREIGN KEY (`ID_Tes`) REFERENCES `tes` (`ID_Tes`) ON DELETE CASCADE;

--
-- Constraints for table `detail_tes`
--
ALTER TABLE `detail_tes`
  ADD CONSTRAINT `detail_tes_ibfk_1` FOREIGN KEY (`ID_Hasil`) REFERENCES `hasil_tes` (`ID_Hasil`) ON DELETE CASCADE,
  ADD CONSTRAINT `detail_tes_ibfk_2` FOREIGN KEY (`ID_Soal`) REFERENCES `bank_soal` (`ID_Soal`) ON DELETE CASCADE;

--
-- Constraints for table `hasil_tes`
--
ALTER TABLE `hasil_tes`
  ADD CONSTRAINT `hasil_tes_ibfk_1` FOREIGN KEY (`ID_Mahasiswa`) REFERENCES `mahasiswa` (`ID_Mahasiswa`) ON DELETE CASCADE,
  ADD CONSTRAINT `hasil_tes_ibfk_2` FOREIGN KEY (`ID_Tes`) REFERENCES `tes` (`ID_Tes`) ON DELETE CASCADE,
  ADD CONSTRAINT `hasil_tes_ibfk_3` FOREIGN KEY (`ID_Jenis`) REFERENCES `jenis_hasil_tes` (`ID_Jenis`) ON DELETE SET NULL;

--
-- Constraints for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD CONSTRAINT `mahasiswa_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `admin` (`ID_Admin`) ON DELETE SET NULL;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;