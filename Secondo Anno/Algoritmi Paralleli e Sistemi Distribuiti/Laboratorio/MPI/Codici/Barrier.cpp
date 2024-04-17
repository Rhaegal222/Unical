#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define maxsize 3000

MPI_Request send_reqs[maxsize], recv_reqs[maxsize];
MPI_Status send_statuses[maxsize], recv_statuses[maxsize];
int cont, send_buffer[maxsize], recv_buffer[maxsize];

void barrier(int rank, int size) {
    cont++;

    // Invia token a tutti gli altri processi
    for (int dest = 0; dest < size; dest++) {
        if (dest != rank) {
            MPI_Isend(&send_buffer[0], 1, MPI_INT, dest, cont, MPI_COMM_WORLD, &send_reqs[dest]);
        }
    }

    // Ricevi token da tutti gli altri processi
    for (int src = 0; src < size; src++) {
        if (src != rank) {
            MPI_Irecv(&recv_buffer[src], 1, MPI_INT, src, cont, MPI_COMM_WORLD, &recv_reqs[src]);
        }
    }

    // Attendi tutte le comunicazioni
    for (int dest = 0; dest < size; dest++) {
        if (dest != rank) {
            MPI_Wait(&send_reqs[dest], &send_statuses[dest]);
            MPI_Wait(&recv_reqs[dest], &recv_statuses[dest]);
        }
    }
}

int main(int argc, char *argv[]) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // Chiamata alla barriera personalizzata
    printf("Process %d: Before Barrier\n", rank);
    barrier(rank, size);
    printf("Process %d: After Barrier\n", rank);

    MPI_Finalize();
    return 0;
}
