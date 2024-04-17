/*
Dato un array in memoria (variabile globale) di dimensione N dividere l'operazione 
di somma degli elementi dell'array equamente tra un numero T di thread.
*/

#include <stdio.h>
#include <pthread.h>

#define N 99999999 // Dimensione dell'array
#define T 4         // Numero di thread

pthread_mutex_t mutex;

int array[N];
int result[T] = {0}; // Un array per immagazzinare i risultati parziali
int R = 0;

// Funzione che calcola la somma degli elementi in un intervallo specifico
void* sum_array(void* arg) {
    int thread_id = *((int*)arg);
    int start = thread_id * (N / T); // Calcola l'inizio dell'intervallo
    int end = (thread_id == (T - 1)) ? N : (thread_id + 1) * (N / T); // Calcola la fine dell'intervallo

    int sum = 0;
    for (int i = start; i < end; i++) {
        sum += array[i];
    }
    result[thread_id] = sum; // Memorizza il risultato parziale nella posizione corrispondente

    pthread_exit(NULL);
}

int main() {
    pthread_t threads[T];
    int thread_ids[T];

    // Inizializza l'array con dati di esempio
    for (int i = 0; i < N; i++) {
        array[i] = i + 1;
    }

    // Creazione dei thread
    for (int i = 0; i < T; i++) {
        thread_ids[i] = i;
        pthread_create(&threads[i], NULL, sum_array, &thread_ids[i]);
    }

    // Attendere la terminazione dei thread
    for (int i = 0; i < T; i++) {
        pthread_join(threads[i], NULL);
    }

    // Calcola la somma totale sommando i risultati parziali
    int total_sum = 0;
    for (int i = 0; i < T; i++) {
        total_sum += result[i];
    }

    printf("La somma totale degli elementi dell'array è %d\n", total_sum);

    return 0;
}
