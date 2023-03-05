/*
Navicat MySQL Data Transfer

Source Server         : zoo
Source Server Version : 50614
Source Host           : localhost:3306
Source Database       : Attendance

Target Server Type    : MYSQL
Target Server Version : 50614
File Encoding         : 65001

Date: 2022-03-14 11:20:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for company
-- ----------------------------
DROP TABLE IF EXISTS `company`;
CREATE TABLE `company` (
  `c_id` varchar(20) NOT NULL DEFAULT '',
  `c_hr_phone` char(11) NOT NULL,
  `c_name` varchar(30) NOT NULL,
  `c_phone` varchar(11) DEFAULT NULL,
  `c_type` varchar(20) NOT NULL,
  `c_location` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`c_id`),
  KEY `fk_hr_phone` (`c_hr_phone`) USING BTREE,
  CONSTRAINT `fk_hr_phone` FOREIGN KEY (`c_hr_phone`) REFERENCES `hr` (`hr_phone`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of company
-- ----------------------------
INSERT INTO `company` VALUES ('110000410108012', '18515981156', '微软', '18515981156', '软件和信息技术服务业', '北京市海淀区');
INSERT INTO `company` VALUES ('110108017732595', '18844112685', '北京菁英天下国际教育咨询有限公司', '010-8233433', '租赁和商务服务业', '北京市海淀区学院南路15号16号楼1层1028');
INSERT INTO `company` VALUES ('913100007178530512', '18514774056', '西窗科技（上海）有限公司', '021-5368785', '互联网相关服务', '上海市');
INSERT INTO `company` VALUES ('914403005840880762', '13510289812', '深圳市博伦思品牌管理有限公司', '13510286266', '零售业', '深圳市福田区深南大道星河世纪大厦B栋401');

-- ----------------------------
-- Table structure for dailyAttendance
-- ----------------------------
DROP TABLE IF EXISTS `dailyAttendance`;
CREATE TABLE `dailyAttendance` (
  `att_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `att_s_phone` char(11) NOT NULL,
  `att_datetime` datetime NOT NULL,
  `att_state` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`att_id`),
  KEY `daily_attendance_ibfk_1` (`att_s_phone`) USING BTREE,
  CONSTRAINT `att_s_phone` FOREIGN KEY (`att_s_phone`) REFERENCES `staff` (`s_phone`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of dailyAttendance
-- ----------------------------

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `dep_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `dep_com_id` varchar(20) NOT NULL,
  `dep_name` varchar(20) NOT NULL,
  `dep_start_time` time(6) NOT NULL,
  `dep_end_time` time(6) NOT NULL,
  PRIMARY KEY (`dep_id`),
  KEY `dep_com_id` (`dep_com_id`),
  CONSTRAINT `dep_com_id` FOREIGN KEY (`dep_com_id`) REFERENCES `company` (`c_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of department
-- ----------------------------

-- ----------------------------
-- Table structure for hr
-- ----------------------------
DROP TABLE IF EXISTS `hr`;
CREATE TABLE `hr` (
  `hr_phone` char(11) NOT NULL,
  `hr_id` varchar(16) NOT NULL,
  `hr_name` varchar(20) NOT NULL,
  `hr_passwd` varchar(32) NOT NULL,
  `hr_email` varchar(30) DEFAULT NULL,
  `hr_sex` int(1) DEFAULT NULL,
  PRIMARY KEY (`hr_phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hr
-- ----------------------------
INSERT INTO `hr` VALUES ('13510289812', 'z2569854', '张颂', '123456', 'bolun@163.com', '1');
INSERT INTO `hr` VALUES ('18514774056', 'l1020305', '刘振宇', '123456', 'liuzhenyu@163.com', '1');
INSERT INTO `hr` VALUES ('18515981156', 'k4567', '候阳', '123456', 'vcv@qq.cn', '1');
INSERT INTO `hr` VALUES ('18844112685', 'lui4569', '刘宇熙', '123456', 'kfnb@bjyjwy.com', '1');

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `m_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `m_s_phone` char(11) NOT NULL,
  `m_apply_datetime` datetime NOT NULL,
  `m_type` int(2) NOT NULL,
  `m_demand` text,
  `m_state` int(2) NOT NULL,
  `m_begin_datetime` datetime DEFAULT NULL,
  `m_end_datetime` datetime DEFAULT NULL,
  `m_treat_hr_id` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`m_id`),
  KEY `m_treat_hr_phone` (`m_treat_hr_id`),
  KEY `m_s_phone` (`m_s_phone`) USING BTREE,
  CONSTRAINT `m_s_phone` FOREIGN KEY (`m_s_phone`) REFERENCES `staff` (`s_phone`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message
-- ----------------------------

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff` (
  `s_phone` char(11) NOT NULL,
  `s_passwd` varchar(32) NOT NULL,
  `s_name` varchar(20) DEFAULT NULL,
  `s_addr` varchar(30) DEFAULT NULL,
  `s_email` varchar(30) DEFAULT NULL,
  `s_id` varchar(16) DEFAULT NULL,
  `s_depart_id` bigint(20) DEFAULT NULL,
  `s_com_id` varchar(20) DEFAULT NULL,
  `s_position` varchar(15) DEFAULT NULL,
  `s_salary` decimal(8,2) DEFAULT NULL,
  `s_sex` int(1) DEFAULT NULL,
  PRIMARY KEY (`s_phone`),
  UNIQUE KEY `s_phone_UNIQUE` (`s_phone`),
  UNIQUE KEY `s_id_UNIQUE` (`s_id`),
  KEY `s_com_id_idx` (`s_com_id`),
  KEY `s_depart_id_idx` (`s_depart_id`),
  KEY `s_name` (`s_name`),
  CONSTRAINT `s_dep_id` FOREIGN KEY (`s_depart_id`) REFERENCES `department` (`dep_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `s_com_id` FOREIGN KEY (`s_com_id`) REFERENCES `company` (`c_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES ('18709906729', '123456', 'ghjf', '1', '12@q.com', null, null, null, null, '0.00', '1');

-- ----------------------------
-- Table structure for staff_Management
-- ----------------------------
DROP TABLE IF EXISTS `staff_Management`;
CREATE TABLE `staff_Management` (
  `sm_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sm_s_phone` char(11) NOT NULL,
  `sm_c_id` varchar(20) NOT NULL,
  `sm_type` int(1) NOT NULL,
  `sm_state` int(1) NOT NULL,
  `sm_apply_datetime` datetime NOT NULL,
  `sm_treat_datetime` datetime DEFAULT NULL,
  `sm_treat_hr_id` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`sm_id`),
  KEY `sm_c_id_idx` (`sm_c_id`),
  KEY `sm_s_phone` (`sm_s_phone`) USING BTREE,
  CONSTRAINT `sm_c_id` FOREIGN KEY (`sm_c_id`) REFERENCES `company` (`c_id`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `sm_s_phone` FOREIGN KEY (`sm_s_phone`) REFERENCES `staff` (`s_phone`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of staff_Management
-- ----------------------------
DROP TRIGGER IF EXISTS `check_company_insert`;
DELIMITER ;;
CREATE TRIGGER `check_company_insert` BEFORE INSERT ON `company` FOR EACH ROW BEGIN
  IF NEW.c_hr_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.c_id NOT REGEXP  '[0-9]{13}$|[0-9]{13}-[0-9]{2}$'
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '企业注册号格式不正确.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_company_update`;
DELIMITER ;;
CREATE TRIGGER `check_company_update` BEFORE UPDATE ON `company` FOR EACH ROW BEGIN
  IF NEW.c_hr_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.c_id NOT REGEXP  '[0-9]{13}$|[0-9]{13}-[0-9]{2}$'
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '企业注册号格式不正确.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_dailyAttendance_insert`;
DELIMITER ;;
CREATE TRIGGER `check_dailyAttendance_insert` BEFORE INSERT ON `dailyAttendance` FOR EACH ROW BEGIN
  IF NEW.att_s_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.att_state NOT in (0,1,2,3,4)
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '打卡类型不正确.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_dailyAttendance_update`;
DELIMITER ;;
CREATE TRIGGER `check_dailyAttendance_update` BEFORE UPDATE ON `dailyAttendance` FOR EACH ROW BEGIN
  IF NEW.att_s_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.att_state NOT in (0,1,2,3,4)
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '打卡类型不正确.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_hr_insert`;
DELIMITER ;;
CREATE TRIGGER `check_hr_insert` BEFORE INSERT ON `hr` FOR EACH ROW BEGIN
  IF NEW.hr_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.hr_email NOT REGEXP  '^([a-z0-9A-Z]+[-|\.]?)+[a-z0-9A-Z]@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\.)+[a-zA-Z]{2,}$'
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'email is not correct.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_hr_update`;
DELIMITER ;;
CREATE TRIGGER `check_hr_update` BEFORE UPDATE ON `hr` FOR EACH ROW BEGIN
  IF NEW.hr_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.hr_email NOT REGEXP  '^([a-z0-9A-Z]+[-|\.]?)+[a-z0-9A-Z]@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\.)+[a-zA-Z]{2,}$'
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'email is not correct.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_message_insert`;
DELIMITER ;;
CREATE TRIGGER `check_message_insert` BEFORE INSERT ON `message` FOR EACH ROW BEGIN
  IF NEW.m_s_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.m_type NOT in (0,1,2)
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '申请类型不正确.';
  END IF;
    IF NEW.m_state NOT in (0,1,2)
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '处理类型不正确.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_message_update`;
DELIMITER ;;
CREATE TRIGGER `check_message_update` BEFORE UPDATE ON `message` FOR EACH ROW BEGIN
  IF NEW.m_s_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.m_type NOT in ('请假','外勤','申诉')
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '申请类型不正确.';
  END IF;
  IF NEW.m_state NOT in ('未处理','已同意','已拒绝')
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '处理类型不正确.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_staff_insert`;
DELIMITER ;;
CREATE TRIGGER `check_staff_insert` BEFORE INSERT ON `staff` FOR EACH ROW BEGIN
  IF NEW.s_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.s_email NOT REGEXP  '^([a-z0-9A-Z]+[-|.]?)+[a-z0-9A-Z]@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?.)+[a-zA-Z]{2,}$'
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'email is not correct.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_staff_update`;
DELIMITER ;;
CREATE TRIGGER `check_staff_update` BEFORE UPDATE ON `staff` FOR EACH ROW BEGIN
  IF NEW.s_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.s_email NOT REGEXP  '^([a-z0-9A-Z]+[-|.]?)+[a-z0-9A-Z]@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?.)+[a-zA-Z]{2,}$'
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'email is not correct.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_staff_Management_insert`;
DELIMITER ;;
CREATE TRIGGER `check_staff_Management_insert` BEFORE INSERT ON `staff_Management` FOR EACH ROW BEGIN
  IF NEW.sm_s_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.sm_c_id NOT REGEXP  '[0-9]{13}$|[0-9]{13}-[0-9]{2}$'
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '企业注册号格式不正确.';
  END IF;
  IF NEW.sm_type NOT in (0,1)
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '申请类型不正确.';
  END IF;
  IF NEW.sm_state NOT in (0,1,2)
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '处理类型不正确.';
  END IF;
END
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `check_staff_Management_update`;
DELIMITER ;;
CREATE TRIGGER `check_staff_Management_update` BEFORE UPDATE ON `staff_Management` FOR EACH ROW BEGIN
  IF NEW.sm_s_phone NOT REGEXP "[1][35678][0-9]{9}$"
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'phonenumber is not correct.';
  END IF;
  IF NEW.sm_c_id NOT REGEXP  '[0-9]{13}$|[0-9]{13}-[0-9]{2}$'
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '企业注册号格式不正确.';
  END IF;
  IF NEW.sm_type NOT in ('申请职位','移除职位','更换职位')
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '申请类型不正确.';
  END IF;
  IF NEW.sm_state NOT in ('未处理','已同意','已拒绝')
  THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = '处理类型不正确.';
  END IF;
END
;;
DELIMITER ;
