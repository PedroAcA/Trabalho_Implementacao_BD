DELIMITER $$
CREATE PROCEDURE teste(IN nome VARCHAR(200))
BEGIN
	IF nome<>'x' THEN
		INSERT INTO crud_cargo VALUES (15,nome,15.5,'Fazer tal coisa');
	ELSE
		SELECT 'Nao conheco cargo x' as Msg;
	END IF;
END $$
DELIMITER ;
