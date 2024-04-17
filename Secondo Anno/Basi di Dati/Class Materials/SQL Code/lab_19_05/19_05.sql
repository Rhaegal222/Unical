#Creare la tabella:

create table noleggi_scaduti(
	codice mediumint, 
	rental_id int,
    giorni_oltre_scadenza smallint,
    FOREIGN KEY (rental_id) REFERENCES rental(rental_id)
);

#1.



#2.
select title
from film
where rental_duration <= 10;

#3.

select title
from film
where rental_duration > 0;

#4.

select title
from film
where rental_duration < (select avg(rental_duration) from film);

#5.

#6.