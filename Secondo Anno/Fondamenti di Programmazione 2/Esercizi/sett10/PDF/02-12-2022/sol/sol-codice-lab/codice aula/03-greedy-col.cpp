#include<iostream>
#include<vector>
using namespace std; 

// LINK: https://pastebin.com/skdym1fB

/*
	Preso in input un grafo G, vogliamo calcolare una (D+1)-colorazione per il grafo, dove D è il grado dei nodi con grado massimo in G.
	(nel PDF visto a laboratorio c'era un errore nella traccia dove si chiedeva di farlo con D colori.
	
	il grafo completo su 4 nodi, con k = 3 è un controesempio del perché è sbagliato. grazie domenico per la segnalazione) 
	
	usando almeno D+1 colori la colorazione esiste sempre e si può calcolare in modo greedy.
	
	Idea:
		Scorriamo i nodi in qualsiasi ordine 
			Vediamo quali sono i colori "disponibili" per il nodo corrente
			Coloriamo il nodo corrente con il primo colore disponibile
*/

int main() {
	/* Lettura input */
	int num_nodes, num_edges;
	cin >> num_nodes >> num_edges; 
	
	/*
		nell'esercitazione sui grafi abbiamo visto la rappresentazione
		a matrice di adiacenza, 
		mat[i][j] = true se e solo se esiste l'arco (i,j) nel grafo.
		
		rappresentazione alternativa: lista di adiacenza, dove


		g[i] = una lista di nodi, i vicini del nodi i 
		usiamo una rappresentazione con lista di adiacenza
	*/
	
	vector<vector<int>> graph;
	for (int i = 0; i < num_nodes; ++i) {
		graph.push_back(vector<int>()); 
	}
	
	/*
		Assumiamo l'input sia fatto così:
		[numero nodi] [numero archi]
		[arco sorgente] [arco destinazione]
		... numero archi volte ...
	*/
	
	vector<int> degree(num_nodes);
	for (int i = 0; i < num_edges; ++i) {
		int a, b;
		cin >> a >> b; 
		graph[a].push_https://pastebin.com/skdym1fBback(b);
		graph[b].push_back(a);
		
		/* pre-calcoliamo i gradi dei nodi */
		degree[a]++;
		degree[b]++;
	}
	
	int colors = 0; 
	for (int i = 0; i < num_nodes; ++i) {
		if (degree[i] > colors) {
			colors = degree[i]; 
		}
	}
	colors++; 
	
	// importiamo algorithm
	// int colors = *max_element(degree.begin(), degree.end()) +1 ; 
	
	// Scorriamo in qualsiasi ordine
	// -1: nodo non ancora colorato
	// k >= 0: nodo con colore k
	vector<int> colorazione(num_nodes, -1);
	for (int i = 0; i < num_nodes; ++i) {
		// Colori disponibili: tutti tranne quelli usati dai vicini
		vector<bool> disponibili(colors, true);
		
		// Iteriamo sul vicinato di nodi `i` e togliamo
		// da disponibili i colori usati dai vicini
		// equivalente: for (int u: graph[i]) { ... }
		for (int u = 0; u < graph[i].size(); ++u) {
			if (colorazione[u] != -1) { // il nodo u ha un colore assegnato
				disponibili[colorazione[u]] = false;
			}
		}
		
		// usciti dal for, in disponibili ci sono solamente i colori
		// buoni per il nodo `i`
		int c = 0; 
		while (not disponibili[c]) {
			++c; 
		} // usciti dal while, c è un colore libero
		colorazione[i] = c; 
	}
	
	/* Check per vedere se il nostro codice funziona */
	// -> vediamo non esista un arco (a,b) tale che colorazione[a] == colorazione[b], oppure colorazione[a] == -1, colorazione[b] == -1
	
	for (int i = 0; i < num_nodes; ++i) {
		if (colorazione[i] == -1) {
			cout << "Qua non ci dovrei arrivare" << endl; 
		}
		for (int v = 0; i < graph[i].size(); ++v) {
			if (colorazione[i] == colorazione[v]) {
				cout << "Qua non ci dovrei arrivare" << endl; 
			}
		}
	}
	
	return 0; 
}
