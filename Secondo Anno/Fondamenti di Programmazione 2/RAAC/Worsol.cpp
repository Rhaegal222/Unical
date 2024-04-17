#include <iostream>
#include <vector>

using namespace std;

/*Parametri: 
    I: vector di elementi di tipo generico;
    k: numero di elementi distinti (se k=-1 stampa tutte le combinazioni contenenti da 1 a N elementi);
    C: vector vuoto dello stesso tipo di I
    s: 0 di default
*/

template<class T> bool isComplete(vector<T>& Parola){
    if(Parola.size()==5) return true
}


template<class T> bool canAdd(vector<T>& Parola, vector<T>& Esclusi){
    for(auto x:Parola){
        for (auto y:Esclusi){
            if(x==y){
                return false;
            }
        }
    }
    return true;
}

template<class T> void Combinazioni_Semplici(vector<T>& Alphabet, vector<T>& Parola, vector<T>& Esclusi, int index){
    for(int i=0;i<I.size();i++){
        if(canAdd(Parola, Esclusi)) C.push_back(I[i]);
        if(isComplete(Parola)){cout << "{ "; for(auto x:Parola) cout << x << " "; cout << "}" << endl; return true;}
        if(Combinazioni_Semplici(Alphabet, Parola, Esclusi, index+1)) return true;
        C.pop_back();
    }
    return false;
}
int main()
{
    /* Combinazioni Semplici */
    vector<string> Alphabet{"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
    vector<string> Esclusi;
    vector<string> Parola;
    Combinazioni_Semplici(Alphabet,Esclusi,Parola,0);
    return 0;
}
