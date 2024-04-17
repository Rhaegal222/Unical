#include "Prodotto.h"
#include <list>
#include <iostream>
using namespace std;

class ListaDellaSpesa{
    protected: //io ho messo private
    list<pair<Prodotto, int>> Lista;
    public:
    ListaDellaSpesa(){};
    void inserisci(const Prodotto& p, int q){
        for(auto x:Lista){
            if(x.first==p){
                x.second+=q;
                return;
            }
        }
        Lista.push_back(make_pair(p,q));
    }
    bool rimuovi(const Prodotto& p){
        for(auto x:Lista){
            if(x.first==p){
                Lista.remove(x);
                return true;
            }
        }
        return false;
    }
    virtual double totale() const{
        double totale = 0.0;
        for(auto x:Lista){
            Prodotto prodotto = x.first;
            totale += prodotto.get_prezzo()*x.second;
        }
        return totale;
    }
};

class ListaDellaSpesaScontata:public ListaDellaSpesa{
    public:
    virtual double totale() const override{
        double totale = 0.0;
        for(auto x:Lista){
            Prodotto prodotto = x.first;
            int quant = x.second;
            if(quant>5){
                totale+=((prodotto.get_prezzo()*quant)*0.25);
            }
            else totale+=(prodotto.get_prezzo()*quant);
        }
        return totale; //mancava il return
    } 
};

int main(){
    Prodotto pasta = Prodotto("pasta", 1.0);
    Prodotto pane = Prodotto("pane", 2.0);
    Prodotto riso = Prodotto("riso", 3.0);
    Prodotto sugo = Prodotto("sugo", 3.0);
    Prodotto mele = Prodotto("mele", 1.0);
    ListaDellaSpesa lista1;
    lista1.inserisci(pasta, 10);
    lista1.inserisci(pane, 1);
    lista1.inserisci(riso, 4);
    lista1.inserisci(sugo, 2);
    lista1.inserisci(mele, 12);
    ListaDellaSpesaScontata lista2 ;
    lista2.inserisci(pasta, 10);
    lista2.inserisci(pane, 1);
    lista2.inserisci(riso, 4);
    lista2.inserisci(sugo, 2);
    lista2.inserisci(mele, 12);
    cout << lista1.totale() << endl;
    cout << lista2.totale() << endl;
  


    return 0;
}
