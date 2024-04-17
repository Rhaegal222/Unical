#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

// Definizione delle mutex e delle condition variable
pthread_mutex_t mutexFuel;
pthread_cond_t condFuel;

int fuel = 0;

// Thread che rifornisce il carburante
void* fuel_filling(void* arg) {
    for (int i = 0; i < 5; i++) {
        pthread_mutex_lock(&mutexFuel); // Acquisizione della mutex
        fuel += 30;
        printf("Filled fuel... %d\n", fuel);
        pthread_mutex_unlock(&mutexFuel); // Rilascio della mutex
        pthread_cond_broadcast(&condFuel); // Invia un segnale a tutti i thread in attesa sulla condition variable
        sleep(1);
    }
    return NULL;
}

// Thread dell'auto
void* car(void* arg) {
    pthread_mutex_lock(&mutexFuel); // Acquisizione della mutex
    while (fuel < 40) {
        printf("No fuel. Waiting...\n");
        pthread_cond_wait(&condFuel, &mutexFuel); // Attende il segnale sulla condition variable e rilascia temporaneamente la mutex
    }
    fuel -= 40;
    printf("Got fuel. Now left: %d\n", fuel);
    pthread_mutex_unlock(&mutexFuel); // Rilascio della mutex
    return NULL;
}

int main(int argc, char* argv[]) {
    pthread_t th[6];
    pthread_mutex_init(&mutexFuel, NULL);
    pthread_cond_init(&condFuel, NULL);

    // Creazione dei thread
    for (int i = 0; i < 6; i++) {
        if (i == 4 || i == 5) {
            if (pthread_create(&th[i], NULL, &fuel_filling, NULL) != 0) {
                perror("Failed to create thread");
            }
        } else {
            if (pthread_create(&th[i], NULL, &car, NULL) != 0) {
                perror("Failed to create thread");
            }
        }
    }

    // Attesa del termine dei thread
    for (int i = 0; i < 6; i++) {
        if (pthread_join(th[i], NULL) != 0) {
            perror("Failed to join thread");
        }
    }

    pthread_mutex_destroy(&mutexFuel);
    pthread_cond_destroy(&condFuel);

    return 0; // Termina il programma con successo
}
