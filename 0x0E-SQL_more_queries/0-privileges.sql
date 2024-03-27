-- Write a script that lists all MySQL user_0d_1 and user_0d_2 user privileges on localhost.
-- CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'Str0ngP@ssw0rd!';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
