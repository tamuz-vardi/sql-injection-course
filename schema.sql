CREATE DATABASE IF NOT EXISTS sqli_training;
USE sqli_training;
DROP TABLE IF EXISTS `users1`;
CREATE TABLE `users1` (
    `user_id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) DEFAULT NULL, 
    `password` varchar(50) DEFAULT NULL,
    `is_admin` int(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (`user_id`)
    ) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10001 ;
INSERT INTO `users1` (`username`, `password`, `is_admin`) VALUES 
('rogers63', 'RogerTheBest', 0),
('admin', 'TopSecretClassified', 1);