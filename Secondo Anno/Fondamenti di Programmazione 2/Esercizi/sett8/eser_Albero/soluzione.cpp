#include "AlberoB.h"
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/* Esercizio 1 */
template<typename T>
void stampaAlbero(const AlberoB<T>&,int=0);

/* Esercizio 2 */
bool isHeap(const AlberoB<int> & a);

/* Esercizio 3 */
bool ogniPercorsoRadiceFoglia(const AlberoB<int>& a, int max);
bool ogniPercorsoRadiceFoglia(const AlberoB<int>& a, int max, int current);

/* Esercizio 4 */
bool pariEDispari(const AlberoB<int>& a);
bool pariEDispari(const AlberoB<int>& a, int livello);


/* Esercizio 5 */
bool vocaliEConsonanti(const AlberoB<char>& a);
bool vocaliEConsonanti (const AlberoB<char>& a, int diff);

/* Esercizio 6 */
int sommaPath(const AlberoB<int>& a);
int sommaPath(const AlberoB<int>& a, int somma_corrente);

/* Esercizio 7 */
/* Esercizio 8 */
bool sommaLivelliAdiacenti(const AlberoB<int>& a, int max);

/* Esercizio 9 */
bool fogliePosEqfoglieNeg(const AlberoB<int>& a);
int diffFoglie(const AlberoB<int>& a);

/* Esercizio 10 */
template<typename T>
AlberoB<T> vecToAlbero(const vector<T>& valori);
int main(){
	AlberoB<int> T1 = vecToAlbero(
		vector<int>({6,7,2,3,4,2,1})
	);

	AlberoB<int> T2 = vecToAlbero(
		vector<int>({0,1,2,3,4,5,6,7,8,9,10,11,12,13,14})
	);

	cout << "T1" << endl;
	stampaAlbero(T1);

	cout<< "T2" << endl; 
	stampaAlbero(T2);

	cout << isHeap(T1) << ", " << isHeap(T2) << endl; 
	cout << ogniPercorsoRadiceFoglia(T2, 100) << endl; 
	cout << ogniPercorsoRadiceFoglia(T2, 23) << endl; 

	cout << sommaPath(T1) << endl; 

	AlberoB<int> T3 = vecToAlbero(
		vector<int>({0,1,2,1,-1,1,-1})
	);
	stampaAlbero(T3);
	cout << fogliePosEqfoglieNeg(T3) << endl; 

	cout << sommaLivelliAdiacenti(T3, 2) << endl; 
	cout << sommaLivelliAdiacenti(T3, 4) << endl; 


	// x -> y -> {o,u}
	AlberoB<char> T4 = vecToAlbero(
		vector<char>({'x', 'e', 'y', 'a', 'i', 'o', 'u'})
	);

	stampaAlbero(T4); 
	cout << vocaliEConsonanti(T4) << endl;

	AlberoB<char> T5 = vecToAlbero(
		vector<char>({'x', 'e', 'u', 'a', 'i', 'o', 'u'})
	);

	stampaAlbero(T5); 
	cout << vocaliEConsonanti(T5) << endl;


	return 0;
}

template<typename T>
void stampaAlbero(const AlberoB<T>& tree, int depth) {
	if (tree.nullo()) { 
		return; 
	}
	for (int i = 0; i < depth; ++i) {
		cout << "  ";
	}
	cout << tree.radice() << endl; 
	stampaAlbero(tree.figlio(SIN), depth+1);
	stampaAlbero(tree.figlio(DES), depth+1);
}

/***************************************************/
//controlla se a è un heap con il max come radice
bool isHeap(const AlberoB<int>& a){
	
	if (a.nullo() || a.foglia())
		return true;

	if (!a.figlio(DES).nullo() && a.radice() >= a.figlio(DES).radice())
		return false;

	if (!a.figlio(SIN).nullo() && a.radice() >= a.figlio(SIN).radice())
		return false;


	return isHeap(a.figlio(SIN)) && isHeap(a.figlio(DES));

}
/***************************************************/



/***************************************************/
// ogni percorso radice foglia non deve superare il valore max
bool ogniPercorsoRadiceFoglia(const AlberoB<int>& a, int max){

	return ogniPercorsoRadiceFoglia(a, max, 0);
}

bool ogniPercorsoRadiceFoglia(const AlberoB<int>& a, int max, int current){

	//se a è nullo significa che non esiste come percorso e dunque non devo controllare la proprietà
	if (a.nullo())
		return true;

	if (a.foglia())
		return current + a.radice() <= max;

	return ogniPercorsoRadiceFoglia (a.figlio(SIN), max, current + a.radice()) && ogniPercorsoRadiceFoglia (a.figlio(DES), max, current + a.radice());
		
}
/***************************************************/


/***************************************************/
// ogni valore su un livello pari deve essere pari ed ogni valore su un livello dispari deve essere dispari: si supponga che si parta dal livello 1
bool pariEDispari(const AlberoB<int>& a){
	return pariEDispari(a, 1);
}

//sebbene entri in gioco il concetto di livello, la proprietà riguarda ogni singolo nodo e per questo
//non sono costretto ad effettuare una visita per livelli ma posso usare ancora la ricorsione
bool pariEDispari(const AlberoB<int>& a, int livello){

	if (a.nullo())
		return true;

	if ((livello % 2 == 0 && a.radice() % 2 != 0) || (livello % 2 == 1 && a.radice() % 2 == 0))
		return false;

	return pariEDispari(a.figlio(SIN), livello + 1) && pariEDispari(a.figlio(DES), livello + 1);
}
/***************************************************/


