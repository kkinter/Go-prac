CREATE DATABASE company;

USE company;

SELECT
  DATABASE();

CREATE TABLE DEPARTMENT (
  id INT PRIMARY KEY,
  name VARCHAR(20) NOT NULL UNIQUE,
  leader_id INT
);

CREATE TABLE EMPLOYEE(
  id INT PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  birth_date DATE,
  sex CHAR(1) CHECK(sex IN ('M', 'F')),
  position VARCHAR(10),
  salary INT DEFAULT 50000000,
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES DEPARTMENT(id)
    on delete SET NULL on update CASCADE,
  CHECK (salary >= 50000000)
);

CREATE table PROJECT(
  id INT PRIMARY KEY,
  name VARCHAR(20) NOT NULL UNIQUE,
  leader_id INT,
  start_date DATE,
  end_date DATE,
  FOREIGN KEY (leader_id) REFERENCES EMPLOYEE(id)
    on delete SET NULL on update CASCADE,
  CHECK (start_date < end_date)
);

CREATE table WORKS_ON(
  empl_id INT,
  proj_id INT,
  PRIMARY KEY (empl_id, proj_id),
  Foreign Key (empl_id) REFERENCES EMPLOYEE(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  Foreign Key (proj_id) REFERENCES PROJECT(id)
    ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE department ADD FOREIGN KEY (leader_id)
REFERENCES employee(id)
on update CASCADE
on delete SET NULL;