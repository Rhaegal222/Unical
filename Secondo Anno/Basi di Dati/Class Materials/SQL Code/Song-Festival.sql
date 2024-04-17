create database music;
use music;

create table canzone(
	titolo char(50) primary key,
    durata int not null,
    artista char(50) not null
    );
create table festival(
	nome char(50) primary key,
    num_edizione int not null
);
create table partecipazione(
	anno int not null,
    posizione int not null,
    canzone char(50),
    festival char(50),
    primary key(anno, festival, canzone),
    foreign key(canzone) references canzone(titolo),
    foreign key(festival) references festival(nome),
    unique(anno, posizione, festival)
);

insert into canzone(titolo, durata, artista) values ("Brividi", 199, "Mahmood e Blanco");
insert into canzone(titolo, durata, artista) values ("O forse sei tu", 233, "Elisa");
insert into canzone(titolo, durata, artista) values ("Apri tutte le porte", 223, "Gianni Morandi");
insert into canzone(titolo, durata, artista) values ("Ovunque sarai", 209, "Irama");
insert into canzone(titolo, durata, artista) values ("Farfalle", 164, "Sangiovanni");
insert into canzone(titolo, durata, artista) values ("Ogni volta è così", 207, "Emma");
insert into canzone(titolo, durata, artista) values ("Ciao ciao", 184, "La Rappresentante di Lista");
insert into canzone(titolo, durata, artista) values ("Lettera di là dal mare", 218, "Massimo Ranieri");
insert into canzone(titolo, durata, artista) values ("Dove si balla", 198, "Dargen D'Amico");
insert into canzone(titolo, durata, artista) values ("Inverno dei fiori", 176, "Michele Bravi");
insert into canzone(titolo, durata, artista) values ("Musica Leggerissima", 240, "Colapesce Dimartino");
insert into canzone(titolo, durata, artista) values ("Spacco tutto", 200, "Francesco Vecchio");

insert into festival(nome, num_edizioni) values ("Sanremo", 62);
insert into festival(nome, num_edizioni) values ("Eurovision", 66);
insert into festival(nome, num_edizioni) values ("X-Factor", 20);
insert into festival(nome, num_edizioni) values ("Amici", 30);

select * from partecipazione;

insert into partecipazione(anno, posizione, canzone, festival) values (2019, 1, "Spacco tutto", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2019, 1, "Spacco tutto", "Amici");
insert into partecipazione(anno, posizione, canzone, festival) values (2019, 4, "Spacco tutto", "Eurovision");
insert into partecipazione(anno, posizione, canzone, festival) values (2021, 1, "Musica Leggerissima", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2021, 4, "Musica Leggerissima", "Amici");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 1, "Brividi", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 2, "Brividi", "Eurovision");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 2, "O forse sei tu", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 1, "O forse sei tu", "X-Factor");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 5, "O forse sei tu", "Eurovision");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 3, "Apri tutte le porte", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 4, "Ovunque sarai", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 5, "Farfalle", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 6, "Ogni volta è così", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 7, "Ciao ciao", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 8, "Lettera di là dal mare", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 9, "Dove si balla", "Sanremo");
insert into partecipazione(anno, posizione, canzone, festival) values (2022, 10, "Inverno dei fiori", "Sanremo");

insert into partecipazione(anno, posizione, canzone, festival) values(2022, 1, "Brividi", "Sanremo");

SELECT nome, num_edizioni FROM festival
WHERE num_edizioni = (SELECT max(num_edizioni) FROM festival);

SELECT canzone FROM partecipazione
where canzone not in (select canzone from partecipazione where posizione > 3)
group by canzone;

select * from partecipazione;