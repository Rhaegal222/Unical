#include "Cinema.h"
#include <climits>
#include <vector>
using namespace std;

void Cinema::aggiungi(Film* f) {
    film.push_back(f);
}

void Cinema::calcolaGeneri(list<Genere>& generi) const {
    for(auto elem : film) {
        bool trovato = false;
        for(auto elem2 : generi)
            if(elem->getGenere() == elem2)
                trovato = true;
        if(!trovato)
            generi.push_back(elem->getGenere());
    }
    generi.sort();
}

void Cinema::calcolaRegisti(list<string>& registi) const {
    for(auto elem : film) {
        bool trovato = false;
        for(auto elem2 : registi)
            if(elem->getRegista() == elem2)
                trovato = true;
        if(!trovato)
            registi.push_back(elem->getRegista());
    }
}

Genere Cinema::migliorGenere() const
{
    if(film.empty())
        return NONDEFINITO;
	int max = -1;
	Genere genMAX = NONDEFINITO;
	list<Genere> generi;
	calcolaGeneri(generi);
	for(auto elem : generi) {
	    if(elem == NONDEFINITO)
	        continue;
	    int incasso = 0;
	    for(auto f : film) {
	        if(f->getGenere() == elem) {
	            incasso += f->getIncasso();
	        }
	    }
	    if(incasso > max) {
	        max = incasso;
	        genMAX = elem;
	    }
	}
	return genMAX;
}

string Cinema::registaStanco() const
{
    if(film.empty())
        return "-1";
    
    list<string> registi;
    calcolaRegisti(registi);
    registi.sort();
    
    int annoMax = INT_MIN;    
    for(auto f : film) {
        if(f->getAnno() > annoMax)
            annoMax = f->getAnno();
    }
    
    int min = INT_MAX;
    string r = "";
    for(auto regista : registi) {
        int count = 0;
        for(auto f : film) {
            if(f->getAnno() == annoMax && f->getRegista() == regista)
                count++;
        }
        
        if(count < min) {
            min = count;
            r = regista;
        }
    }
    
    return r;
}

int Cinema::registiSettoriali() const
{
    if(film.empty())
        return -1;
    
    list<string> registi;
    calcolaRegisti(registi);
    
    list<Genere> generi;
    calcolaGeneri(generi);    
    
    int settoriali = 0;    
    for(auto elem : registi) {
        vector<int> numeroFilmPerGenere;
        int numeroFilm = 0;
        for(auto genere : generi) {
            int count = 0;
            for(auto f : film) {
                if(f->getRegista() == elem && f->getGenere() == genere) {
                    count++;
                    numeroFilm++;
                }
            }
            numeroFilmPerGenere.push_back(count);
        }
                    
        for(auto n : numeroFilmPerGenere) {
            if((n*100/numeroFilm) >= 70) {
                settoriali++;
                break;
            }
        } 
    }
    
    return settoriali;
}

int Cinema::differenzaIncassoMaggiore() const
{
    if(film.size() < 2)
        return -1;
    
    int incassoMin = INT_MAX;
    int incassoMax = INT_MIN;
    for(auto f : film) {
        int incasso = f->getIncasso();
        if(incasso < incassoMin)
            incassoMin = incasso;                        
        if(incasso > incassoMax)
            incassoMax = incasso;
    }
    
    return incassoMax - incassoMin;
}


