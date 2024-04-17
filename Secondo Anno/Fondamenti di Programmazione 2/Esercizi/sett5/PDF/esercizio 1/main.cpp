#include <iostream>
#include "calcolatrice.cpp"
using namespace :: std;

int main(){
    const char* phrases[4]
        = { "Il risultato della somma", 
            "Il risultato della sottrazione", 
            "Il risultato della moltiplicazione", 
            "Il risultato della divisione" };
    
    const char* types[3]
        = { "int", 
            "double", 
            "float"};
    
    short k;

    for(int i=0; i<3; i++)
        cout << i+1 << " " << types[i] << endl;

    cout<<"Scegli il tipo: ";

    cin >> k;
    
    switch(k){
        case 1:
        {
            int n1,n2;
            cout << "Inserisci due numeri: ";
            cin >> n1 >> n2;
            Calcolatrice<int> C1(n1, n2);
            const int results[4] = {C1.Somma(), C1.Sottrazione(), C1.Moltiplicazione(), C1.Divisione()};

            for(int i=0; i<4; i++)
                cout << phrases[i] << " " << types[0] << ": " << results[i] << endl;
            return 0;
        }
        
        case 2:
        {
            double n1, n2;
            cout << "Inserisci due numeri: ";
            cin >> n1 >> n2;
            Calcolatrice<int> C1(n1, n2);
            const int results[4] = {C1.Somma(), C1.Sottrazione(), C1.Moltiplicazione(), C1.Divisione()};

            for(int i=0; i<4; i++)
                cout << phrases[i] << " " << types[1] << ": " << results[i] << endl;
            return 0;
        }
        
        case 3:
        {
            float n1,n2;
            cout << "Inserisci due numeri: ";
            cin >> n1 >> n2;
            Calcolatrice<int> C1(n1, n2);
            const int results[4] = {C1.Somma(), C1.Sottrazione(), C1.Moltiplicazione(), C1.Divisione()};

            for(int i=0; i<4; i++)
                cout << phrases[i] << " " << types[2] << ": " << results[i] << endl;
            return 0;
        }
    }
}