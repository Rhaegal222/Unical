#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

// Definizione di una mutex
pthread_mutex_t mutex;

// Numero di iterazioni nei thread
int n = 100000;

// Variabile condivisa tra i thread
int num = 0;

// Funzione eseguita dai thread
void* run(void* arg) {
    for (int i = 0; i < n; i++) {
        pthread_mutex_lock(&mutex); // Acquisizione della mutex per evitare race condition
        num++;  // Modifica della variabile condivisa
        pthread_mutex_unlock(&mutex); // Rilascio della mutex
    }
    return NULL;
}

int main(int arg, char* argv[]) {
    pthread_t thid0, thid1;

    // Inizializzazione della mutex
    pthread_mutex_init(&mutex, NULL);

    // Creazione dei due thread
    int ris = pthread_create(&thid0, NULL, &run, NULL);
    if (ris) {
        printf("errore creazione thread\n");
        exit(-1);
    }
    ris = pthread_create(&thid1, NULL, &run, NULL);
    if (ris) {
        printf("errore creazione thread\n");
        exit(-1);
    }

    // Attesa del termine dei thread
    pthread_join(thid0, NULL);
    pthread_join(thid1, NULL);

    // Distruzione della mutex
    pthread_mutex_destroy(&mutex);

    // Stampa del valore della variabile condivisa
    printf("num=%d\n", num);

    return 0; // Termina il programma con successo
}
