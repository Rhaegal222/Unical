#ifndef __INIT__H__
#define __INIT__H__

#include "golfunctions.h"

// Distribuzione delle righe e delle colonne tra le partizioni
void distributeRowsAndCols(int total, int numPartitions, int* partitionSizes) {
    int resto = total % numPartitions; // Numero di righe o colonne che non possono essere divise equamente tra le partizioni
    for (int i = 0; i < numPartitions; i++) {
        partitionSizes[i] = total / numPartitions; // Assegna a ciascuna partizione un numero di righe o colonne
        if (resto > 0) {
            partitionSizes[i]++; // Se il resto è maggiore di 0, assegna una riga o colonna in più alla partizione
            resto--; // Decrementa il resto
        }
    }
}

// Calcola la somma delle partizioni
int sumPartitions(int start, int numPartitions, int* partitionSizes) {
    int sum = 0;
    for (int i = 0; i < numPartitions; i++) // Itera sul numeri di partizioni
        sum += partitionSizes[start + i]; // partitionSizes[start + i] restituisce il numero di celle della partizione
    return sum; // Restituisce la dimensione totale della sottomatrice
}

// Inizializza le dimensioni delle partizioni
void initAllPartitions() {

    nRowsPerPartition = new int[nPartY]; // Quante righe di celle per ogni partizione
    nColsPerPartition = new int[nPartX]; // Quante colonne di celle per ogni partizione
	
    /* 
    Trova un divisore comune (i) per nThreads e nPartX o nThreads e nPartY 
    (in base alla formula size * nThreads = nPartX * nPartY si sa che ne esiste sempre uno)
	Decide COME suddividere la matrice totale tra i processi (quali sottomatrici assegnare a ciascun processo)
    */
    for (int i = nThreads; i > 0; i--) {
        if ((nThreads % i == 0) && (nPartX % i == 0)) { // Se i è un divisore comune di nThreads e nPartX
            nPartYPerProc = nThreads / i; // Assegna il numero di partizioni per processo lungo l'asse Y
            nPartXPerProc = i; // Assegna il numero di partizioni per processo lungo l'asse X
            break;
        } else if ((nThreads % i == 0) && (nPartY % i == 0)) { // Se i è un divisore comune di nThreads e nPartY
            nPartYPerProc = i; // Assegna il numero di partizioni per processo lungo l'asse Y
            nPartXPerProc = nThreads / i; // Assegna il numero di partizioni per processo lungo l'asse X
            break;
        } 
	}

	// Distribuisce le righe e le colonne tra le partizioni
    distributeRowsAndCols(totRows, nPartY, nRowsPerPartition);
    distributeRowsAndCols(totCols, nPartX, nColsPerPartition);

    nProcOnX = nPartX / nPartXPerProc; // Calcola il numero di processi lungo l'asse X

    rankX = rank % nProcOnX; // Calcola il rank del processo corrente lungo l'asse X
    rankY = rank / nProcOnX; // Calcola il rank del processo corrente lungo l'asse Y

    // Calcola le dimensioni della sottomatrice per il processo corrente
    nRowsThisRank = sumPartitions(rankY * nPartYPerProc, nPartYPerProc, nRowsPerPartition);
    nColsThisRank = sumPartitions(rankX * nPartXPerProc, nPartXPerProc, nColsPerPartition);

    // Inizializza matrici di lettura e scrittura
    readM = new int[(nRowsThisRank + 2) * (nColsThisRank + 2)]; //+2 perchè si considerano le halo cells
    writeM = new int[(nRowsThisRank + 2) * (nColsThisRank + 2)];
}

// Calcola il rank dei processi adiacenti (sopra, sotto, sinistra, destra, diagonali) applicando la regola di Moore
void calculateMooreNeighbourhood(){
    rankUp = ((rank - nProcOnX + size) % size);
    rankDown = ((rank + nProcOnX) % size);
    rankLeft = ((rank - 1 + nProcOnX) % nProcOnX) + (rank / nProcOnX) * nProcOnX;
    rankRight = ((rank + 1) % nProcOnX) + (rank / nProcOnX) * nProcOnX;
    rankUpLeft = ((rankUp - 1 + nProcOnX) % nProcOnX) + (rankUp / nProcOnX) * nProcOnX;
    rankUpRight = ((rankUp + 1) % nProcOnX) + (rankUp / nProcOnX) * nProcOnX;
    rankDownLeft = ((rankDown - 1 + nProcOnX) % nProcOnX) + (rankDown / nProcOnX) * nProcOnX;
    rankDownRight = ((rankDown + 1) % nProcOnX) + (rankDown / nProcOnX) * nProcOnX;
}

// Per ogni processo, calcola la posizione di inizio della sottomatrice e la dimensione della sottomatrice
void initArrays(){
	startColPerProc = new int[size];
	startRowPerProc = new int[size];
	vecRowSizePerProc = new int[size];
	vecColSizePerProc = new int[size];
}

