#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isComplete(vector<vector<int>>& S, vector<int>& H, int& k){
    for(auto x:H) cout<<x<< " "; cout<<endl;
    if(H.size() < k) return false;
    for(auto x:S){ //scorre il vettore delle stringhe
        bool cond = false; 
        for(auto y:H) if(find(x.begin(), x.end(), y)!=x.end()) cond = true; //scorre la combinazione e controlla che il carattere selezionato è presente nella stringa
        if(!cond) return false; //se non è presente almeno un carattere della combinazione nella sottostringa restituisce falso
    }
    return true; //la condizione è verificata
}

bool canAdd(int index, vector <int> sol){
    if(find(sol.begin(), sol.end(), index) == sol.end()) return true; // se nella soluzione non è presente un elemento uguale lo aggiunge
    return false;
}

bool esercizio4(vector<vector<int>>& S, vector<int>& H, int& k, int& n){
    int index = 0;
    if(!(H.empty())) index = H.back(); //evita la ripetizione delle combinazioni
    while(index < n){
        if(canAdd(index, H)){
            H.push_back(index);
            if(isComplete(S, H, k))return true;
            if(esercizio4(S,H,k,n)) return true;
            H.pop_back();
        }
        index++;
    }
    return false;
}

int main(){
    vector<vector<int>> S{{1, 2, 3}, {4, 3, 5}, {5, 6}};
    vector<int> H;
    int k = 1, n = 5;

    if(esercizio4(S,H,k,n)) cout << "SI"; else cout << "NO"; cout << endl;
    
    return 0;
}