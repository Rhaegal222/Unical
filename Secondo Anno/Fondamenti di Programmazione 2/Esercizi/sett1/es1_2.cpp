/*
Scrivi un programma che stampi le tabelline fino a 10 ben formattata
*/
#include <iostream>
using namespace std;

int main(){
    for (int i = 0; i <= 10; i++){
        for (int j = 0; j <= 10; j++){
            if (i == 0 && j == 0){
                cout << "\t";
            }
            if(i == 0 && j < 10){
                cout << j+1 << "\t";
            }
            else if(j == 0){
                cout << i << "\t";
            }
            else if(i != 0 && j != 0){
                cout << i*j << "\t";
            }
        }
        cout << endl;
    }
}