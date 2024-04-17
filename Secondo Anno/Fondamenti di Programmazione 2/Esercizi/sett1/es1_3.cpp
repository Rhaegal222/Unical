/*
max e submax di una sequenza di 10 numeri
50 30 40 0 0 0 0 0 0 0
40 30 50 0 0 0 0 0 0 0
30 40 50 0 0 0 0 0 0 0
*/
#include <iostream>
using namespace std;

int main(){
    int numero, max, submax;
    for (int i = 0; i < 10; i++){
        cin >> numero;
        if (numero >= max){
            max = numero;
        }
        if (numero >= submax && numero < max){
            submax = numero;
        }
    }
    cout << max << " " << submax << endl;
}