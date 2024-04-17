#include "GrafoNonOrientato.h"
#include <iostream>
#include <vector>
using namespace std;

int grado(GrafoNonOrientato& g, unsigned& nodo){ //ho messo int invece di unsigned
    int valore = 0;
    for(int i=0; i<g.n();i++){
        if(g(nodo,i))valore++;
    }
    return valore;
}

bool isComplete(GrafoNonOrientato& g, int& k, vector<unsigned>& W){
    if(W.size()<k) return false;
    for(int i=0; i<W.size(); i++){
        for(int j=0; j<W.size(); j++){
            if(i!=j){
                if(g(W[i],W[j])) return false; // ho messo if(g(i,j))
            }
        }
    }
    int somma = 0;
    for(auto x:W){
        somma+=grado(g,x);
    }
    if(somma>g.n()) return false;
    return true;
}

bool esercizio4(GrafoNonOrientato& g, int& k, vector<unsigned>& W, int index){
    for(int i=index;i<g.n();i++){
        W.push_back(i);
        if(isComplete(g,k,W)) return true;
        if(esercizio4(g,k,W,i+1)) return true;
        W.pop_back();
    }
    return false;
}

int main(){
    GrafoNonOrientato g(4);
    g(0,1,true);g(0,2,true);g(0,3,true);
    g(1,2,true);//g(1,3,true);
    g(2,3,true);

    int k = 3;
    vector<unsigned> W;

    if(esercizio4(g,k,W,0))cout<<"SI"; else cout<<"NO";

    return 0;
}
