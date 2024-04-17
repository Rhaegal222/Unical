#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

// Dichiarazione delle variabili globali
pthread_mutex_t mutex;  // Mutex per proteggere le variabili condivise
pthread_cond_t cond;    // Variabile di condizione per la sincronizzazione
int nThread = 5;        // Numero totale di thread
int nJoined = 0;        // Numero di thread che hanno raggiunto la barriera

// Inizializza la barriera
void initBarrier() {
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&cond, NULL);
}

// Funzione di barriera personalizzata
void barrier() {
    pthread_mutex_lock(&mutex);
    nJoined++;  // Incrementa il numero di thread che hanno raggiunto la barriera
    
    // Attendi finché tutti i thread non hanno raggiunto la barriera
    while (nJoined < nThread) {
        pthread_cond_wait(&cond, &mutex);  // Attendi sulla variabile di condizione
    }
    
    pthread_mutex_unlock(&mutex);         // Sblocca il mutex
    pthread_cond_broadcast(&cond);        // Invia un segnale a tutti i thread in attesa
}

// Distruggi la barriera e rilascia le risorse
void destroyBarrier() {
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond);
}

// Funzione eseguita da ogni thread
void* start(void* arg) {
    printf("inizio\n");
    barrier();  // Punto di sincronizzazione
    printf("fine\n");
    return NULL;
}

int main(int argc, char* argv[]) {
    pthread_t th[nThread];  // Array di thread
    initBarrier();          // Inizializza la barriera
    
    // Crea i thread
    for (int i = 0; i < nThread; i++) {
        pthread_create(&th[i], NULL, &start, NULL);
    }
    
    // Attendi che tutti i thread terminino
    for (int i = 0; i < nThread; i++) {
        pthread_join(th[i], NULL);
    }
    
    destroyBarrier();  // Distruggi la barriera
    
    return 0;
}
