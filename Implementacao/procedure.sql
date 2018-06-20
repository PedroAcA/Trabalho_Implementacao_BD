DELIMITER $$
CREATE PROCEDURE teste(IN nome VARCHAR(200))
BEGIN
	IF nome<>'x' THEN
		INSERT INTO crud_cargo VALUES (15,nome,15.5,'Executei o if da procedure!');
	ELSE
		INSERT INTO crud_cargo VALUES (16,'x',0.3,'Executei o else da procedure!');
	END IF;
END $$
DELIMITER ;
