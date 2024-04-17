#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

// Funzione che verrà eseguita nel nuovo thread
void* run(void* arg) {
    printf("ciao\n");
    return NULL;
}

int main(int argc, char* argv[]) {
    pthread_t thid;     // Variabile per l'ID del nuovo thread

    // Creazione di un nuovo thread
    int result = pthread_create(&thid, NULL, &run, NULL);
    if (result != 0) {
        printf("Errore durante la creazione del thread\n");
        exit(-1);       // Termina il programma in caso di errore
    }

    // Attende che il nuovo thread termini
    pthread_join(thid, NULL);

    return 0;   // Termina il programma con successo
}
