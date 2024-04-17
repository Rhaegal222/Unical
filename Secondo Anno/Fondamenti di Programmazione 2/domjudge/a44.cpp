#include <iostream>
using namespace::std;

int main(){
    float numero;
    int cont, somma1 = 0, somma2 = 0, intero;
    cin >> numero;
    while (numero > 1)
    {
        numero /= 10;
        cont += 1; 
    }

    for(int i=0; i<cont/2; i++){
        numero *= 10;
        intero = numero;
        somma1 += intero;
        numero -= intero;
        intero = 0;
    }

    for(int i=0; i<cont/2; i++){
        numero *= 10;
        intero = numero;
        somma2 += intero;
        numero -= intero;
        intero = 0;
    }
}