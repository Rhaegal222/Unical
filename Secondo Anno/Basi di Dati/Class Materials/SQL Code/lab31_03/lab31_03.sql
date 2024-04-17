CREATE TABLE Ricercatore(
    cf char(16) NOT NULL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    dip INT UNSIGNED NOT NULL,
    ruolo INT UNSIGNED NOT NULl,
    FOREIGN KEY (dip) REFERENCES Dipartimento(codice),
    FOREIGN KEY (ruolo) REFERENCES Ruolo(codice)
);

CREATE TABLE Progetto(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(250) NOT NULL,
    responsabile CHAR(16) NOT NULL,
    FOREIGN KEY (responsabile) REFERENCES Ricercatore(cf)
);

CREATE TABLE Partecipante(
    progetto INT NOT NULL,
    ricercatore CHAR(16) NOT NULL,
	PRIMARY KEY(progetto, ricercatore),
    FOREIGN KEY (progetto) REFERENCES Progetto(id),
	FOREIGN KEY (ricercatore) REFERENCES Ricercatore(cf)
);

ALTER TABLE dipartimento 
MODIFY nome VARCHAR(250) NOT NULL UNIQUE;

ALTER TABLE Ruolo
MODIFY nome VARCHAR(100) NOT NULL UNIQUE;

ALTER TABLE Ruolo
ADD UNIQUE KEY unica(codice, nome);
