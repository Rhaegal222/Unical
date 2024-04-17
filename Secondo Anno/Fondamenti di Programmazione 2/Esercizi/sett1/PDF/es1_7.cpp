/*
Scrivere una funzione che ricevuti in input due numeri interi a, b ∈ Zcalcoli a^b.
Esempio: Se a = 3, b = 2 la funzione dovrà restituire ab= 32= 9.
2

*/
#include <iostream>
using namespace std;

int potenza(int a, int b){
    int risultato = 1;
    for(int i = 0; i < b; i++){
        risultato*=a;
    }
    return risultato;
}

int main(){
    int a, b, potenza=1;
    cin >> a >> b;
    cout << potenza;
}
