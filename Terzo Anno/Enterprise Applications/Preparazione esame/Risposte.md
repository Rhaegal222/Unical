### Java e Hibernate/JPA

1. Come mappare l’eredità usando l’url? Quali sono le diverse strategie?
    Per mappare l'eredità usando l'url si possono utilizzare diverse strategie:
    - **Single Table Inheritance**: si mappa l'intera gerarchia di classi in una singola tabella. Si utilizza un campo discriminatorio per distinguere i diversi tipi di entità. Vantaggi: semplicità, nessuna join, nessuna query complessa. Svantaggi: tabella molto grande, campi nulli, non supporta relazioni tra le entità.
    - **Table per Class Inheritance**: si mappa ogni classe in una tabella separata. Vantaggi: tabella più piccola, nessun campo null, supporta relazioni tra le entità. Svantaggi: query complesse, join necessarie.
    - **Joined Table Inheritance**: si mappa ogni classe in una tabella separata, ma si mantiene una tabella per la classe padre con i campi comuni. Vantaggi: tabella più piccola, nessun campo null, supporta relazioni tra le entità, query più semplici. Svantaggi: join necessarie.
2. Quali sono le annotazioni corrispondenti in Hibernate/JPA? I modi per mappare.
    Le annotazioni corrispondenti in Hibernate/JPA per mappare l'eredità sono:
    - **@Inheritance(strategy = InheritanceType.SINGLE_TABLE)**: per la strategia di Single Table Inheritance.
    - **@Inheritance(strategy = InheritanceType.TABLE_PER_CLASS)**: per la strategia di Table per Class Inheritance.
    - **@Inheritance(strategy = InheritanceType.JOINED)**: per la strategia di Joined Table Inheritance.
3. Problemi del mismatch tra paradigma relazionale e a oggetti (problema dell’identità (equals), ereditarietà, associazioni).
    I principali problemi del mismatch tra il paradigma relazionale e quello ad oggetti sono:
    - **Problema dell'identità**: in un database relazionale l'identità di un'entità è data dal valore della chiave primaria, mentre in un'istanza di classe in Java l'identità è data dall'indirizzo di memoria. Questo può portare a problemi di confronto tra oggetti.
    - **Problema dell'ereditarietà**: il modello relazionale non supporta direttamente l'ereditarietà, quindi è necessario utilizzare strategie di mappatura per gestire le gerarchie di classi.
    - **Problema delle associazioni**: le relazioni tra entità in un database relazionale sono gestite tramite chiavi esterne, mentre in un modello ad oggetti le associazioni sono rappresentate direttamente tra le classi. Questo può portare a problemi di navigazione e caricamento dei dati.
4. Cosa si usa per non rendere una colonna persistente sul database?
    Per non rendere una colonna persistente sul database si può utilizzare l'annotazione **@Transient** su un campo della classe. Questo indica a Hibernate/JPA di non considerare quel campo durante la persistenza dell'entità. Ad esempio, si può utilizzare per campi calcolati o temporanei che non devono essere memorizzati nel database.
5. Qual è il comportamento predefinito di JPA per la proprietà hibernate.hbm2ddl.auto? È create o update?
    Di default, JPA utilizza la strategia di **create** per le operazioni di persistenza. Questo significa che quando si salva un'entità tramite il metodo `entityManager.persist(entity)`, verrà creata una nuova riga nel database con i valori dell'entità. Se si desidera aggiornare un'entità esistente, è necessario utilizzare il metodo `entityManager.merge(entity)` che esegue un'operazione di update. In alternativa, è possibile utilizzare il metodo `entityManager.find(entityClass, id)` per ottenere un'istanza gestita dell'entità e modificarla direttamente.
6. Dentro file properties: hibernate con prembul per aggiornare o modificare.
    Per configurare Hibernate tramite un file di properties, è possibile utilizzare le seguenti proprietà:
    - **hibernate.hbm2ddl.auto**: questa proprietà specifica il comportamento di Hibernate per la creazione e l'aggiornamento dello schema del database. I valori possibili sono `create`, `update`, `create-drop`, `validate`. Ad esempio, `hibernate.hbm2ddl.auto=update` indica di aggiornare lo schema del database in base alle modifiche alle entità.
7. Qual è la differenza tra Entity, POJO, DTO e DAO?
    - **Entity**: un'entità è una classe che rappresenta un'istanza persistente nel database. È mappata direttamente a una tabella del database e può contenere annotazioni specifiche per la persistenza.
    - **POJO (Plain Old Java Object)**: un POJO è una classe Java semplice che non ha dipendenze da framework o librerie esterne. È spesso utilizzato per rappresentare dati o oggetti di dominio.
    - **DTO (Data Transfer Object)**: un DTO è un oggetto utilizzato per trasferire dati tra diversi componenti di un'applicazione. È spesso utilizzato per incapsulare dati da più entità o per ridurre il traffico di rete.
    - **DAO (Data Access Object)**: un DAO è un'interfaccia o una classe che fornisce metodi per accedere e manipolare i dati nel database. È spesso utilizzato per separare la logica di accesso ai dati dalla logica di business.
8. Come funziona l'ereditarietà nelle entità JPA? Spiega le differenze tra Single Table Inheritance e Class Table Inheritance, e descrivi il ruolo della parte in comune.
    Nelle entità JPA, l'ereditarietà può essere gestita utilizzando le annotazioni `@Inheritance` e `@DiscriminatorColumn`. 
    - **Single Table Inheritance**: in questo caso, tutte le classi figlie vengono mappate sulla stessa tabella, con un campo discriminatorio che indica il tipo di entità. Le colonne comuni a tutte le entità vengono definite nella tabella principale, mentre le colonne specifiche di ciascuna entità vengono definite solo per quella specifica entità.
    - **Class Table Inheritance**: in questo caso, ogni classe figlia viene mappata su una tabella separata, con una relazione uno a uno tra la tabella della classe padre e le tabelle delle classi figlie. Le colonne comuni vengono definite nella tabella della classe padre, mentre le colonne specifiche vengono definite nelle tabelle delle classi figlie.
    La parte in comune tra le entità è rappresentata dalle colonne comuni definite nella tabella principale o nella tabella della classe padre. Queste colonne vengono ereditate dalle classi figlie e possono essere utilizzate per rappresentare attributi condivisi tra le diverse entità.
9. Cos'è la strategia di "Joined Table" in JPA e come funziona?
    La strategia di "Joined Table" in JPA è una strategia di mappatura per l'ereditarietà che prevede la creazione di una tabella separata per ciascuna classe figlia, mantenendo una tabella comune per la classe padre con i campi condivisi. Le caratteristiche principali di questa strategia sono:
    - Ogni tabella corrisponde a una classe concreta dell'ereditarietà.
    - La tabella della classe padre contiene i campi comuni a tutte le classi figlie.
    - Le tabelle delle classi figlie contengono i campi specifici di ciascuna classe.
    - Viene utilizzata una relazione uno a uno tra la tabella della classe padre e le tabelle delle classi figlie per mantenere l'integrità referenziale.
    - Le query che coinvolgono le classi figlie richiedono join tra le tabelle per recuperare i dati.
    Questa strategia permette di mantenere una struttura più normalizzata del database, evitando campi nulli e ridondanze di dati. Tuttavia, può richiedere query più complesse a causa delle join necessarie per recuperare i dati delle classi figlie.