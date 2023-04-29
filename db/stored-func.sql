DELIMITER $$
CREATE FUNCTION id_generator()
RETURNS int
NO SQL
BEGIN
  RETURN (1000000000 + floor(rand() * 1000000000));
END$$
DELIMITER;

INSERT INTO employee
VALUES (id_generator(), 'JEHN', '1991-08-04', 'F', 'PO', 100000000, 1005);

DELIMITER $$
CREATE FUNCTION dept_avg_salary(d_id int)
RETURNS int
READS SQL DATA
BEGIN
  DECLARE avg_sal int;
  SELECT avg(salary) into avg_sal
                    from employee
                    where dept_id = d_id;
  RETURN avg_sal;
END$$
DELIMITER ;

SELECT *, dept_avg_salary(id)
FROM department;

