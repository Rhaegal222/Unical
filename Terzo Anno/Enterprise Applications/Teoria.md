# Enterprise Applications - Teoria

## Cos’è un’applicazione enterprise?

Un'applicazione enterprise è un sistema software progettato per soddisfare le esigenze aziendali complesse e scalabili. Sebbene non esista una definizione standard, queste applicazioni condividono molte caratteristiche. Spesso coinvolgono dati complessi con persistenza a lungo termine e devono gestire volumi significativi di informazioni. Gli utenti possono accedere ai dati contemporaneamente attraverso diverse interfacce, come dispositivi mobili o web. Inoltre, le applicazioni enterprise richiedono integrazione con altri sistemi aziendali e devono comunicare con diverse piattaforme. La gestione della logica aziendale complessa è fondamentale, indipendentemente dalle dimensioni del progetto, poiché anche le soluzioni più piccole possono avere un impatto significativo sull'efficienza aziendale.

### Applicazioni Enterprise: Esempi

| Esempi di applicazioni enterprise | Esempi di applicazioni non enterprise |
|----------|----------|
| Pagamenti del personale | Processamento di testo |
| Gestione pazienti | Sistemi operativi |
| Gestione delle spedizioni | Compilatori |
| Assicurazioni | Giochi |

### Persistenza dei dati

La persistenza a lungo termine dei dati è una pratica comune, spesso richiedendo la memorizzazione dei dati per anni. È essenziale che i nuovi elementi informativi vengano integrati senza modificare i dati originali, mantenendo l'integrità e la coerenza delle informazioni nel tempo. Tuttavia, è importante considerare che la durata dei dati può superare quella del software sviluppato per gestirli. In queste circostanze, diventa necessario pianificare e condurre migrazioni e integrazioni dei dati nel nuovo software per garantire la continuità delle operazioni aziendali e la disponibilità delle informazioni storiche.

### Grossa quantità di dati

Anche se alcuni sistemi possono avere un numero limitato di utenti e una quantità modesta di dati da gestire, come nel caso delle applicazioni per piccole e medie imprese, è comune che la quantità di dati da memorizzare sia considerevole, con milioni o addirittura miliardi di tuple nei database. La scelta tra l'uso di database relazionali o NoSQL dipende dalle esigenze specifiche dell'applicazione in fase di sviluppo. Entrambi i tipi di database offrono vantaggi e svantaggi, e la decisione finale dipende dalla struttura dei dati, dalle prestazioni richieste e dalle operazioni di lettura/scrittura previste.

### Concorrenza

Le applicazioni enterprise, indipendentemente dalle dimensioni dell'azienda, devono affrontare il challenge dell'accesso concorrente ai dati. Anche nelle piccole e medie imprese, è essenziale garantire la correttezza delle azioni quando più utenti richiedono contemporaneamente una stessa risorsa. Gestire l'accesso concorrente in modo efficace assicura che le operazioni siano eseguite correttamente e che le informazioni siano mantenute coerenti e aggiornate per tutti gli utenti coinvolti.

### Diverse interfacce grafiche

Oggi, è sempre più comune che le persone accedano alle stesse informazioni utilizzando una varietà di dispositivi con caratteristiche differenti. Questi dispositivi possono variare nelle dimensioni dello schermo, come tablet, smartphone e computer, e nelle capacità dei sensori integrati, come microfono, fotocamera e GPS. Inoltre, presentano differenti capacità computazionali. Di conseguenza, le applicazioni devono essere progettate per adattarsi il più possibile a questi dispositivi, prevedendo interfacce diverse per soddisfare le esigenze di ciascuno e offrire un'esperienza utente ottimale indipendentemente dal dispositivo utilizzato.

### Integrazione con altre applicazioni enterprise

Nel contesto delle applicazioni enterprise, è raro che un sistema operi in isolamento. È comune che debba comunicare con altre applicazioni, le quali potrebbero essere sviluppate utilizzando linguaggi di programmazione diversi o tecnologie completamente differenti. Anche all'interno di un'organizzazione che adotti una singola tecnologia per tutte le sue applicazioni, possono sorgere problemi dovuti a interpretazioni varie di concetti comuni. Ad esempio, mentre una divisione universitaria potrebbe definire gli studenti come coloro attualmente iscritti a corsi triennali o magistrali, un'altra divisione potrebbe considerare studenti anche coloro che si sono laureati. Inoltre, la complessità intrinseca della logica aziendale rende la progettazione dell'applicazione un'attività complessa e soggetta a sfide.

### Tipi di applicazioni enterprise

