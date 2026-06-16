CREATE DATABASE seafood_db;

USE seafood_db;

CREATE TABLE orders(
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(50),
    customer_phone VARCHAR(20),
    product VARCHAR(100),
    quantity INT,
    status VARCHAR(50)
);

CREATE TABLE drivers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    driver_name VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE sms_logs(
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone VARCHAR(20),
    message TEXT
);