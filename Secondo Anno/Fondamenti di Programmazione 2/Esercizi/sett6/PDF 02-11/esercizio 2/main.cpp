#include <iostream>
using namespace std;

#include "Posta.h"

void stampaMenu() {
    cout << "==== Menu ====" << endl;
    cout << "  Premi 1 per aggiungere un utente specificando la tipologia di operazione" << endl;
    cout << "  Premi 2 per selezionare il prossimo utente da servire" << endl;
    cout << "  Premi 3 per stampare gli utenti in coda" << endl;
    cout << "  Premi 4 per stampare gli utenti in coda per una determinata operazione" << endl;
    cout << "  Premi 5 per effettuare un reset" << endl;
    cout << "  Premi 9 per uscire" << endl;
}

int main() {
    int scelta = 0;
    Posta p;    
    do {
        stampaMenu();
        cin >> scelta;    
        switch(scelta) {
            case 1: {
                int tipologiaOperazione;
                cout << "Inserisci tipologia operazione (0=spedizione,1=pagamento,2=riscossione)" << endl;
                cin >> tipologiaOperazione;
                
                if(tipologiaOperazione < 0 || tipologiaOperazione > 2)
                    cout << "Operazione non valida" << endl;
                else {
                    p.aggiungiUtente(tipologiaOperazione);
                    p.stampaUtentiInCoda();
                }
                }
                break;
            case 2:
                cout << "Prossimo utente " << p.prossimoUtente() << endl;
                break;
            case 3:
                p.stampaUtentiInCoda();
                break;
            case 4: {
                int tipologiaOperazione;
                cout << "Inserisci tipologia operazione (0=spedizione,1=pagamento,2=riscossione)" << endl;
                cin >> tipologiaOperazione;
                
                if(tipologiaOperazione < 0 || tipologiaOperazione > 2)
                    cout << "Operazione non valida" << endl;
                else {
                    p.aggiungiUtente(tipologiaOperazione);
                    p.stampaUtenti(tipologiaOperazione);
                }
                }
                break;
            case 5:   
                p.reset();
                break;
            case 9:   
                cout << "Grazie e a presto!" << endl;
                break;
            default:   
                cout << "Scelta non valida" << endl;
                break;            
        }        
    } while(scelta != 9);
    
    return 0;
}