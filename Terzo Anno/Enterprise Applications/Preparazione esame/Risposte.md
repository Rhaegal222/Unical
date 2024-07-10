## **JPA e Hibernate**

### **1. Come mappare l’ereditarietà nelle entità JPA? Quali sono le diverse strategie disponibili e quali sono i vantaggi e gli svantaggi di ciascuna?**

Per mappare l’ereditarietà nelle entità JPA, si utilizzano diverse strategie, ognuna con i propri vantaggi e svantaggi. Le principali strategie disponibili sono:

- **Single Table (Strategia TABLE_PER_CLASS)**: tutte le classi dell'ereditarietà vengono mappate su una singola tabella. Questo approccio è semplice e non richiede join, il che migliora le prestazioni di lettura. Tuttavia, può causare spargimento di colonne non utilizzate se le classi figlie hanno molti campi specifici.

- **Joined Table (Strategia JOINED)**: ogni classe dell'ereditarietà ha la propria tabella e le tabelle sono collegate tramite chiavi esterne. Questo approccio normalizza i dati e minimizza la ridondanza, ma può comportare un overhead di prestazioni a causa dei join richiesti per recuperare i dati completi dell'entità.

- **Table per Concrete Class (Strategia TABLE_PER_CLASS)**: ogni classe concreta ha la propria tabella con tutte le sue proprietà, inclusi i campi ereditati. Questo approccio non richiede join e le tabelle sono semplici e dirette, ma c'è una certa ridondanza di dati e problemi di manutenzione se le gerarchie sono profonde.

Ogni strategia offre un equilibrio diverso tra normalizzazione dei dati, semplicità della struttura delle tabelle e prestazioni di lettura/scrittura, e la scelta della strategia giusta dipende dai requisiti specifici dell'applicazione.

### **2. Quali sono le annotazioni corrispondenti in Hibernate/JPA per mappare l’ereditarietà? Quali sono i diversi modi per mappare?**

In Hibernate/JPA, l'ereditarietà si mappa usando diverse annotazioni che indicano quale strategia utilizzare. Le principali annotazioni sono:

- `@Inheritance(strategy = InheritanceType.SINGLE_TABLE)`: utilizza la strategia Single Table.
- `@Inheritance(strategy = InheritanceType.JOINED)`: utilizza la strategia Joined Table.
- `@Inheritance(strategy = InheritanceType.TABLE_PER_CLASS)`: utilizza la strategia Table per Concrete Class.
- `@DiscriminatorColumn` e `@DiscriminatorValue`: usate con la strategia Single Table per differenziare i tipi di entità.

Questi modi di mappare l'ereditarietà consentono di definire come JPA gestisce le relazioni tra le classi e le rispettive tabelle nel database, permettendo di ottimizzare la struttura del database in base alle esigenze specifiche dell'applicazione.

<div class="page"/>

### **3. Quali sono i problemi del mismatch tra paradigma relazionale e a oggetti, in particolare per quanto riguarda l'identità (equals), l'ereditarietà e le associazioni?**

Il mismatch tra paradigma relazionale e a oggetti, noto anche come "impedance mismatch", comporta diversi problemi. Per quanto riguarda l'identità (equals), le differenze nel modo in cui gli oggetti sono identificati nel codice rispetto a come sono identificati nelle tabelle del database possono causare incoerenze. Nell'ereditarietà, il problema principale è come mappare le classi derivate a tabelle relazionali in modo efficiente. Le associazioni, invece, possono essere complesse da gestire, specialmente nelle relazioni molti-a-molti, che richiedono tabelle di join. Questi problemi richiedono soluzioni e accorgimenti specifici per garantire che le operazioni di persistenza siano coerenti ed efficienti.

### **4. Quale annotazione si usa per non rendere una colonna persistente nel database? Come si usa l'annotazione `@Transient`?**

Per non rendere una colonna persistente nel database, si usa l'annotazione `@Transient`. Questa annotazione indica che un campo non deve essere considerato per la persistenza. Si utilizza semplicemente anteponendo `@Transient` al campo in questione, come mostrato nell'esempio:

```java
@Transient
private String temporaryData;
```

In questo modo, il campo `temporaryData` non verrà salvato nel database quando l'entità viene persistita.

### **5. Qual è il comportamento predefinito di JPA? Come si può modificare il comportamento predefinito?**

Il comportamento predefinito di JPA è di mappare le entità a tabelle, i campi a colonne e di utilizzare determinate convenzioni per le chiavi primarie e le relazioni. Questo comportamento può essere modificato utilizzando varie annotazioni JPA, come `@Entity`, `@Table`, `@Column`, `@Id`, `@GeneratedValue` e altre, per specificare configurazioni personalizzate per le entità, i campi e le relazioni. Inoltre, il file `persistence.xml` o le proprietà di configurazione in un'applicazione Spring Boot permettono di configurare ulteriormente il comportamento di JPA, come il nome del database, il dialetto SQL, e le strategie di creazione e aggiornamento dello schema.

<div class="page"/>

### **6. Quali sono le proprietà del file di configurazione di Hibernate che permettono di gestire la creazione e l'aggiornamento dello schema del database?**

Le proprietà del file di configurazione di Hibernate che permettono di gestire la creazione e l'aggiornamento dello schema del database includono:

- `hibernate.hbm2ddl.auto`: controlla la generazione dello schema, con valori come `create`, `update`, `validate`, `create-drop`.
- `hibernate.dialect`: specifica il dialetto SQL utilizzato da Hibernate per generare il SQL appropriato per il database specifico.
- `hibernate.show_sql`: abilita la visualizzazione delle query SQL generate da Hibernate.
- `hibernate.format_sql`: abilita la formattazione delle query SQL generate.
- `hibernate.use_sql_comments`: aggiunge commenti SQL per migliorare la leggibilità.

Queste proprietà sono definite nel file `hibernate.cfg.xml` o nel file di configurazione delle proprietà dell'applicazione.

### **7. Qual è la differenza tra Entity, POJO, DTO e DAO?**

Le differenze tra Entity, POJO, DTO e DAO sono le seguenti:

- **Entity**: rappresenta un oggetto persistente nel database, mappato a una tabella attraverso JPA/Hibernate.
- **POJO (Plain Old Java Object)**: un semplice oggetto Java che non segue alcuna convenzione particolare, spesso utilizzato come modello di dati.
- **DTO (Data Transfer Object)**: un oggetto usato per trasferire dati tra diverse parti di un'applicazione, spesso utilizzato per evitare di esporre le entità direttamente.
- **DAO (Data Access Object)**: un pattern che fornisce un'interfaccia astratta per operazioni CRUD e di accesso ai dati, isolando l'applicazione dal meccanismo di persistenza.

