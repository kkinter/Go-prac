DELIMITER $$
CREATE TRIGGER log_user_nickname_trigger
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
  insert into users_log values(OLD.id, OLD.nickname, now());
END
$$
DELIMITER ;