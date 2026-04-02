DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';

CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS user_2_db;

CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
