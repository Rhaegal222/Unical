#include <iostream>
#include "Grafo.h"

using namespace std;

int transfer(int i, int j){
    //vector<vector<int>> transfers{{0, 0, 3, 0},{1, 0, 0, 0},{1, 0, 0, 0},{0, -2, 0, 0}};//NO
    //vector<vector<int>> transfers{{0, 0, 1, 0},{1, 0, 0, 0},{1, 0, 0, 0},{0, 1, 0, 0}}; //SI
    vector<vector<int>> transfers{{0, 0, 2, 0},{3, 0, 0, -2},{2, 0, 0, 0},{0, 1, 0, 0}};//SI
    return transfers[i][j];
}

bool esercizio3(){
    Grafo g(4);
    g(0,2,true);
    g(1,0,true);g(1,3,true);
    g(2,0,true);
    g(3,1,true);

    int k1, k2;
    cin >> k1 >> k2;
    
    //verifico condizione 1:
    for(int i=0; i<g.n(); i++){
        for(int j=0; j<g.n(); j++){
            int value = transfer(i,j);
            if(g(i,j) && (value<k1 || value>k2)){
                return false;
            }
        }
    }
    //cout << "Controllo 1: PASSED" << endl;

    vector<unsigned> gradi_in(g.n(), 0);
    
    for(int i=0; i<gradi_in.size(); i++){
        int transfer_in = 0, transfer_out = 0;
        for(int j=0; j<gradi_in.size(); j++){
            if(g(j,i)){
                transfer_in += transfer(j,i);
                gradi_in[i]++;
            }
            if(g(i,j)){
                transfer_out += transfer(i,j);
            }
        }
        //cout << "Gradi: " << gradi_in[i] << " TI: " << transfer_in << " TO: " << transfer_out;
        if(gradi_in[i]%2 && (transfer_in > transfer_out)) return  false;
        else if(!(gradi_in[i]%2) && (transfer_in < transfer_out)) return false;
    }
    return true;
}

int main(){
    if(esercizio3()) cout << "SI";
    else cout << "NO";
    return 0;
}
