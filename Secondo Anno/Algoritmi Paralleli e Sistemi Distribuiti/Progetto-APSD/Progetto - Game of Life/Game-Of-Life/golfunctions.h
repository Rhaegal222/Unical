#ifndef  __GOLFUNCTIONS__H
#define __GOLFUNCTIONS__H

#include "mpifunctions.h"

int countAliveNeighbors(int x, int y) {
    int count = 0;
    for (int dx = -1; dx < 2; ++dx){
        for (int dy = -1; dy < 2; ++dy) {
            if((dx != 0 || dy != 0) && readM[v((x+dx+totRows) % totRows, (y+dy+totCols) % totCols)] == 1) {
                count++;
            }
        }
	}
	return count;
}
void transitionFunction(int x, int y){ 
	/*
        * Funzione di transizione per il gioco della vita.
        * 
        * @param x: coordinata x della cella
        * @param y: coordinata y della cella
        
        Regole del gioco della vita:
            - se una cella viva ha meno di 2 o più di 3 vicini vivi --> MUORE
            - se una cella viva ha 2 o 3 vicini vivi --> SOPRAVVIVE
            - se una cella morta ha 3 vicini vivi --> NASCE
    */

	int cont = countAliveNeighbors(x, y); // Funzione per contare i vicini vivi

	//Applica le regole:
    if(readM[v(x, y)] == 1) {
        if(cont == 2 || cont == 3) {
            writeM[v(x, y)] = 1;
        }
        else {
            writeM[v(x, y)] = 0;
        }
    }
    else {
        if(cont == 3) {
            writeM[v(x, y)] = 1;
        }
        else {
            writeM[v(x, y)] = 0;
        }
    }
}
void execTransFunc(int beginThreadX, int beginThreadY, int sizePartizX, int sizePartizY){
	for(int i = beginThreadX; i < beginThreadX + sizePartizX; i++){
		for(int j = beginThreadY; j < beginThreadY + sizePartizY; j++){
			transitionFunction(j, i);
		}
	}
}

void swap(){
	int* p = readM;
    readM = writeM;
    writeM = p;
}


#endif //!__GOLFUNCTIONS__H