### **8. Come funziona l'ereditarietà nelle entità JPA? Spiega le differenze tra Single Table Inheritance e Class Table Inheritance, e descrivi il ruolo della parte in comune**

L'ereditarietà nelle entità JPA permette di modellare le classi Java in modo che corrispondano alle relazioni di ereditarietà nel database. La Single Table Inheritance utilizza una singola tabella per tutte le classi della gerarchia, con una colonna discriminatore per distinguere i tipi. Questo riduce i join, ma può portare a tabelle sparse. La Class Table Inheritance utilizza una tabella per ogni classe concreta, con una tabella base che contiene i campi comuni. Questo normalizza i dati ma richiede join complessi per ricostruire l'oggetto. La parte in comune è definita nella tabella base, e le tabelle derivate contengono solo i campi specifici della classe.

<div class="page"/>

### **9. Cos'è la strategia di "Joined Table" in JPA e come funziona?**

La strategia di "Joined Table" in JPA mappa ogni classe della gerarchia di ereditarietà a una tabella separata nel database. La tabella della classe base contiene i campi comuni, mentre le tabelle delle classi derivate contengono i campi specifici. Le tabelle sono collegate tramite chiavi esterne. Questo approccio normalizza i dati e riduce la ridondanza, ma può comportare un overhead di prestazioni a causa dei join richiesti per recuperare i dati completi dell'entità. Per implementare questa strategia, si utilizza l'annotazione `@Inheritance(strategy = InheritanceType.JOINED)` sulla classe base.

## **Spring Framework**

### **1. Qual è la differenza tra le varie interfacce di repository in Spring (CrudRepository, PagingAndSortingRepository, JpaRepository)?**

Le varie interfacce di repository in Spring offrono diversi livelli di funzionalità per la gestione dei dati. CrudRepository fornisce operazioni CRUD di base come `save`, `findAll`, `findById`, e `delete`. PagingAndSortingRepository estende CrudRepository aggiungendo metodi per la paginazione e l'ordinamento, come `findAll(Pageable pageable)`, che permette di gestire grandi set di dati in modo più efficiente. JpaRepository, infine, estende PagingAndSortingRepository e aggiunge funzionalità specifiche di JPA come `flush`, `saveAndFlush`, e metodi per il batching delle operazioni. Ogni interfaccia offre un set crescente di funzionalità, con JpaRepository che rappresenta il livello più avanzato.

### **2. Qual è la differenza tra Filter e Interceptor in Spring?**

La differenza principale tra Filter e Interceptor in Spring risiede nel loro ambito di applicazione e nel modo in cui vengono gestiti nel ciclo di vita delle richieste. I Filter sono parte delle specifiche Servlet e vengono applicati alle richieste e risposte HTTP, permettendo di manipolare le richieste prima che raggiungano i servlet e le risposte prima che vengano inviate al client. Gli Interceptor, invece, sono specifici di Spring e vengono applicati alle richieste che sono indirizzate ai controller, permettendo di eseguire logica prima e dopo l'esecuzione di un metodo del controller. I Filter sono configurati nel web.xml o tramite annotazioni in una classe di configurazione, mentre gli Interceptor sono configurati tramite la classe WebMvcConfigurer.

### **3. Come si gestiscono le eccezioni in Spring e quali strumenti offre Spring per questa gestione?**

In Spring, la gestione delle eccezioni può essere effettuata utilizzando diverse strategie e strumenti. Una delle tecniche più comuni è l'uso di `@ExceptionHandler` nei controller per catturare e gestire le eccezioni specifiche. Inoltre, l'annotazione `@ControllerAdvice` può essere utilizzata per definire globalmente la gestione delle eccezioni, applicabile a tutti i controller. Spring offre anche il supporto per la definizione di pagine di errore personalizzate tramite il file di configurazione o annotazioni come `@ResponseStatus`. Per le applicazioni REST, `ResponseEntityExceptionHandler` fornisce una gestione strutturata delle eccezioni, permettendo di restituire risposte HTTP significative.

<div class="page"/>

### **4. Come si utilizza Model Mapper per collegare entità e DTO/DAO?**

Model Mapper è una libreria che facilita la mappatura tra oggetti, come entità e DTO/DAO, riducendo il codice boilerplate. Per utilizzare Model Mapper, si crea un'istanza della classe `ModelMapper`, si configura il mapping tra le classi e si invocano i metodi di mappatura. Ad esempio, per mappare un'entità `User` a un `UserDTO`, si può utilizzare il seguente codice:

```java
ModelMapper modelMapper = new ModelMapper();
UserDTO userDTO = modelMapper.map(user, UserDTO.class);
```

Model Mapper supporta anche mappature complesse e personalizzate attraverso l'uso di `PropertyMap`, permettendo di definire come le proprietà di origine vengono mappate alle proprietà di destinazione.

### **5. Cos'è Swagger e quali funzionalità offre?**

Swagger è un framework per la documentazione delle API REST che permette di generare una documentazione interattiva e di esplorare le API attraverso una interfaccia web. Le principali funzionalità di Swagger includono la generazione automatica della documentazione delle API, la possibilità di eseguire richieste direttamente dall'interfaccia web per testare gli endpoint, e l'integrazione con diversi linguaggi e framework. Swagger utilizza annotazioni come `@Api`, `@ApiOperation`, e `@ApiParam` per descrivere le API e i loro parametri, facilitando la generazione della documentazione e migliorando la comprensione e l'uso delle API.

### **6. Cosa si intende per audit logging nelle REST API?**

L'audit logging nelle REST API si riferisce al processo di registrazione delle attività e degli eventi che si verificano all'interno di un sistema. Questo include la registrazione delle richieste e risposte HTTP, delle modifiche ai dati, delle operazioni eseguite dagli utenti e altri eventi significativi. L'audit logging è essenziale per garantire la sicurezza, la conformità alle normative e per facilitare il debugging e l'analisi forense. In Spring, l'audit logging può essere implementato utilizzando AOP (Aspect-Oriented Programming) per intercettare le chiamate ai metodi e registrare le informazioni rilevanti.

### **7. Quali sono i vantaggi e gli svantaggi dei metodi di query rispetto alle query personalizzate con @Query?**

