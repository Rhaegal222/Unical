#include "../ListaT.h"

int main(){
List<int> L;
    for(int i =0; i <3; i++)
    {
        L.pushFront(i);
        L.pushBack(-i);
    }
    L.print();		// 2 1 0 0 -1 -2

    //cerca -2
    if(L.find(-2))
        cout<<"Trovato"<<endl;
    
    //Aggiunge -1 alla fine della lista
    L.pushBack(-1);	
    L.print();		// 2 1 0 0 -1 -2 -1
}