#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<utility>
#include<limits>
#include "GrafoNonOrientato.h"
using namespace std; 


/* Esercizio 2 */
template<class T>
void stampaGrafo(const T& g) {
	cout << "Il grafo contiene " << g.n() << " nodi:" << endl;
	vector<unsigned> ds = g.gradi();
	for (int i = 0; i < g.n(); ++i) {
		cout << "\td(" << i << ") = " << ds[i] << endl;
	}

	cout << "Il grafo contiene " << g.m() << " archi:" << endl;
	for (int i = 0; i < g.n(); ++i) {
		for (int j = 0; j < g.n(); ++j) {
			if (g(i,j)) cout << "\t(" << i << "," << j <<")" << endl;
		}
	}
}

/* Esercizio 3 */
template<class T>
pair<unsigned,vector<unsigned>> getNodiConGradoMassimo(const T& g) {
	// Calcolo del grado massimo 
	vector<unsigned> gradi = g.gradi();
	int max_grado = *max_element(gradi.begin(), gradi.end());

	// Nodi con grado massimo
	vector<unsigned> max_grado_nodi;
	for (unsigned i = 0; i < g.n(); ++i) {
		if (gradi[i] == max_grado) max_grado_nodi.push_back(i);
	}

	return make_pair(max_grado, max_grado_nodi);

	// Extra: Per 'ammortizzare' il calcolo dei gradi dei nodi,
	// se dovesse essere un'operazione che è necessaria spesso durante 
	// l'esecuzione del programma,
	// si può aggiungere un vector<unsigned>(g.n(),0) alla classe Grafo per tenere
	// traccia del grado di ciascun nodo e aggiornarne il valore 
	// ad ogni inserimento/rimozione di arco.
}

/* Esercizio 4 */
template<class T>
bool stessoNumeroNodiStessoGrado(const T& g1, const T& g2) {
	if (g1.n() != g2.n()) return false;

	vector<unsigned> ds_1 = g1.gradi();
	vector<unsigned> ds_2 = g2.gradi();
	sort(ds_1.begin(), ds_1.end());
	sort(ds_2.begin(), ds_2.end());

	for (unsigned i = 0; i < g1.n(); ++i) {
		if (ds_1[i] != ds_2[i]) return false;
	}
	return true; 
}

/* Esercizio 5 */
template<class T>
bool almenoUnNodoAdiacenteATutti(const T& g) {
	vector<unsigned> ds = g.gradi();
	for (unsigned i = 0; i < g.n(); ++i) {
		if (ds[i] == g.n() - 1) return true;
	}
	return false;
}

/* Esercizio 6 */
template<class T>
unsigned viciniComuni(unsigned i, unsigned j, const T& g) {
	unsigned answer = 0;
	for (int k = 0; k < g.n(); ++k) {
		if (g(i,k) and g(j,k)) answer++;
	}
	return answer;
}

/* Esercizio 8 */
bool proprieta_1(const Grafo& g, int k) {
	int x = 0; 
	for (int i = 0; i < g.n(); ++i) {
		for (int j = i+1; j < g.n(); ++j) {
			if (viciniComuni(i,j,g) > 0) {
				++x;
				if (x >= k) return true;
			}
		}
	}
	return false;
}

/* Esercizio 10 */
bool proprieta_2(const Grafo& g, const vector<int>& pesi) {
	vector<unsigned> ds = g.gradi();
	for (int i = 0; i < g.n(); ++i) {
		// prodotto peso-grado
		int a = ds[i] * pesi[i];

		// somma pesi adiacenti
		int b = 0;
		for (unsigned v: g.vicinato(i)) {
			b += pesi[v];
		}

		if (b >= a) return false;
	}
	return true; 
}

template<class T>
pair<unsigned, pair<unsigned,unsigned>> getCoppiaPiuAdiacenti(const T& g) {
	unsigned max_vicini = 0;
	pair<unsigned,unsigned> p;

	for (unsigned i = 0; i < g.n(); ++i) {
		for (unsigned j = i + 1; j < g.n(); ++j) {
			unsigned vicini = viciniComuni(i,j,g);
			if (vicini > max_vicini) {
				max_vicini = vicini;
				p = make_pair(i,j);
			}
		}
	}
	return make_pair(max_vicini, p);
};

