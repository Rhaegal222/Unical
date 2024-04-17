#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;

void next(int& index){
    index++;
}

void remove(vector<string>& C){
    C.pop_back();
}

bool isComplete(vector<vector<string>>& L, vector<string>& C, int& k){
    if(C.size()<k) return false;
    for(auto y:C)cout<<y<<" ";cout<<endl;
    vector<bool> condL(L.size(), false); //inizializzo un vettore tutto falso che indica le stringhe che non violano la condizione
    for(int i=0; i<L.size(); i++){
        vector<bool> condC(L[i].size(), false);
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

void add(vector<string>& S, vector<string>& C, int index){
    C.push_back(S[index]);
}

bool canAdd(vector<string>& S, vector<string>& C, int& index){
    if(find(C.begin(), C.end(), S[index]) == C.end()) return true;
    return false;
}

bool esercizio4(vector<string>& S, vector<vector<string>>& L, vector<string>& C, int& k){
    int index = 0;
    while(index < S.size()){
        if(canAdd(S, C, index)){
            add(S, C, index);
            if(isComplete(L, C, k)) return true;
            else if(esercizio4(S,L,C,k)) return true; remove(C); next(index);
        }
        else next(index);
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
