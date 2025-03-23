-- Create the database
CREATE DATABASE IF NOT EXISTS hotel;
USE hotel;

-- Create the payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    check_number VARCHAR(50),
    payment_date DATE,
    amount DECIMAL(10, 2)
);

-- Insert sample data into payments table
INSERT INTO payments (customer_id, check_number, payment_date, amount) VALUES
(1, 'AB123', '2023-03-01', 150.00),
(2, 'CD456', '2023-03-02', 200.00),
(3, 'EF789', '2023-03-03', 250.00),
(1, 'GH012', '2023-03-04', 300.00),
(2, 'IJ345', '2023-03-05', 350.00);

-- Create the customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    country VARCHAR(50),
    credit_limit DECIMAL(10, 2)
);

-- Insert sample data into customers table
INSERT INTO customers (customer_name, country, credit_limit) VALUES
('Alika', 'Kenya', 8000.00),
('Benson', 'Somalia', 9000.00),
('Emanuel', 'Uganda', 10000.00),
('Davido', 'Malawi', 12000.00),
('Evaline', 'Tanzania', 6000.00);

-- Create the orderdetails table
CREATE TABLE IF NOT EXISTS orderdetails (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    product_code VARCHAR(50),
    quantity_ordered INT,
    price_each DECIMAL(10, 2)
);

-- Insert sample data into orderdetails table
INSERT INTO orderdetails (product_code, quantity_ordered, price_each) VALUES
('P001', 10, 15.00),
('P002', 20, 25.00),
('P003', 30, 35.00),
('P004', 40, 45.00),
('P005', 50, 55.00);