#include <iostream>
#include "GestorePartite.h"
using namespace std;

int main(){
    GestorePartite p1;
    p1.aggiungiPartita("Milan", "Inter", 1, 1);
    p1.aggiungiPartita("Juventus", "Napoli", 2, 3);
    p1.aggiungiPartita("Lecce", "Bari", 4, 2);
    p1.aggiungiPartita("Reggina", "Cagliari", 3, 0);
    p1.aggiungiPartita("Latina", "Reggina", 2, 4);

    GestorePartite p2(p1);

    p2.stampaPartite();
    cout<<p2.getSquadraPiuForte()<<endl;
    cout<<p2.mediaGoal()<<endl;

    return 0;
}
