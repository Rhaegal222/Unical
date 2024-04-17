#include <iostream>
#include "ListaOT.h"
using namespace std;

int main()
{
	OrderedList<int> L;
	for (int i=5; i>0; i--) L.insert(i);
	L.print();		//OUTPUT: 1 2 3 4 5 
	L.remove(3);
	L.print();		//OUTPUT: 1 2 4 5 
	if (L.find(4)) L.remove(4);	//OUTPUT: 1 2 5
	L.print();
    return 0;
}