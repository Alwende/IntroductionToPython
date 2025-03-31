-- answers.sql

-- Question 1: Creating the 'student' table
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

-- Question 2: Inserting records into the 'student' table
INSERT INTO student (id, fullName, age) VALUES
    (1, 'Alice Akinyi', 20),
    (2, 'Bobson Daniel', 22),
    (3, 'Charles Mark', 19),
    (4, 'Diana Lelei', 21);

    -- Question 3: Updating age in the 'student' table
UPDATE student
SET age = 20
WHERE id = 2;