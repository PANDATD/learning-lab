CREATE TABLE employee(
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE,
    address TEXT,
    monthly_salary REAL CHECK (monthly_salary >= 15000),
    joining_date TEXT NOT NULL,
    employment_type TEXT DEFAULT 'FULL TIME'
);
