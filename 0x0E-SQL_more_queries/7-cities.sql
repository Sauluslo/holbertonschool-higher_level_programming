-- 7. Cities table
-- A Script that creates the database hbtn_0d_usa and
-- the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- (1) cities description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY
-- that references to id of the states table
-- name VARCHAR(256) can’t be null
-- (2) If the database hbtn_0d_usa already exists, your script should not fail
-- (3) If the table cities already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY(state_id) REFERENCES states(id),
       name VARCHAR(256) NOT NULL
);
