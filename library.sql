-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.29
--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
CREATE TABLE `author` (
  `aut_name` varchar(255) NOT NULL,
  `aut_id` int NOT NULL,
  PRIMARY KEY (`aut_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
INSERT INTO `author` VALUES ('张金',1);
INSERT INTO `author` VALUES ('宋春瑶',2);
INSERT INTO `author` VALUES ('王刚',3);
INSERT INTO `author` VALUES ('刘哲理',4);
INSERT INTO `author` VALUES ('罗翔',5);
INSERT INTO `author` VALUES ('周六野',6);
INSERT INTO `author` VALUES ('戴维迈尔斯',7);
INSERT INTO `author` VALUES ('王艺昕',8);
INSERT INTO `author` VALUES ('mike',9);
INSERT INTO `author` VALUES ('amy',10);
UNLOCK TABLES;

--
-- Table structure for table `belong`
--

DROP TABLE IF EXISTS `belong`;
CREATE TABLE `belong` (
  `b_id` int NOT NULL,
  `c_id` int NOT NULL,
  PRIMARY KEY (`b_id`,`c_id`),
  KEY `c_id` (`c_id`),
  CONSTRAINT `belong_ibfk_1` FOREIGN KEY (`c_id`) REFERENCES `class` (`c_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `belong_ibfk_2` FOREIGN KEY (`b_id`) REFERENCES `book` (`b_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `belong`
--

LOCK TABLES `belong` WRITE;
INSERT INTO `belong` VALUES (1,1);
INSERT INTO `belong` VALUES (3,1);
INSERT INTO `belong` VALUES (4,1);
INSERT INTO `belong` VALUES (5,2);
INSERT INTO `belong` VALUES (6,2);
INSERT INTO `belong` VALUES (7,2);
INSERT INTO `belong` VALUES (9,4);
INSERT INTO `belong` VALUES (11,4);
INSERT INTO `belong` VALUES (10,5);
INSERT INTO `belong` VALUES (12,6);
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `b_name` varchar(255) NOT NULL,
  `b_id` int NOT NULL,
  `b_price` float(10,2) NOT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
INSERT INTO `book` VALUES ('计组',1,44.44);
INSERT INTO `book` VALUES ('数据库',3,44.44);
INSERT INTO `book` VALUES ('软件安全',4,79.99);
INSERT INTO `book` VALUES ('民法典',5,44.43);
INSERT INTO `book` VALUES ('婚姻法',6,44.44);
INSERT INTO `book` VALUES ('刑法',7,44.44);
INSERT INTO `book` VALUES ('社会心理学',8,44.44);
INSERT INTO `book` VALUES ('胶囊衣橱',9,44.44);
INSERT INTO `book` VALUES ('瑜伽教程',10,27.88);
INSERT INTO `book` VALUES ('写作技巧',11,44.44),
INSERT INTO `book` VALUES ('英语六级必背单词',12,44.44);
INSERT INTO `book` VALUES ('软件安全',13,79.99);
INSERT INTO `book` VALUES ('人生效率管理',19,44.44);
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `c_name` varchar(255) NOT NULL,
  `c_id` int NOT NULL,
  `c_floor` int NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
INSERT INTO `class` VALUES ('计算机',1,4);
INSERT INTO `class` VALUES ('法学',2,3);
INSERT INTO `class` VALUES ('心理学',3,5);
INSERT INTO `class` VALUES ('文学',4,3);
INSERT INTO `class` VALUES ('体育',5,4);
INSERT INTO `class` VALUES ('外语',6,3);
UNLOCK TABLES;

--
-- Table structure for table `lend`
--

DROP TABLE IF EXISTS `lend`;
CREATE TABLE `lend` (
  `b_id` int NOT NULL,
  `std_id` int NOT NULL,
  `begin_t` date NOT NULL,
  `end_t` date NOT NULL,
  PRIMARY KEY (`b_id`,`std_id`,`begin_t`) USING BTREE,
  KEY `std_id` (`std_id`),
  CONSTRAINT `lend_ibfk_1` FOREIGN KEY (`b_id`) REFERENCES `book` (`b_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `lend_ibfk_2` FOREIGN KEY (`std_id`) REFERENCES `student` (`std_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lend`
--

LOCK TABLES `lend` WRITE;
INSERT INTO `lend` VALUES (1,5,'2022-05-11','2022-05-25');
INSERT INTO `lend` VALUES (1,6,'2022-05-17','2022-05-31');
INSERT INTO `lend` VALUES (3,1,'2022-05-24','2022-06-07');
INSERT INTO `lend` VALUES (3,2,'2022-05-24','2022-06-07');
INSERT INTO `lend` VALUES (4,1,'2021-06-18','2021-06-30');
INSERT INTO `lend` VALUES (4,5,'2022-05-11','2022-05-25');
INSERT INTO `lend` VALUES (4,6,'2022-05-10','2022-05-24');
INSERT INTO `lend` VALUES (5,3,'2022-05-26','2022-06-19');
INSERT INTO `lend` VALUES (6,3,'2022-05-10','2022-05-24');
INSERT INTO `lend` VALUES (7,3,'2022-05-10','2022-05-24');
INSERT INTO `lend` VALUES (7,8,'2021-06-01','2021-06-14');
INSERT INTO `lend` VALUES (9,4,'2022-05-21','2022-06-04');
INSERT INTO `lend` VALUES (10,2,'2022-05-22','2022-06-05');
INSERT INTO `lend` VALUES (11,7,'2022-05-24','2022-06-07');
INSERT INTO `lend` VALUES (12,4,'2022-05-20','2022-06-03');
INSERT INTO `lend` VALUES (12,5,'2021-05-26','2021-05-30');
UNLOCK TABLES;


--
-- Table structure for table `publish`
--

DROP TABLE IF EXISTS `publish`;
CREATE TABLE `publish` (
  `b_id` int NOT NULL,
  `pub_name` varchar(255) NOT NULL,
  `pub_date` date NOT NULL,
  PRIMARY KEY (`b_id`,`pub_name`),
  KEY `pub_name` (`pub_name`),
  CONSTRAINT `publish_ibfk_1` FOREIGN KEY (`b_id`) REFERENCES `book` (`b_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `publish_ibfk_2` FOREIGN KEY (`pub_name`) REFERENCES `publisher` (`pub_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `publish`
--

LOCK TABLES `publish` WRITE;
INSERT INTO `publish` VALUES (1,'南开大学出版社','2022-02-08');
INSERT INTO `publish` VALUES (3,'南开大学出版社','2019-02-06');
INSERT INTO `publish` VALUES (4,'南开大学出版社','2009-11-12');
INSERT INTO `publish` VALUES (5,'清华大学出版社','2020-02-06');
INSERT INTO `publish` VALUES (6,'北京大学出版社','2015-07-30');
INSERT INTO `publish` VALUES (7,'三联书店','2017-10-19');
INSERT INTO `publish` VALUES (8,'清华大学出版社','2013-01-09');
INSERT INTO `publish` VALUES (9,'三联书店','2013-05-06');
INSERT INTO `publish` VALUES (10,'三联书店','2020-02-06');
INSERT INTO `publish` VALUES (11,'人民教育出版社','2022-03-15');
INSERT INTO `publish` VALUES (12,'人民教育出版社','2019-12-27');
INSERT INTO `publish` VALUES (13,'南开大学出版社','2021-08-19');
UNLOCK TABLES;

--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
CREATE TABLE `publisher` (
  `pub_name` varchar(255) NOT NULL,
  PRIMARY KEY (`pub_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `publisher`
--

LOCK TABLES `publisher` WRITE;
INSERT INTO `publisher` VALUES ('三联书店');
INSERT INTO `publisher` VALUES ('人民教育出版社');
INSERT INTO `publisher` VALUES ('北京大学出版社');
INSERT INTO `publisher` VALUES ('南开大学出版社');
INSERT INTO `publisher` VALUES ('清华大学出版社');
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `std_name` varchar(255) NOT NULL,
  `std_id` int NOT NULL,
  `std_major` varchar(255) NOT NULL,
  PRIMARY KEY (`std_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
INSERT INTO `student` VALUES ('张驰',1,'计科');
INSERT INTO `student` VALUES ('杨馨仪',2,'体育');
INSERT INTO `student` VALUES ('韩菁菁',3,'法学');
INSERT INTO `student` VALUES ('乐佳檬',4,'表演');
INSERT INTO `student` VALUES ('边笛',5,'计科');
INSERT INTO `student` VALUES ('贺祎昕',6,'计科');
INSERT INTO `student` VALUES ('韩萍',7,'新闻');
INSERT INTO `student` VALUES ('李博睿',8,'新闻');
UNLOCK TABLES;

--
-- Table structure for table `write`
--

DROP TABLE IF EXISTS `write`;
CREATE TABLE `write` (
  `b_id` int NOT NULL,
  `aut_id` int NOT NULL,
  PRIMARY KEY (`b_id`,`aut_id`),
  KEY `aut_id` (`aut_id`),
  CONSTRAINT `write_ibfk_1` FOREIGN KEY (`b_id`) REFERENCES `book` (`b_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `write_ibfk_2` FOREIGN KEY (`aut_id`) REFERENCES `author` (`aut_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `write`
--

LOCK TABLES `write` WRITE;
INSERT INTO `write` VALUES (1,1);
INSERT INTO `write` VALUES (3,2);
INSERT INTO `write` VALUES (4,4);
INSERT INTO `write` VALUES (5,5);
INSERT INTO `write` VALUES (6,5);
INSERT INTO `write` VALUES (7,5);
INSERT INTO `write` VALUES (10,6);
INSERT INTO `write` VALUES (8,7);
INSERT INTO `write` VALUES (12,8);
INSERT INTO `write` VALUES (11,9);
INSERT INTO `write` VALUES (9,10);
UNLOCK TABLES;


DROP trigger IF EXISTS `check_date`;
delimiter //
CREATE trigger `check_date` BEFORE INSERT ON lend for each ROW
BEGIN
IF new.begin_t>curtime() OR new.begin_t>new.end_t
THEN
signal sqlstate '22003' SET message_text='借阅时间输入不合法';
END IF;
END
//
DELIMITER ;


DROP PROCEDURE IF EXISTS `book_update`;
delimiter //
CREATE PROCEDURE `book_update`(in `publish_name` varchar(255),in `book_name` varchar(255),in `book_price` float(10,2))
IF book_name NOT IN (SELECT b_name FROM book) OR publish_name NOT IN (SELECT pub_name FROM publish)
THEN signal sqlstate '22003' set message_text='输入的书籍名称或出版社名称不正确';
ELSE
UPDATE `book` SET `b_price`=book_price WHERE `b_name`=book_name AND `b_id` IN (SELECT b_id FROM publish WHERE pub_name=publish_name);
END IF;
END
//
delimiter ;


DROP view IF EXISTS `author_find`;
CREATE view `author_find`(author_name,countworks) AS
SELECT author.aut_name,count(*)
FROM `write` natural join `author`
GROUP BY author.aut_id;