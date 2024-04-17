#include <omp.h>        // Includi la libreria OpenMP
#include <stdio.h>      // Includi la libreria standard di input/output
#include <stdlib.h>     // Includi la libreria standard di utilità

int main(int argc, char *argv[]) {
    int nthreads, tid, procs, maxt, inpar, dynamic, nested;
    
    /* Inizia la regione parallela */
    #pragma omp parallel private(nthreads, tid) 
    {
        
        /* Ottieni il numero di thread attivo */
        tid = omp_get_thread_num();
        
        /* Solo il thread master (tid == 0) esegue questo blocco */
        if (tid == 0) {
            printf("Thread %d getting environment info...\n", tid);
            
            /* Ottieni informazioni sull'ambiente OpenMP */
            procs = omp_get_num_procs();    // Numero di processori disponibili
            nthreads = omp_get_num_threads();   // Numero di thread attivi
            maxt = omp_get_max_threads();   // Numero massimo di thread che possono essere utilizzati
            inpar = omp_in_parallel();    // Verifica se siamo in una regione parallela
            dynamic = omp_get_dynamic();   // Verifica se il bilanciamento del carico è abilitato
            nested = omp_get_nested();    // Verifica se il parallelismo nidificato è supportato
            
            /* Stampa le informazioni sull'ambiente */
            printf("Number of processors = %d\n", procs);
            printf("Number of threads = %d\n", nthreads);
            printf("Max threads = %d\n", maxt);
            printf("In parallel? = %d\n", inpar);
            printf("Dynamic threads enabled? = %d\n", dynamic);
            printf("Nested parallelism supported? = %d\n", nested);
        }
    }  
    /* Fine */
    exit(0);    // Termina il programma
}
