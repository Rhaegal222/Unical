/*
Scrivere un programma che calcoli la somma di due numeri x, y ∈ Ne il loro
prodotto mediante le funzioni int somma(int,int), e int prodotto(int,int).
La funzione prodotto dovrà essere implementata facendo uso della funzione
somma precedentemente definita.
*/
#include <iostream>
using namespace std;

int somma(int, int);
int prodotto(int, int);

int main(){
    int n1, n2;

    cin >> n1 >> n2;
    cout << "Somma: " << somma(n1, n2) << endl;
    cout << "Prodotto: " << prodotto(n1, n2) << endl;
    return 0;
}

int somma(int n1,  int n2){
    return n1+n2;
}

int prodotto(int n1, int n2){
    int risultato = 0;
    for (int i=0; i<n2; i++){
        risultato = somma(risultato, n1);    
    }
    return risultato;
}