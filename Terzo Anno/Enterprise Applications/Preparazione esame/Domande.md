### Java e Hibernate/JPA\

1. Come mappare l’eredità usando l’url? Quali sono le diverse strategie? vantaggi e svantaggi
2. Quali sono le annotazioni corrispondenti in Hiberate/jpa? I modi per mappare
3. Problemi del mismatch tra paradigma relazione e a oggetti (problema dell’identità (equals), ereditarietà, associazioni)
4. Cosa si usa per non rendere una colonna persistente sul db? Transient
5. Qual è il comportamento predefinito di JPA per la proprietà hibernate.hbm2ddl.auto? È create o update?
6. Quali sono le proprietà del file di configurazione di Hibernate che permettono di gestire la creazione e l'aggiornamento dello schema del database?
7. Qual è la differenza tra Entity, POJO, DTO e DAO?
8. Come funziona l'ereditarietà nelle entità JPA? Spiega le differenze tra Single Table Inheritance e Class Table Inheritance, e descrivi il ruolo della parte in comune.
9. Cos'è la strategia di "Joined Table" in JPA e come funziona?

### Spring

1. Qual è la differenza tra le varie interfacce di repository in Spring (CrudRepository, PagingAndSortingRepository, JpaRepository)?
2. Qual è la differenza tra Filter e Interceptor in Spring?
3. Come si gestiscono le eccezioni in Spring e quali strumenti offre Spring per questa gestione?
4. Qual è la differenza tra Authentication e Authorization?
5. Cos'è Swagger e quali funzionalità offre?
6. Come si utilizza Model Mapper per collegare entità e DTO/DAO?
7. Cosa si intende per audit logging nelle REST API?
8. Quali sono i vantaggi e gli svantaggi dei metodi di query rispetto alle query personalizzate con @Query?
9. Come si gestiscono le transazioni nei microservizi utilizzando il pattern Saga?
10. Quali sono gli stili di interazione dei microservizi con i processi?
11. Cos'è il pattern Circuit Breaker, quali problemi risolve e come si implementa con Resilience4j?
12. Quali sono i tre stati del pattern Circuit Breaker?
13. Come funziona il two-phase commit (2PC) nei microservizi e perché può essere preferito rispetto ai Saga? Serve un coordinatore?
14. Qual è la differenza tra un Dockerfile (per definire una nuova immagine) e Docker Compose?
15. Qual è la differenza tra un'immagine e un container in Docker?
16. Perché è necessario avere un servizio di discovery nei microservizi?
17. Qual è la differenza tra OAuth2 e OpenID Connect?
18. Cos'è Keycloak?
19. Cos'è il Role-based Access Control (RBAC)?
20. Che tipo di volumi possono essere montati in Docker? È possibile creare un’immagine partendo da una già esistente?
21. Quali sono i vantaggi e gli svantaggi di REST nell'ambito dei microservizi e quali problemi possono sorgere nel fetch dei dati?
22. Cos'è il problema di granularità nei sistemi distribuiti?
23. Cos'è il Phantom Token Pattern?
24. Cos'è il Mutual TLS e come funziona?

### REST API e Sicurezza

1. Le caratteristiche REST? stateless, struttura standard, nomi ecc.
2. Cosa è rate limiting?
3. Cosa è Oauth2? Perché è stato introdotto? Cosa risolve?
4. Cosa sono i Token?
5. Cosa sono i JWT? Come fanno ad essere self-contained? Ovvero come garantiscono la sicurezza?
6. Come si gestisce il logout nel caso dei JWT?
7. Flusso del token OAuth2, Client Credential Grant?
8. Differenza tra authentication e authorization?
9. Cos'è il Cross-site Scripting?
10. Differenza tra crittografia simmetrica e asimmetrica?
11. Cosa sono i Macaroons?

### Microservizi e Architettura

1. Microservizi in Spring? Vantaggi e svantaggi?
2. Come comunicano i microservizi tra di loro (sincrona e asincrona)?
3. Vantaggi e svantaggi dei microservizi e lato database?
4. Problemi sul database per unire i dati da più microservizi? Data mart ecc.
5. Vantaggi e svantaggi dei microservizi? E lato database? Nel caso in cui volessimo lavorare in ambito dati per raggrupparli assieme?
6. Cos'è il pattern API Gateway?
7. Quanti modi per scalare un'applicazione (verticale, orizzontale ecc.)?
8. Ruolo del message broker nei microservizi? I message broker più popolari

### Android e Kotlin

1. Come implementare i metodi del lazy load? Quali sono le 3 tecniche?
2. Componenti grafici di Jetpack Compose
3. Layout di base
4. LazyColumn e LazyRow
5. LazyVerticalGrid e LazyHorizontalGrid

### Altri Argomenti

1. Cosa sono le Capabilities? E come si possono implementare?
2. Organizzazione logica di business?
3. Come gestire la concorrenza?
4. Come viene implementato l’optimistic lock?
5. Quali sono le proprietà AGID?
6. Altri modi di interrogazione in Spring Data
7. Problemi di granularità?
8. Cos'è l'Attacco ReDDos?
