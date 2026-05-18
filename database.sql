-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2026 at 01:49 PM
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
(1, 1, 'Gender: What is your gender? (1=Male, 2=Female, 3=Other)'),
(2, 1, 'Age: What is your age in years?'),
(3, 1, 'Q1: I would never audition to be on a game show.'),
(4, 1, 'Q2: I am not much of a flirt.'),
(5, 1, 'Q3: I have to psych myself up before I am brave enough to make a phone call.'),
(6, 1, 'Q4: I would hate living with room mates.'),
(7, 1, 'Q5: I mostly listen to people in conversations.'),
(8, 1, 'Q6: I reveal little about myself.'),
(9, 1, 'Q7: I spend hours alone with my hobbies.'),
(10, 1, 'Q8: I prefer to eat alone.'),
(11, 1, 'Q9: I have trouble finding people I want to be friends with.'),
(12, 1, 'Q10: I prefer to socialize 1 on 1, than with a group.'),
(13, 1, 'Q11: I sometimes speak so quietly people sometimes have trouble hearing me.'),
(14, 1, 'Q12: I do not like to get my picture taken.'),
(15, 1, 'Q13: I can keep a conversation going with anyone about anything.'),
(16, 1, 'Q14: I want a huge social circle.'),
(17, 1, 'Q15: I talk to people when waiting in lines.'),
(18, 1, 'Q16: I act wild and crazy.'),
(19, 1, 'Q17: I am a bundle of joy.'),
(20, 1, 'Q18: I love excitement.'),
(21, 1, 'Q19: I\'d like to be in a parade.'),
(22, 1, 'Q20: I am a flamboyant person.'),
(23, 1, 'Q21: I am good at making impromptu speeches.'),
(24, 1, 'Q22: I naturally emerge as a leader.'),
(25, 1, 'Q23: I am spontaneous.'),
(26, 1, 'Q24: I would enjoy being a sports team coach.'),
(27, 1, 'Q25: I have a strong personality.'),
(28, 1, 'Q26: I am excited by many different activities.'),
(29, 1, 'Q27: I spend most of my time in fantasy worlds.'),
(30, 1, 'Q28: I often feel lucky.'),
(31, 1, 'Q29: I don\'t make eye contact when I talk with people.'),
(32, 1, 'Q30: I have a monotone voice.'),
(33, 1, 'Q31: I am a touchy feely person.'),
(34, 1, 'Q32: I would like to try bungee jumping.'),
(35, 1, 'Q33: I tend to be admired by others.'),
(36, 1, 'Q34: I make big physical movements whenever I get excited.'),
(37, 1, 'Q35: I am brave.'),
(38, 1, 'Q36: I am always in the moment.'),
(39, 1, 'Q37: I am involved with my community.'),
(40, 1, 'Q38: I am good an entertaining children.'),
(41, 1, 'Q39: I like formal occasions.'),
(42, 1, 'Q40: I would have to be lost for a very long time before asking help.'),
(43, 1, 'Q41: I do not care about sports.'),
(44, 1, 'Q42: I prefer individual sports to team sports.'),
(45, 1, 'Q43: My parents know nothing about my love life.'),
(46, 1, 'Q44: I mostly listen to people in conversations.'),
(47, 1, 'Q45: I never leave the door to my room open.'),
(48, 1, 'Q46: I make a lot of hand motions when I talk.'),
(49, 1, 'Q47: I take lots of pictures of my activities.'),
(50, 1, 'Q48: When I was a child, I put on fake concerts and plays with my friends.'),
(51, 1, 'Q49: I really like dancing.'),
(52, 1, 'Q50: I would have difficulty describing myself to someone.'),
(53, 1, 'Q51: My life would not make a good story.'),
(54, 1, 'Q52: I am hesitant to give suggestions.'),
(55, 1, 'Q53: I tire out quickly.'),
(56, 1, 'Q54: I never tell people the important things about myself.'),
(57, 1, 'Q55: I avoid going to unknown places.'),
(58, 1, 'Q56: Going to the doctor is always awkward for me.'),
(59, 1, 'Q57: I have not kept up with my old friends over the years.'),
(60, 1, 'Q58: I have not been joyful for quite some time.'),
(61, 1, 'Q59: I hate to ask for help.'),
(62, 1, 'Q60: If I were to die, I would not want there to be a memorial for me.'),
(63, 1, 'Q61: I hate shopping.'),
(64, 1, 'Q62: I love to do impressions.'),
(65, 1, 'Q63: I would be pleased if asked to speak at a funeral.'),
(66, 1, 'Q64: I would never go to a dance club.'),
(67, 1, 'Q65: I find it very hard to tell people I find them attractive.'),
(68, 1, 'Q66: I hate people.'),
(69, 1, 'Q67: I was an outcast in school.'),
(70, 1, 'Q68: I would enjoy being a librarian.'),
(71, 1, 'Q69: I am usually not single.'),
(72, 1, 'Q70: I am able to stand up for myself.'),
(73, 1, 'Q71: I would go surfing regularly if I lived on a beach.'),
(74, 1, 'Q72: I have wanted to be a stand-up comedian.'),
(75, 1, 'Q73: I am a high status person.'),
(76, 1, 'Q74: I work out regularly.'),
(77, 1, 'Q75: I laugh a lot.'),
(78, 1, 'Q76: I like pranks.'),
(79, 1, 'Q77: I am happy with my life.'),
(80, 1, 'Q78: I am never at a loss for words.'),
(81, 1, 'Q79: I feel healthy and vibrant most of the time.'),
(82, 1, 'Q80: I love large parties.'),
(83, 1, 'Q81: I am quiet around strangers.'),
(84, 1, 'Q82: I don\'t talk a lot.'),
(85, 1, 'Q83: I keep in the background.'),
(86, 1, 'Q84: I don\'t like to draw attention to myself.'),
(87, 1, 'Q85: I have little to say.'),
(88, 1, 'Q86: I often feel blue.'),
(89, 1, 'Q87: I am not really interested in others.'),
(90, 1, 'Q88: I make people feel at ease.'),
(91, 1, 'Q89: I don\'t mind being the center of attention.'),
(92, 1, 'Q90: I start conversations.'),
(93, 1, 'Q91: I talk to a lot of different people at parties.');

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
-- Dumping data for table `detail_tes`
--