I metodi di query in Spring Data JPA offrono diversi vantaggi e svantaggi rispetto alle query personalizzate con `@Query`. I vantaggi dei metodi di query includono una maggiore leggibilità e manutenibilità del codice, poiché il nome del metodo descrive chiaramente la query eseguita. Inoltre, non è necessario scrivere codice SQL, riducendo la possibilità di errori. Tuttavia, i metodi di query possono essere limitati in termini di complessità e flessibilità rispetto alle query personalizzate. Le query personalizzate con `@Query` permettono di scrivere query SQL o JPQL complesse, offrendo maggiore controllo e ottimizzazione. Tuttavia, richiedono una maggiore attenzione nella scrittura e manutenzione del codice SQL.

<div class="page"/>

## **Microservizi**

### **1. Come si gestiscono le transazioni nei microservizi utilizzando il pattern Saga?**

Il pattern Saga gestisce le transazioni nei microservizi suddividendole in una serie di transazioni più piccole e indipendenti che possono essere annullate o compensate in caso di fallimento. Ogni microservizio esegue una parte della transazione globale e pubblica un evento che attiva la successiva transazione in un altro microservizio. Se una transazione fallisce, si eseguono le operazioni di compensazione per annullare gli effetti delle transazioni precedenti. Questo approccio assicura che lo stato del sistema rimanga coerente senza necessitare di blocchi distribuiti. Le Sagas possono essere implementate in due modi:

- Coreografia: ogni servizio pubblica e sottoscrive eventi per coordinare le azioni, senza un coordinatore centrale.
- Orchestrazione: un coordinatore centrale invia comandi ai servizi per eseguire le transazioni e le compensazioni.

### **2. Quali sono gli stili di interazione dei microservizi con i processi?**

Gli stili di interazione dei microservizi con i processi possono essere classificati principalmente in due categorie: sincrono e asincrono. Nell'interazione sincrona, un microservizio fa una chiamata diretta a un altro microservizio e attende la risposta, utilizzando protocolli come HTTP/REST o gRPC. Questo metodo è semplice da implementare ma può portare a problemi di latenza e fallimenti cascata. Nell'interazione asincrona, i microservizi comunicano tra loro tramite messaggi attraverso un broker di messaggi come RabbitMQ o Apache Kafka. Questo metodo decouples i servizi, migliora la resilienza e scala meglio, ma introduce complessità nella gestione dei messaggi e nella coerenza eventuale.

### **3. Cos'è il pattern Circuit Breaker, quali problemi risolve e come si implementa con Resilience4j?**

Il pattern Circuit Breaker è un modello di design che previene il fallimento continuo di un servizio chiamando un servizio remoto in caso di malfunzionamento. Funziona come un interruttore che "apre" il circuito dopo un certo numero di fallimenti consecutivi, interrompendo ulteriori tentativi di chiamata e permettendo al servizio di riprendersi. Questo pattern risolve problemi di fallimento a cascata e migliora la resilienza del sistema. Si implementa con Resilience4j configurando un'istanza di CircuitBreaker, definendo i parametri come la soglia di fallimento e il tempo di attesa prima di tentare nuove chiamate, come mostrato nel codice seguente:

```java
CircuitBreakerConfig circuitBreakerConfig = CircuitBreakerConfig.custom()
    .failureRateThreshold(50)
    .waitDurationInOpenState(Duration.ofMillis(1000))
    .build();
CircuitBreakerRegistry circuitBreakerRegistry = CircuitBreakerRegistry.of(circuitBreakerConfig);
CircuitBreaker circuitBreaker = circuitBreakerRegistry.circuitBreaker("myService");
```

<div class="page"/>

### **4. Quali sono i tre stati del pattern Circuit Breaker?**

Il pattern Circuit Breaker opera in tre stati principali:

- **Closed**: lo stato iniziale in cui tutte le richieste vengono inviate al servizio remoto. Se il numero di fallimenti supera una soglia definita, il circuito passa allo stato aperto.
- **Open**: il circuito blocca tutte le richieste al servizio remoto per un periodo di tempo predefinito. Durante questo periodo, le richieste falliscono immediatamente senza tentare di chiamare il servizio.
- **Half-Open**: dopo il periodo di apertura, il circuito permette un numero limitato di richieste di test per verificare se il servizio remoto è tornato operativo. Se le richieste hanno successo, il circuito torna allo stato chiuso; in caso contrario, ritorna allo stato aperto.

### **5. Come funziona il two-phase commit (2PC) nei microservizi e perché può essere preferito rispetto ai Saga? Serve un coordinatore?**

Il two-phase commit (2PC) nei microservizi è un protocollo distribuito che assicura che una transazione globale sia completata in tutti i partecipanti o annullata in tutti. Funziona in due fasi: nella prima fase, il coordinatore invia una richiesta di preparazione a tutti i partecipanti, che rispondono se sono pronti a commettere. Nella seconda fase, se tutti i partecipanti sono pronti, il coordinatore invia un commit; altrimenti, invia un rollback. Il 2PC può essere preferito ai Saga quando la coerenza stretta è critica. Tuttavia, introduce un coordinatore che può diventare un punto di fallimento e richiede blocchi che possono impattare la scalabilità e la disponibilità.

### **6. Perché è necessario avere un servizio discovery nei microservizi e come funziona?**

Un servizio discovery è necessario nei microservizi per gestire la registrazione e la scoperta dinamica dei servizi, facilitando la comunicazione tra di essi senza bisogno di conoscere preventivamente gli indirizzi di rete. Funziona attraverso un registro centrale dove i servizi si registrano con i loro endpoint. I client dei servizi possono quindi interrogare il registro per ottenere l'indirizzo del servizio richiesto. Questo approccio supporta la scalabilità e la resilienza, permettendo ai servizi di essere aggiunti o rimossi dinamicamente. Esempi di strumenti di servizio discovery includono Netflix Eureka, Consul e Apache Zookeeper.

### **7. Qual è la differenza tra un'architettura monolitica e un'architettura a microservizi?**

La differenza principale tra un'architettura monolitica e un'architettura a microservizi risiede nel modo in cui le applicazioni sono strutturate e distribuite. In un'architettura monolitica, tutte le funzionalità dell'applicazione sono contenute in un'unica codebase e vengono distribuite come un singolo artefatto. Questo può semplificare lo sviluppo e il deployment, ma porta a problemi di scalabilità e manutenibilità. Un'architettura a microservizi, invece, suddivide l'applicazione in servizi piccoli e indipendenti che comunicano tra loro attraverso API ben definite. Questo approccio offre scalabilità, flessibilità e facilità di manutenzione, ma introduce complessità nella gestione delle comunicazioni e delle transazioni distribuite.

<div class="page"/>

### **8. Quali sono i vantaggi e gli svantaggi di REST nell'ambito dei microservizi e quali problemi possono sorgere nel fetch dei dati?**

