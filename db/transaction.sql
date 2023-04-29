START TRANSACTION;
UPDATE account SET balance = balance - 200000 WHERE id = 'J';
UPDATE account SET balance = balance + 200000 WHERE id = 'H';
COMMIT;

START TRANSACTION;
UPDATE account SET balance = balance - 300000 WHERE id = 'J';

ROLLBACK;

SELECT @@AUTOCOMMIT;