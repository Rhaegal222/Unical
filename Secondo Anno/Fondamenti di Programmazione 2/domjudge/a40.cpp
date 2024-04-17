#include <iostream>
using namespace std;

int main(){
    int numero, somma = 0, ins = 0;
    while (numero != -50)
    {
        cin >> numero;
        if (numero != -50){
            ins++;
            somma += numero;
        }     
    }
    cout << somma <<endl;
}