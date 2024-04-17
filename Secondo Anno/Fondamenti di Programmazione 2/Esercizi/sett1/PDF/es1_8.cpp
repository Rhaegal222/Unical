/*
Scrivere una funzione che ricevuti in input due numeri a, b ∈ N calcoli (se esiste)
il logaritmo discreto di a in base b, cioè l’intero c tale che b^c= a. Se c non esiste,
la funzione dovrà restituire -1.
Esempio: Se a = 64 e b = 4, allora c = 3 perché b^c= 4^3= 64 = a. Se invece
a = 100 e b = 3, allora c non esiste e quindi la funzione dovrà restituire -1.
3
*/
#include <iostream>
using namespace std;

int potenza(int base, int esponente){
    int risultato = 1;
    for(int i = 0; i < esponente; i++){
        risultato*=base;
    }
    return risultato;
}

int log(int a, int b, int c){
    int risultato;
    risultato = potenza(b, c);
    if (risultato==a) return c;
    else if(risultato < a) return log(a, b, c+1);
    else return -1;
}

int main(){
    int a, b;
    cin>>a>>b;
    cout<<log(a,b,1);        
}
