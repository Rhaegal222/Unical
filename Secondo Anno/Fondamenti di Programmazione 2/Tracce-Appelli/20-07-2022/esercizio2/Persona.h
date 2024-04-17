#include <iostream>
#include <string>
using namespace std;

class Persona{
private:
    string nome, cognome;
public:
    Persona(){};
    Persona(string nome, string cognome){
        this->nome = nome;
        this->cognome = cognome;
    };
    string getNome()const{return this-> nome;}
    string getCognome()const{return this-> cognome;}
    void setNome(string nome){this->nome = nome;}
    void setCognome(string cognome){this->cognome = cognome;}
    virtual int getStipendio() const = 0;
    ~Persona(){};
};

class Studente : public Persona{
    public:
    Studente():Persona(){};
    Studente(string nome, string cognome):Persona{nome, cognome}{};
    virtual int getStipendio() const override{return 10;}
};

class Impiegato : public Persona{
    public:
    Impiegato():Persona(){};
    Impiegato(string nome, string cognome):Persona(nome, cognome){};
    virtual int getStipendio() const override{return 100;}
};