I vantaggi di utilizzare REST nell'ambito dei microservizi includono l'interoperabilità, la semplicità e l'adozione di protocolli standard come HTTP, che facilitano la comunicazione tra servizi eterogenei. Tuttavia, gli svantaggi includono la latenza aggiuntiva dovuta alle chiamate di rete e la difficoltà di gestire transazioni distribuite. Un problema comune nel fetch dei dati è l'over-fetching, dove vengono recuperati più dati del necessario, o l'under-fetching, dove vengono recuperati dati insufficienti, richiedendo ulteriori chiamate. Questi problemi possono essere mitigati utilizzando tecniche come il GraphQL, che permette di specificare esattamente i dati richiesti.

### **9. Cos'è il problema di granularità nei sistemi distribuiti?**

Il problema di granularità nei sistemi distribuiti si riferisce alla difficoltà di determinare la dimensione ottimale dei servizi. Servizi troppo granulari possono comportare un overhead significativo nella comunicazione e nella gestione delle dipendenze, mentre servizi troppo grossolani possono risultare in moduli difficili da manutenere e scalare indipendentemente. Trovare il giusto equilibrio è cruciale per massimizzare i benefici dei microservizi, come la scalabilità e la manutenibilità, riducendo al contempo la complessità operativa.

### **10. Cos'è il Phantom Token Pattern?**

Il Phantom Token Pattern è un pattern di sicurezza utilizzato per mitigare i rischi associati alla gestione dei token di accesso. Invece di trasmettere il token di accesso originale, il client invia un token temporaneo (phantom token) a un servizio intermediario, che verifica e scambia il phantom token con il token di accesso reale. Questo approccio riduce l'esposizione del token di accesso reale, migliorando la sicurezza e riducendo il rischio di furti di token.

### **11. Quali sono i vantaggi e gli svantaggi dell'uso dei microservizi in Spring?**

I vantaggi dell'uso dei microservizi in Spring includono la modularità, la facilità di scalabilità e l'indipendenza delle componenti, che permettono una gestione efficiente e flessibile delle applicazioni. Spring offre un ecosistema robusto con Spring Boot, Spring Cloud e altri strumenti che facilitano la costruzione e la gestione di microservizi. Tuttavia, gli svantaggi includono la complessità operativa dovuta alla gestione di più servizi distribuiti, la necessità di implementare meccanismi di sicurezza e resilienza, e la difficoltà nella gestione delle transazioni distribuite.

<div class="page"/>

### **12. Come comunicano i microservizi tra di loro? Descrivi le differenze tra comunicazione sincrona e asincrona**

I microservizi comunicano tra di loro principalmente attraverso chiamate HTTP/REST o gRPC per la comunicazione sincrona, e attraverso broker di messaggi come RabbitMQ o Kafka per la comunicazione asincrona. La comunicazione sincrona implica che il client attende la risposta del server prima di continuare, rendendo più semplice il coordinamento ma aumentando la latenza e la possibilità di fallimenti a cascata. La comunicazione asincrona, invece, decouples i servizi permettendo loro di funzionare in modo indipendente, migliorando la resilienza e la scalabilità, ma introducendo complessità nella gestione dei messaggi e della coerenza eventuale.

### **13. Quali sono i vantaggi e gli svantaggi dei microservizi, soprattutto per quanto riguarda la gestione del database?**

I vantaggi dei microservizi includono la scalabilità indipendente, la facilità di deploy e la resilienza. Per quanto riguarda la gestione del database, ogni microservizio può avere il proprio database, che permette un isolamento maggiore e una scelta ottimale della tecnologia di persistenza. Tuttavia, questo porta anche a sfide come la gestione della coerenza dei dati tra i servizi, la complessità delle transazioni distribuite e la necessità di strategie di replica e sincronizzazione dei dati.

### **14. Quali problemi possono sorgere nell'unire i dati provenienti da più microservizi in un database? Come possono essere utilizzati strumenti come i data mart?**

Unire i dati provenienti da più microservizi può comportare problemi di coerenza, sincronizzazione e performance. La distribuzione dei dati tra diversi servizi può rendere difficile eseguire query aggregate o unire dati in modo efficiente. Strumenti come i data mart possono essere utilizzati per aggregare i dati da vari microservizi in un singolo repository, permettendo query efficienti e analisi dei dati. I data mart possono essere aggiornati periodicamente attraverso processi ETL (Extract, Transform, Load) per mantenere la coerenza dei dati.

### **15. Quali sono i vantaggi e gli svantaggi dei microservizi in generale e nella gestione dei database? Come affrontare le sfide di raggruppare dati da vari microservizi?**

I vantaggi dei microservizi includono la scalabilità, l'indipendenza del ciclo di vita del deploy e la modularità. Tuttavia, gestire database separati per ogni microservizio può introdurre complessità nella gestione delle transazioni distribuite e nella coerenza dei dati. Per affrontare queste sfide, si possono utilizzare pattern come l'event sourcing e il CQRS (Command Query Responsibility Segregation), che permettono di mantenere la coerenza dei dati attraverso eventi e viste materializzate. Inoltre, l'uso di strumenti di orchestrazione e servizi di integrazione può facilitare la gestione dei dati distribuiti.

<div class="page"/>

### **16. Cos'è il pattern API Gateway e quale ruolo svolge nei microservizi?**

Il pattern API Gateway è un pattern di architettura che prevede l'uso di un gateway centralizzato che funge da unico punto di ingresso per tutte le chiamate ai microservizi. L'API Gateway gestisce la rotta delle richieste ai microservizi appropriati, aggrega le risposte, gestisce la sicurezza, il bilanciamento del carico e la traduzione dei protocolli. Questo pattern aiuta a semplificare la comunicazione tra client e microservizi, migliorando la sicurezza e la gestione delle richieste, ma introduce un ulteriore punto di fallimento e può diventare un collo di bottiglia se non scalato correttamente.

### **17. Quali sono i diversi modi per scalare un'applicazione? Spiega la scalabilità verticale e orizzontale**

Le applicazioni possono essere scalate principalmente in due modi: verticalmente e orizzontalmente. La scalabilità verticale (scaling up) implica l'aggiunta di risorse (CPU, memoria, storage) a un singolo nodo o server, aumentando la sua capacità di gestire il carico. Questo approccio è limitato dalla capacità massima dell'hardware e può essere costoso. La scalabilità orizzontale (scaling out) implica l'aggiunta di più nodi o server che lavorano insieme per gestire il carico. Questo approccio è più flessibile e può offrire una maggiore resilienza e disponibilità, ma richiede una gestione più complessa della distribuzione del carico e della coerenza dei dati.

### **18. Qual è il ruolo di un message broker nei microservizi? Quali sono i message broker più popolari e utilizzati?**

