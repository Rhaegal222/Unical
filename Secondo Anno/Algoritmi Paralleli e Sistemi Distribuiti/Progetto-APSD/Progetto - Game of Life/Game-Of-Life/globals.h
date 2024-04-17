#ifndef __GLOBALS__H__
#define __GLOBALS__H__

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <algorithm>
#include <pthread.h>
#include <mpi.h>  
#include <allegro.h>

/*
La macro v(r,c) permette di accedere alla matrice in modo più semplice,
infatti, per accedere alla cella (r,c) della matrice, si può scrivere v(r,c) invece di scrivere
(r)*(nColsThisRank+2)+(c), che è più lungo e meno leggibile.
*/
#define v(r,c) (r)*(nColsThisRank+2)+(c)                        // Macro per accedere alla matrice

// Variabili contenute nel file di configurazione config.txt
int nPartX;                                                     // N° di partizioni orizzontali (asse x)
int nPartY;		                                                // N° di partizioni verticali (asse y)
int nThreads;                                                   // N° di thread
int steps;	                                                    // N° totale di step

// Variabili globali
int totRows;                                                    // N° totale di righe
int totCols;	                                                // N° totale di colonne

//Valori dell'ambiente MPI
int size;		                                                // N° complessivo di processi
int rank;		                                                // id del processo attuale

//Variabili inizializzate dalla funzione initAllPartitions
int nRowsThisRank;                                              // N° di righe del processo corrente
int nColsThisRank;                                              // N° di colonne del processo corrente

/*	
Array che contengono, per ogni partizione, il n° di righe/colonne al proprio interno (nella partizione), 
ad esempio nRowsPerPartition[0] conterrà il n° di righe nella prima partizione e nColsPerPartition[0] il n° di colonne.
*/
int *nRowsPerPartition;                                         // N° di righe per partizione
int *nColsPerPartition;                                         // N° di colonne per partizione
      
int nPartXPerProc;                                              // N° di partizioni lungo l'asse x per processo
int nPartYPerProc;                                              // N° di partizioni lungo l'asse y per processo
int nProcOnX;	                                                // N° di processi lungo l'asse x

int rankX;                                                      // Rank del processo sull'asse x
int rankY;                                                      // Rank del processo sull'asse y       
int rankMaster = 0;		                                        // Rank del processo master
int rankUp, rankDown, rankLeft, rankRight;                      // Rank dei processi vicini
int rankUpLeft, rankUpRight, rankDownLeft, rankDownRight;       // Rank dei processi vicini (diagonali)

// Matrici di lettura e scrittura
int * readM;		                                            // Matrice di lettura
int * writeM;		                                            // Matrice di scrittura

int startXThisProc;                                             // Indice di inizio delle colonne del processo corrente
int startYThisProc;                                             // Indice di inizio delle righe del processo corrente

/*	
Array che contengono, per ogni posizione, gli indici d'inizio delle colonne/righe di ciascun processo, 
ad esempio startColPerProc[0] conterrà l'indice d'inizio delle colonne del primo processo e startRowPerProc[0] l'indice d'inizio delle righe.
*/
int *startColPerProc;                                           // Array che contiene, per ogni posizione, gli indici d'inizio delle colonne di ciascun processo
int *startRowPerProc;                                           // Array che contiene, per ogni posizione, gli indici d'inizio delle righe di ciascun processo

/*
Array che contengono, per ogni posizione, la sizeY (rows) / sizeX (cols) di ciascun processo,
ad esempio vecRowSizePerProc[0] conterrà la sizeY del primo processo e vecColSizePerProc[0] la sizeX.
*/
int *vecRowSizePerProc;                                         // Array che contiene, per ogni posizione, la sizeY di ciascun processo
int *vecColSizePerProc;	                                        // Array che contiene, per ogni posizione, la sizeX di ciascun processo

int *matrix;	                                                // Matrice totale (contenente tutte le partizioni) --> usata per la stampa a schermo

//Datatypes
MPI_Datatype typeColumn;				                        // Datatype per inviare una colonna
MPI_Datatype typeMatWithoutHalos;	                            // Datatype per inviare una matrice SENZA gli halo borders (mat interna) 

//Variabili Pthread
pthread_t * vecThreads;	                                        // Vettore di thread

//Mutex
pthread_mutex_t mutexReadyBarrier;    				            // Mutex per la barriera di completamento
pthread_mutex_t mutexComunicationBarrier;   			        // Mutex per la barriera di comunicazione
int contReadyBarrier =0, contComunicationBarrier=0;	            // Contatori per le barriere

//Condition
pthread_cond_t condReadyBarrier;                                // Condition per la ReadyBarrier
pthread_cond_t condComunicationBarrier;                         // Condition per la ComunicationBarrier


//Variabili per la stampa a schermo (Allegro)
clock_t inizio, fine;		                                    // Variabili per calcolare il tempo di esecuzione
int delayAllegro = 80;		                                    // Delay per la stampa a schermo
int graphicCellDim = 50;	                                    // Dimensione di una cella grafica
int infoLine = 55;			                                    // Altezza della riga delle informazioni
bool allegroRun = true;                                         // Variabile per la stampa a schermo
 
#endif // !__GLOBALS__H__