vector<unsigned> ricostruisciCiclo(const vector<unsigned>& parent, unsigned src) {
	vector<unsigned> cycle;

	unsigned p = parent[src];

	while (p != src) {
		cycle.push_back(p);
		p = parent[p];
	}
	cycle.push_back(src);

	return cycle;
}

/* Esercizio 8 */
bool inUnCiclo(const Grafo& g, unsigned x) {
	// visitati[i] true se il nodo i è stato visitato
	vector<bool> visitati(g.n(), false);

	// nodi che sono ancora da visitare
	queue<unsigned> da_visitare;

	// parent[i] = j vuol dire che nella visita raggiungiamo
	// il nodo i dal nodo j
	// serve solo per "ricostruire" il ciclo
	vector<unsigned> parent(g.n(), 0);

	// inserisco il nodo x nella queue	
	// NON lo visito - se lo raggiungo nuovamente
	// durante la visita vuol dire che fa parte di un ciclo
	da_visitare.push(x);

	bool ciclo = false;

	while (not da_visitare.empty()) {
		unsigned top = da_visitare.front();
		da_visitare.pop();

		// ho raggiunto il nodo x
		if (top == x and visitati[top] == true) {
			ciclo = true;
			break;
		}

		// push nella queue dei vicini
		// non visitati di top
		for (unsigned v: g.vicinato(top)) {
			if (not visitati[v]) {
				da_visitare.push(v);
				visitati[v] = true;

				// serve solo per ricostruire il ciclo
				parent[v] = top;
			}
		}
	}

	// Extra: di che ciclo fa parte x?
	// Possiamo restituire un pair<bool,vector<unsigned>> 
	// per evitare la stampa all'interno della funzione
	// non era richiesto nell'esercizio, lasciamo stare
	if (ciclo) {
		vector<unsigned> ciclo_di_x = ricostruisciCiclo(parent,x);
		for (auto i = ciclo_di_x.rbegin(); i != ciclo_di_x.rend(); ++i) {
			cout << *i << " -> ";
		}
		cout << x << endl; 
	}

	return ciclo;
}


/* Esercizio 9 */
bool connesso(const GrafoNonOrientato& g) {
	vector<bool> visitati(g.n(), false);
	queue<unsigned> da_visitare;

	// va bene qualsiasi nodo
	da_visitare.push(0);
	unsigned nodi_visitati = 1;
	visitati[0] = true;
	

	while (not da_visitare.empty()) {
		unsigned top = da_visitare.front();
		cerr << "Sto visitando il nodo " << top << ". Al momento ho visitato " << nodi_visitati << " nodi" << endl; 
		da_visitare.pop();

		for (unsigned v: g.vicinato(top)) {
			if (not visitati[v]) {
				cerr << "Sto aggiungendo alla queue il nodo " << v << endl; 
				visitati[v] = true;
				nodi_visitati++;
				da_visitare.push(v); 
			}
		}
	}

	return nodi_visitati == g.n(); 
}


struct NodeCost {
	const unsigned node;
	const unsigned cost;

	NodeCost(unsigned a, unsigned b)
	: node(a)
	, cost(b) { }

	bool operator<(const NodeCost& b) const {
		return cost >= b.cost;
	}
};

/* Dijkstra */
pair<vector<unsigned>,vector<unsigned>> dijkstra_single_source_all_nodes(const Grafo& g, unsigned src, const vector<vector<unsigned>>& pesi ) {
	// Queue di (nodo, costo) da esplorare
	queue<NodeCost> da_visitare;

	// costs[i] è il costo per raggiungere i da src
	// inizializzato a +inf
	vector<unsigned> costs(g.n(), numeric_limits<unsigned>::max());
	costs[src] = 0;

	// parent[i] = j quando nel percorso più breve per andare in j passiamo da i
	vector<unsigned> parent(g.n(), 0);

	// la visita parte da src, a costo 0 
	da_visitare.push(NodeCost(src, 0));

	while (not da_visitare.empty()) {
		NodeCost top = da_visitare.front();
		cout << "Sto visitando il nodo " << top.node << " a prezzo " << top.cost << endl; 

		da_visitare.pop();

		for (unsigned v: g.vicinato(top.node)) {
			if (top.cost + pesi[top.node][v] < costs[v]) {
				cout << "Inserisco il nodo " << v << " a prezzo " << top.cost + pesi[top.node][v] << endl; 

				da_visitare.push({v, top.cost+pesi[top.node][v]});
				parent[v] = top.node;
				costs[v] = top.cost + pesi[top.node][v];
			}
		}
	}

	return make_pair(costs, parent);
}

