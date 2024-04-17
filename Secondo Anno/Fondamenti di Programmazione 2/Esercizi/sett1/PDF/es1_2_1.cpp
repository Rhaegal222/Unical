#include <iostream>
using namespace std;

int main(){
    int prec, att, pros, cont_picchi = 0, cont_giorni = 0;
    cout << "Inserire la sequenza di numeri: ";
    cin >> prec;
    cont_giorni++;
    
    if (prec >= 0)
        cout << "Inserire la sequenza di numeri: ";
        cin >> att;
        cont_giorni++;
    
    if (att>=0)
        while(pros >= 0){
            cout << "Inserire la sequenza di numeri: ";
            cin >> pros;
            while(pros > 100){
                cout << "Errore, inserire un numero valido!";
                cin >> pros;
            }
            // qui avrà messo sicuro un numero <= di 100
            if(pros >= 0){
                cont_giorni++;
                if (att > prec && att > pros){
                    cout << "c'e' un picco" << att << " " << cont_giorni-1 << endl;
                    cont_picchi++;
                }
                prec = att;
                att = pros;
            }
        }
        cout << "Numero di picchi massimi rilevati: " << cont_picchi << endl;
        cout << "Numero totale dei dati: "<< cont_giorni << endl;
        return 0;
}