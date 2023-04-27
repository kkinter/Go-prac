SELECT name, position FROM employee WHERE id = 9;

SELECT employee.id, employee.name, position
FROM project, employee
WHERE project.id = 2002 and project.leader_id = employee.id;

SELECT E.id AS leader_id, E.name AS leader_name, position
FROM project AS P, employee AS E
WHERE P.id = 2002 and P.leader_id = E.id;

SELECT P.id, P.name
FROM employee AS E, works_on AS W, project AS P
WHERE E.position = 'DSGN' AND
    E.id = W.empl_id and W.proj_id = P.id;

SELECT name
FROM employee
WHERE name LIKE 'N%' or name LIKE '%N';

SELECT name
FROM employee
WHERE name LIKE '%NG%';

SELECT name FROM employee WHERE name LIKE 'J___';

SELECT name FROM project WHERE name LIKE '\%%' or name LIKE '%\_';

SELECT * FROM employee WHERE id = 9;

