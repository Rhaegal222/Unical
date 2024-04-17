#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

// Definizione di una funzione eseguita dai thread
void* run(void* arg) {
    printf("start thread\n"); // Messaggio di inizio del thread
    sleep(3); // Il thread aspetta per 3 secondi (simulando un'attività)
    printf("end thread\n"); // Messaggio di fine del thread
    return NULL;
}

int main(int arg, char* argv[]) {
    pthread_t thid0, thid1;

    // Creazione del primo thread
    int ris = pthread_create(&thid0, NULL, &run, NULL);
    if (ris) {
        printf("errore creazione thread\n");
        exit(-1);
    }

    // Creazione del secondo thread
    ris = pthread_create(&thid1, NULL, &run, NULL);
    if (ris) {
        printf("errore creazione thread\n");
        exit(-1);
    }

    // Attesa del termine dei thread
    pthread_join(thid0, NULL);
    pthread_join(thid1, NULL);

    return 0; // Termina il programma con successo
}