Il ruolo di un message broker nei microservizi è quello di facilitare la comunicazione asincrona tra i servizi, permettendo loro di inviare e ricevere messaggi senza essere direttamente collegati. I message broker decouples i produttori e i consumatori di messaggi, migliorando la resilienza, la scalabilità e la tolleranza ai guasti del sistema. I message broker più popolari e utilizzati includono:

- **RabbitMQ**: noto per la sua flessibilità e supporto per vari protocolli di messaggistica.
- **Apache Kafka**: ideale per l'elaborazione di flussi di dati in tempo reale e per la gestione di grandi volumi di dati.
- **Amazon SQS**: un servizio di messaggistica completamente gestito offerto da AWS, noto per la sua scalabilità e semplicità d'uso.

Questi message broker offrono funzionalità avanzate come la gestione delle code, la persistenza dei messaggi e la distribuzione dei messaggi a più consumatori.

<div class="page"/>

## **Docker**

### **1. Qual è la differenza tra un Dockerfile (per definire una nuova immagine) e Docker Compose?**

Un Dockerfile è un file di testo contenente una serie di istruzioni che Docker utilizza per costruire una nuova immagine. Le istruzioni includono il settaggio del sistema operativo di base, l'installazione di software necessario, la copia di file e la configurazione delle impostazioni di runtime. Docker Compose, invece, è uno strumento che permette di definire e gestire applicazioni multi-container. Utilizzando un file YAML (`docker-compose.yml`), Docker Compose consente di descrivere come i servizi dovrebbero interagire, includendo configurazioni per networking, volumi e dipendenze. Le principali differenze sono:

- **Dockerfile**: utilizzato per creare singole immagini, specificando l'ambiente e le applicazioni necessarie.
- **Docker Compose**: utilizzato per orchestrare e gestire applicazioni che richiedono più container, facilitando il processo di deploy e gestione di servizi complessi.

### **2. Qual è la differenza tra un'immagine Docker e un container Docker?**

Un'immagine Docker è un pacchetto leggibile di un'applicazione, comprensivo di tutto il necessario per il suo funzionamento: codice, runtime, librerie, variabili d'ambiente e configurazioni. È una sorta di snapshot immutabile del filesystem di un'applicazione. Un container Docker, invece, è un'istanza eseguibile di un'immagine Docker. Mentre l'immagine è statica, il container è dinamico e rappresenta un'istanza runtime che può essere avviata, eseguita, fermata o eliminata. In sintesi:

- **Immagine Docker**: un template immutabile con tutto il necessario per eseguire un'applicazione.
- **Container Docker**: un'istanza eseguibile dell'immagine, che rappresenta l'applicazione in esecuzione con risorse e stato runtime specifico.

### **3. Che tipo di volumi possono essere montati in Docker? È possibile creare un’immagine partendo da una già esistente?**

In Docker, i volumi possono essere di diversi tipi, principalmente:

- **Named volumes**: gestiti da Docker, sono volumi con un nome specifico che viene creato e gestito separatamente dai container.
- **Anonymous volumes**: creati senza un nome specifico, sono legati al ciclo di vita del container.
- **Bind mounts**: mappano una directory del filesystem host a una directory del container, fornendo un accesso diretto ai dati del filesystem host.

È possibile creare un’immagine partendo da una già esistente utilizzando il concetto di immagini di base. In un Dockerfile, si può specificare una base esistente utilizzando l'istruzione `FROM`, e poi aggiungere ulteriori istruzioni per modificare o estendere l'immagine di base. Questo permette di costruire immagini personalizzate a partire da immagini ufficiali o altre immagini già configurate.

<div class="page"/>

## **REST API e Sicurezza**

### **1. Quali sono le caratteristiche principali delle API REST? Spiega il concetto di statelessness, la struttura standard degli URL, la convenzione dei nomi e altri principi fondamentali**

Le API REST (Representational State Transfer) sono progettate secondo alcuni principi fondamentali per garantire scalabilità, manutenibilità e facilità di utilizzo. Le caratteristiche principali includono l'uso del protocollo HTTP per la comunicazione, l'identificazione delle risorse tramite URL, e l'uso di metodi HTTP standard come GET, POST, PUT, DELETE per operazioni CRUD. Il concetto di statelessness implica che ogni richiesta dal client al server deve contenere tutte le informazioni necessarie per comprendere e processare la richiesta; il server non deve mantenere alcuno stato della sessione del client tra le richieste. La struttura standard degli URL è organizzata in modo gerarchico per rappresentare le risorse, ad esempio `/users/123` per accedere all'utente con ID 123. Le convenzioni di nomenclatura prevedono l'uso di sostantivi al plurale per rappresentare le risorse, metodi HTTP per le azioni e formati di risposta standardizzati come JSON o XML.

### **2. Cos'è il rate limiting e come viene utilizzato per controllare l'accesso alle API?**

Il rate limiting è una tecnica utilizzata per controllare il numero di richieste che un client può effettuare a un'API entro un determinato periodo di tempo. Questo aiuta a prevenire abusi, proteggere le risorse del server e garantire una distribuzione equa delle risorse tra gli utenti. Viene implementato utilizzando diverse strategie, come il token bucket, il leaky bucket, il fixed window counter o il sliding window log. Ad esempio, un'API potrebbe limitare un client a 1000 richieste al minuto, restituendo una risposta HTTP 429 (Too Many Requests) quando il limite viene superato. Il rate limiting può essere configurato a livello di API gateway o direttamente all'interno dell'applicazione.

### **3. Cos'è OAuth2? Perché è stato introdotto e quali problemi risolve?**

OAuth2 è un protocollo di autorizzazione che consente a un'applicazione di accedere alle risorse di un utente su un altro servizio, senza richiedere all'utente di condividere le proprie credenziali. È stato introdotto per risolvere problemi di sicurezza e facilità d'uso nelle interazioni tra servizi, consentendo l'accesso delegato. OAuth2 fornisce un framework per flussi di autorizzazione diversi, come l'autorizzazione tramite codice, implicita, password e credenziali del client. Questo approccio riduce i rischi associati alla gestione delle password e migliora la sicurezza, poiché le credenziali dell'utente non vengono esposte alle applicazioni di terze parti.

<div class="page"/>

### **4. Cosa sono i token e come vengono utilizzati nelle operazioni di autenticazione e autorizzazione?**

