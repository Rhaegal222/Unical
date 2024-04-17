#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

pthread_mutex_t mutex;    // Mutex per proteggere le risorse condivise
pthread_cond_t condFull;  // Variabile di condizione per la piena del buffer
pthread_cond_t condEmpty; // Variabile di condizione per l'empty del buffer

const int NUM_CONSUMER = 5;  // Numero di consumatori
const int NUM_PRODUCER = 2;  // Numero di produttori
const int DIM_BUFFER = 10;    // Dimensione del buffer condiviso

int buffer[DIM_BUFFER];  // Buffer condiviso
int head = 0;            // Puntatore alla prossima posizione libera nel buffer

// Funzione per la produzione di dati
void* produce(void* arg) {
    while (true) {
        sleep(1);
        pthread_mutex_lock(&mutex);

        // Attendi finché il buffer è pieno
        while (head >= DIM_BUFFER) {
            pthread_cond_wait(&condFull, &mutex);
        }

        int num = rand() % 100;
        buffer[head] = num;
        head++;
        printf("produce: %d\n", num);

        pthread_mutex_unlock(&mutex);
        pthread_cond_broadcast(&condEmpty); // Segnala ai consumatori che il buffer non è vuoto
    }
    return NULL;
}

// Funzione per il consumo di dati
void* consume(void* arg) {
    while (true) {
        sleep(1);
        pthread_mutex_lock(&mutex);

        // Attendi finché il buffer è vuoto
        while (head == 0) {
            pthread_cond_wait(&condEmpty, &mutex);
        }

        int num = buffer[head - 1];
        head--;
        printf("head: %d consume: %d\n", head, num);

        pthread_mutex_unlock(&mutex);
        pthread_cond_broadcast(&condFull); // Segnala ai produttori che il buffer non è pieno
    }
    return NULL;
}

int main(int argc, char* argv[]) {
    pthread_t thC[NUM_CONSUMER];  // Array di thread consumatori
    pthread_t thP[NUM_PRODUCER];  // Array di thread produttori

    // Inizializza mutex e variabili di condizione
    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&condFull, NULL);
    pthread_cond_init(&condEmpty, NULL);

    // Crea thread consumatori
    for (int i = 0; i < NUM_CONSUMER; i++) {
        if (pthread_create(&thC[i], NULL, &consume, NULL) != 0) {
            perror("Failed to create thread");
        }
    }

    // Crea thread produttori
    for (int i = 0; i < NUM_PRODUCER; i++) {
        if (pthread_create(&thP[i], NULL, &produce, NULL) != 0) {
            perror("Failed to create thread");
        }
    }

    // Attendere la terminazione dei thread consumatori
    for (int i = 0; i < NUM_CONSUMER; i++) {
        if (pthread_join(thC[i], NULL) != 0) {
            perror("Failed to join thread");
        }
    }

    // Attendere la terminazione dei thread produttori
    for (int i = 0; i < NUM_PRODUCER; i++) {
        if (pthread_join(thP[i], NULL) != 0) {
            perror("Failed to join thread");
        }
    }

    // Distruggere mutex e variabili di condizione
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&condFull);
    pthread_cond_destroy(&condEmpty);

    return 0;
}
