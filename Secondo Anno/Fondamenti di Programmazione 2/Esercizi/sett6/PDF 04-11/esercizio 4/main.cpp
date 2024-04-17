#include "Mensa.h"
int main()
{
    AnagraficaUniversitaria regUni;

    Studente Francesco("VCC", "Francesco", "Vecchio", 7390.0);
    Professore Pastore("PST", "Patrizia", "Pastore", 4500.49);

    regUni.aggiungiProfessore(Pastore);
    regUni.aggiungiStudente(Francesco);

    regUni.stampa();

    Mensa regMensa;

    regMensa.accesso(regUni.getPersona("VCC"));
    regMensa.accesso(regUni.getPersona("VCC"));

    regMensa.stampa();
    
    return 0;
}
