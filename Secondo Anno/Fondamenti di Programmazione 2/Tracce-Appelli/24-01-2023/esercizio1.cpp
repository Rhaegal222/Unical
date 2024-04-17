#include <iostream>
using namespace std;
    
int main(){     
    int v[] = {2,1,9,9,0,1};
    int *p1, *p2, a, b;
    a = v[0]; b=v[1]; //a=2; b=1 //assegno ad a e b i valori della matrice
    cout<<a<<b<<endl;
    p1 = &a; p2=&b; //a=2; b=1 //assegno ai puntatori p1 e p2 rispettivamente l'indirizzo di a e b
    cout<<a<<b<<endl;
    p1 = p2; //a=2;b=1 // assegno a p1 l'indirizzo di p2
    cout<<a<<b<<endl;
    *p2 = v[2]; //a=2; b=9 // assegno al valore contenuto in p2 il nuovo valore che é v[2] cioé 9, di conseguenza a tutti quelli che sono puntati da p2 viene assegnato 9
    cout<<a<<b<<endl;
    a = v[3]; //a=9; b=9 aasegno ad a il valore di v[3]

    cout<<*p1<<*p2<<a<<b<<endl;

    int* q1 = new int(20);
    delete q1;

    int *ptr = &v[0];
    int *qtr = &v[3];

    cout << qtr - ptr << endl; // stampa la differenza tra l'indirizzo di v[3] e v[0] che é 3

    int &f = v[2];
    f = 7;
    for(int i=0;i<5;i++){
        cout << *(v+i);
    }
    cout << endl;

    return 0; 
}
