#ifndef Dipendente2_h
#define Dipendente2_h

#include <string>
#include <iostream>
using namespace std;

class Dipendente{
private:
    string id;
    string nome;
    string cognome;
    float stipendio;

public:

    Dipendente(){}; //COSTRUTTORE DI DEFAULT: serve per costruire l'oggetto senza passare i parametri
    Dipendente(string id, string nome, string cognome, float stipendio); //PROTOTIPO: serve per costruire l'oggetto con i parametri. COSTRUTTORE A RIGA 34.
    ~Dipendente(); //DISTRUTTORE RIGA 42

    //setters
    void setId(string id) { this->id = id; }
    void setNome(string nome) { this->nome = nome; }
    void setCognome(string cognome) { this->cognome = cognome; }
    void setStipendio(float stipendio) { this->stipendio = stipendio; }

    //getters
    string getId() const {return id;}; 
    string getNome() const {return nome;};
    string getCognome() const {return cognome;};
    float getStipendio() const {return stipendio;}

};

//COSTRUTTORE
Dipendente::Dipendente(string id, string nome, string cognome, float stipendio): 
    id{id}, //AttributoDellaClasse{Parametro}, si devono omettere i this->
    nome{nome},
    cognome{cognome},
    stipendio{stipendio}
{}

//ALTRO MODO DI DICHIARARE IL COSTRUTTORE COME SOPRA
/*
Dipendente::Dipendente(string id, string nome, string cognome, float stipendio){
    this->id = id; // attenzione: usare id = id; lascerebbe il membro di classe Dipendente::id inalterato.
    this->nome = nome; //this->AttributoDellaClasse = Parametro
    this->cognome = cognome;
    this->stipendio = stipendio;
}
*/

Dipendente::~Dipendente() {
    // Deallocate the memory that was previously reserved for this objects.
    cout << "Oggetto Eliminato" << endl;
}

#endif