I token sono stringhe alfanumeriche generate durante il processo di autenticazione, utilizzate per verificare l'identità dell'utente e autorizzare l'accesso alle risorse. Ci sono diversi tipi di token, come i token di accesso (access tokens) e i token di aggiornamento (refresh tokens). I token di accesso vengono inclusi nelle richieste API per autorizzare l'accesso alle risorse protette, mentre i token di aggiornamento possono essere utilizzati per ottenere nuovi token di accesso senza richiedere nuovamente le credenziali dell'utente. I token sono solitamente a tempo limitato e possono includere informazioni aggiuntive sull'utente e sui permessi.

### **5. Cosa sono i JWT (JSON Web Tokens)? Come fanno ad essere self-contained e come garantiscono la sicurezza?**

I JSON Web Tokens (JWT) sono un tipo di token utilizzato per l'autenticazione e l'autorizzazione. Sono self-contained, cioè contengono tutte le informazioni necessarie per verificare l'identità dell'utente e i suoi permessi. Un JWT è composto da tre parti: header, payload e signature. Il header specifica l'algoritmo di firma, il payload contiene le dichiarazioni (claims) sull'utente e il signature è una firma crittografica che garantisce l'integrità e l'autenticità del token. La sicurezza è garantita tramite la firma crittografica, che impedisce la manomissione del token, e tramite l'uso di protocolli sicuri (HTTPS) per la trasmissione del token.

### **6. Come si gestisce il logout quando si utilizzano i JWT per l'autenticazione?**

Quando si utilizzano i JWT per l'autenticazione, il logout può essere gestito in diversi modi. Un approccio comune è invalidare il token lato client eliminandolo dal browser o dall'applicazione. Tuttavia, per garantire una sicurezza maggiore, è consigliabile implementare una blacklist di token sul server, dove i token invalidati vengono memorizzati e controllati per ogni richiesta. Un altro approccio è utilizzare token con una durata breve e aggiornare frequentemente il token di accesso tramite un token di aggiornamento, riducendo l'impatto di eventuali token compromessi.

### **7. Spiega il flusso del Client Credential Grant in OAuth2**

Il flusso del Client Credential Grant in OAuth2 è un flusso di autorizzazione utilizzato quando un client deve accedere alle proprie risorse, non agendo per conto di un utente. In questo flusso, il client invia le proprie credenziali (client ID e client secret) al server di autorizzazione, richiedendo un token di accesso. Se le credenziali sono valide, il server di autorizzazione rilascia un token di accesso che il client può utilizzare per autenticarsi e accedere alle risorse protette. Questo flusso è tipicamente utilizzato per server-to-server communication, dove non è coinvolto un utente finale.

<div class="page"/>

### **8. Qual è la differenza tra autenticazione e autorizzazione?**

L'autenticazione e l'autorizzazione sono due concetti distinti ma correlati. L'autenticazione è il processo di verifica dell'identità di un utente, cioè confermare che l'utente è chi dice di essere. Questo processo può includere la verifica delle credenziali come username e password. L'autorizzazione, invece, è il processo di concedere o negare l'accesso alle risorse basato sui permessi dell'utente autenticato. In altre parole, l'autenticazione risponde alla domanda "Chi sei?", mentre l'autorizzazione risponde alla domanda "Cosa sei autorizzato a fare?".

### **9. Cos'è il Cross-site Scripting (XSS) e come può essere prevenuto?**

Il Cross-site Scripting (XSS) è una vulnerabilità di sicurezza che consente agli attaccanti di iniettare script malevoli in pagine web visualizzate da altri utenti. Questi script possono essere utilizzati per rubare dati, sessioni, o eseguire altre azioni malevole a nome dell'utente. Per prevenire XSS, è fondamentale:

- **Sanitizzare**: rimuovere o neutralizzare i dati in input che possono contenere codice malevolo.
- **Escapare**: assicurarsi che i dati in input siano trattati come dati e non come codice eseguibile.
- **Content Security Policy (CSP)**: implementare CSP per limitare le fonti di script che possono essere eseguiti nel browser.

### **10. Qual è la differenza tra crittografia simmetrica e asimmetrica?**

La crittografia simmetrica e asimmetrica differiscono principalmente nella gestione delle chiavi. Nella crittografia simmetrica, la stessa chiave è utilizzata sia per crittografare che per decrittografare i dati, il che richiede che la chiave sia condivisa in modo sicuro tra le parti. È veloce ed efficiente per grandi quantità di dati. Nella crittografia asimmetrica, si utilizzano una coppia di chiavi, una pubblica e una privata. La chiave pubblica viene utilizzata per crittografare i dati, mentre la chiave privata viene utilizzata per decrittografarli. Questo metodo elimina la necessità di condividere segretamente la chiave di decrittazione, ma è computazionalmente più costoso rispetto alla crittografia simmetrica.

### **11. Cosa sono i Macaroons e come vengono utilizzati per l'autenticazione?**

I Macaroons sono un tipo di token di autenticazione che offre flessibilità e controllo fine-grained sull'accesso. A differenza dei token tradizionali, i Macaroons possono essere attenuati, ovvero possono avere restrizioni aggiuntive applicate, come la limitazione a determinate azioni, tempi di validità o risorse specifiche. Ogni attenuazione produce un nuovo Macaroon, che può essere ulteriormente attenuato. Questo consente una delega sicura e controllata delle autorizzazioni, permettendo di gestire l'accesso con maggiore precisione rispetto ai token standard.

<div class="page"/>

### **12. Qual è la differenza tra OAuth2 e OpenID Connect?**

OAuth2 è un protocollo di autorizzazione che consente a un'applicazione di ottenere accesso limitato alle risorse di un utente su un altro servizio. OpenID Connect è un'estensione di OAuth2 che aggiunge l'autenticazione, permettendo di verificare l'identità dell'utente oltre a ottenere l'autorizzazione. Mentre OAuth2 fornisce solo token di accesso per l'autorizzazione, OpenID Connect fornisce anche un ID token, che contiene informazioni sull'utente e può essere utilizzato per l'autenticazione.

### **13. Cos'è Keycloak?**

Keycloak è una soluzione di gestione dell'identità e dell'accesso open-source sviluppata da Red Hat. Fornisce funzionalità di autenticazione e autorizzazione per applicazioni web e servizi RESTful. Keycloak supporta protocolli standard come OAuth2, OpenID Connect e SAML, permettendo l'integrazione con una vasta gamma di applicazioni e servizi. Include funzionalità come l'autenticazione a più fattori, la gestione delle sessioni, la federazione delle identità e il single sign-on (SSO), semplificando la gestione degli accessi e migliorando la sicurezza.

### **14. Cos'è il Role-based Access Control (RBAC)?**

