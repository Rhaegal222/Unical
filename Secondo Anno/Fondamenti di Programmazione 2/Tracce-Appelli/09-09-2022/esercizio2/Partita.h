#ifndef __PARTITA__H__
#define __PARTITA__H__

#include <string>
using namespace std;

class Partita
{
private:
    string squadraCasa, squadraOspite;
    int goalCasa, goalOspite;
    
public:
    Partita(string squadraCasa, string squadraOspite, int goalCasa, int goalOspite){
        this->squadraCasa=squadraCasa;
        this->squadraOspite=squadraOspite;
        this->goalCasa=goalCasa;
        this->goalOspite=goalOspite;
    };

    //getters
    string getSquadraCasa() const {return this->squadraCasa;}
    string getSquadraOspite() const {return this->squadraOspite;}
    int getGoalCasa() const {return this->goalCasa;}
    int getGoalOspite() const {return this->goalOspite;}

    //setters
    void setSquadraCasa(string squadra){this->squadraCasa = squadra;}
    void setSquadraOspite(string squadra){this->squadraOspite = squadra;}
    void setGoalCasa(int goal){this->goalCasa = goal;}
    void setGoalOspite(int goal){this->goalOspite = goal;}
    ~Partita(){};
};

#endif  //!__PARTITA__H__