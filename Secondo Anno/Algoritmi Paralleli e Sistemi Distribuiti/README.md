# Algoritirmi-Paralleli-e-Sistemi-Distribuiti
https://www.mat.unical.it/informatica/AlgoritmiParalleliESistemiDistribuiti#Course_Information

## Posix

Le POSIX Threads, spesso abbreviate in Pthreads, sono un'API (Application Programming Interface) per la programmazione di thread in sistemi operativi basati su UNIX o UNIX-like. Questa interfaccia definisce un set di funzioni e chiamate di sistema che consentono agli sviluppatori di creare e gestire thread all'interno di un processo.

Ecco alcuni punti chiave sulle POSIX Threads:

1. **Thread**: Un thread rappresenta un flusso di esecuzione all'interno di un processo. I thread condividono lo stesso spazio di indirizzamento e le risorse del processo genitore, ma hanno il proprio stato di esecuzione, inclusi i registri del processore e lo stack. L'uso dei thread consente di sfruttare meglio le architetture multi-core e multi-processore per ottenere l'elaborazione parallela.

2. **API POSIX Threads**: Le Pthreads definiscono un insieme di funzioni per creare, sincronizzare e terminare thread. Queste funzioni includono la creazione di thread, la sincronizzazione tra thread con mutex (mutual exclusion), le variabili condizionali per la sincronizzazione e il coordinamento, la gestione dei thread terminati e altre operazioni relative ai thread.

3. **Sincronizzazione**: Le Pthreads forniscono meccanismi di sincronizzazione come i mutex (speroni di mutua esclusione) per garantire l'accesso sicuro alle risorse condivise tra i thread. I mutex evitano che più thread accedano contemporaneamente alle stesse risorse, prevenendo situazioni di "race condition".

4. **Variabili condizionali**: Le variabili condizionali consentono ai thread di attendere specifici eventi o condizioni prima di procedere con l'esecuzione. Possono essere utilizzate per sincronizzare l'accesso alle risorse o per l'ordinamento dei thread.

5. **Vantaggi**: L'utilizzo di Pthreads offre diversi vantaggi, tra cui l'elaborazione parallela per migliorare le prestazioni, la gestione dei carichi di lavoro concorrenti, la sincronizzazione dei thread per evitare problemi di accesso concorrente non sicuro alle risorse e l'uso efficiente delle risorse hardware.

6. **Portabilità**: Una delle caratteristiche principali delle Pthreads è la portabilità. L'API è stata progettata per essere indipendente dall'architettura e dal sistema operativo sottostante, purché sia compatibile con lo standard POSIX.

In sintesi, le POSIX Threads (Pthreads) sono un'interfaccia per la programmazione di thread in ambienti UNIX-like. Consentono agli sviluppatori di creare applicazioni multithreaded con sincronizzazione e coordinamento efficaci tra i thread.

## MPI

La libreria MPI (Message Passing Interface) è uno standard e un insieme di funzioni utilizzate per la comunicazione e la programmazione parallela su sistemi distribuiti o con architetture a molti nodi. MPI è spesso impiegato in applicazioni di calcolo ad alte prestazioni (HPC) per sfruttare le risorse di cluster di computer o di supercomputer.

Ecco alcuni punti chiave riguardo alla libreria MPI:

1. **Comunicazione tra processi**: MPI fornisce un'ampia gamma di funzioni per la comunicazione tra i processi. I processi possono scambiare messaggi, dati e informazioni attraverso queste funzioni. Questo consente di sincronizzare e coordinare l'elaborazione tra i nodi di un cluster.

2. **Modello di programmazione a messaggi**: MPI segue un modello di programmazione a messaggi, in cui i processi comunicano tra loro inviando e ricevendo messaggi. Ciò permette di creare applicazioni parallele in cui i processi cooperano attraverso lo scambio di dati.

3. **Operazioni collettive**: Oltre alla comunicazione punto a punto, MPI offre operazioni collettive che coinvolgono più processi. Ad esempio, le operazioni di riduzione consentono di calcolare somme, prodotti o altre aggregazioni su dati distribuiti tra i processi.

4. **Topologie**: MPI supporta la definizione di topologie di comunicazione, come griglie, anelli o comunicazione punto a punto diretta. Questo è utile per ottimizzare il routing dei messaggi in base alla disposizione fisica dei processi.

5. **Scalabilità**: MPI è progettato per offrire un alto grado di scalabilità, consentendo di eseguire applicazioni parallele su sistemi con un grande numero di nodi o processori.

6. **Portabilità**: Una caratteristica chiave di MPI è la portabilità. Gli standard MPI sono implementati su diverse piattaforme e sistemi operativi, consentendo agli sviluppatori di scrivere codice una volta e eseguirlo su una varietà di ambienti.

7. **Librerie MPI**: Ci sono diverse implementazioni della libreria MPI, tra cui Open MPI, MPICH e Intel MPI. Ogni implementazione può avere alcune differenze nel supporto delle funzionalità e nella performance.

In sintesi, MPI è un'interfaccia che consente ai processi in esecuzione su diversi nodi di comunicare e collaborare all'interno di applicazioni parallele. È ampiamente utilizzato nei campi della modellizzazione scientifica, della simulazione e di altre applicazioni che richiedono una notevole potenza di calcolo distribuito.

## Allegro 5

Allegro 5 è una libreria di programmazione grafica e multimediale utilizzata per creare applicazioni interattive, principalmente giochi e software multimediali. 
È l'ultima versione della serie di librerie Allegro. Allegro 5 fornisce una serie di funzioni e strumenti per semplificare la creazione di grafica, suono, input da tastiera e mouse e altro ancora. È spesso utilizzato per la creazione di giochi 2D e applicazioni grafiche su diverse piattaforme.

Alcune delle funzionalità principali di Allegro 5 includono:

1. **Grafica 2D**: Allegro 5 offre un'ampia gamma di funzioni per disegnare forme, immagini e testo su schermo. Supporta la gestione dei bitmap, la trasformazione delle immagini, il disegno vettoriale e altro ancora.

2. **Gestione dell'input**: La libreria gestisce input da tastiera, mouse e controller. Puoi rilevare eventi come pressioni dei tasti, movimenti del mouse e altro ancora.

3. **Suono e musica**: Allegro 5 supporta la riproduzione di suoni e la gestione della musica di sottofondo. È possibile caricare e riprodurre file audio in vari formati.

4. **Gestione del tempo**: La libreria offre funzioni per misurare il tempo e controllare gli aggiornamenti del gioco in base al tempo trascorso.

5. **Supporto multipiattaforma**: Allegro 5 è progettato per essere portabile su diverse piattaforme, compresi sistemi Windows, macOS e Linux.

6. **Gestione dei file**: Fornisce funzioni per la lettura e la scrittura di file, il caricamento di risorse multimediali e altro ancora.

7. **Gestione delle finestre**: Allegro 5 semplifica la creazione e la gestione delle finestre dell'applicazione.

In sintesi, Allegro 5 è una libreria versatile che offre un insieme di strumenti per semplificare lo sviluppo di applicazioni multimediali e giochi 2D. È spesso utilizzato da sviluppatori per creare esperienze interattive su diverse piattaforme.