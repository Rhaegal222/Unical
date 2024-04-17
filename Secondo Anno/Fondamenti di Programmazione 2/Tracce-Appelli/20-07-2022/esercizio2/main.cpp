#include "GestorePersone.h"
#include <iostream>
using namespace std;
int main()
{
    Impiegato Paolo;
    Studente Francesco;

    Paolo.setNome("Paolo"); Paolo.setCognome("Impalato");
    Francesco.setNome("Francesco"); Francesco.setCognome("Imparato");
    cout << Paolo.getCognome() << " " << Paolo.getNome() << " " << Paolo.getStipendio() << endl;
    cout << Francesco.getCognome() << " " << Francesco.getNome() << " " << Francesco.getStipendio() << endl;

    Persona* P = &Paolo;

    GestorePersone persone;
    persone.aggiungiPersona(&Francesco);
    persone.aggiungiPersona(&Paolo);
    cout << persone.getStipendioMedio();

    return 0;
}
