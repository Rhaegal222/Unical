La creazione di una piattaforma per l'esecuzione parallela di modelli ad automi cellulari che sfrutta sia MPI (Message Passing Interface) per la comunicazione tra nodi distribuiti che i thread POSIX per la parallelizzazione locale richiede un'implementazione complessa. Di seguito, fornirò una panoramica generale su come si potrebbe affrontare questo problema, ma tenga presente che l'implementazione dettagliata richiederebbe una pianificazione, progettazione e sviluppo significativi.

1. **Definizione del dominio**: Innanzitutto, è necessario definire la griglia bidimensionale in cui verranno eseguiti gli automi cellulari. Questo dominio può essere partizionato in una griglia di celle, ciascuna gestita da un processo MPI. Inoltre, ogni cella potrebbe essere manipolata da un thread POSIX separato.

2. **Inizializzazione**: Inizializzare la griglia con valori iniziali per ogni cella. Questo può essere fatto all'inizio del programma o in modo distribuito tra i processi MPI, a seconda della dimensione della griglia.

3. **Ciclo temporale**: Eseguire il modello ad automa cellulare iterativamente in un ciclo temporale. In ogni passo del ciclo temporale, eseguire i seguenti passaggi:

   a. **Calcolo locale**: Ogni thread POSIX (uno per ogni cella) esegue la funzione di transizione `transitionFunction` per le celle di sua competenza.

   b. **Comunicazione tra processi MPI**: Dopo che ogni thread ha completato il calcolo locale, è necessario sincronizzare i risultati tra i processi MPI. Questo può essere fatto utilizzando le primitive di comunicazione di MPI come `MPI_Send` e `MPI_Recv`.

   c. **Aggiornamento globale**: Dopo la sincronizzazione, aggiornare il valore di ogni cella basato sui risultati dei calcoli locali e sulle comunicazioni tra i processi MPI.

   d. **Visualizzazione**: Aggiornare la visualizzazione in Allegro per riflettere lo stato corrente della griglia.

4. **Terminazione**: Ripetere il ciclo temporale fino a quando si raggiunge una condizione di terminazione specifica.

5. **Gestione della memoria**: Assicurarsi di gestire correttamente la memoria condivisa tra i thread POSIX e la memoria distribuita tra i processi MPI per evitare conflitti e problemi di sincronizzazione.

6. **Visualizzazione in Allegro**: Implementare un visualizzatore Allegro che possa rappresentare istantaneamente lo stato corrente della griglia ad ogni passo del ciclo temporale.

7. **Parallelizzazione**: Utilizzare le librerie MPI e POSIX Threads per la gestione della concorrenza e della comunicazione tra i processi e i thread.

8. **Gestione degli input utente**: Consentire all'utente di specificare i parametri iniziali del modello ad automa cellulare e di interagire con il visualizzatore durante l'esecuzione.

9. **Gestione degli errori**: Implementare la gestione degli errori e il rilevamento delle condizioni di terminazione.

Questo è solo un'idea generale su come affrontare il problema. L'implementazione specifica richiederebbe un'attenta pianificazione e programmazione dettagliata. È importante tenere presente che il bilanciamento del carico, la sincronizzazione tra i processi e i thread e la gestione della memoria sono aspetti critici per il successo di un sistema del genere.

## NOTE

- Leggere la matrice e salvarla
- Leggere il file di configurazione
- Processo 0 legge il file di configurazione e assegna la porzione di matrice al procio
  - gestire il parizionamento
- La cosa brutta sono i Thread hai vasta scelta chiedere a Spataro come gestire i Thread
  - Piú processi
  - Ogni processo ha diversi thread
- I Thread comunicano tra solo tipo send/recive
- Gli esempi li trovi i Game Of Life di Spataro