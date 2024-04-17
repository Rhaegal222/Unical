#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

bool isComplete(vector<vector<string>>& L, vector<string>& C, int& q){
    if(C.size()<q) return false;
    //for(auto y:C)cout<<y<<" ";cout<<endl;
    vector<bool> condL(L.size(), false); //inizializzo un vettore tutto falso che indica le stringhe che non violano la condizione
    for(int i=0; i<L.size(); i++){ //scorre le liste di stringhe
        vector<bool> condC(L[i].size(), false); //inizializzo un vettore tutto falso che indica quante leggere uguali ci sono nella combinazione generata (P)
        for(int j=0; j<L[i].size(); j++){ // prendo la lettera della stringa
            for(int k=0; k<C.size(); k++){ // prendo la lettera in P
                if(L[i][j]==C[k]) condC[j] = true; // confronto se la lettera della stringa i == alla lettera della stringa P
            }
        }
        for(auto l:condC){
            if(!l) condL[i] = true;
        }
    }
    for(auto x:condL) if(!x) return false;
    return true;
}

bool canAdd(vector<string>& S, vector<string>& C, int& index){
    if(find(C.begin(), C.end(), S[index]) == C.end()) return true;
    return false;
}

bool esercizio4(vector<string>& S, vector<vector<string>>& L, vector<string>& C, int& q){
    int index = 0;
    if(!(C.empty())) index = find(S.begin(),S.end(),C.back()) - S.begin();
    while(index < S.size()){
        if(canAdd(S, C, index)){
            C.push_back(S[index]);
            if(isComplete(L, C, q)) return true;
            if(esercizio4(S,L,C,q)) return true; 
            C.pop_back();
        }
        index++;
    }
    return false;
}

int	main()
{
    vector<string> S{"a", "b", "c", "d", "e", "f"};
    vector<vector<string>> L{{"a"}, {"b"}, {"c"}, {"d"}, {"e"}, {"f"}, {"a", "b", "c"}, {"a", "d"}, {"d", "e"}, {"b", "f"}};
    vector<string> C;
    int q=3;
    if(esercizio4(S, L, C, q)) cout << "ESISTE"; else cout << "NON ESISTE";

    return 0;
}
