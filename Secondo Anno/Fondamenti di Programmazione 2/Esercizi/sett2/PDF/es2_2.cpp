/* Esercizio 2
	PUNTO DI SELLA
	Leggere da tastiera una matrice M di interi di dimensione N x N 
	(con N costante definita) e determinare se la matrice M ha un punto di sella
	Un punto di sella è un elemento della matriche che è contemporaneamente il minimo
	sulla riga ed il massimo sulla colonna
*/

#include<iostream>
using namespace::std;

const int N = 4;

void readMat(int M[][N], int dim){
    for (int i = 0; i < dim; i++){
        for(int j = 0; j < dim; j++){
            cin >> M[i][j];
        }
    }
}

void printMat(int M[][N], int dim){
    for (int i = 0; i < dim; i++){
        for(int j = 0; j < dim; j++){
            cout << M[i][j] << " ";
        }
    cout << endl;
    }
    cout << endl;
}

bool puntoDiSella(int M[][N],int r, int c, int N){ //come trovare un "Punto di Sella"
    int max;
    max = M[r][c];
    for (int i = 0; i < N; i++){
        if (M[i][c] > max) return false;
    }
    return true;
}

bool esistePuntoDiSella(int M[][N], int dim){ //cerco un "Punto di Sella"
    bool trovato = false;
    int min, r = 0, c = 0;
    min = M[0][0];
    for (int i = 0; i < N && !trovato; i++){
        for (int j = 0; j < N && !trovato; j++){
            if(M[i][j] < min){ //se puntoDiSella = True
                min = M[i][j];
                r = i;
                c = j;
            }
        }
        trovato = puntoDiSella(M, r, c, N);
    }
    return trovato;
}

int main(){
    int M[N][N];
    bool esiste = false;

    readMat(M,N);
    printMat(M,N);

    if(esistePuntoDiSella(M,N)) //se esistePuntoDiSella = True
        cout << "Esiste";
    else
        cout << "Non Esiste";
return 0;
}