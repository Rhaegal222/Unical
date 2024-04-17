#include <iostream>
#include "ListaT.h"
using namespace std;


int main()
{
//Riempimento della lista
    List<int> L;
    for(int i =0; i <3; i++)
    {
        L.pushFront(i);
        L.pushBack(-i);
    }
    L.print();

//Eliminazione di un nodo specifico	(N.B. per semplicità la condizione è su un valore, ma potrebbe essere qualcosa di più complicato

	for (Node<int> * n=L.front(); n!=NULL; n=n->getNextNode())
	{ 
		if (n->getValue()==2)
		{	cout<<"Trovato il 2, lo rimuovo"<<endl;
			L.delNode(n); //n potrebbe non essere più un riferimento valido
		}
		
		
	}
	L.print();

//Rimozione di un nodo con un certo contenuto
	L.remove(1);
	L.print();	

//Funzone di ricerca di un nodo
    if(L.find(-2))
        cout<<"si"<<endl;
    L.pushBack(-1);
    L.print();

//Esempio con liste di caratteri
    List<char> C;
    C.pushBack('a');
    C.pushBack('b');
    C.pushBack('B');
    C.pushBack('A');
    C.print();
    char c;
    if(C.popFront(c))
        cout<<"dopo aver rimosso "<<c<<" alla lista " ;
    C.print();

    if(C.popBack(c))
        cout<<"dopo aver rimosso "<<c<<" alla lista " ;
    C.print();
    return 0;
}

/*
APPLICAZIONI DELL’EREDITARIETA’: LISTE ORDINATE
N.B. Occorre definire OrderedList come friend di Node
N.B. La definizione protected per List serve a far accedere ai suoi elementi first e last alla classe derivata.
*/