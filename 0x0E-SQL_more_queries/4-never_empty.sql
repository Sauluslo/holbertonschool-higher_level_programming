-- 4. ID can't be null mandatory
-- A Script that creates the table id_not_null on your MySQL server.
-- (1) id_not_null description:
-- id INT with the default value 1
-- name VARCHAR(256)
-- (2) The database name will be passed as an argument of the mysql command
-- (3) If the table id_not_null already exists, your script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INTNOT NULL DEFAULT 1, name VARCHAR(256));
