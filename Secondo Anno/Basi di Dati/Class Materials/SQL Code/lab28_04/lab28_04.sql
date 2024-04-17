
-- 1

CREATE TABLE rental_recap (
	cd_film_id  INT PRIMARY KEY, 
	available   BOOLEAN,
	FOREIGN KEY (cd_film_id) REFERENCES CDFilm(cd_film_id)
);


DELIMETER //
-- 2
-- fate voi, quando volete, senza fretta. oh mi raccomando eh, con calma
CREATE TRIGGER new_line2 AFTER INSERT ON CDFilm --FOR EACH ROW
BEGIN

END
//

-- 3
DROP TRIGGER IF EXISTS NOME3;
//
CREATE TRIGGER NOME3 AFTER INSERT ON CDFilm --FOR EACH ROW
BEGIN
	INSERT INTO rental_recap VALUE(NEW.cd_film_id, TRUE)
END;
//

-- 4
CREATE TRIGGER NOME4 AFTER UPDATE ON Rental
BEGIN
    IF OLD.return_date == NULL AND NEW.return_date == NOW() THEN
        UPDATE rental_recap SET 
    END IF;
END;
//

OLD.COLONNA 
NEW.COLONNA


-- 5
//
CREATE TRIGGER NOME5 BEFORE INSERT ON Rental -- FOR EACH ROW
BEGIN
-- soluzione con rental_recap
IF
	SELECT available
	FROM rental_recap
	WHERE rental_recap.cd_film_id = NEW.cd_film_id

END;
//


-- 6
DROP TRIGGER IF EXISTS NOME6;
//
CREATE TRIGGER NOME6 BEFORE INSERT ON Payment --FOR EACH ROW
BEGIN
    IF NEW.rental_id != NULL THEN
END;
//

--7
DROP TRIGGER IF EXISTS NOME7
//
CREATE TRIGGER NOME7 BEFORE INSERT ON Customer 
BEGIN

	IF

END;
//

-- 8


-- 9


-- FINITO
DELIMETER ;
