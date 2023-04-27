SELECT birth_date FROM employee WHERE id = 14;

SELECT id, name, birth_date FROM employee
WHERE birth_date < '1992-08-04';


SELECT id, name, birth_date FROM employee
WHERE birth_date < (
  SELECT birth_date FROM employee WHERE id = 14
  );

SELECT id, name, position
FROM employee
WHERE (dept_id, sex) = (
  SELECT dept_id, sex
  FROM employee
  WHERE id = 1
)

SELECT proj_id FROM works_on WHERE empl_id = 5;

SELECT DISTINCT empl_id FROM works_on
WHERE empl_id != 5 AND (proj_id = 2001 OR proj_id = 2002);

SELECT DISTINCT empl_id FROM works_on
WHERE empl_id != 5 AND proj_id IN (
  SELECT proj_id 
  FROM works_on 
  WHERE empl_id = 5
);




SELECT DISTINCT empl_id FROM works_on
WHERE empl_id != 5 AND proj_id IN (
  SELECT proj_id 
  FROM works_on 
  WHERE empl_id = 5
);

SELECT id, name
FROM employee
WHERE id IN (
  SELECT DISTINCT empl_id 
  FROM works_on
  WHERE empl_id != 5 AND proj_id IN (
    SELECT proj_id 
    FROM works_on 
    WHERE empl_id = 5
  )
);

SELECT id, name
FROM employee
  (
    SELECT DISTINCT empl_id
    FROM works_on
    WHERE empl_id != 5 AND proj_id IN(
      SELECT proj_id
      FROM works_on
      WHERE empl_id = 5
    )
  ) AS DSTNCT_E
WHERE id = DSTNCT_E.empl_id;

SELECT P.id, P.name
FROM project P
WHERE EXISTS (
          SELECT *
          FROM works_on W
          WHERE W.proj_id = P.id AND W.empl_id IN (7, 12)
      );

SELECT D.id, D.name
FROM department AS D
WHERE NOT EXISTS (
          SELECT *
          FROM employee E
          WHERE E.dept_id = D.id AND E.birth_date >= '2000-01-01'
      );