/*
Scrivere una funzione che stampi l’istogramma di una sequenza di numeri interi
terminata da un numero negativo.
*/
#include <iostream>
using namespace std;


int main(){
    int n=0;
    while(n>=0){
        cin >> n;
        for(int i = 0; i < n; i++){
            cout << "*";
        }
        cout << endl;
    }
}
