/* Esercizio 4 */

#include<iostream>
#include<cmath>
using namespace::std;

const int N = 4;

bool allineate(int V[N], int A[][N], int B[][N]){
    for(int i = 0; i < N; i++){
        if (V[i] < N-3) return false;
    }

    for (int x = 0; x < N; x++){
        for(int y = 0; y < N; y++){
            for(int j = 0; j < N; j++){
                if ((A[x][j] == B[y][j]) && (abs(x-y)>=2)){
                    cout << "A: " << A[x][j] << " B: " << B[y][j] << " x: "<< x << " y: " << y << " j: " << j << " abs: " << abs(x-y) << endl;
                    return false;
                } 
            }
        }
    }
    return true;
}

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

int somiglianza(int A[][N], int B[][N], int ca, int cb, int N){ //come trovare il "Grado di somiglianza"
    int grado = 0;
    for(int i = 0; i < N; i++){
        bool cond = true;
        for(int j = 0; j < N; j++){
            if (A[i][ca] == B[j][cb] && cond){
                grado++;
                cond = !cond;
            }
        }
    }
    return grado;
}

int main(){
    int A[N][N], B[N][N], V[N];
    int ca, cb, grado;

    readMat(A,N);
    readMat(B,N);

    printMat(A, N);
    printMat(B, N);

    for(int i = 0; i < N; i++){
        V[i] = somiglianza(A, B, i, i, N);
    }

    for(int i = 0; i < N; i++){
        cout << V[i] << " ";
    }
    cout << endl;

    if(allineate(V, A, B)) cout << "Allineate di grado 3";
    else cout << "Non allineate di grado 3";
    
    return 0;
}