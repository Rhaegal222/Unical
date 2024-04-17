#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "AlberoB.h"

using namespace std;

void esercizio3(const AlberoB<int>& tree, int& value, bool& trovato, vector<int> percorso){
    if(tree.nullo()){
        return;
    }

    percorso.push_back(tree.radice());

    if(tree.radice()==value){
        trovato = true;
        for(auto i:percorso) cout << i << " ";
        return;
    }

    esercizio3(tree.figlio(DES), value, trovato, percorso);
    esercizio3(tree.figlio(SIN), value, trovato, percorso);
    
    if(!trovato && tree.padre().nullo()){ 
        percorso.clear(); percorso.push_back(-1);
        for(auto i:percorso) cout << i << " ";
        return;
    }
    return;
}

int main(){

AlberoB<int> CINQUE(5);
AlberoB<int> SEI(6);
AlberoB<int> DODICI(12);
AlberoB<int> DIECI(10);
AlberoB<int> QUARANTADUE(42);
AlberoB<int> TRENTADUE(32);

CINQUE.insFiglio(SIN,SEI);
CINQUE.insFiglio(DES,DODICI);
SEI.insFiglio(SIN, DIECI);
DODICI.insFiglio(SIN, QUARANTADUE); DODICI.insFiglio(DES, TRENTADUE);

int value = 10;
vector<int>percorso;
bool trovato = false;
esercizio3(CINQUE, value, trovato, percorso);
//for(auto x:percorso) cout << x << " ";
}