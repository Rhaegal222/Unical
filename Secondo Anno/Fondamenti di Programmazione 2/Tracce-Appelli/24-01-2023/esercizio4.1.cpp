#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool isComplete(vector<vector<int>>& S, vector<int>& H){
    for(auto x:S){ //scorre il vettore delle stringhe
        bool cond = false; 
        for(auto y:H) if(find(x.begin(), x.end(), y)!=x.end()) cond = true; //scorre la combinazione e controlla che il carattere selezionato è presente nella stringa
        if(!cond) return false; //se non è presente almeno un carattere della combinazione nella sottostringa restituisce falso
    }
    return true; //la condizione è verificata
}

bool esercizio4(vector<vector<int>>& S, vector<int>& H, int& k, int& n, int index){
    //if(H.size()>0) for(auto x:H) cout<<x<< " "; cout<<endl;

    if(H.size() == k){ 
        if(isComplete(S, H)) return true; 
        return false; 
    }
    
    for(int i=index; i<n; i++){
        H.push_back(i);
        if(esercizio4(S, H, k, n, i+1)) return true;
        H.pop_back();
    }
    return false;
}

int main(){
    vector<vector<int>> S{{1, 2, 3}, {4, 3, 5}, {5, 6}};
    vector<int> H;
    int k = 3, n = 5;
    int cont = 0;
    if(esercizio4(S,H,k,n,0)) cout << "SI"; else cout << "NO"; cout << endl;
    cout << cont;
    
    return 0;
}
