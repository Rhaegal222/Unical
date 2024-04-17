#include <stdio.h>
#include <string.h>
#include "mpi.h"

int main(int argc, char** argv) {
    int my_rank;            /* Il rango del processo */
    int rank_x_10;          /* Il rango del processo moltiplicato per 10 */
    int received_rank_x_10; /* Il rango del processo ricevuto moltiplicato per 10 */
    int p;                  /* Il numero di processi */
    int source;             /* Il rango del mittente */
    int dest;               /* Il rango del destinatario */
    int tag = 0;            /* Etichetta per i messaggi */

    MPI_Status status;      /* Status di ritorno per le operazioni MPI */
    MPI_Request request;    /* Richiesta per le operazioni di ricezione asincrona */

    printf("Questo programma è bello\n"); /* Stampa un messaggio */

    MPI_Init(&argc, &argv); /* Inizializza l'ambiente MPI */
    
    MPI_Comm_size(MPI_COMM_WORLD, &p);  /* Ottieni il numero totale di processi */
    
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank); /* Ottieni il rango del processo corrente */

    if (my_rank != 0) {   // Processi non zero (slave)
        /* Crea un messaggio contenente il proprio rango moltiplicato per 10 */
        dest = 0; // Il destinatario è il processo con rango 0 (master)
        rank_x_10 = my_rank * 10;
        MPI_Send(&rank_x_10, 1, MPI_INT, dest, tag, MPI_COMM_WORLD); // Invia il messaggio
        rank_x_10 = 666; // Modifica il valore locale
    } else { /* my_rank == 0 (master) */
        for (source = 1; source < p; source++) {
            /* Ricevi il messaggio dai processi non zero (slaves) */
            MPI_Recv(&received_rank_x_10, 1, MPI_INT, source, tag, MPI_COMM_WORLD, &status);
            printf("Received %d rank10 from source %d\n", received_rank_x_10, status.MPI_SOURCE);
        }
    }
    
    /* Termina l'ambiente MPI */
    MPI_Finalize();
    
    return 0;
}