int main() {
	GrafoNonOrientato g(6);
	g(1, 3, true);
	g(2, 3, true);
	g(4, 1, true);
	g(4, 5, true);
	g(3, 5, true);
	g(0, 5, true);

	cout << "Il grado del nodo 3 è " << g.grado(3) << endl; 
	vector<unsigned> ds = g.gradi();
	for (int i = 0; i < 6; ++i) {
		cout << "Il grado del nodo " << i << " è " << ds[i] << endl; 
	}

	vector<unsigned> nbs = g.vicinato(4);
	for (int i = 0; i < nbs.size(); ++i) {
		cout << "Il nodo " << nbs[i] << " è un vicino di " << 4 << endl;
	}

	stampaGrafo(g);

	pair<unsigned,vector<unsigned>> p = getNodiConGradoMassimo(g);
	cout << "Grado massimo: " << p.first << endl; 
	for (unsigned i = 0; i < p.second.size(); ++i) {
		cout << "\tIl nodo " << p.second[i] << " ha grado " << p.first << endl; 
	}

	pair<unsigned,pair<unsigned,unsigned>> q = getCoppiaPiuAdiacenti(g);
	cout << "(" << q.second.first << "," << q.second.second << ") è la coppia di nodi con più adiacenti in comune, in particolare condividono " << q.first << " vicini!" << endl;

	Grafo ciclo(15);
	ciclo(1,2,true);
	ciclo(2,3,true);
	ciclo(3,4,true);
	ciclo(4,5,true);
	ciclo(5,1,true);

	ciclo(6,8,true);
	ciclo(8,10,true);

	ciclo(10,11,true);
	ciclo(11,12,true);
	ciclo(12,13,true);
	ciclo(13,14,true);
	ciclo(14,10,true);

	for (int i = 0; i < ciclo.n(); ++i) {
		bool in_ciclo = inUnCiclo(ciclo,i);
		if (in_ciclo) {
			cout << "Il nodo " << i << " fa parte di un ciclo." << endl;
		} else {
			cout << "Il nodo " << i << " non fa parte di un ciclo." << endl; 
		}
		cout << endl; 
	}

	if (connesso(g)) {
		cout << "Il grafo è connesso" << endl; 
	} else {
		cout << "Il grafo non è connesso" << endl; 
	}

	Grafo dijkstra(8);

	vector<vector<unsigned>> pesi = {
	  // s  1  2  3  4  5  6  7
	    {0, 1, 4, 0, 0, 0, 0, 0}, // s
	    {0, 0, 2, 4, 1, 0, 0, 0}, // 1
		{0, 0, 0, 0, 4, 0, 0, 0}, // 2
		{0, 0, 0, 0, 0, 6, 1, 0}, // 3
		{0, 0, 0, 1, 0, 0, 0, 0}, // 4
		{0, 0, 0, 0, 0, 0, 0, 0}, // 5
		{0, 0, 0, 0, 5, 9, 0, 1}, // 6
		{0, 0, 0, 0, 0, 2, 0, 0}, // 7
	};

	for (int i = 0; i < pesi.size(); ++i) {
		for (int j = 0; j < pesi.size(); ++j) {
			if (pesi[i][j] > 0) dijkstra(i,j,true);
		}
	}

	cout << "--- visita con dijkstra ---" << endl;
	pair<vector<unsigned>,vector<unsigned>> vpair = dijkstra_single_source_all_nodes(dijkstra, 0, pesi);
	for (int i = 0; i < dijkstra.n(); ++i) {
		cout << i << " "; 
	} 
	cout << endl; 

	for (unsigned c: vpair.first) {
		cout << c << " ";
	}
	cout << endl; 

	for (unsigned c: vpair.second) {
		cout << c << " ";
	}
	cout << endl; 

};
