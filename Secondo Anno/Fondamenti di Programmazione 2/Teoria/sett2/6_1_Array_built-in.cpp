// Array Built-in

#include <iostream> 

using namespace std;

// TIPO_BASE NOME [DIMENSIONE];

int a[10];
// il nome in cpp viene interpretato come l'indirizzo della prima cella di memoria

const int dim = 10;
int b[dim];  

// questo si può fare nelle ultime versioni di cpp 
int dim;
cin >> dim;
int c[dim]; 

// una volta stabilito la dimensione dell'array, essa non può cambiare

//Per inizializzare:
const unsigned sz = 3;
int a1[sz] = {0, 1, 2};
int a2[] = {0, 1, 2};
int a3[5] = {0, 1, 2}; // a3 = {0, 1, 2, 0, 0}

#if 0
int a4[2] = {0, 1, 2}; // ERRORE

// Non si può leggere o scrivere un array per intero

cin >> a; // NO

// unica eccezione per gli array di char
int a[] = {0,1,2};
int a2[] = a; // ERRORE
a2 = a; // ERRORE
#endif

// accesso agli elementi 
// struttura ad "Accesso diretto"

// indice primo elemento 0
int dim5 = 10;
int a5[dim5];
a5[0]; // primo elemento
a5[dim5-1]; // ultimo elemento









