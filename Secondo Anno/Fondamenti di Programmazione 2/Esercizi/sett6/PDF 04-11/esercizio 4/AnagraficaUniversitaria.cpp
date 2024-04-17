#include "Persona.h"
#include <Vector>
using namespace std;

class AnagraficaUniversitaria{
private:
    vector<Persona> regUni;
public:
    AnagraficaUniversitaria(){};

    bool cercaPersona(Persona& persona){
        vector<Persona>::iterator it;
        if(regUni.empty()) return false;
        for(it=regUni.begin(); it!=regUni.end(); it++){
            if(persona.get_codiceFiscale() == (*it).get_codiceFiscale())
                return true;
        }
        return false;
    }

    void aggiungiStudente(Studente& studente){
        if(!cercaPersona(studente)) 
            regUni.push_back(studente);
    }

    void aggiungiProfessore(Professore& professore){
        if(!cercaPersona(professore))
        regUni.push_back(professore);}

    Persona* getPersona(string codiceFiscale) const{
        Persona* const persona = nullptr;
        if(regUni.empty()) return persona;
        for(int i=0; i!=regUni.size(); i++){
            if(codiceFiscale == regUni[i].get_codiceFiscale()){
                Persona p = regUni[i];
                Persona *const persona = &p;
                return persona;
            }
        }
        return persona;
    }

    void stampa() const{
        for(int i=0; i<=regUni.size(); i++){
            cout << regUni[i];
        }
    }
};
