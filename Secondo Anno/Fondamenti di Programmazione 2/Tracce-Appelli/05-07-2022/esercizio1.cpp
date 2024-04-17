#include <iostream>
using namespace std;

int main(){
    /* Data la seguente porzione di programma, rispondere alle domande corrispondenti: */
    int voti[6] = {2,1,9,9,0,1};
    /* 1. La seguente istruzione è corretta? Se sì, cosa stampa? */
    // cout << *voti[0]; Non è CORRETTA

    /* 2. La seguente istruzione è corretta? Se sì, cosa stampa? */
    cout << voti[0] + *(voti+2); //11

    /* 3. Cosa stampa la seguente porzione di codice? Qual è il significato di tale porzione di codice? */
    double s = 0; //INIZIALIZZA UNA VARIABILE DI TIPO DOUBLE A 0
    for(int i = 0; i < 6; i++) 
    s += *(voti+i); //SOMMA A S IL VALORE DI OGNI SINGOLA CIFRA NELL'ARRAY
    if(s/6 > 20) //SE LA MEDIA è MAGGIORE DI 20 STAMPA OK ALTRIMENTI STAMPA NO
    cout << "OK"; 
    else 
    cout << "NO"; 
    /* 4. Cosa stampa la seguente porzione di codice? */
    int a = voti[1]; 
    --a; 
    cout << voti[1]; //STAMPA 1
    return 0;
}