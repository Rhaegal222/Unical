## JPA e Hibernate

1. Come mappare l’ereditarietà nelle entità JPA? Quali sono le diverse strategie disponibili e quali sono i vantaggi e gli svantaggi di ciascuna?
2. Quali sono le annotazioni corrispondenti in Hibernate/JPA per mappare l’ereditarietà? Quali sono i diversi modi per mappare?
3. Quali sono i problemi del mismatch tra paradigma relazionale e a oggetti, in particolare per quanto riguarda l'identità (equals), l'ereditarietà e le associazioni?
4. Quale annotazione si usa per non rendere una colonna persistente nel database? Come si usa l'annotazione `@Transient`?
5. Qual è il comportamento predefinito di JPA? Come si può modificare il comportamento predefinito?
6. Quali sono le proprietà del file di configurazione di Hibernate che permettono di gestire la creazione e l'aggiornamento dello schema del database?
7. Qual è la differenza tra Entity, POJO, DTO e DAO?
8. Come funziona l'ereditarietà nelle entità JPA? Spiega le differenze tra Single Table Inheritance e Class Table Inheritance, e descrivi il ruolo della parte in comune.
9. Cos'è la strategia di "Joined Table" in JPA e come funziona?

## Spring Framework

1. Qual è la differenza tra le varie interfacce di repository in Spring (CrudRepository, PagingAndSortingRepository, JpaRepository)?
2. Qual è la differenza tra Filter e Interceptor in Spring?
3. Come si gestiscono le eccezioni in Spring e quali strumenti offre Spring per questa gestione?
4. Come si utilizza Model Mapper per collegare entità e DTO/DAO?
5. Cos'è Swagger e quali funzionalità offre?
6. Cosa si intende per audit logging nelle REST API?
7. Quali sono i vantaggi e gli svantaggi dei metodi di query rispetto alle query personalizzate con @Query?

## Microservizi

1. Come si gestiscono le transazioni nei microservizi utilizzando il pattern Saga?
2. Quali sono gli stili di interazione dei microservizi con i processi?
3. Cos'è il pattern Circuit Breaker, quali problemi risolve e come si implementa con Resilience4j?
4. Quali sono i tre stati del pattern Circuit Breaker?
5. Come funziona il two-phase commit (2PC) nei microservizi e perché può essere preferito rispetto ai Saga? Serve un coordinatore?
6. Perché è necessario avere un servizio discovery nei microservizi e come funziona?
7. Qual è la differenza tra un'architettura monolitica e un'architettura a microservizi?
8. Quali sono i vantaggi e gli svantaggi di REST nell'ambito dei microservizi e quali problemi possono sorgere nel fetch dei dati?
9. Cos'è il problema di granularità nei sistemi distribuiti?
10. Cos'è il Phantom Token Pattern?
11. Quali sono i vantaggi e gli svantaggi dell'uso dei microservizi in Spring?
12. Come comunicano i microservizi tra di loro? Descrivi le differenze tra comunicazione sincrona e asincrona.
13. Quali sono i vantaggi e gli svantaggi dei microservizi, soprattutto per quanto riguarda la gestione del database?
14. Quali problemi possono sorgere nell'unire i dati provenienti da più microservizi in un database? Come possono essere utilizzati strumenti come i data mart?
15. Quali sono i vantaggi e gli svantaggi dei microservizi in generale e nella gestione dei database? Come affrontare le sfide di raggruppare dati da vari microservizi?
16. Cos'è il pattern API Gateway e quale ruolo svolge nei microservizi?
17. Quali sono i diversi modi per scalare un'applicazione? Spiega la scalabilità verticale e orizzontale.
18. Qual è il ruolo di un message broker nei microservizi? Quali sono i message broker più popolari e utilizzati?

## Docker

1. Qual è la differenza tra un Dockerfile (per definire una nuova immagine) e Docker Compose?
2. Qual è la differenza tra un'immagine Docker e un container Docker?
3. Che tipo di volumi possono essere montati in Docker? È possibile creare un’immagine partendo da una già esistente?

## REST API e Sicurezza

1. Quali sono le caratteristiche principali delle API REST? Spiega il concetto di statelessness, la struttura standard degli URL, la convenzione dei nomi e altri principi fondamentali.
2. Cos'è il rate limiting e come viene utilizzato per controllare l'accesso alle API?
3. Cos'è OAuth2? Perché è stato introdotto e quali problemi risolve?
4. Cosa sono i token e come vengono utilizzati nelle operazioni di autenticazione e autorizzazione?
5. Cosa sono i JWT (JSON Web Tokens)? Come fanno ad essere self-contained e come garantiscono la sicurezza?
6. Come si gestisce il logout quando si utilizzano i JWT per l'autenticazione?
7. Spiega il flusso del Client Credential Grant in OAuth2.
8. Qual è la differenza tra autenticazione e autorizzazione?
9. Cos'è il Cross-site Scripting (XSS) e come può essere prevenuto?
10. Qual è la differenza tra crittografia simmetrica e asimmetrica?
11. Cosa sono i Macaroons e come vengono utilizzati per l'autenticazione?
12. Qual è la differenza tra OAuth2 e OpenID Connect?
13. Cos'è Keycloak?
14. Cos'è il Role-based Access Control (RBAC)?
15. Cos'è il Mutual TLS e come funziona?

## Android e Kotlin

1. Come si implementano i metodi del lazy loading? Quali sono le tre tecniche principali utilizzate?
2. Quali sono i componenti grafici disponibili in Jetpack Compose?
3. Quali sono i layout di base in Jetpack Compose e come vengono utilizzati?
4. Cosa sono LazyColumn e LazyRow in Jetpack Compose e come funzionano?
5. Cosa sono LazyVerticalGrid e LazyHorizontalGrid in Jetpack Compose e come funzionano?

## Altri Argomenti

1. Cosa sono le Capabilities e come si possono implementare?
2. Come si organizza logicamente la business logic in un'applicazione enterprise?
3. Come si gestisce la concorrenza nelle applicazioni software?
4. Come viene implementato l'optimistic locking in un sistema di gestione dei dati?
5. Quali sono le proprietà ACID e come vengono utilizzate?
6. Quali sono gli altri modi di eseguire interrogazioni in Spring Data oltre ai metodi di repository standard?
7. Quali sono i problemi di granularità nei sistemi software e come possono essere risolti?
8. Cos'è un attacco ReDDos e come può essere mitigato?
