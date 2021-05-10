-- create databases
CREATE DATABASE IF NOT EXISTS adjustdb;
CREATE DATABASE IF NOT EXISTS test_adjustdb;

-- create user
CREATE USER 'adjust'@'%' IDENTIFIED WITH mysql_native_password BY 'adjust';

-- grant priviliges
GRANT ALL ON adjustdb.* TO 'adjust'@'%';
GRANT ALL ON test_adjustdb.* TO 'adjust'@'%';
FLUSH PRIVILEGES;
