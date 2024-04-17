//ESERCIZIO 1
#include <iostream>
using namespace::std;

int main(){
    int* matricola = new int[6]{2,1,9,5,6,1}; //scrivi sul foglio la tua matricola
    //1. La seguente istruzione è corretta? Se sì, cosa stampa? 00
    cout << *(matricola + 3) << *(matricola + 2) << endl; 
    
    //2. La seguente istruzione è corretta? Se sì, cosa stampa?
    // NON CORRETTA: cout << *(matricola[0])  << endl;
    cout << matricola[0] << endl; 
    
    //3. Cosa viene stampato dalla seguente porzione di codice?     
    
    int& a = matricola[2];
    int b = matricola[5];
    
    --a;
    b += 1;
    
    cout << "Indirizzo di memoria Prima: " << matricola << endl;
    delete [] matricola;
    cout << "Indirizzo di memoria Dopo: " << matricola << endl;

    cout << endl;
    for(int i = 0; i < 10; i++)
        cout << matricola[i] << endl;

    /*
    4. Come andrebbe deallocata la memoria dinamica allocata inizialmente?
    A -> for(int i = 0; i < 6; i++)delete matricola[i];
    B -> for(int i = 0; i < 6; i++)delete *matricola[i];
    [X] C -> Nel main non serve deallocare la memoria dinamica.
    D -> delete [] matricola;
    */
}

//ESERCIZIO 2

