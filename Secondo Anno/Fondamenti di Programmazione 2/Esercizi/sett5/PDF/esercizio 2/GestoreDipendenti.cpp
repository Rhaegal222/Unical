#include "GestoreDipendenti.h"
#include <iostream>
#include <algorithm>
using namespace std;

bool GestoreDipendenti::esisteDipendente(string id) const {
    for (int i = 0; i < dipendenti.size(); i++)
        if(dipendenti[i].getId() == id)
            return true;
    return false;
}

bool GestoreDipendenti::aggiungiDipendente(Dipendente d){
    if(!esisteDipendente(d.getId())){
        dipendenti.push_back(d);
        return true;
    }
    return false;
}

void GestoreDipendenti::rimuoviDipendente(string id){
    if(!esisteDipendente(id)) return;

    for(vector<Dipendente>::iterator it = dipendenti.begin(); it != dipendenti.end(); it++){
        if(it->getId() == id){
            dipendenti.erase(it);
            return;
        }
    }
}

void GestoreDipendenti::stampa() const {
    for(int i = 0; i < dipendenti.size(); i++) 
        cout << dipendenti[i];
}

float GestoreDipendenti::calcolaCostoDipendenti() const {
    float sum = 0.0;
    for(int i = 0; i < dipendenti.size(); i++)
        sum += dipendenti[i].getStipendio();

    return sum;

}