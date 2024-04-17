#ifndef UTENTE_H
#define UTENTE_H

#include <iostream>
using namespace std;

class Utente {
    public:
        Utente() : numero(0), tipologiaOperazione(0) {}
        Utente(int n, int to) : numero(n), tipologiaOperazione(to) {}
        int getNumero() const { return numero; }
        int getTipologiaOperazione() const { return tipologiaOperazione; }
        
        friend ostream& operator<<(ostream& o, const Utente& u) {
            o << "Numero: " << u.numero << ", ";
            
            switch(u.tipologiaOperazione) {
                case 0:
                    o << "spedizione";
                    break;
                    
                case 1:
                    o << "pagamento";
                    break;
                    
                case 2:
                    o << "riscossione";
                    break;
                
            }
            
            return o;
        }
    private:
        int numero;
        int tipologiaOperazione;

};

#endif