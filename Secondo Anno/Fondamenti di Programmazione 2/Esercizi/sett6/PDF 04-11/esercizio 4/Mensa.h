#ifndef __MENSA__H__
#define __MENSA__H__

#include "AnagraficaUniversitaria.cpp"
using namespace std;

class Mensa : public AnagraficaUniversitaria{
private:
    vector<Persona> regMensa;
public:
    Mensa(){};

    void accesso(Persona* p){
        if(!cercaPersona(*p)){
            regMensa.push_back(*p);
            cout << "Aggiunto: " << *p << endl;
        }
        else 
            cout << "Hello" << endl;
    }

    void stampa() const {
        for(int i=0; i<=regMensa.size(); i++){
            cout << regMensa[i];
        }
    }

    //float calcolaIncassoGiornaliero() const{
    //    float incasso = 0;
    //    vector<Persona>::const_iterator it;
    //    for(it=regMensa.begin(); it!=regMensa.end(); it++)
    //        
    //    return incasso;
    //}

    void nuovoGiorno(){return regMensa.clear();} 
};

#endif  //!__MENSA__H__