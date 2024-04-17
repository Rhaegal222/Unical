#ifndef __GESTOREPARTITE__H__
#define __GESTOREPARTITE__H__

#include <list>
#include <vector>
#include <iostream>
#include <algorithm>

#include "Partita.h"

using namespace std;

class GestorePartite
{
private:
    list<Partita*> partite;

public:
    GestorePartite(){};
    ~GestorePartite(){};

    void aggiungiPartita(string squadraCasa, string squadraOspite, int goalCasa, int goalOspite){
        Partita* partita = new Partita(squadraCasa, squadraOspite, goalCasa, goalOspite);
        partite.push_back(partita);
    }

    string getSquadraPiuForte()const{
        vector<string> Squadre;
        
        for(auto x:partite){
            string Squadra = x->getSquadraCasa();
            if(find(Squadre.begin(), Squadre.end(), Squadra)==Squadre.end()) Squadre.push_back(Squadra);
            
            Squadra = x->getSquadraOspite();
            if(find(Squadre.begin(), Squadre.end(), Squadra)==Squadre.end()) Squadre.push_back(Squadra);
        }

        vector<int> vittorie(Squadre.size(), 0);
        for(int i=0; i<vittorie.size(); i++){
            string Squadra = Squadre[i];
            for(auto x:partite){
                if(x->getSquadraCasa() == Squadra && (x->getGoalCasa()>x->getGoalOspite())) vittorie[i]++;
                if(x->getSquadraOspite() == Squadra && (x->getGoalOspite()>x->getGoalCasa())) vittorie[i]++;
            }
        }

        pair<string, int> best("",-1);
        for(int i=0; i<vittorie.size(); i++){
            if(vittorie[i] > best.second){
                best.second = vittorie[i];
                best.first = Squadre[i];                
            }
        }
        return best.first;
    }

    double mediaGoal()const{
        if(partite.size() < 1) return 0;
        int sumGoal = 0;
        for(auto x:partite) sumGoal += (x->getGoalCasa()+x->getGoalOspite());
        return sumGoal / partite.size();
    }

    GestorePartite(GestorePartite& p){
        for(auto x:p.partite){
            this->partite.push_back(x);
        }
    }

    void stampaPartite(){
            for(auto x:partite){
                Partita match = *x;
                cout << match.getSquadraCasa() << " " << match.getGoalCasa() << " - " << match.getGoalOspite() << " " << match.getSquadraOspite() << endl;
        }
    }
};

#endif  //!__GESTOREPARTITE__H__