#include <iostream>
#include <vector>

using namespace std;

/*Parametri: 
    I: vector di elementi di tipo generico;
    k: numero di elementi distinti (se k=-1 stampa tutte le combinazioni contenenti da 1 a N elementi);
    C: vector vuoto dello stesso tipo di I
    s: 0 di default
*/

template<class T> void Combinazioni_Semplici(vector<T>& I, int k, vector<T>& C, int s){
    if(k==-1 && C.size()>0){cout << " { "; for(auto x:C) cout << x << " "; cout << "}" << endl;}

    if(C.size()==k){cout << "{ "; for(auto x:C) cout << x << " "; cout << "}" << endl;}

    for(int i=s;i<I.size();i++){
        C.push_back(I[i]);
        Combinazioni_Semplici(I, k, C, i+1);
        C.pop_back();
    }
}

int main()
{
    /* Combinazioni Semplici */
    vector<string> S{"a","b","c"};
    vector<string> C;
    Combinazioni_Semplici(S,-1,C,0);
    return 0;
}
