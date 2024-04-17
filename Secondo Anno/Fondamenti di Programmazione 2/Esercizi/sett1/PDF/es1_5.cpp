/*
Scrivere una funzione che calcoli l’n-esimo numero della sequenza di Fibonacci,
definito come F (n) = F (n −1) + F (n −2), dove F (0) = 0, F (1) = 1.
Esempio: I primi 8 numeri della sequenza di Fibonacci sono: 0, 1, 1, 2, 3, 5, 8, 13, 21.
*/
#include <iostream>
using namespace std;

int fib(int n){
    if (n == 0) return 0;
    else if (n == 1) return 1;
    else return fib(n-1)+fib(n-2);
}

int main(){
    int n;
    cout << "Inserisci il numero: ";
    cin >> n;
    cout << "Risultato: " << fib(n);
}
