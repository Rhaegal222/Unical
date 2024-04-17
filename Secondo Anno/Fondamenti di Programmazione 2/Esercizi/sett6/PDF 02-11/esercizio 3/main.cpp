#include "Cinema.h"
#include <iostream>
#include <vector>
using namespace std;

int main() {
        
    Cinema c;
    vector<Film*> film;
    for(int i = 0; i < 10; i++) {
        Genere g;
        if(i % 2 == 0)
            g = ANIMAZIONE;
        else
            g = COMMEDIA;
        Film* f = new Film("titolo", 2002+i, 10*i+100, "regista", g);
        film.push_back(f);
        c.aggiungi(f);
    }
    Film* f = new Film("titolo", 2001, 100, "regista1", ANIMAZIONE);
    film.push_back(f);
    c.aggiungi(f);
    
    cout << "Miglior genere " << c.migliorGenere() << endl;
    cout << "Regista stanco " << c.registaStanco() << endl;
    cout << "Registi settoriali " << c.registiSettoriali() << endl;
    cout << "Differenza incasso maggiore " << c.differenzaIncassoMaggiore() << endl;
    
    for(int i = 0; i < film.size(); i++) {
        delete film[i];
    }
    
    return 0;
}
