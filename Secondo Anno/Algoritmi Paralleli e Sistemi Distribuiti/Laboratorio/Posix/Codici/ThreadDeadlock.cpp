#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

// thread deadlock example

int n = 1000000;

/*
In linguaggio C, la libreria pthread fornisce supporto per la gestione dei thread multipli e della sincronizzazione. 
pthread_mutex_t è un tipo di dato definito dalla libreria pthread che rappresenta una variabile di tipo mutex (mutual exclusion), 
che è utilizzata per sincronizzare l'accesso concorrente a risorse condivise tra thread diversi, 
al fine di prevenire race condition e garantire la coerenza dei dati.
*/

pthread_mutex_t mutex0;
pthread_mutex_t mutex1;

int num0 = 0;
int num1 = 0;

// Funzione eseguita dal primo thread
void* run0(void* arg) {
    for (int i = 0; i < n; i++) {
        pthread_mutex_lock(&mutex1);  // Acquisisce mutex1
        sleep(1);  // Simula un ritardo per evidenziare il deadlock
        pthread_mutex_lock(&mutex0);  // Tenta di acquisire mutex0 (possibile stallo)

        num0++;
        num1--;
        printf("num1 --> %d\n", num1);

        pthread_mutex_unlock(&mutex0);  // Rilascia mutex0
        pthread_mutex_unlock(&mutex1);  // Rilascia mutex1
    }
    return NULL;
}

// Funzione eseguita dal secondo thread
void* run1(void* arg) {
    for (int i = 0; i < n; i++) {
        pthread_mutex_lock(&mutex1);  // Acquisisce mutex1 (possibile stallo)
        sleep(1);  // Simula un ritardo per evidenziare il deadlock
        pthread_mutex_lock(&mutex0);  // Tenta di acquisire mutex0

        num0--;
        num1++;
        printf("num0 --> %d\n", num0);

        pthread_mutex_unlock(&mutex0);  // Rilascia mutex0
        pthread_mutex_unlock(&mutex1);  // Rilascia mutex1
    }
    return NULL;
}

int main(int argc, char* argv[]) {
    pthread_t thid0, thid1;
    pthread_mutex_init(&mutex0, NULL);
    pthread_mutex_init(&mutex1, NULL);

    // Creazione dei thread
    int ris = pthread_create(&thid0, NULL, &run0, NULL);
    if (ris) {
        printf("Errore durante la creazione del thread\n");
        exit(-1);
    }
    ris = pthread_create(&thid1, NULL, &run1, NULL);
    if (ris) {
        printf("Errore durante la creazione del thread\n");
        exit(-1);
    }

    // Attesa dei thread
    pthread_join(thid0, NULL);
    pthread_join(thid1, NULL);

    // Distruzione delle mutex
    pthread_mutex_destroy(&mutex0);
    pthread_mutex_destroy(&mutex1);
    
    return 0;  // Termina il programma con successo
}
