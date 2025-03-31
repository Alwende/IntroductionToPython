-- answers.sql

-- Question 1: Achieving 1NF (First Normal Form)
-- Create a new table in 1NF called OrderProducts
CREATE TABLE IF NOT EXISTS OrderProducts (
    OrderID INT,
    CustomerName VARCHAR(100),
    Product VARCHAR(100),
    PRIMARY KEY (OrderID, Product)
);

-- Insert data into the OrderProducts table, splitting the Products column
INSERT INTO OrderProducts (OrderID, CustomerName, Product)
SELECT OrderID, CustomerName, SUBSTRING_INDEX(Products, ',', 1)
FROM ProductDetail
UNION ALL
SELECT OrderID, CustomerName, SUBSTRING_INDEX(SUBSTRING_INDEX(Products, ',', 2), ',', -1)
FROM ProductDetail
WHERE FIND_IN_SET(',', Products) > 0
UNION ALL
SELECT OrderID, CustomerName, SUBSTRING_INDEX(SUBSTRING_INDEX(Products, ',', 3), ',', -1)
FROM ProductDetail
WHERE LENGTH(Products) - LENGTH(REPLACE(Products, ',', '')) >= 2
AND Products LIKE '%,%,%';

-- Note: This approach using SUBSTRING_INDEX and UNION ALL works for a limited number of products.
-- A more robust solution in a real-world scenario might involve a procedural approach
-- or using application-level logic to split the comma-separated values.

-- answers.sql

-- Question 2: Achieving 2NF (Second Normal Form)
-- Create two new tables: Orders and OrderItems
CREATE TABLE IF NOT EXISTS Orders2NF (
    OrderID INT PRIMARY KEY,
    CustomerName VARCHAR(100)
);

-- Insert data into the Orders table
INSERT INTO Orders2NF (OrderID, CustomerName)
SELECT DISTINCT OrderID, CustomerName
FROM OrderDetails;

-- Create the OrderItems table
CREATE TABLE IF NOT EXISTS OrderItems2NF (
    OrderID INT,
    Product VARCHAR(100),
    Quantity INT,
    PRIMARY KEY (OrderID, Product),
    FOREIGN KEY (OrderID) REFERENCES Orders2NF(OrderID)
);

-- Insert data into the OrderItems table
INSERT INTO OrderItems2NF (OrderID, Product, Quantity)
SELECT OrderID, Product, Quantity
FROM OrderDetails;

-- Note: The original OrderDetails table is now decomposed into two tables:
-- Orders2NF, where CustomerName depends only on OrderID (the primary key).
-- OrderItems2NF, where Product and Quantity depend on the composite primary key (OrderID, Product).
-- The foreign key relationship ensures data integrity between the two tables.