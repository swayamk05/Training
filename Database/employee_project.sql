
CREATE TABLE projects (
    project_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    employee_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    age INTEGER,
    salary NUMERIC(10,2),
    project_id INTEGER,
    FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
);

INSERT INTO projects (project_name)
VALUES
('AI Chatbot'),
('E-Commerce Website'),
('Travel Planner'),
('Banking Application');

INSERT INTO employees
(employee_name, email, age, salary, project_id)
VALUES
('Rahul', 'rahul@gmail.com', 24, 50000, 1),
('Amit', 'amit@gmail.com', 27, 60000, 1),
('Priya', 'priya@gmail.com', 25, 55000, 2),
('Sneha', 'sneha@gmail.com', 29, 70000, 3);

SELECT * FROM projects;
SELECT * FROM employees;