/***************************************************/
// supponiamo che ogni percorso dalla radice alla foglia constituisca una parola. si controlli 
// se vale la proprietà che ogni parola ha un numero di vocali e di consonanti che differisce al più di uno
// si supponga che la parola contenga solo lettere e che siano tutte minuscole
bool vocaliEConsonanti(const AlberoB<char>& a){

	return vocaliEConsonanti(a, 0);
}

bool vocaliEConsonanti (const AlberoB<char>& a, int diff){
	if (a.nullo())
		return true;

	if (a.foglia())
		return abs(diff) <= 1;

	if (a.radice() == 'a' || a.radice() == 'e' || a.radice() == 'i' || a.radice() == 'o' || a.radice() == 'u')
		diff ++ ;
	else
		diff --;

	return vocaliEConsonanti(a.figlio(SIN), diff) && vocaliEConsonanti(a.figlio(DES), diff);
}
/***************************************************/

/***************************************************/
//Restituisce true se e solo se il numero di foglie con valore < 0 è uguale al numero di foglie con valore >= 0
bool fogliePosEqfoglieNeg(const AlberoB<int>& a){
	return diffFoglie(a) == 0;
}

int diffFoglie(const AlberoB<int>& a){
	if(a.nullo())
		return 0;
	
	if(a.foglia())
		if(a.radice() < 0)
			return -1;
		else 
			return 1;
	
	return diffFoglie(a.figlio(SIN)) + diffFoglie(a.figlio(DES));

}    	
/***************************************************/
//Considerando ogni path radice->foglia come un numero intero, restituisce la somma di tutti i path.
/*
   2
  /	\
 3  4
   /
  5
restituisce 23 + 245 = 268
*/

int sommaPath(const AlberoB<int>& a){
	return sommaPath(a, 0);
}

int sommaPath(const AlberoB<int>& a, int somma_corrente){
	if(a.nullo())
		return 0;

	if (a.foglia())
		return somma_corrente * 10 + a.radice();

	return sommaPath(a.figlio(DES), somma_corrente * 10 + a.radice()) + sommaPath(a.figlio(SIN), somma_corrente * 10 + a.radice());
}
/***************************************************/




/***************************************************/
/*riceve un vector di interi e popola l'albero (-1 o valore qualsiasi per i figli assenti)

/* vettore = 3, 5, 7, 2, 4, 1, 5*/
/* alberi = {(3), (5), (7)
/* albero ->       3
				 /  \
			    5    7
			   / \  / \
			  2	 4 1   5
*/
template<typename T>
AlberoB<T> vecToAlbero(const vector<T>& vettore)
{
	AlberoB<T> albero(vettore[0]);

	vector<AlberoB<T>> alberi;
	alberi.push_back(albero);

	for (int i = 1; i < vettore.size(); i++)
	{
		//nota che in alberi inseriamo una copia dell'albero "nuovo", ma avendo internamente dei puntatori,
		//gli alberi che troviamo nel vector sono quelli reali
		AlberoB<T> nuovo(vettore[i]);
		alberi.push_back(nuovo);

		if(i % 2 == 1)
			alberi[ (i-1) / 2 ].insFiglio(SIN, nuovo);
		else
			alberi[ (i-1) / 2 ].insFiglio(DES, nuovo);
			
	}

	return albero;
}
/***************************************************/

/***************************************************/
//restituisce true se la somma di ogni coppia di livelli adiacenti non supera il max
bool sommaLivelliAdiacenti(const AlberoB<int>& a, int pesoMax) {
    if (!a.nullo()) {
 
        queue<AlberoB<int> > qAlberi;  // coda per gli alberi
        queue<int> qLivelli;           // coda per i livelli
		/* Soluzioni alternative:
		Invece di queue<AlberoB<int>> qAlberi, queue<int> qLivelli
		e "push e pop sincronizzati", possiamo utilizzare una unica
		queue queue<pair<AlberoB<int>,int>> dove ogni pair (t,l) 
		rappresenta un albero (~ che in questa soluzione è in qAlberi)
		e un livello (~ che in questa soluzione è in qLivelli) 
		*/
        
		// l'albero a e' al livello 1
        qAlberi.push(a);
        qLivelli.push(1);
        
        int sommaLivPrecedente = a.radice(), sommaLivSuccessivo = 0;
        int livelloPrecedente = 1, livelloSuccessivo = 2;

        while (!qAlberi.empty()) {
            AlberoB<int> temp = qAlberi.front();
            qAlberi.pop();
            int livelloTemp = qLivelli.front();
            qLivelli.pop();

            if (livelloTemp == livelloSuccessivo)
                sommaLivSuccessivo += temp.radice();
            else if(livelloTemp == livelloSuccessivo + 1 ) {

				if (sommaLivPrecedente + sommaLivSuccessivo > pesoMax)
                    return false;
                // (2) livelloCorrente != livelloPrecedente
                // ho estratto un nodo che non fa parte di questo livello
                livelloPrecedente = livelloSuccessivo;
				livelloSuccessivo ++;
                sommaLivPrecedente = sommaLivSuccessivo;
				sommaLivSuccessivo = temp.radice();
            }

            // (3) superati i controlli, aggiungo i figli di temp nella coda
            if (!temp.figlio(SIN).nullo()) {
                qAlberi.push(temp.figlio(SIN));
                qLivelli.push(livelloTemp + 1);
            }
            if (!temp.figlio(DES).nullo()) {
                qAlberi.push(temp.figlio(DES));
                qLivelli.push(livelloTemp + 1);
            }
        }

        if (sommaLivPrecedente + sommaLivSuccessivo > pesoMax)
            return false;
    }
    return true;
}
