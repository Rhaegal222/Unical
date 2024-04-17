/* Esercizio 2
	Sia A un array di interi di dimensione n. Scrivere una funzione ricorsiva che
    calcoli la somma degli elementi di A.
*/

#include<iostream>
using namespace::std;

const int dim = 100;

void readArr(int A[dim], int N){
    int x;
    for (int i = 0; i < N; i++){
        cin >> x;
        A[i] = x;
    }
}

void printArr(int A[dim], int N){
    for (int i = 0; i < N; i++)
        cout << A[i] << " ";
    cout << endl;
}

int sumArr(int A[dim], int N, int sum){
    if (N < 0)
        return sum;
    else{
        sum += A[N];
        return sumArr(A, N-1, sum);
        }
}

int main(){
    int A[dim], N;
    cout << "Inserisci la dimensione dell'array: ";
    cin >> N;

    readArr(A,N);
    printArr(A,N);

    cout << sumArr(A, N-1, 0);

return 0;
}