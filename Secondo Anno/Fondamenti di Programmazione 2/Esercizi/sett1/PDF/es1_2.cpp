#include <iostream>
using namespace std;

int main(){
    int prec, att, pros;
    int cont = 0, picchi = 0;
    cin >> prec;
    cont++;
    if (prec >= 0)
        cin >> att;
        cont++;
    if (att >= 0)
        while(pros >= 0)
        {
            cin >> pros;
            if (att > prec && att > pros){
                cout << att << " " << cont << endl;
                picchi++;
            }
            cont++;
            prec = att;
            att = pros;
        }
        cout << "Numero di picchi massimi rilevati: " << picchi << endl;
        cout << "Numero totale dei dati: "<< cont-1 << endl;
}