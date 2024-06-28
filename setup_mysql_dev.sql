-- A script that prepares a MySQL server for the project

-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- Allow all privileges on the project database to the new user
GRANT ALL PRIVILEGES
ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';

-- Allow SELECT privilege on the database performance_schema to the new user
GRANT SELECT
ON performance_schema.*
TO 'hbnb_dev'@'localhost';
