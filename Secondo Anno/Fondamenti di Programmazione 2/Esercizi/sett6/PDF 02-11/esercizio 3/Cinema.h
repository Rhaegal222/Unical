#ifndef CINEMA_H
#define CINEMA_H

#include "Film.h"
#include <list>
using namespace std;

class Cinema
{
    private:
        list<Film*> film;
        void calcolaGeneri(list<Genere>&) const;
        void calcolaRegisti(list<string>&) const;        
    
    public:
        Genere migliorGenere() const;
        string registaStanco() const;
        int registiSettoriali() const;    
        int differenzaIncassoMaggiore() const;
    
        void aggiungi(Film* f);
};
#endif
