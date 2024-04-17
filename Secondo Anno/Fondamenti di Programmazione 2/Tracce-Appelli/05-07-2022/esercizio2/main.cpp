#include <iostream>
#include "Carriera.h"

using namespace std;

int main(){

    Carriera c;
    for(int i = 0; i < 100; i++){
        c.aggiungiTentativo("Fisica", true);
        c.aggiungiTentativo("Analisi", false);
        c.aggiungiTentativo("Fondamenti", true);
        c.aggiungiTentativo("Discreta", false);
		c.aggiungiTentativo("Economia", false);
		c.aggiungiTentativo("Sistemi", false);
    }

	c.stampaElencoAppelli();

	for(int i = 0; i < 599; i++) c.rimuoviUltimoAppello();

	c.stampaElencoAppelli();

	if(c.studenteDiligente()) cout<<"Lo studente e' diligente"<<endl;
	else cout<<"Lo studente NON e' diligente"<<endl; cout<<endl;

    return 0;
}