INSERT INTO `detail_tes` (`ID_Hasil`, `ID_Soal`, `Jawaban_Mahasiswa`) VALUES
(1, 1, '1'),
(1, 2, '20'),
(1, 3, '5'),
(1, 4, '4'),
(1, 5, '5'),
(1, 6, '4'),
(1, 7, '5'),
(1, 8, '4'),
(1, 9, '5'),
(1, 10, '4'),
(1, 11, '4'),
(1, 12, '5'),
(1, 13, '4'),
(1, 14, '5'),
(1, 15, '2'),
(1, 16, '2'),
(1, 17, '1'),
(1, 18, '1'),
(1, 19, '2'),
(1, 20, '2'),
(1, 21, '1'),
(1, 22, '1'),
(1, 23, '2'),
(1, 24, '2'),
(1, 25, '3'),
(1, 26, '2'),
(1, 27, '2'),
(1, 28, '3'),
(1, 29, '4'),
(1, 30, '3'),
(1, 31, '4'),
(1, 32, '4'),
(1, 33, '2'),
(1, 34, '2'),
(1, 35, '2'),
(1, 36, '2'),
(1, 37, '2'),
(1, 38, '3'),
(1, 39, '2'),
(1, 40, '3'),
(1, 41, '3'),
(1, 42, '4'),
(1, 43, '3'),
(1, 44, '4'),
(1, 45, '4'),
(1, 46, '5'),
(1, 47, '4'),
(1, 48, '2'),
(1, 49, '2'),
(1, 50, '2'),
(1, 51, '2'),
(1, 52, '4'),
(1, 53, '4'),
(1, 54, '4'),
(1, 55, '3'),
(1, 56, '4'),
(1, 57, '4'),
(1, 58, '4'),
(1, 59, '3'),
(1, 60, '4'),
(1, 61, '4'),
(1, 62, '4'),
(1, 63, '3'),
(1, 64, '2'),
(1, 65, '2'),
(1, 66, '4'),
(1, 67, '4'),
(1, 68, '2'),
(1, 69, '3'),
(1, 70, '3'),
(1, 71, '3'),
(1, 72, '2'),
(1, 73, '2'),
(1, 74, '1'),
(1, 75, '2'),
(1, 76, '3'),
(1, 77, '3'),
(1, 78, '2'),
(1, 79, '3'),
(1, 80, '2'),
(1, 81, '3'),
(1, 82, '1'),
(1, 83, '4'),
(1, 84, '4'),
(1, 85, '4'),
(1, 86, '4'),
(1, 87, '4'),
(1, 88, '3'),
(1, 89, '2'),
(1, 90, '3'),
(1, 91, '1'),
(1, 92, '2'),
(1, 93, '1'),
(2, 1, '1'),
(2, 2, '21'),
(2, 3, '1'),
(2, 4, '1'),
(2, 5, '1'),
(2, 6, '2'),
(2, 7, '2'),
(2, 8, '2'),
(2, 9, '2'),
(2, 10, '2'),
(2, 11, '2'),
(2, 12, '2'),
(2, 13, '2'),
(2, 14, '2'),
(2, 15, '5'),
(2, 16, '5'),
(2, 17, '5'),
(2, 18, '4'),
(2, 19, '4'),
(2, 20, '5'),
(2, 21, '4'),
(2, 22, '4'),
(2, 23, '4'),
(2, 24, '4'),
(2, 25, '4'),
(2, 26, '4'),
(2, 27, '4'),
(2, 28, '5'),
(2, 29, '2'),
(2, 30, '4'),
(2, 31, '2'),
(2, 32, '2'),
(2, 33, '4'),
(2, 34, '4'),
(2, 35, '4'),
(2, 36, '4'),
(2, 37, '4'),
(2, 38, '3'),
(2, 39, '4'),
(2, 40, '4'),
(2, 41, '3'),
(2, 42, '2'),
(2, 43, '3'),
(2, 44, '2'),
(2, 45, '2'),
(2, 46, '2'),
(2, 47, '2'),
(2, 48, '4'),
(2, 49, '4'),
(2, 50, '4'),
(2, 51, '4'),
(2, 52, '2'),
(2, 53, '2'),
(2, 54, '2'),
(2, 55, '3'),
(2, 56, '2'),
(2, 57, '2'),
(2, 58, '2'),
(2, 59, '3'),
(2, 60, '2'),
(2, 61, '2'),
(2, 62, '2'),
(2, 63, '3'),
(2, 64, '4'),
(2, 65, '3'),
(2, 66, '2'),
(2, 67, '2'),
(2, 68, '1'),
(2, 69, '3'),
(2, 70, '3'),
(2, 71, '4'),
(2, 72, '4'),
(2, 73, '4'),
(2, 74, '4'),
(2, 75, '4'),
(2, 76, '4'),
(2, 77, '5'),
(2, 78, '4'),
(2, 79, '4'),
(2, 80, '4'),
(2, 81, '4'),
(2, 82, '5'),
(2, 83, '2'),
(2, 84, '2'),
(2, 85, '2'),
(2, 86, '2'),
(2, 87, '2'),
(2, 88, '3'),
(2, 89, '2'),
(2, 90, '4'),
(2, 91, '5'),
(2, 92, '5'),
(2, 93, '5');

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
(1, 1, 1, 1, '2026-05-12 14:50:55', '2026-05-12 15:00:55'),
(2, 2, 1, 2, '2026-05-13 14:50:55', '2026-05-13 14:58:55');

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
(2, 2408561152, 'I Gede Andhika Pratama', 'mahasiswa2', 'Jl. Merdeka No. 45, Gianyar, Bali', '081298765432', 'andhika.pratama@student.unud.ac.id', 'Mahasiswa semester 6 yang aktif dalam berbagai kegiatan kemahasiswaan.', 1);

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
  MODIFY `ID_Hasil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `jenis_hasil_tes`
--
ALTER TABLE `jenis_hasil_tes`
  MODIFY `ID_Jenis` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `ID_Mahasiswa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
