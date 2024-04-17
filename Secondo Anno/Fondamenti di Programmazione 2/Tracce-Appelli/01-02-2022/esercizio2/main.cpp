#include "GestoreValori.h"

using namespace std;

int main(){

    GestoreValoriB valori;
    valori.inserisciCoppia(2, 'c');
    valori.inserisciCoppia(2, 'c');
    valori.inserisciCoppia(7, 'c');
    valori.inserisciCoppia(1, 'c');

    valori.inserisciCoppia(3, 'd');
    valori.inserisciCoppia(3, 'd');
    valori.inserisciCoppia(4, 'd');
    valori.inserisciCoppia(5, 'd');
    valori.inserisciCoppia(7, 'd');

    cout << valori.getRisultato() << " " << valori.numCoppie() << endl;
}