Il Role-based Access Control (RBAC) è un modello di controllo degli accessi che assegna permessi agli utenti in base ai loro ruoli all'interno di un'organizzazione. Invece di assegnare permessi individuali, RBAC associa ruoli a permessi e utenti a ruoli, semplificando la gestione degli accessi. Ad esempio, un ruolo "Amministratore" può avere permessi per creare, leggere, aggiornare e eliminare risorse, mentre un ruolo "Utente" può avere permessi solo per leggere le risorse. Questo approccio facilita la gestione dei permessi e migliora la sicurezza, assicurando che gli utenti abbiano accesso solo alle risorse necessarie per il loro ruolo.

### **15. Cos'è il Mutual TLS e come funziona?**

Il Mutual TLS (Transport Layer Security) è un protocollo di sicurezza che autentica sia il client che il server durante la stabilizzazione di una connessione sicura. Mentre il TLS standard autentica solo il server al client, il Mutual TLS richiede che entrambi i lati presentino certificati digitali validi per verificare le loro identità. Funziona come segue:

- Il client invia una richiesta di connessione al server.
- Il server risponde con il suo certificato.
- Il client verifica il certificato del server e, se valido, invia il proprio certificato al server.
- Il server verifica il certificato del client.
Se entrambi i certificati sono validi, viene stabilita una connessione sicura e autenticata, garantendo una maggiore sicurezza per le comunicazioni sensibili.

<div class="page"/>

## **Android e Kotlin**

### **1. Come si implementano i metodi del lazy loading? Quali sono le tre tecniche principali utilizzate?**

I metodi del lazy loading in Kotlin vengono implementati per ritardare l'inizializzazione di un oggetto fino a quando non è necessario, migliorando le prestazioni e riducendo l'uso di memoria. Kotlin offre diverse tecniche per il lazy loading, tra cui:

- **Delegated Properties con `lazy`**: utilizza il costrutto `by lazy` per delegare l'inizializzazione di una proprietà fino a quando non viene acceduta per la prima volta.
- **Custom Lazy Initialization**: implementa una propria logica di lazy loading tramite una variabile privata che viene inizializzata solo quando necessaria.
- **Double-Checked Locking**: in contesti multithreaded, si può utilizzare la tecnica di double-checked locking per assicurarsi che l'oggetto venga inizializzato solo una volta, anche in presenza di concorrenza.

Esempio di `by lazy`:

```kotlin
val myLazyValue: String by lazy {
    println("Computed!")
    "Hello"
}
```

### ****2. Quali sono i componenti grafici disponibili in Jetpack Compose?****

Jetpack Compose, il moderno toolkit per l'interfaccia utente di Android, offre una vasta gamma di componenti grafici (UI components) per costruire interfacce utente intuitive e dinamiche. Alcuni dei componenti principali includono:

- **Text**: per visualizzare testo.
- **Button**: per creare pulsanti interattivi.
- **Image**: per mostrare immagini.
- **Row** e **Column**: per disporre elementi in righe e colonne.
- **Box**: per sovrapporre elementi.
- **Scaffold**: per strutturare il layout di base di un'applicazione.
- **Card**: per creare contenitori stilizzati.
- **TextField**: per input di testo.
- **Slider**: per selezionare valori in un intervallo.
- **Switch**: per creare toggle switches.

Questi componenti permettono di creare interfacce utente moderne e responsive utilizzando un approccio dichiarativo.

<div class="page"/>

### **3. Quali sono i layout di base in Jetpack Compose e come vengono utilizzati?**

In Jetpack Compose, i layout di base sono utilizzati per strutturare e posizionare gli elementi dell'interfaccia utente. I layout principali includono:

- **Row**: organizza i componenti orizzontalmente in una singola riga. Utilizzato quando si desidera posizionare elementi uno accanto all'altro.
- **Column**: organizza i componenti verticalmente in una singola colonna. Utilizzato per disporre gli elementi uno sopra l'altro.
- **Box**: sovrappone i componenti, permettendo di posizionare elementi uno sopra l'altro. Ideale per scenari in cui si desidera che gli elementi si sovrappongano.
- **ConstraintLayout**: offre un layout flessibile simile al ConstraintLayout tradizionale di Android, permettendo di posizionare gli elementi in base a vincoli.

Esempio di utilizzo di Row e Column:

```kotlin
Column {
    Text("Hello")
    Row {
        Text("World")
        Text("!")
    }
}
```

### **4. Cosa sono LazyColumn e LazyRow in Jetpack Compose e come funzionano?**

LazyColumn e LazyRow sono componenti di Jetpack Compose progettati per visualizzare liste di elementi in modo efficiente, caricando solo gli elementi visibili sullo schermo per migliorare le prestazioni. Funzionano in modo simile a RecyclerView, ma con un approccio dichiarativo:

- **LazyColumn**: visualizza gli elementi in una colonna verticale, caricando solo gli elementi visibili e scorrendo verticalmente.
- **LazyRow**: visualizza gli elementi in una riga orizzontale, caricando solo gli elementi visibili e scorrendo orizzontalmente.

Esempio di LazyColumn:

```kotlin
LazyColumn {
    items(100) { index ->
        Text("Item #$index")
    }
}
```

Questi layout sono utilizzati per creare liste dinamiche e scorrevoli in modo efficiente.

<div class="page"/>

### **5. Cosa sono LazyVerticalGrid e LazyHorizontalGrid in Jetpack Compose e come funzionano?**

LazyVerticalGrid e LazyHorizontalGrid sono componenti di Jetpack Compose utilizzati per visualizzare elementi in una griglia con scorrimento rispettivamente verticale e orizzontale. Questi componenti caricano solo gli elementi visibili sullo schermo, migliorando l'efficienza del rendering. Funzionano in modo simile a LazyColumn e LazyRow ma con una disposizione a griglia:

- **LazyVerticalGrid**: organizza gli elementi in una griglia che scorre verticalmente.
- **LazyHorizontalGrid**: organizza gli elementi in una griglia che scorre orizzontalmente.

Esempio di LazyVerticalGrid:

```kotlin
LazyVerticalGrid(
    cells = GridCells.Fixed(2)
) {
    items(100) { index ->
        Text("Item #$index")
    }
}
```

Questi layout permettono di creare interfacce utente complesse e dinamiche con un approccio dichiarativo e ottimizzato.

### **6. Come si gestiscono gli eventi di click in Jetpack Compose?**

Per gestire gli eventi di click in Jetpack Compose, si utilizza il composable `Clickable`, che permette di rendere un componente interattivo e reagire ai click dell'utente. È possibile utilizzare `Clickable` direttamente o combinare un composable con `Modifier.clickable` per rendere un componente cliccabile. Ad esempio, per gestire un evento di click su un `Text`, si può utilizzare `ClickableText`:

