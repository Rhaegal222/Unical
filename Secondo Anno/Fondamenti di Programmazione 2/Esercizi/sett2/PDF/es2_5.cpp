/*
Esercizio 5
Due matrici A,B di dimensione n ×n sono simili se la somma degli elementi
sulla diagonale principale di A è uguale alla somma degli elementi sulla diagonale
principale di B.
Si scriva una funzione che ricevuto in input due matrici quadrate di interi, A di
dimensione n×n e Q di dimensione k ×k con n > k, verifichi se A contiene una
sottomatrice Q′di dimensione k ×k simile a Q.
Se questa sottomatrice esiste, la funzione dovrà sostituirla con la matrice Q,
modificando A, e restituire true. Altrimenti, dovrò restituire false senza
modificare A. Qualora A contenesse più sottomatrici simili a Q′, solamente la
più in alto a sinistra dovrà essere sostituita.
*/
#include <iostream>
using namespace std;

const int N = 4;
const int K = 3;

int sommaDiagonale(int M[][N], int riga, int colonna, int dim);
void individuaSottomatrice(int A[][N], int Q[][N]);
void sostituisceInA(int A[][N], int Q[][N], int riga, int colonna, int dim);

void LeggiMatrice(int A[][N], int dim){
	for (int i = 0; i < dim; i++)
		for (int j = 0; j < dim; j++)
			cin >> A[i][j];
}

void StampaMatrice(int A[][N], int dim){
	cout << endl;
    for (int i = 0; i < dim; i++){
        for(int j = 0; j < dim; j++){
            cout << A[i][j] << " ";
        }
    cout << endl;
    }
    cout << endl;
}

int main(){
	int A[N][N];
    int Q[N][N];

    cout << "Inserisci la matrice A: " << endl;
    LeggiMatrice(A, 4);
	StampaMatrice(A, 4);
    
    cout << "Inserisci la matrice Q: " << endl;
	LeggiMatrice(Q, 3);
    StampaMatrice(Q, 3);
    
	individuaSottomatrice(A, Q);
}

int sommaDiagonale(int M[][N], int riga, int colonna, int dim){
    int somma = 0;
	for (int i = 0; i < dim; i++){
        somma += M[i+riga][i+colonna];
    }
	return somma;
}

void sostituisceInA(int A[][N], int Q[][N], int riga, int colonna, int dim){
	for(int i = 0; i < K; i++){
		for(int j = 0; j < K; j++){
			A[riga+i][colonna+j] = Q[i][j];
		}
	}
	StampaMatrice(A, 4);
}

void individuaSottomatrice(int A[][N], int Q[][N]){
    int sommaDiagonaleQ = sommaDiagonale(Q, 0, 0, N);
	int dim = K;
	for (int riga = 0; riga <= N-dim; riga++){
		for (int colonna = 0; colonna <= N-dim; colonna++){
			if (sommaDiagonale(A, riga, colonna, dim) == sommaDiagonaleQ)  
			{
				cout << "Somma della diagonale di Q: " << sommaDiagonaleQ << endl;
				cout << "Coordinate del primo punto in A di Q': [" << riga << "," << colonna << "]\n";
				sostituisceInA(A, Q, riga, colonna, dim);
				return;
			}
		}
	}
	cout << "Nessuna matrice Q' simile a Q Trovata!" << endl;
}

