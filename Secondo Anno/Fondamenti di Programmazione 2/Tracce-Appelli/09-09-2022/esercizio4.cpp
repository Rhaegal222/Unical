#include <iostream>
#include <vector>
using namespace std;

bool check(vector<string> W, vector<vector<string>>& T){
    for(int i=0; i<W.size(); i++){//scorre la stringa generata e seleziona un carattere
        vector<string> coppia; coppia.push_back(W[i]);//inserisco la prima lettera della coppia
        for(int j=0; j<W.size(); j++){//scorre la stringa generata e seleziona un carattere
            if(i!=j){
                coppia.push_back(W[j]);//inserisco la seconda lettera della coppia
                vector<bool> condTransizioni(T.size(), true);
                for(auto k=0;k<T.size();k++){ //scorre il vettore delle transizioni
                    vector<string> transizione = T[k];
                    vector<bool> condCoppia(2, true);
                    for(int l=0; l<coppia.size(); l++) //scorre la coppia
                        for(auto m:transizione) //scorre la transizione
                            if(coppia[l] == m) condCoppia[l] = false; //setta la lettera dalla coppia a true
                    int contCondCoppia = 0;
                    for(auto n:condCoppia) if(!n) contCondCoppia++;
                    if(contCondCoppia==2) condTransizioni[k] = false;
                }
                for(auto o:condTransizioni)if(!o)return false;
                coppia.pop_back();
            }
        }
        coppia.pop_back();
    }
    return true;
}

bool esercizio4(vector<string>& V, vector<vector<string>>& T, int& k, vector<string> W, int start){
    cout << start << " {"; for(auto x:W) cout << x << ", "; cout << "}" << endl;
    if(W.size()>=k && check(W,T)){
        return true;
    }
    for(int i=start;i<V.size();i++){
        W.push_back(V[i]);
        if(esercizio4(V, T, k, W, i+1)) return true;
        W.pop_back();
    }
    return false;
}

int main(){
    //vector<string> V = {"a","b","c"};

    //vector<vector<string>> T = {{"a","b"},{"b","c"},{"a","c"}}; //NO
    
    vector<string> V = {"a","b","c","d","e","f","g","h"};
    
    vector<vector<string>> T = {{"a","b","f","c"}, {"b","h","d"}, {"b","a","c"}, {"d","h"}, {"e","f","g","h"}}; //SI

    //vector<vector<string>> T = {{"a","b","c","d","f","h"}, {"b","e","g"}, {"e","a","g"}, {"a","h"}, {"e","f","g","h"},}; //SI
    
    //vector<vector<string>> T = {{"a","b","c","d","e","f","h"}, {"b","e","g"}, {"a","f","g"}, {"a","h"}, {"c","d","g","h"},}; //NO
    
    //vector<vector<string>> T = {{"a","b","c","d","e","f","g","h"}, {"b","e","g"}, {"a","d","g"}, {"g","h"}, {"c","a","g","h"},{"h","b"}}; //NO

    //vector<vector<string>> T = {{"a","b","c","d","e","f","g","h"}, {"b","e","g"}, {"a","d","g"}, {"g","h"}, {"d","h"}, {"e","h"}, {"c","a","g","h"},{"h","b"}}; //NO

    int k = 2;
    vector<string> W;
    if(esercizio4(V, T, k, W, 0)) cout << "SI";
    else cout << "NO";
    
    return 0;
}
