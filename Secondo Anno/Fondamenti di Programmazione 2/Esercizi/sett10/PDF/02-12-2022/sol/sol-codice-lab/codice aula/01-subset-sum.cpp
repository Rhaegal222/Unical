#include<iostream>
#include<vector>
#include<algorithm> // per usare std::sort
#include<utility> // per usare std::pair
using namespace std; 

// LINK: https://pastebin.com/JWcdCTAv


/* 
	sequenza di n interi 
	vogliamo un sottoinsieme di k elementi con somma massima

	k = 1 ~ equivalente a trovare il massimo, lo sappiamo fare in O(n)
	k > 1
		trovo il massimo del vettore, lo sommo da qualche parte
		lo rimuvo dal vettore
		risolvo il problema con il nuovo vettore, su k-1 elementi
		
		O(k·n) ~ O(n^2)

	Soluzione intesa:
		Ordino il vettore, prendo i primi k elementi in ordine decrescente
		O(n log n) = O(n log n) + O(k) 
									^^^ ordinare
																^^^ scorrere i primi/ultimi k
																
																
	Approccio naive per tenere gli indici originali degli elementi del sottoinsieme:
		Fare due copie della sequenza input
		Ri-cercare nella sequenza in input gli elementi del sottoinsieme ottimo
		Tenere traccia dell'indice originale
		
		* NON FUNZIONA (subito) se ci sono duplicati nella sequenza originale
		* non è necessario, si può fare in modo più furbo  
*/

/* Per ordinare std::pair */
bool by_value(const pair<int, int>& a, const pair<int,int>& b) {
	return a.first > b.first; 
}

int main() {
	/* Lettura input */
	int n, k;
	cin >> n >> k; 
	
	/*
		Il vettore contiene coppie (a,b)
		dove `a` è il valore letto dalla sequenza
		`b` sarà l'indice (originale) in cui appare l'elemento
	*/

	vector<pair<int,int>> seq(n);
	for (int i = 0; i < n; ++i) {
		cin >> seq[i].first; 
		seq[i].second = i; 
	}
	
	/* Ordino la sequenza, il default è operator< */
	sort(seq.begin(), seq.end(), by_value); //oridina dal piú piccolo al piú grande
	
	int sum = 0; 
	cout << "Elementi ottimi: "; 
	for (int i = 0; i < k; ++i) {
		sum += seq[i].first; 
		cout << seq[i].first << " ";
	}
	cout << endl; 
	
	cout << "Somma massima: " << sum << endl; 
	
	cout << "Indici elementi ottimi nella sequenza originale: "; 
	for (int i = 0; i < k; ++i) {
		cout << seq[n-1-i].second << " ";
	}
	cout << endl; 
	
	return 0; 
}
