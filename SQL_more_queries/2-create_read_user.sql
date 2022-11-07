-- Creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF EXISTS 'hbtn_0d_2'@'user_0d_2'IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ALL PRIVILEGES ON 'hbtn_0d_2'. * TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
