#include <allegro5/allegro.h>
#include <allegro5/allegro_primitives.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_font.h> // Aggiunta per gestire i font
#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;

// Dichiarazione delle variabili
ALLEGRO_COLOR nero, bianco;
ALLEGRO_DISPLAY *display;
ALLEGRO_BITMAP *buffer;
ALLEGRO_FONT *font; // Aggiunta per gestire i font

int numStep;
int numRows;
int numCols;
int rowCentro;
int colCentro;
int raggio;

int dir = 1;

int **readMatrix;
int **writeMatrix;

// Funzione per l'inizializzazione di Allegro
void initAllegro() {
    if (!al_init()) {
        cerr << "Errore nell'inizializzazione di Allegro." << endl;
        exit(-1);
    }

    // Inizializza addon per l'input da tastiera
    if (!al_install_keyboard()) {
        cerr << "Errore nell'inizializzazione della tastiera." << endl;
        exit(-1);
    }

    // Crea un buffer per il disegno
    buffer = al_create_bitmap(numCols, numRows);

    // Imposta la modalità grafica
    al_set_new_display_flags(ALLEGRO_WINDOWED);
    display = al_create_display(numCols, numRows);
    if (!display) {
        cerr << "Errore nella creazione del display." << endl;
        exit(-1);
    }

    // Imposta i colori
    nero = al_map_rgb(0, 0, 0);
    bianco = al_map_rgb(255, 255, 255);

    // Inizializza i font
    font = al_create_builtin_font();
    if (!font) {
        cerr << "Errore nella creazione del font." << endl;
        exit(-1);
    }
}

// Restituisci una variabile di tipo ALLEGRO_COLOR
ALLEGRO_COLOR getAllegroColor(int r, int g, int b) {
    return al_map_rgb(r, g, b);
}

// Funzione per leggere i parametri dal file di configurazione
void readConfigFile() {
    char str[20];
    FILE *file;
    file = fopen("Configuration.txt", "r");
    if (file) {
        fscanf(file, "%s", str);
        numRows = atoi(str);
        fscanf(file, "%s", str);
        numCols = atoi(str);
        fscanf(file, "%s", str);
        rowCentro = atoi(str);
        fscanf(file, "%s", str);
        colCentro = atoi(str);
        fscanf(file, "%s", str);
        raggio = atoi(str);
        fscanf(file, "%s", str);
        numStep = atoi(str);
        fclose(file);
    }
}

// Funzione per creare una matrice
void createMatrix(int **&m, int numRows, int numCols) {
    m = new int *[numRows];
    for (int row = 0; row < numRows; ++row) {
        m[row] = new int[numCols];
    }
}

// Inizializzazione del modello
void initModel() {
    createMatrix(readMatrix, numRows, numCols);
    createMatrix(writeMatrix, numRows, numCols);
    for (int row = 0; row < numRows; row++) {
        for (int col = 0; col < numCols; col++) {
            // Calcola la distanza dal centro e inizializza la matrice
            double distanza = sqrt(pow((row - rowCentro), 2) + pow((col - colCentro), 2));
            if (distanza <= raggio) {
                readMatrix[row][col] = 1;
                writeMatrix[row][col] = 1;
            } else {
                readMatrix[row][col] = 0;
                writeMatrix[row][col] = 0;
            }
        }
    }
}

// Funzione per disegnare con Allegro
void drawWithAllegro(int step) {
    al_set_target_bitmap(buffer);

    // Pulisci il buffer con il colore nero
    al_clear_to_color(nero);

    // Disegna ogni pixel in base allo stato nella matrice
    for (int row = 0; row < numRows; row++) {
        for (int col = 0; col < numCols; col++) {
            switch (readMatrix[row][col]) {
                case 0:
                    // Pixel nero
                    al_put_pixel(col, row, nero);
                    break;
                case 1:
                    // Pixel bianco
                    al_put_pixel(col, row, bianco);
                    break;
            }
        }
    }

    al_set_target_backbuffer(display);

    // Disegna il numero di passi
    al_draw_textf(font, bianco, 0, 0, 0, "Step: %i", step);

    // Aggiorna il display
    al_flip_display();
}

// Funzione per calcolare l'incremento circolare
int incMod(int num, int inc, int dim) {
    return (num + inc + dim) % dim;
}

// Funzione di transizione
void transitionFunction(int row, int col) {
    writeMatrix[row][col] = readMatrix[row][incMod(col, dir, numCols)];
}

// Esegui la funzione di transizione su tutta la matrice
void executeTransitionFunction() {
    for (int row = 0; row < numRows; row++) {
        for (int col = 0; col < numCols; col++) {
            transitionFunction(row, col);
        }
    }
}

// Scambia le matrici lette e scritte
void swapMatrices() {
    int **p = readMatrix;
    readMatrix = writeMatrix;
    writeMatrix = p;
}

// Funzione di controllo principale
void controlLoop() {
    readConfigFile();
    initAllegro();
    initModel();

    // Ciclo principale
    for (int step = 0; step < numStep; ++step) {
        drawWithAllegro(step);

        // Gestione dell'input da tastiera
        ALLEGRO_KEYBOARD_STATE keystate;
        al_get_keyboard_state(&keystate);

        if (al_key_down(&keystate, ALLEGRO_KEY_LEFT)) {
            dir = 1;
        }

        if (al_key_down(&keystate, ALLEGRO_KEY_RIGHT)) {
            dir = -1;
        }

        executeTransitionFunction();
        swapMatrices();
    }

    al_rest(2.0); // Pausa per 2 secondi alla fine

    // Pulizia e uscita
    al_destroy_font(font);
    al_destroy_bitmap(buffer);
    al_destroy_display(display);
}

int main() {
    controlLoop();
    return 0;
}
