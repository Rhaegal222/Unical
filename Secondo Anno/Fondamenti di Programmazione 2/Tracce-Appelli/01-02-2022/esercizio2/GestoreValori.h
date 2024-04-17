#ifndef __GESTOREVALORI__H__
#define __GESTOREVALORI__H__

#include <iostream>
#include <vector>
using namespace std;

class GestoreValori{
protected:
    vector<pair<int, char>> Valori;
public:
    GestoreValori(){};
    void inserisciCoppia(int a, char b){
        Valori.push_back(make_pair(a, b));
    }
    int numCoppie() const {return Valori.size();}
    virtual int getRisultato() const {return -1;}
};

class GestoreValoriA : public GestoreValori{
public:
    GestoreValoriA():GestoreValori(){};
    virtual int getRisultato() const override{
        int somma = 0;
        for(auto i : Valori){
            if(i.second == 'a')
                somma+=i.first;
        }
        return somma;
    }
};

class GestoreValoriB : public GestoreValori{
public:
    GestoreValoriB():GestoreValori(){};
    virtual int getRisultato() const override{
        int somma = 0, media = 0;
        int b = 0;
        for(auto i : Valori){
            if(i.second == 'b'){
                somma+=i.first;
                b++;
            }
        }
        if(b > 0) int media = somma / b;
        return media;
    }
};

#endif  //!__GESTOREVALORI__H__