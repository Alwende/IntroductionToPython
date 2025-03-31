-- answers.sql

-- Question 1: Drop an index named IdxPhone from customers table.
DROP INDEX IdxPhone ON customers;

-- Question 2: Create a user named bob with the password 'S$cu3r3!', restricted to the localhost hostname.
CREATE USER 'bob'@'localhost' IDENTIFIED BY 'S$cu3r3!';

-- Question 3: Grant the INSERT privilege to the user bob on the salesDB database.
GRANT INSERT ON salesDB.* TO 'bob'@'localhost';

-- Question 4: Change the password for the user bob to 'P$55!23'
ALTER USER 'bob'@'localhost' IDENTIFIED BY 'P$55!23';