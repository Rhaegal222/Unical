#ifndef POSTA_H
#define POSTA_H

#include <list>
#include <vector>
using namespace std;

#include "Utente.h"

class Posta {
    public:
        Posta();
        void aggiungiUtente(int tipologiaOperazione);
        Utente prossimoUtente();
        void stampaUtentiInCoda() const;
        void stampaUtenti(int tipologiaOperazione) const;
        void reset();
        
    private:
        list<Utente> utenti;
        vector<int> operazioni;        
};

#endif