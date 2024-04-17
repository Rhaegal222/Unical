#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
using namespace std; 

/*
	Pastebin: https://pastebin.com/q2ttDudf


	Abbiamo un array di n elementi, siamo interessati a calcolare
	i, j tale che A[i] + ... + A[j] sia massimo, con i < j.


	Soluzione naive ~ O(n^3)
		Scorro tutti i possibili i da 0 a n-1
			Scorro tutti i possibili j da i a n-1
				Faccio la somma di A[i] + ... + A[j]

	Con programmazione dinamica esiste una soluzione in O(n)
	
	A = 1 3 4 -2 5 -20 10 12
	
	S[i] -> la massima somma di un sottoarray in A[0..i]
	esempio: S[5] è la massima somma di un sottoarray in A[0..5],
		A[0..5] = 1 3 4 -2 5
	
	S[0] è un array di un solo elemento, quindi la soluzione ottima è 
	
							vvvvvvvvv "estendiamo la soluzione corrente"
	S[i] = max( S[i-1] + A[i], A[i] )
															^^^^ "facciamo partire una nuova soluzione"
				
	i   0 1 2  3 4   5  6  7											
	A = 1 3 4 -2 5 -20 10 12
	
	quindi noi siamo interessati a calcolare il max S[i], per i = 0 ... n-1
	
																																   is_max?
	S[0] = A[0] = 1 (caso base)												  i = 0, j = 0
	S[1] = max( S[0] + A[1], A[1] ) = max(4, 3) = 4		  i = 0, j = 1 
	S[2] = max( S[1] + A[2], A[2] ) = max(8, 4) = 8 	  i = 0, j = 2 
	S[3] = max( S[2] + A[3], A[3] ) = max(6,-2) = 6		  i = 0, j = 3
	S[4] = max( S[3] + A[4], A[4] ) = max(11,5) = 11    i = 0, j = 4
	S[5] = max( S[4] + A[5], A[5] ) = max(-9,-20) = -9, i = 0, j = 5
	S[6] = max( S[5] + A[6], A[6] ) = max(1, 10) = 10		i = 6, j = 6
	S[7] = max( S[6] + A[7], A[7] ) = max(22, 12) = 22  i = 6, j = 7 (*)
	
	Idea: facciamo fare i calcoli al computer, nello stesso ordine che ci detta la ricorrenza
	(è un problema classico sui libri si chiama algoritmo di Kadane)
	
	S[i] ~ elemento di un vettore 
*/

int main() {
	/* Lettura input */ 
	int n; 
	cin >> n; 
	
	/* Il costruttore di default di vector crea un vector vuoto 
		quindi vec[1] potrebbe dare un segmentation fault se l'implementazione
		di STL che stiamo usando non "pre-alloca" un vettore di lunghezza non nulla.
	
		Se usiamo il costruttore ad un parametro di std::vector, 
		pre-allochiamo una lunghezza minima per il vettore.
		Gli elementi pre-allocati usano il costruttore di default del tipo corrispondente.
		(Su g++, senza ottimizzazioni particolari, per int è 0)
		(Per le classi che scriviamo noi, è il costruttore di default) 
	*/
	vector<int> seq(n); 
	for (int i = 0; i < n; ++i) {
		cin >> seq[i]; 
	}
	
	/* Creiamo un vettore per S per applicare 
		la programmazione https://pastebin.com/q2ttDudfdinamica.
	*/
	vector<int> S(n); 
	
	/* Caso base */
	S[0] = seq[0]; 
	
	/* Iteriamo sull'array e facciamo i conti che servono
		per la ricorrenza della versione dinamica
	*/
	int best_solution = S[0];
	int best_i = 0, best_j = 0; 
https://pastebin.com/q2ttDudf
	int curr_sum = S[0]; 
	int curr_i = 0, curr_j = 0;
	
	for (int i = 1; i < n; ++i) {
		int extend = S[i-1] + seq[i]; 
		int new_array = seq[i]; 
		
		S[i] = max(extend, new_array);
		//best_solution = max(best_solution, S[i]); 
		
		if (extend > new_array) {
			/* Il massimo viene dal primo termine della ricorrenza*/
			++curr_j;
		} else {
			/* Il massimo viene dal secondo termine della ricorrenza
			(oppure è indifferente) */
			curr_i = curr_j = 0; 
		}
		
		if (S[i] > best_solution) {
			best_solution = S[i]; 
			best_i = curr_i; 
			best_j = curr_j; 
		}
	}
	
	cout << best_solution << " " << best_i << ":" << best_j << endl; 
	return 0; 
}
