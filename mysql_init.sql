CREATE DATABASE IF NOT EXISTS stepic;
USE stepic;
GRANT ALL PRIVILEGES ON stepic to box@localhost IDENTIFIED BY 'box';
GRANT ALL PRIVILEGES ON stepic.* to box@localhost;
flush privileges;