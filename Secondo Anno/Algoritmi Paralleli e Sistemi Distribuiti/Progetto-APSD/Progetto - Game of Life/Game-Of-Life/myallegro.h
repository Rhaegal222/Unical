#ifndef __MYALLEGRO__H__
#define __MYALLEGRO__H__


#include "globals.h"

void initAllegro(){ 
    allegro_init();
	install_keyboard();
    set_color_depth(32);  
	set_window_title("Vecchio Francesco - Progetto APSD - Game of Life - Allegro");
    set_gfx_mode(GFX_AUTODETECT_WINDOWED, totCols * graphicCellDim, totRows * graphicCellDim + infoLine, 0, 0);  
}

void closeAllegro(){
	allegro_exit();
}

void drawOrizzontalPartitions(){
	int x=0;
	for(int i = 0; i < nPartX; i++){
		if(x>0) rectfill(screen, x, 0, x+2, totRows * graphicCellDim, makecol(193, 140, 93));
		x += nColsPerPartition[i] * graphicCellDim;
	}
}

void drawVerticalPartitions(){
	int y=0;
	for(int i = 0; i < nPartY; i++){
		if (y>0) rectfill(screen, 0, y, totCols * graphicCellDim, y+2, makecol(197, 120, 221));
		y += nRowsPerPartition[i] * graphicCellDim;
	}
}

void drawPartitions(){
	drawOrizzontalPartitions(); // Partizioni lungo l'asse X
	drawVerticalPartitions(); // Partizioni lungo l'asse Y
}

void drawGrid(){
	for(int i = 1; i < totRows; i++) line(screen, 0, i * graphicCellDim, totCols * graphicCellDim, i * graphicCellDim, makecol(97, 175, 239));
	for(int i = 0; i < totCols; i++) line(screen, i * graphicCellDim, 0, i * graphicCellDim, totRows * graphicCellDim, makecol(97, 175, 239));
}

void drawMatrix(){
	for(int i = 0; i < totRows; i++){
		for(int j = 0; j < totCols; j++){
			int x = j * graphicCellDim;
			int y = i * graphicCellDim;
			if (matrix[i * totCols + j] == 1) rectfill(screen, x, y, x + graphicCellDim, y + graphicCellDim,  makecol(146, 195, 121)); 	// Cellula VIVA
			else rectfill(screen, x, y, x + graphicCellDim, y + graphicCellDim, makecol(40, 44, 42));									// Cellula MORTA
		}
	}
}

void drawInfo(int stepCurr){
	int endY = totRows * graphicCellDim; // Altezza della matrice (in pixel)
	char str[64];
	sprintf(str, "Step %d su %d", stepCurr, steps);
	textout_ex(screen, font, str, 0, endY+1, makecol(255, 255, 255), -1); //+1 per farlo partire poco dopo la fineY della matrice
	sprintf(str, "N° di partizioni su X: %d",nPartX);
	textout_ex(screen, font, str, 0, endY+15, makecol(255, 255, 255), -1); // Testo bianco
	sprintf(str, "N° di partizioni su Y: %d",nPartY);
	textout_ex(screen, font, str, 0, endY+26, makecol(255, 255, 255), -1); // Testo bianco
	sprintf(str, "N° di Thread: %d",nThreads);	
	textout_ex(screen, font, str, 0, endY+37, makecol(255, 255, 255), -1); // Testo bianco
	sprintf(str, "Dimensioni TOT dell'AC: %d x %d",totRows, totCols);
	textout_ex(screen, font, str, 250, endY+26, makecol(255, 255, 255), -1); // Testo bianco
}



// Funzione per la stampa a schermo tramite allegro
void drawWithAllegro(int stepCurr){
	clear_to_color(screen, makecol(40, 44, 42)); // Sfondo nero
	drawInfo(stepCurr);
	drawMatrix();
	drawGrid();
	drawPartitions();
}


#endif //!__MYALLEGRO__H__