```kotlin
val count = remember { mutableStateOf(0) }

ClickableText(
    text = "Click me!",
    onClick = {
        count.value++
    }
)
```

In questo esempio, ogni volta che l'utente clicca sul testo "Click me!", il contatore `count` viene incrementato.

<div class="page"/>

## **Altri Argomenti**

### **1. Cosa sono le Capabilities e come si possono implementare?**

Le Capabilities in un'applicazione enterprise rappresentano le funzionalità o i servizi che un sistema può offrire agli utenti o ad altri sistemi. Si possono implementare tramite una struttura modulare, dove ogni modulo rappresenta una capability specifica, facilitando così la gestione e l'estensione delle funzionalità. Un approccio comune è l'uso di microservizi, dove ogni microservizio implementa una singola capability, comunicando con gli altri tramite API ben definite. Questo permette di scalare e manutenere le capabilities in modo indipendente.

### **2. Come si organizza logicamente la business logic in un'applicazione enterprise?**

La business logic in un'applicazione enterprise viene organizzata in modo da separare le responsabilità e facilitare la manutenzione e l'espansione del sistema. Di solito, la business logic è suddivisa in strati (layer) come il layer di presentazione, il layer di applicazione, il layer di dominio e il layer di persistenza. Ogni strato ha una responsabilità specifica:

- **Layer di Presentazione**: gestisce l'interfaccia utente e l'interazione con l'utente.
- **Layer di Applicazione**: coordina le operazioni tra il layer di presentazione e il layer di dominio.
- **Layer di Dominio**: contiene la logica di business core, rappresentando le regole e i comportamenti del sistema.
- **Layer di Persistenza**: gestisce l'accesso ai dati e le operazioni sul database.

### **3. Come si gestisce la concorrenza nelle applicazioni software?**

La gestione della concorrenza nelle applicazioni software si realizza utilizzando varie tecniche per assicurare che le risorse condivise siano accessibili in modo sicuro da più thread o processi. Alcune tecniche comuni includono:

- **Locking**: l'uso di mutex o semafori per bloccare l'accesso alle risorse condivise.
- **Atomic Operations**: operazioni indivisibili che assicurano che una serie di operazioni venga completata senza interruzioni.
- **Thread Pools**: per limitare il numero di thread attivi e migliorare la gestione delle risorse.
- **Transactional Memory**: per gestire la concorrenza a livello di memoria tramite transazioni.

### **4. Come viene implementato l'optimistic locking in un sistema di gestione dei dati?**

L'optimistic locking è una tecnica utilizzata per gestire le concorrenze nelle operazioni di aggiornamento dei dati senza bloccare risorse. Si basa sull'assunzione che i conflitti di accesso saranno rari. Ogni entità ha un campo di versione che viene incrementato ad ogni aggiornamento. Quando un client legge un'entità, memorizza il valore di versione. Al momento dell'aggiornamento, il client invia il valore di versione originale. Se il valore corrente nel database corrisponde a quello inviato dal client, l'aggiornamento procede; altrimenti, viene generato un errore indicando un conflitto. Questo metodo riduce il locking e migliora le performance.

<div class="page"/>

### **5. Quali sono le proprietà ACID e come vengono utilizzate?**

Le proprietà ACID sono un insieme di proprietà che garantiscono l'affidabilità delle transazioni nei sistemi di gestione dei dati:

- **Atomicità**: garantisce che tutte le operazioni all'interno di una transazione siano completate con successo o nessuna.
- **Consistenza**: assicura che una transazione porti il database da uno stato valido a un altro stato valido.
- **Isolamento**: garantisce che le operazioni di una transazione siano isolate dalle operazioni di altre transazioni.
- **Durabilità**: assicura che una volta che una transazione è completata, i suoi effetti persistono nel sistema anche in caso di guasti.
Queste proprietà vengono utilizzate per garantire che le operazioni sui dati siano affidabili e che il database rimanga in uno stato consistente.

### **6. Quali sono gli altri modi di eseguire interrogazioni in Spring Data oltre ai metodi di repository standard?**

Oltre ai metodi di repository standard, Spring Data offre diversi modi per eseguire interrogazioni:

- **Query Methods**: definendo metodi nel repository seguendo convenzioni di naming che Spring Data traduce automaticamente in query.
- **@Query Annotation**: per scrivere query personalizzate utilizzando JPQL o SQL direttamente nei metodi del repository.
- **Named Queries**: predefinendo le query in XML o annotazioni e richiamandole per nome.
- **Criteria API**: per costruire query dinamicamente in modo programmatico, utile per query complesse che cambiano in base a vari parametri.
- **QueryDSL**: una libreria che consente di costruire query in modo tipizzato e sicuro al compile-time.

### **7. Quali sono i problemi di granularità nei sistemi software e come possono essere risolti?**

I problemi di granularità nei sistemi software si riferiscono alla difficoltà di trovare il giusto livello di dettaglio per i componenti del sistema. Granularità troppo fine può portare a un eccesso di comunicazione e complessità di gestione, mentre granularità troppo grossolana può rendere difficile la riusabilità e la scalabilità. Per risolvere questi problemi, si possono adottare strategie come:

- **Modularizzazione**: suddividere il sistema in moduli ben definiti con responsabilità chiare.
- **Microservizi**: adottare un'architettura a microservizi per mantenere i servizi indipendenti e scalabili.
- **Service Layer**: introdurre livelli di servizio per aggregare funzionalità comuni e ridurre la complessità.
- **Domain-Driven Design (DDD)**: utilizzare i principi del DDD per definire chiaramente i contesti delimitati e le responsabilità dei componenti.

### **8. Cos'è un attacco ReDDos e come può essere mitigato?**

Un attacco ReDDos (Reflection-based Distributed Denial of Service) sfrutta server vulnerabili per riflettere il traffico verso una vittima, amplificando l'attacco. Gli attaccanti inviano richieste con l'indirizzo IP della vittima come mittente a server con servizi come DNS, NTP o Memcached, che rispondono con una quantità di dati molto maggiore. Per mitigare gli attacchi ReDDos:

- **Protezione dei server riflettori**: configurare i server per prevenire l'uso abusivo, limitando i servizi esposti e applicando patch di sicurezza.
- **Filtraggio del traffico**: utilizzare firewall e sistemi di prevenzione delle intrusioni per filtrare il traffico sospetto.
- **Rete di distribuzione dei contenuti (CDN)**: distribuire il traffico su più server per assorbire meglio l'impatto degli attacchi.
- **Servizi di mitigazione DDoS**: impiegare servizi specializzati che rilevano e mitigano automaticamente gli attacchi DDoS.
