# modello relazionale

>**insegnante** (<ins>cf</ins>, nome, cognome, data_di_nascita, materia, di_ruolo)

>**classe** (<ins>lettera, numero, id_scuola*</ins>, numerosa)

>**insegna** (<ins>cf_insegnante*, id_scuola*, numero, lettera, anno_scolastico</ins>, ore)

>**alunno** (<ins>cf</ins>, nome, cognome, data_di_nascita, sostegno)

>**storico_iscrizioni** (<ins>cf_alunno*, anno_scolatico, lettera, numero</ins>, data_iscrizione)

>**aula** (<ins>id_plesso</ins>, superfice, indirizzo*, max_stud, min*, max*)

>**assegnamento** (<ins>id_aula*, lettera*, numero*, anno_scolastico*</ins>)

>**scuola** (<ins>id_scuola</ins>, nome, telefono, tipo, tempo_pieno)
>>vincolo integrtià referenziale tra tempo pieno
