Tabelle:

Categorie
ID_Categoria
Tipo (hardware, software)
Nome
Note

Attributi

Valore

Prodotto
SKU (PK)
Nome
ID_Categoria
ID_Proprietà (FK a Proprietà.ID_Proprietà)
Nel_Magazzino (Booleano, default TRUE)
Funzionante (Booleano)

Proprietà
ID_Proprietà(PK)
Data
ID_Luogo (FK a Luoghi.ID_Luogo)
ID_Responsabile (FK a Utenti.ID_Utente, nullable)
Note

Luoghi
ID_Luogo (PK)
Edificio
Piano
Stanza
Note

Utenti
ID_Utente (PK)
Nome
Cognome
Note

Relazioni:
Oggetti <-> Postazioni (relazione uno a uno o uno a molti)
Postazioni <-> Luoghi (relazione uno a uno o uno a molti)
Postazioni <-> Utenti (opzionale, relazione uno a uno o uno a molti)