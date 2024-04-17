#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

#include "Grafo.h"

using namespace std;

bool isComplete(Grafo& g, vector<unsigned> U, int& k1, int& k2){
    if(U.size()<k1 || U.size() > k2) return false;
    return true;
}

bool canAdd(Grafo& g, vector<unsigned>& U, unsigned& index){
    if(find(U.begin(), U.end(), index)!=U.end())return false;
    for(auto x:U)if(g(index,x))return false;
    return true;
}

bool esercizio4(Grafo& g, int& k1, int& k2, vector<unsigned>& U){
    unsigned index = 0; //inizializza index;
    //if(!(U.empty())) index = U.back(); //siccome gli elementi aggiunti in U sono in ordine crescente per evitare di ripetere le combinazioni inizializzo l'index a quello più grande al momento
    while(index<g.n()){
        if(canAdd(g, U, index)){
            U.push_back(index);
            for(auto x:U) cout << x << " "; cout << endl;
            if(isComplete(g, U, k1, k2)) return true;
            if(esercizio4(g, k1, k2, U)) return true;
            U.pop_back();
        }
        index++;
    }
    return false;
}

int main(){
    Grafo g(4);
    g(0,3,true);
    g(1,0,true);g(1,3,true);
    g(2,0,true);g(2,3,true);

    int k1 = 4, k2 = 3;
    vector<unsigned> U;

    if(esercizio4(g,k1,k2,U)) cout << "ESISTE"; else cout << "NON ESISTE"; cout << endl;

    return 0;
}
