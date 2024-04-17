#include <iostream>
#include "CatenaDiMontaggio.h"
using namespace std;

int main(){
	CatenaDiMontaggio<int> C;

    C.aggiungi(10);
	C.aggiungi(100);
	C.aggiungi(120);
	C.aggiungi(13);

	cout << "Numero di elementi nella lista: " << C.size() << endl;
	cout << "Il primo elemento della lista: " << C.prossimo() << endl;
	C.rimuovi();
	cout << "Il primo elemento della dopo la cancellazione: " << C.prossimo() << endl;
	cout << "Numero di elementi nella lista alla fine: " << C.size() << endl;


	return 0;
}
