#include "Grafo.h"
#include <iostream>

using namespace std;

bool esercizio3(const Grafo& g, const vector<int> W){
    vector<int> arc_in(g.n(), 0);
    vector<int> arc_out(g.n(), 0);
    for(int i=0; i<g.n(); i++){
        for(int j=0; j<g.n(); j++){
            if(i!=j){
                if(g(i,j))arc_out[i]+=W[j];
                if(g(j,i))arc_in[i]+=W[j];
            }
        }
    }

    for(int i=0; i<g.n(); i++)if(arc_out[i]<arc_in[i])return false;
    return true;
}

int main(){

    vector<int> W{0,2,4,0};
    Grafo g(4);
    g(0,1,true); g(0,2,true);
    g(3,1,true); g(3,2,true);
    
    if(esercizio3(g,W)) cout << "CONDIZIONE RISPETTATA";
    else cout << "CONDIZIONE NON RISPETTATA"; cout << endl;
    
    return 0;
}
