DROP TABLE INSEGNA;
DROP TABLE ASSEGNAMENTO;
DROP TABLE STORICOISCRIZIONE;
DROP TABLE ALUNNO;
DROP TABLE SCUOLA;
DROP TABLE INSEGNANTE;
DROP TABLE CLASSE;
DROP TABLE PLESSO;
DROP TABLE FASCIAETÀ;
DROP TABLE AULA;

CREATE TABLE ALUNNO ( 
    CF char(16) not null, 
    nome varchar(30), 
    cognome varchar(30), 
    data_nascita date,
    sostegno boolean,
    primary key (CF)
    );

CREATE TABLE INSEGNANTE (
    CF char(16) not null, 
    nome varchar(30), 
    cognome varchar(30), 
    data_nascita date, 
    di_ruolo boolean, 
    materia varchar(30),
    primary key (CF)
    );

CREATE TABLE SCUOLA ( 
    id_scuola varchar(16) not null, 
    nome varchar(30), 
    telefono varchar(30), 
    tipo char(2), 
    tempoPieno boolean,
    primary key (id_scuola)
    );

CREATE TABLE CLASSE (
    id_classe varchar(16) not null,
    numero int, 
    lettera char, 
    scuola varchar(16),
    primary key (id_classe),
    foreign key (scuola) references SCUOLA(id_scuola)
    );

CREATE TABLE PLESSO (
    id_plesso varchar(16) not null, 
    indirizzo varchar(40), 
    n_piani int, 
    ascensore int,
    primary key (id_plesso)
    );

CREATE TABLE FASCIAETÀ (
    nome varchar(30) not null, 
    min int, 
    max int,
    primary key (nome)
    );

CREATE TABLE AULA ( 
    id_aula varchar(16) not null, 
    mq int, 
    max_stud int, 
    fasciaEtà varchar(30), 
    plesso varchar(16),
    piano int,
    primary key (id_aula),
    foreign key (plesso) references PLESSO(id_plesso),
    foreign key (fasciaEtà) references FASCIAETÀ(nome)
    );

CREATE TABLE INSEGNA(
    id_ins varchar(16), 
    id_classe varchar(16), 
    a_s year, 
    ore int,
    primary key (id_ins, id_classe, a_s),
    foreign key (id_ins) references INSEGNANTE(CF),
    foreign key (id_classe) references CLASSE(id_classe)
    );

CREATE TABLE ASSEGNAMENTO (
    id_classe varchar(16),
    id_aula varchar(16),
    a_s varchar(9),
    numerosa boolean,
    primary key (id_classe, id_aula, a_s),
    foreign key (id_classe) references CLASSE(id_classe),
    foreign key (id_aula) references AULA(id_aula)
    );

CREATE TABLE STORICOISCRIZIONE ( 
    id_alunno varchar(16), 
    id_classe varchar(16), 
    a_s varchar(9),
    primary key (id_alunno, id_classe, a_s),
    foreign key (id_classe) references CLASSE(id_classe),
    foreign key (id_alunno) references ALUNNO(CF)
    );


SELECT regione_sociale, denominazione
FROM azienda
WHERE p_iva IN( 
    SELECT P1.p_iva, P1.prodotto /*seleziona tutti i prodotti che vengono venduti*/
    FROM produce AS P1
    EXCEPT( /*Aziende che vengono solo alcuni prodotti*/
        SELECT p_iva, prodotto /*seleziona tutte le aziende associate a tutti i prodotti venduti*/
        FROM azienda, prodotto
        EXCEPT(
            SELECT P2.p_iva, P2.prodotto /*seleziona tutti i prodotti che vengono venduti*/
            FROM produce AS P2
            )
        )
    )

/*Città con il maggior numero di aziende*/
SELECT Città FROM(
    SELECT Città, MAX(C) FROM(
        SELECT Città, COUNT(Città) AS C
        FROM Azienda
        GROUP BY Città
    )
)

/*Numero di aziende per ciascuna città*/
SELECT Città, COUNT(*)
FROM Azienda
GROUP BY Città

/*Denominazione delle aziende i cui prodotti costano tutti meno di 100 euro*/
SELECT Denominazione
FROM Azienda AS A
WHERE NOT EXISTS(
    SELECT *
    FROM Produce AS P
    WHERE A.p_iva = P.p_iva AND prezzo >= 100
)

SELECT Denominazione
FROM Azienda
WHERE p_iva NOT IN(
    SELECT p_iva
    FROM Produce
    WHERE PREZZO >= 100
)
