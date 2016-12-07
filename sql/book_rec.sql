/*
Navicat MySQL Data Transfer

Source Server         : LOCAL
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : book_recommendation

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-12-06 22:03:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bx-book-avg
-- ----------------------------
DROP TABLE IF EXISTS `bx-book-avg`;
CREATE TABLE `bx-book-avg` (
`ISBN`  varchar(13) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`rating_sum`  bigint(20) NULL DEFAULT NULL ,
`rating_num`  bigint(20) NULL DEFAULT NULL ,
`rating_avg`  double NULL DEFAULT NULL ,
PRIMARY KEY (`ISBN`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci

;

-- ----------------------------
-- Table structure for bx-book-ratings
-- ----------------------------
DROP TABLE IF EXISTS `bx-book-ratings`;
CREATE TABLE `bx-book-ratings` (
`id`  int(11) NOT NULL AUTO_INCREMENT ,
`User-ID`  int(11) NOT NULL DEFAULT 0 ,
`ISBN`  varchar(13) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' ,
`Book-Rating`  int(11) NOT NULL DEFAULT 0 ,
PRIMARY KEY (`id`),
FOREIGN KEY (`User-ID`) REFERENCES `bx-users` (`User-ID`) ON DELETE CASCADE ON UPDATE NO ACTION,
INDEX `FGN` (`User-ID`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
AUTO_INCREMENT=601771

;

-- ----------------------------
-- Table structure for bx-books
-- ----------------------------
DROP TABLE IF EXISTS `bx-books`;
CREATE TABLE `bx-books` (
`ISBN`  varchar(13) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '' ,
`Book-Title`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`Book-Author`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`Year-Of-Publication`  int(10) UNSIGNED NULL DEFAULT NULL ,
`Publisher`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`Image-URL-S`  varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`Image-URL-M`  varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
`Image-URL-L`  varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NULL DEFAULT NULL ,
PRIMARY KEY (`ISBN`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci

;

-- ----------------------------
-- Table structure for bx-users
-- ----------------------------
DROP TABLE IF EXISTS `bx-users`;
CREATE TABLE `bx-users` (
`User-ID`  int(11) NOT NULL ,
`City`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`State`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`Country`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`Age`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
PRIMARY KEY (`User-ID`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci

;

-- ----------------------------
-- Auto increment value for bx-book-ratings
-- ----------------------------
ALTER TABLE `bx-book-ratings` AUTO_INCREMENT=601771;
SET FOREIGN_KEY_CHECKS=1;
