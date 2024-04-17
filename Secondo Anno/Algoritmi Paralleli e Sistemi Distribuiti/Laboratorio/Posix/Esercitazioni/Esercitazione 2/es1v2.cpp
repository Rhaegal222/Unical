#include <stdio.h>
#include <pthread.h>
#include <chrono>

#define N 99999999 // Dimensione dell'array
#define T 6        // Numero di thread

pthread_mutex_t mutex;

int array[N];
int result[T] = {0}; // Un array per immagazzinare i risultati parziali
int R = 0;

// Funzione che calcola la somma degli elementi in un intervallo specifico
void* sum_array(void* arg) {
    // Estrai l'ID del thread dalla variabile argomento
    int thread_id = *((int*)arg);

    // Calcola quanti elementi ciascun thread deve sommare
    int elements_for_thread = N / T;

    // Calcola l'indice di inizio dell'intervallo per il thread corrente
    int start_index = thread_id * elements_for_thread;

    // Calcola l'indice di fine dell'intervallo per il thread corrente
    int end_index = (thread_id == T - 1) ? N : (start_index + elements_for_thread);

    // Inizializza la somma parziale per il thread corrente
    int partial_sum = 0;

    // Effettua la somma degli elementi nell'intervallo assegnato al thread
    for (int i = start_index; i < end_index; i++) {
        partial_sum += array[i];
    }

    // Blocca il mutex prima di aggiornare la variabile condivisa R
    pthread_mutex_lock(&mutex);

    // Aggiorna la variabile condivisa R con la somma parziale
    R += partial_sum;

    // Rilascia il mutex
    pthread_mutex_unlock(&mutex);

    // Misura il tempo di fine
    auto end = std::chrono::high_resolution_clock::now();

    // Calcola la differenza di tempo in millisecondi
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    // Stampa il tempo di esecuzione per il thread corrente
    printf("Tempo di esecuzione per il thread %d: %lld millisecondi\n", thread_id, duration.count());

    // Restituisci NULL
    return NULL;
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

    printf("La somma totale degli elementi dell'array è %d\n", R);

    return 0;
}
