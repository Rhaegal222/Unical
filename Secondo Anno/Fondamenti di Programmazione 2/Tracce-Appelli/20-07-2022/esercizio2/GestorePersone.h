#include "Persona.h"
#include <iostream>
#include <vector>

using namespace std;

class GestorePersone
{
private:
    vector<Persona*> persone;
public:
    GestorePersone(){};
    void aggiungiPersona(Persona* p){
        persone.push_back(p);
    }
    double getStipendioMedio(){
        double sum = 0;
        for(auto x:persone) sum+=x->getStipendio();
        int num_persone = persone.size();
        if(num_persone>0) return sum / num_persone;
        else return sum;
    }
    ~GestorePersone(){};
};
