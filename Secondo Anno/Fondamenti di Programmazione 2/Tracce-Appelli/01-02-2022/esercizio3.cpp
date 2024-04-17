#include <iostream>
#include <vector>
#include <list>

#include "Grafo.h"

using namespace std;

int f(Grafo& g, unsigned nodo){ //f(u)
    int valore = 0;
    vector<bool> visited(g.n(), false);
    for(int i=0; i<g.n(); i++) if(!TrovaCammino(g,visited,i,nodo)) valore++;
    return valore;
};

vector<unsigned> vicinatoFattaMoMo(Grafo& g, int nodo){
    vector<unsigned> vicinato;
    for(int i=0; i<g.n(); i++) if(g(nodo,i)) vicinato.push_back(i);
    return vicinato;
}

bool TrovaCammino(Grafo& g, vector<bool> visited, int nodo, int dest){
    if(nodo==dest) return true;
    
    visited[nodo] = true;
    vector<unsigned> vicinato = vicinatoFattaMoMo(g, nodo);
    
    for(auto x:vicinato) if(!visited[x]) return TrovaCammino(g, visited, x, dest);
    
    return false;
}

int esercizio3(Grafo& g){
    pair<int, int> nodo_valore = make_pair(g.n(), -1);
    for(int i=0; i<g.n(); i++){
        int valore = f(g, i);
        if(valore > nodo_valore.second){
            nodo_valore.first = i;
            nodo_valore.second = valore;
        }
    }
    return nodo_valore.first;
}

int main(){
    Grafo g(5);
    g(0,1,true); g(0,4,true);
    g(1,4,true);
    g(2,3,true);g(2,0,true);
    g(3,1,true);

    cout << "Esercizio3: " << esercizio3(g) << endl;
    return 0;
}

