#ifndef GESTORE_DIPENDENTI_H
#define GESTORE_DIPENDENTI_H

#include <iostream>
#include <vector>
#include <string>
#include "Dipendente.h"

class GestoreDipendenti{
    private:
        vector<Dipendente> dipendenti;
    
    public:

        GestoreDipendenti() {};

        bool esisteDipendente(string id) const;
        bool aggiungiDipendente(Dipendente d);
        void rimuoviDipendente(string id);
        void stampa() const;
        float calcolaCostoDipendenti() const;
};

#endif