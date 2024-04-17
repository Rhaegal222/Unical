#ifndef __PERSONA__H__
#define __PERSONA__H__

#include <iostream>
#include <string>

using namespace std;

class Persona
{
protected:
    string codiceFiscale, nome, cognome;
public:
    Persona(string codiceFiscale, string nome, string cognome) : codiceFiscale{codiceFiscale}, nome{nome}, cognome{cognome}{}

    Persona(const Persona& persona):            
    codiceFiscale{persona.codiceFiscale}, nome{persona.nome}, cognome{persona.cognome}{}

    string get_codiceFiscale() const {return codiceFiscale;}
    string get_nome() const {return nome;}
    string get_cognome() const {return cognome;}

    friend ostream& operator<<(ostream& o, const Persona& p){
        cout << p.codiceFiscale << " " << p.cognome << " " << p.nome << endl;
        return o;
    }
};

class Studente : public Persona{
private:
    float isee;
public:
    Studente(string codiceFiscale, string nome, string cognome, float isee) : Persona{codiceFiscale, nome, cognome},
    isee{isee}{}
};

class Professore : public Persona{
private:
    float stipendio;
public:
    Professore(string codiceFiscale, string nome, string cognome, float stipendio) : Persona{codiceFiscale, nome, cognome},
    stipendio{stipendio}{}
};

#endif  //!__PERSONA__H__