#include <stdio.h>
#include <pthread.h>
#include <chrono>

#define N 99999999 // Dimensione dell'array
#define T 8        // Numero di thread

pthread_mutex_t mutex;

int array[N];
int R = 0;

// Funzione che calcola la somma degli elementi in un intervallo specifico
void* sum_array(void* arg) {
    // Misura il tempo di inizio
    auto start = std::chrono::high_resolution_clock::now();

    // Estrai l'ID del thread dalla variabile argomento
    int thread_id = *((int*)arg);

    // Inizializza la somma parziale per il thread corrente
    int partial_sum = 0;

    // Calcola la dimensione della porzione dell'array per ciascun thread
    int chunk_size = N / T;
    int start_index = thread_id * chunk_size;
    int end_index = (thread_id == T - 1) ? N : start_index + chunk_size;

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

    // Calcola la differenza di tempo
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

    // Stampa il tempo di esecuzione per il thread corrente
    printf("Tempo di esecuzione per il thread %d: %ld millisecondi\n", thread_id, duration.count());

    // Restituisci NULL
    return NULL;
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();
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

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    printf("Tempo di esecuzione complessivo: %ld millisecondi\n", duration.count());

    return 0;
}
