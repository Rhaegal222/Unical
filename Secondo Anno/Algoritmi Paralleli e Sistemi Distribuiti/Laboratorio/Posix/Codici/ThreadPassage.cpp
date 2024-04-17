#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

// Definizione del numero di thread
int numThreads = 10;

// Funzione eseguita dai thread
void* run(void* arg) {
    sleep(1);  // Attendiamo per simulare un ritardo
    int i = *(int*)arg;  // Casting dell'argomento a int per ottenere il valore di i
    printf("i=%d\n", i);
    delete (int*)arg;  // Deallocazione della memoria dinamica
    return NULL;
}

int main(int arg, char* argv[]) {
    pthread_t thid[10];

    // Creazione e avvio dei thread
    for (int i = 0; i < numThreads; i++) {
        int* p = new int;  // Allocazione dinamica di un intero (pointer)
        *p = i;  // Assegnazione del valore di i all'intero puntato da p
        int ris = pthread_create(&thid[i], NULL, &run, p);  // Creazione del thread con l'argomento p
        if (ris) {
            printf("errore creazione thread\n");
            exit(-1);
        }
    }

    // Attesa del termine dei thread
    for (int i = 0; i < numThreads; i++)
        pthread_join(thid[i], NULL);
        
    return 0;
}
