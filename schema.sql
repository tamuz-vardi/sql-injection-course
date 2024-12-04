CREATE DATABASE IF NOT EXISTS sqli_training;
USE sqli_training;
CREATE TABLE IF NOT EXISTS `users1` (
    `user_id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) DEFAULT NULL, 
    `password` varchar(50) DEFAULT NULL,
    PRIMARY KEY (`user_id`)
    ) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10001 ;
INSERT INTO `users1` (`user_id`, `username`, `password`) VALUES 
(1, 'rogers63', 'TopSecretClassified');