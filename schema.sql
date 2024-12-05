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

DROP TABLE IF EXISTS `harry_users`;
CREATE TABLE `users1` (
    `user_id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) DEFAULT NULL, 
    `password` varchar(50) DEFAULT NULL,
    PRIMARY KEY (`user_id`)
    ) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10001 ;
INSERT INTO `harry_users` (`username`, `password`) VALUES 
('Harry Potter', 'Expeliarmus'),
('Hermione Granger', 'Ravenclaw'),
('Ron Weasley', 'RedHead'),
('Voldemort', '4V4D4 K4D4VR4');

DROP TABLE IF EXISTS `harry_products`;
CREATE TABLE `users1` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `description` varchar(255) DEFAULT NULL, 
    `price` int(11) NOT NULL,
    `amount in stock` int(11) NOT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10001 ;
INSERT INTO `harry_products` (`name`, `description`, `price`, `amount in stock`) VALUES 
('Nimbus 2000', 'The fastest broom out there!', 100, 5),
('phoenix-feather Wand', 'You never choose a ward, the wand chooses you', 20, 1),
('Flying Car', 'The only existing one', 1000, 1),
('Witch hat', 'just a base one', 5, 60),
('Golden Snitch', 'A fast tiny golden winged playing ball', 20, 1),
('Owl', 'Great for delivering messages', 20, 30);