// Inizializza le barriere
void initBarriers(){ 
	// Inizializza la barriera per la comunicazione
	contComunicationBarrier = 0;
	pthread_mutex_init(&mutexComunicationBarrier, NULL);

	// Inizializza la barriera per la sincronizzazione e far in modo che tutti i thread abbiano completato il passo corrente
    contReadyBarrier = 0;
	pthread_mutex_init(&mutexReadyBarrier, NULL);
    
	// Inizializza le condizioni per le barriere
    pthread_cond_init(&condComunicationBarrier, NULL);
    pthread_cond_init(&condReadyBarrier, NULL);
}

void handleBarrier(pthread_mutex_t* mutex, int* counter, pthread_cond_t* condition) {
    pthread_mutex_lock(mutex);
    (*counter)++;
    if(*counter < nThreads){
        pthread_cond_wait(condition, mutex);
    }
    *counter = 0;
    pthread_cond_broadcast(condition);
    pthread_mutex_unlock(mutex);
}
void completedBarrier(){ 
    handleBarrier(&mutexReadyBarrier, &contReadyBarrier, &condReadyBarrier);
}
void comunicationBarrier(){ 
    handleBarrier(&mutexComunicationBarrier, &contComunicationBarrier, &condComunicationBarrier);
}
void destroyBarriers(){
	pthread_mutex_destroy(&mutexComunicationBarrier);
	pthread_mutex_destroy(&mutexReadyBarrier);
}
void destroyConditions(){ 
	pthread_cond_destroy(&condComunicationBarrier);
	pthread_cond_destroy(&condReadyBarrier);
}
void destroy(){
	destroyBarriers();
	destroyConditions();
}

void * runThread(void * arg){
	int tid = *(int *)arg;
	int tidX = tid % nPartXPerProc; // Calcola la posizione del thread lungo l'asse X
	int tidY = tid / nPartXPerProc; // Calcola la posizione del thread lungo l'asse Y
	int partXPrevious = rankX * nPartXPerProc + tidX; // Calcola la partizione precedente lungo l'asse X
	int partYPrevious = rankY * nPartYPerProc + tidY; // Calcola la partizione precedente lungo l'asse Y
	int beginThreadX = 1; // Assegna la posizione di inizio del thread lungo l'asse X (escludendo le halo cells --> 0)
	int beginThreadY = 1; // Assegna la posizione di inizio del thread lungo l'asse Y (escludendo le halo cells --> 0)

    // Calcola la posizione di inizio del thread lungo l'asse X
	for(int j = rankX * nPartXPerProc; j<partXPrevious; ++j) beginThreadX += nColsPerPartition[j];
    
    // Calcola la posizione di inizio del thread lungo l'asse Y
	for(int i = rankY * nPartYPerProc; i<partYPrevious; ++i) beginThreadY += nRowsPerPartition[i];

    // Esegue la funzione di trasformazione per il numero di passi specificato
    for(int s = 0; s < steps; s++){
        /*
        Sinconizzazione dei thread per assicurarsi che tutti abbiano ricevuto i dati corretti prima di procedere.
        Mentre i thread vengono creati e eseguono la loro funzione, il main thread è andato avanti nel main e sta facendo la exchangeBorders, perciò c'è bisogno di una barriera di comunicazione.
        */
        comunicationBarrier();
		execTransFunc(beginThreadX, beginThreadY, nColsPerPartition[partXPrevious], nRowsPerPartition[partYPrevious]); // Esegue la funzione di transizione
        completedBarrier(); // Aspetta che tutti i thread abbiano completato il passo corrente prima di procedere al passo successivo
    }
    return NULL;
}

void initializeThreads(){
    vecThreads = new pthread_t[nThreads]; 
    for(int i=1;i<nThreads;i++){  // Parto da 1 perchè il main thread è lo 0
        /*
        Se il numero di thread totali è 8, allora il main thread è il rank 0 e i thread creati da me sono da 1 a 7.
        Nel frattempo, il main thread fa la sua parte.
        */
        int * tid = new int(i); // Creo un puntatore ad un intero e gli assegno il valore i (il rank del thread)
        pthread_create(&vecThreads[i], NULL, runThread, (void *) tid); // Creo un thread e gli passo il puntatore all'intero
    }
}

void createDatatype(){
	MPI_Type_vector(nRowsThisRank+2, 1, nColsThisRank+2, MPI_INT, &typeColumn); 
	MPI_Type_vector(nRowsThisRank, nColsThisRank, nColsThisRank+2, MPI_INT, &typeMatWithoutHalos);
	MPI_Type_commit(&typeColumn);
	MPI_Type_commit(&typeMatWithoutHalos);
}

void freeDatatype(){
	MPI_Type_free(&typeColumn);
	MPI_Type_free(&typeMatWithoutHalos);
}
#endif //!__INIT__H__