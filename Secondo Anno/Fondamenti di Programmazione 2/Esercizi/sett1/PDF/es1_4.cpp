/*
Scrivere una funzione che, ricevuti due interi x, y ∈ Z, restituisca il risultato
dell’operazione x + x + y · y.
*/
#include <iostream>
using namespace std;

int fun(int, int);

int main(){
    int x, y;
    cin >> x >> y;
    cout << fun(x, y) << endl;
    return 0;
}

int fun(int x, int y){
    return (y*y + 2*x);
}

