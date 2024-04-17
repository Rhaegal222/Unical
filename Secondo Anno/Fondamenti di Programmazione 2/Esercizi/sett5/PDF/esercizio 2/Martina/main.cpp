#include "Dipendente2.h"
#include <string>
#include <iostream>
using namespace std;

int main(){
    Dipendente Esteban("Mario", "Gomez", "Gonzalo", 125); //oggetto con parametri
    Dipendente Charles; //oggetto senza parametri

    Esteban.setId("CH196LF");
    Esteban.setNome("Fio");
    Esteban.setCognome("Denamignotta");
    Esteban.setStipendio(20);

	cout << Esteban.getId() << endl;
	cout << Esteban.getNome() << endl;
    cout << Esteban.getCognome() << endl;
    cout << Esteban.getStipendio() << endl;
    return 0;
}