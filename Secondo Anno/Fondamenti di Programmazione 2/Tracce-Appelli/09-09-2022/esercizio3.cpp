#include <iostream>
#include "Grafo.h"

using namespace std;

bool esercizio3(Grafo& g, vector<vector<int>> weights){
    vector<int> sumArcIn(g.n(), 0);
    for(int i=0; i<g.n(); i++)
        for(int j=0; j<g.n(); j++)
            sumArcIn[j] += weights[i][j];
    for(int i=0; i<g.n(); i++) if(sumArcIn[i] > g.dep(i)) return false;
    for(int i=0; i<g.n(); i++)
        for(int j=0; j<g.n(); j++)
            if(weights[i][j]>0 && g.dep(i)<g.dep(j)) return false;
    return true;
}

int main(){
    vector<vector<int>> weights{
        {0,2,0,0},
        {0,0,3,1},
        {0,2,0,2},
        {0,0,0,0},
    };

    Grafo g(4);
    g(0,1,true);
    g(1,2,true);g(1,3,true);
    g(2,1,true);g(2,3,true);

    if(esercizio3(g,weights)) cout << "SI";
    else cout << "NO";
    
}
