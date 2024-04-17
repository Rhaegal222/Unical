#ifndef GESTOREDOCUMENTI_H
#define GESTOREDOCUMENTI_H

#include <list>
#include <algorithm>
#include <iostream>

#include "Documento.h"

using namespace std;

class GestoreDocumenti{
    private:
        list<Documento*> listaDocumenti;
    public:
        GestoreDocumenti(){};
        bool esisteDocumento(Documento* documento){
            for (list<Documento *>::iterator it = listaDocumenti.begin(); it != listaDocumenti.end(); it++){
                Documento selected = **it;
                if(selected.getProprietario() == documento->getProprietario() && selected.getDimensioneFile()==documento->getDimensioneFile() && selected.getDescrizione() == documento->getDescrizione())
                return true;
            }
            return false;
        };
        void aggiungiDocumento(Documento* documento){
            if(!esisteDocumento(documento)){
                listaDocumenti.push_back(documento);
                cout << documento->getProprietario() << " " << documento->getDescrizione() << " " << documento->getDimensioneFile() << ": Aggiunto" << endl;
            }
            else cout << documento->getProprietario() << " " << documento->getDescrizione() << " " << documento->getDimensioneFile() << ": Non Aggiunto" << endl;
        };
        void rimuoviDocumento(Documento* documento){
            if(esisteDocumento(documento)){
                for(list<Documento *>::iterator it = listaDocumenti.begin(); it != listaDocumenti.end(); it++){
                    Documento selected = **it;
                    if(selected.getProprietario() == documento->getProprietario() && selected.getDimensioneFile()==documento->getDimensioneFile() && selected.getDescrizione() == documento->getDescrizione()){

                        listaDocumenti.remove(documento);
                
                        cout << documento->getProprietario() << " " << documento->getDescrizione() << " " << documento->getDimensioneFile() << ": Rimosso" << endl;
                        
                        break;
                    }
                }
            }
            else cout << documento->getProprietario() << " " << documento->getDescrizione() << " " << documento->getDimensioneFile() << ": Non Rimosso" << endl;
        };
        void stampaDocumenti() const{
            int cont = 0;
            cout << endl;
            for(list<Documento*>::const_iterator it = listaDocumenti.begin(); it!=listaDocumenti.end(); it++){
                cout << cont++ << " ";
                Documento selected = **it;
                cout << selected.getProprietario() << " " << selected.getDescrizione() << " " << selected.getDimensioneFile() << endl;
            }
        };
        void ordinaDocumenti(int valore){
            switch (valore){
            case 1:
                for (list<Documento *>::const_iterator it1 = listaDocumenti.begin(); it1 != listaDocumenti.end(); it1++){
                    for (list<Documento *>::const_iterator it2 = listaDocumenti.begin(); it2 != listaDocumenti.end(); it2++){
                        Documento sel1 = **it1;
                        Documento sel2 = **it2;
                        if (sel1.getProprietario() < sel2.getProprietario()){
                            Documento tmp = **it1;
                            **it1 = **it2;
                            **it2 = tmp;
                        }
                    }
                }
                break;
    case 2:
        for (list<Documento *>::const_iterator it1 = listaDocumenti.begin(); it1 != listaDocumenti.end(); it1++){
            for (list<Documento *>::const_iterator it2 = listaDocumenti.begin(); it2 != listaDocumenti.end(); it2++){
                Documento sel1 = **it1;
                Documento sel2 = **it2;
                if (sel1.getDescrizione() < sel2.getDescrizione()){
                    Documento tmp = **it1;
                    **it1 = **it2;
                    **it2 = tmp;
                }
            }
        }
        break;

    case 3:
        for (list<Documento *>::const_iterator it1 = listaDocumenti.begin(); it1 != listaDocumenti.end(); it1++){
            for (list<Documento *>::const_iterator it2 = listaDocumenti.begin(); it2 != listaDocumenti.end(); it2++){
                Documento sel1 = **it1;
                Documento sel2 = **it2;
                if (sel1.getDimensioneFile() < sel2.getDimensioneFile()){
                    Documento tmp = **it1;
                    **it1 = **it2;
                    **it2 = tmp;
                }
            }
        }
        break;
            }
        };
};

#endif