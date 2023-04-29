delimiter $$
CREATE PROCEDURE product(IN a int, IN b int, OUT result int)
BEGIN
  SET result = a * b;
END
$$
delimiter ;

call product(5, 8, @result)
select @result;

delimiter $$
CREATE PROCEDURE swap(INOUT a int, INOUT b int)
BEGIN
  SET @temp = a;
  SET a = b;
  SET b = @temp;
END
$$
delimiter ;

set @a = 5, @b = 7;
call swap(@a, @b);
select @a, @b;

delimiter $$
CREATE PROCEDURE get_dept_avg_salary()
BEGIN
  SELECT dept_id, avg(salary)
  FROM employee
  GROUP BY dept_id;
END
$$
delimiter ;

call get_dept_avg_salary();


delimiter $$
CREATE PROCEDURE get_dept_avg_salary()
BEGIN
  SELECT dept_id, avg(salary)
  FROM employee
  GROUP BY dept_id;
END
$$
delimiter ;