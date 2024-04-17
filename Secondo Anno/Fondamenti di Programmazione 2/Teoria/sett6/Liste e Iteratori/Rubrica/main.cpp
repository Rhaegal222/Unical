#include "Contatto.cpp"
using namespace std;

int main(){
    List<Contatto> rubrica;
    Contatto amico;
    amico.setNome("mario");
    amico.setCognome("rossi");
    rubrica.pushFront(amico);
    amico.setNome("luisa");
    amico.setCognome("verdi");
    rubrica.pushFront(amico);

    if(rubrica.find(amico))
        cout<< "trovato "<< amico << endl; 	// Trovato luisa – verdi - -
    if(cerca(rubrica,"rossi"))
        cout<< "rossi trovato" << endl;	// rossi trovato
}