#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <chrono>
#include <iostream>

// Funzione eseguita dal thread secondario
void* run(void* arg) {
    int* p = (int*)arg; // Converti l'argomento in un puntatore a int
    sleep(1); // Il thread secondario aspetta per 1 secondo
    sleep(4 - (*p)); // Il thread secondario aspetta ulteriormente, inversamente proporzionale al valore di 'i'
    return NULL; // Restituisci NULL quando la funzione termina
}

int main(int argc, char* argv[]) {
    auto start_time = std::chrono::high_resolution_clock::now(); // Ottieni il tempo di inizio

    pthread_t thid; // Variabile per rappresentare il thread secondario
    int i = 1; // Inizializza una variabile intera 'i' a 1

    pthread_create(&thid, NULL, &run, &i); // Crea un thread secondario che eseguirà la funzione 'run' e passa l'indirizzo di 'i' come argomento

    sleep(1); // Il thread principale aspetta per 1 secondo
    i++; // Incrementa 'i'
    sleep(i); // Il thread principale aspetta ulteriormente per un periodo di tempo uguale al valore di 'i'

    pthread_join(thid, NULL); // Aspetta che il thread secondario termini prima di continuare

    return 0;
}
