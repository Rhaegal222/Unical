#include <vector>
#include <iostream>
#include <string>
using namespace std;

bool check(vector<string>& P, vector<vector<string>>& L){
    vector<bool> condL(L.size(), false); //inizializzo un vettore tutto falso che indica le stringhe che non violano la condizione
    for(int i=0; i<L.size(); i++){
        vector<bool> condP(L[i].size(), false); //for(auto y:P)cout<<y<<" ";
        for(int j=0; j<L[i].size(); j++){ // prendo la lettera della stringa
            for(int k=0; k<P.size(); k++){ // prendo la lettera in P
                if(L[i][j]==P[k]) condP[j] = true; // confronto se la lettera della stringa i == alla lettera della stringa P
            }
        }
        for(auto l:condP){
            if(!l) condL[i] = true;
        }
    }
    for(auto x:condL) if(!x) return false;
    return true;
}
/*Combinazioni senza ripetizione*/
bool esercizio4(vector<string>& S, vector<vector<string>>& L, vector<string>& P, int& q, int start){
        //cout << " {"; for(auto x:P) cout << x << ", "; cout << "}" << endl;
    if(P.size() == q){
        if(check(P, L)){ //se la dimensione della combinazione é quella richiesta verifico la condizione
            return true;
        }
    }
    for(int i = start; i < S.size(); i++){
        P.push_back(S[i]);
        if(esercizio4(S, L, P, q, i+1)) return true;
        P.pop_back();
    }
    return false;
}

int	main()
{
    vector<string> S{"a", "b", "c", "d", "e", "f"};
    vector<vector<string>> L{/*{"a"}, {"b"}, {"c"}, {"d"}, {"e"}, {"f"},*/ {"a", "b", "c"}, {"a", "d"}, {"d", "e"}, {"b", "f"}};
    int q=3;
    vector<string> combination; // crea un vettore di q elementi nulli
    if(esercizio4(S, L, combination, q, 0)) cout << "ESISTE"; else cout << "NON ESISTE";

    return 0;
}
