/*
	inserisci da input un array di char terminato dal tappo .
	determinare se rappresenta una parola palindroma
*/

#include <iostream>
using namespace std;

void leggi_parola(char v[], int &dim){
	const int maxdim = 100;
	char c;
	dim = 0;
	cin >> c;
	while((c!='.')&&(dim<maxdim)){
		v[dim]=c; dim++;
		cin >> c;
	}
	return;
}

bool Palindroma(char v[], int dim){
	bool trovato_diverso = true;
	for (int i = 0; i < dim/2; i++){
		if (v[i] != v[dim-i-1]) return false;
	}
	return true;
}

int main(){
	int dim;
	char v[dim];
	cin >> dim;
	leggi_parola(v, dim);
	if (Palindroma(v, dim)) cout << "Palindroma";
	else cout << "Non Palindroma";

	return 0;
}
