#ifndef __READINGCONF_H
#define __READINGCONF_H

#include "myallegro.h"
 

int readConfigValue(FILE* file, char* buffer, int maxLineLength, long maxLimit) {
    if (fgets(buffer, maxLineLength, file)) {
        long value = strtol(buffer, NULL, 10);
        if (value <= maxLimit) {
            return (int)value;
        } else {
            fprintf(stderr, "Errore: Valore fuori limite.\n");
            exit(1);
        }
    }
    return -1;
}
//legge il file di configurazione (riga per riga) e inizializza le variabili globali (nPartX, nPartY, nThreads, step)
void configurationReader() {
    int MAX_LINE_LENGTH = 20;
    int INT_MAX_LIMIT = 2147483647;

    char buffer[MAX_LINE_LENGTH];
    FILE *file = fopen("configuration.txt", "r");

    if (file) {
        nPartX = readConfigValue(file, buffer, MAX_LINE_LENGTH, INT_MAX_LIMIT);
        nPartY = readConfigValue(file, buffer, MAX_LINE_LENGTH, INT_MAX_LIMIT);
        nThreads = readConfigValue(file, buffer, MAX_LINE_LENGTH, INT_MAX_LIMIT);
        steps = readConfigValue(file, buffer, MAX_LINE_LENGTH, INT_MAX_LIMIT);
        fclose(file);
    } else {
        fprintf(stderr, "Errore: Impossibile aprire il file di configurazione.\n");
        exit(1);
    }
}
//conta il numero di righe e colonne del file di input
void countRowsAndCols(FILE* inputFile, int& totRows, int& totCols) {
    char c;
    bool end = false, colsCounted = false;
    while (!end) {
        c = fgetc(inputFile);
        if (c == EOF) {
            end = true;
        } else if (c == '\n') {
            colsCounted = true;
            totRows++;
        } else if (!colsCounted) {
            totCols++;
        }
    }
}
void fillMatrix(FILE* inputFile, int* matrix, int totRows, int totCols) {
    rewind(inputFile);
    char c;
    bool end = false;
    int cont = 0;
    while (!end) {
        c = fgetc(inputFile);
        if (c == EOF) {
            end = true;
        } else if (c != '\n') {
            if (cont >= totRows * totCols) {
                printf("Righe: %d, Colonne: %d, cont: %d\n", totRows, totCols, cont);
                perror("La matrice all'interno di input.txt ha un numero errato di righe/colonne");
                delete[] matrix;
                exit(1);
            }
            matrix[cont] = c - '0';
            cont++;
        }
    }
}
void inputDimensionReader() {
    totRows = 0;
    totCols = 0;

    FILE* inputFile = fopen("input.txt", "r");
    if (inputFile == NULL) {
        perror("Impossibile aprire il file di input");
        delete[] matrix;
        exit(1);
    }

    countRowsAndCols(inputFile, totRows, totCols);
    matrix = new int[totRows * totCols];
    fillMatrix(inputFile, matrix, totRows, totCols);

    fclose(inputFile);
}
int countMatProc(int arr[], int end) {
    int result = 0;
    for (int i = 0; i < end; i++) {
        result += arr[i];
    }
    return result;
}
void inputReader(){  // Serve per leggere, da input.txt, la sottomatrice processo corrente.
	int partXPrevious = rankX * nPartXPerProc; //n° di partizioni lungo l'asse X precedenti all'attuale
	int partYPrevious = rankY * nPartYPerProc; 
	startYThisProc = countMatProc(nRowsPerPartition, partYPrevious);
    startXThisProc = countMatProc(nColsPerPartition, partXPrevious);

	//vado a copiare nella matrice readM del processo attuale, la porzione corrispondente dalla matrice totale in input.txt 
    for (int i=0;i<nRowsThisRank+2;i++) { //i e j potrebbero partire anche da 1, in quanto la prima è halo, ma conviene inizializzarle a 0, per avitare errori
        for (int j=0;j<nColsThisRank+2;j++) {
            if (i==0 || i==nRowsThisRank+1 || j==0 || j==nColsThisRank+1) { //gli halo li inizializzo tutti a 0
                readM[v(i, j)] = 0;
            } else {
                readM[v(i, j)] = matrix[(i-1+startYThisProc) * totCols + (j-1+startXThisProc)]; //se non è un halo border copio il valore dalla mat totale in input.txt
				//                        ^^ devo togliere i -1 per gli haloBoard
            }
            writeM[v(i, j)] = 0;
        }
    }
	if(rank != 0)
		delete [] matrix;
	return;
}
#endif //!__READINGCONF_H