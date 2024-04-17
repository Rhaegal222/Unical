#include "init.h"

int main(int argc, char* argv[]){
	
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	configurationReader();  //legge config.txt e calcola nPartX e nPartY
    if (size != nPartX * nPartY / nThreads){   // se non sono divisibili chiudo il programma
        exit(1);  
	}
	inputDimensionReader(); //calcola totCols e totRows, inizializza matrix e ci copia tutti i valori dell'input.txt
	initAllPartitions(); //trova una divisione ottimale calcolando: nPartYPerProc,nPartXPerProc. Inizializza gli array che calcolano le dimensioni di ciascuna
	//partizione nRowsPerPartition,nColsPerPartition. Scompone il rank del proc attuale,calcola il numero di proc lungo X, calcola il numero delle righe e colonne 
	//del proc attuale
	calculateMooreNeighbourhood();  //Calcola i rank dei processi vicini 
	initArrays();
	inputReader();  //inizializza la readM e writeM del proc attuale leggendo input.txt
	
	//creazione e inizializzazione dei typeVector rappresentanti colonna e matrice interna
	createDatatype();
    initBarriers();
	
	inizio = clock();
	if(rank==0){
		if(allegroRun){
			initAllegro();
			drawWithAllegro(0);
		}
		recvInfo();
	}
	else{
		sendInfo();
	}

    initializeThreads();
	for (int i = 0; i < steps; i++){
		sleep(1); //attivare solo per rallentare gli step --> togliere per calcolare il tempo
		exchangeBordersMoore();
        comunicationBarrier(); //main thread arriva alla barriera. Presente sia qua che nella funzione degli altri thread creati. Una volta che sono arrivati
		//tutti, escono dalla barriera. Sicuro i bordi saranno stati inviati e ricevuti, e tutti posso computare.
		execTransFunc(1, 1, nColsPerPartition[rankX * nPartXPerProc], nRowsPerPartition[rankY * nPartYPerProc]);  //Nel frattempo faccio computare anche al main thread.
		//Il main thread computerà ogni volta la partizione iniziale (1,1)
    	completedBarrier(); //stesso ragionamento ma dopo, se non metto la barrier, e ad esempio il main thread finisce prima, continua l'esecuzione del 
		// main e potrebbe aggiornare la grafica, senza che tutti abbiano finito
		if(allegroRun){
			if(rank == rankMaster){
				recvmatrix();
				drawWithAllegro(i + 1);
			}
			else
				MPI_Send(&writeM[v(1,1)], 1, typeMatWithoutHalos, rankMaster, 777, MPI_COMM_WORLD);  //invio la matrice interna (senza halo)
		}
		swap();
	}
	fine = clock();

	if(rank == 0){
		if(allegroRun)
			allegro_exit();
		double tempoEsec = (double)(fine-inizio)/CLOCKS_PER_SEC;
		printf("\nTEMPO DI ESECUZIONE TOTALE: %fs \n", tempoEsec);
	}
	
	destroy();
	freeDatatype();
	
	MPI_Finalize();
	return 0;
}

// mpic++ main.cpp -I/usr/include -L/usr/lib/x86_64-linux-gnu -lalleg -o main
// mpirun -np 2 ./main