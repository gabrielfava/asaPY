/*
 Navicat MySQL Data Transfer

 Source Server         : AsaPY
 Source Server Type    : MySQL
 Source Server Version : 50637
 Source Host           : robb0469.publiccloud.com.br:3306
 Source Schema         : defcode_asap

 Target Server Type    : MySQL
 Target Server Version : 50637
 File Encoding         : 65001

 Date: 24/02/2018 14:23:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for teams
-- ----------------------------
DROP TABLE IF EXISTS `teams`;
CREATE TABLE `teams`  (
  `team_number` int(11) NOT NULL,
  `team_site` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `team_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `team_short_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `enabled` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `multi_login` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `team_full_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`team_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
