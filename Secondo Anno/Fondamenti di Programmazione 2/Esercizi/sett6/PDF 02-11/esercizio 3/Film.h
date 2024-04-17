#ifndef FILM_H_
#define FILM_H_

#include <iostream>
#include <string>
using namespace std;

enum Genere { NONDEFINITO = 0, ANIMAZIONE, COMICO, COMMEDIA, DRAMMATICO, FANTASY, HORROR, STORICO };    

class Film
{
    private:
        string titolo;
        int anno;
        int incasso;
        string regista;
        Genere genere;
    
    public:
        Film(string _titolo = "", int _anno = 0, int _incasso = 0, string _regista = 0, Genere _genere = NONDEFINITO) : titolo(_titolo), anno(_anno), incasso(_incasso), regista(_regista), genere(_genere) {}
    
        string getTitolo() const { return titolo; }
        void setTitolo(string v) { titolo = v; }
    
        int getAnno() const { return anno; }
        void setAnno(int v) { anno = v; }
    
        int getIncasso() const { return incasso; }
        void setIncasso(int v) { incasso = v; }
    
        string getRegista() const { return regista; }
        void setRegista(string v) { regista = v; }
    
        Genere getGenere() const { return genere; }
        void setGenere(Genere v) { genere = v; }
    
        bool operator==(const Film& right) const {
            return titolo == right.titolo && anno == right.anno && incasso == right.incasso && regista == right.regista && genere == right.genere;
        }
    
        friend ostream& operator<<(ostream& out, const Film& x) {
            return out << "[" << x.titolo << ", " << x.anno << ", " << x.incasso << ", " << x.regista << ", " << x.genere << "]";
        }
};

#endif
