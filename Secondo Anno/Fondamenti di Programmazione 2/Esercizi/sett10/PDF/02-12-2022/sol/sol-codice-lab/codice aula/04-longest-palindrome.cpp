#include<iostream>
#include<vector>
using namespace std; 

/* Presa in input una stringa s, vogliamo calcolare una delle più lunghe sottosequenza palindroma contenuta in s.

	Soluzione dinamica:
	Abbiamo una matrice S[][], dove S[i][j] è la lunghezza della sottosequenza palindroma più lunga contenuta in s[i..j], cioè la sottostringa che inizia dall'indice i e finisce in j 

		Casi base:
	- S[i][i] = 1 
	- S[i][j] = 0 se i > j ("non esiste la stringa")
	
	
		Scomposizione dei problemi:
	- S[i][j], con i < j e s[i] == s[i]
	- S[i][j] = 2 + S[i+1][j-1]

             v
		esempio: AJKA con S[0][3]
                ^
	- S[i][j], con i < j, s[i] != s[j]
		abbiamo S[i][j] = max(S[i+1][j], S[i][j-1])
		
				     i
		         v
		esempio: PANNA, con S[0][4]
		             j
		
		sottoproblema: S[1][4] -> "ANNA"
		sottoproblema: S[0][3] -> "PANN"	
		
		per calcolare la soluzione ottima, siamo interessati a calcolare:
		
		S[0][s.size()-1]
		
		per scacciapensieri:
		
		i
		SCACCIAPENSIERI
		              j
		              
		              
		esempio: stringa PANNA
				0 	1		2		3		4	
				P 	A 	N		N		A
				
0		P		1  	?		?		?		?
1		A		0		1		?		?		?
2		N		0		0		1		?   ?
3		N		0		0		0		1		?
4		A		0		0		0		0		1
		              
	Per calcolare la soluzione ottima, dobbiamo calcolare il valore di 
		S[0][4] = max(S[1][4], S[0][3])
			S[1][4] = 2 + S[2][3]
				S[2][3] = 2 + S[3][2]
					S[3][2] = 0
				S[2][3] = 2 + 0 = 2
			S[1][4] = 2 + 2 = 4
		S[0][4] = max(4, S[0][3])
			
			S[0][3] = max(S[1][3], S[0][2]) = max(2, 1) = 2
				S[1][3] = max(S[2][3], S[1][2])
					S[2][3] = 2 + S[3][2] = 2
					S[1][2] = max(S[2][2], S[1][1]) = 1
				S[1][3] = max(2, 1) = 2
				
				S[0][2]		while (i < j) {
			// SEGUIAMO LA DEFINIZIONE A CASI
			// DELLA RICORRENZA
			
			if (s[i] == s[j]) {
				// "costruiamo la stringa dall'interno"
				left = left + s[i]; 
				right = s[j] + right; 
			}
			
			else if (S[i+1][j] > S[i][j-1]) // questi erano i sottoproblemi in cui S[i][j] si scompone {
				++i;
			} else {
				++j; 
			} = max(S[1][2], S[0][1]) = max(1, 1) = 1 
					S[0][1] = max(S[1][1], S[0][0]) = 1
			
		=> S[0][4] = max(2, 4) = 4
		
		
		Esercizio 2: programmazione dinamica bottom-up, 
			~ esiste un modo semplice di calcolare la ricorrenza dai casi base
			
		Questo qui: programmazione dinamica top-down
			~ ci sono diverse chiamate "ricorsive" da fare prima di arrivar eai casi base. questi di solito sono più facili da implementare con ricorsione + memoizzazione
			
		
		Per ricostruire la soluzione, a partire da una tabella S popolata, 
		
		int i = 0; 
		int j = s.size() - 1; 
		
		string left = "", right = "";
		
		while (i < j) {
			// SEGUIAMO LA DEFINIZIONE A CASI
			// DELLA RICORRENZA
			
			if (s[i] == s[j]) {
				// "costruiamo la stringa dall'interno"
				left = left + s[i]; 
				right = s[j] + right; 
			}
			
			else if (S[i+1][j] > S[i][j-1]) // questi erano i sottoproblemi in cui S[i][j] si scompone {
				++i;
			} else {
				++j; 
			}
		}
*/

int longest_palindrome(const string& s, 
	vector<vector<int>>& S, int i, int j) {
	
	/* Caso base / funzione già calcolata */
	if (S[i][j] != -1) return S[i][j]; // O(1)
	
	// siamo nel caso:
	/*
		 i 
		PANNA
		    j
	*/
	if (s[i] == s[j]) {
		// errore grossimo:
		// non stiamo salvando i risultati dei problemi 
		// return 2 + longest_palindrome(s, S, i+1, j-1);
		// potenzialmente un numero esponenziale di chiamate
		
		// questa tecnica, salvare i risultati intermedi
		// dei sottoproblemi
		// per far terminare le chiamate ricorsive di 
		// sottoproblemi già risolti in O(1) 
		// si chiama memoizzazione
		S[i][j] = 2 + longest_palindrome(s, S, i+1, j-1);
		return S[i][j]; 
	}
	
	/* ultimo caso */
	/*
	
				  i
					PANNA
	            j
	*/
	if (s[i] != s[j]) {
		/*
			Sottoproblema "sinistro":
			   i
				PANNA
				    j
		*/
		int left_string_sol = longest_palindrome(s, S, i+1, j);
		/*
			Sottoproblema "destro":
			  i
				PANNA
				   j
		*/
		int right_string_sol = longest_palindrome(s, S, i, j-1);
		S[i][j] = max(left_string_sol, right_string_sol);
		
		return S[i][j]; 
	}
	
	
}

int main() {
	string s; 
	cin >> s; 
	
	int n = s.size(); 
	// -1: "funzione da calcolare"; >= 0: "funzione già calcolata"
	vector<vector<int>> S(n, vector<int>(n, -1)); 
	
	// inizializziamo S con i casi base della ricorrenza
	for (int i = 0; i < n; ++i) {
		S[i][i] = 1; 
		for (int j = i-1; j >= 0; --j) {
			S[i][j] = 0; 
		}
	}
	
	
	return 0; 
}
