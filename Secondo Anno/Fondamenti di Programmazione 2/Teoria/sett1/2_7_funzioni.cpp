#include <iostream>
using namespace std;

// funzioni

/*
tipo nome(parametro){
    blocco;
    return ...;
}
*/

/*
    Una lista è formata da
    - nome
    - tipo di ritorno
    - lista di parametri  
    - un corpo
*/

int fact (int val){ //parametro formale
    int ret = 1;
    while (val > 1){
        ret *= val--;
    }
    return ret;
}

/*
int main()
{
    int j = fact(5);
    cout << "Il fattoriale di 5 è: " << j << endl;
    return 0;
}
*/

int main()
{
    int j = 5;
    cout << "Il fattoriale di 5 è: " << fact(j) << endl;
    return 0;
}

/*
void si usa per funzioni che eseguono le operazioni ma non restituiscono nulla
void stampa_stelle(int n){
    for(int i=0; i<n; ++i) cout<<"+";
    cout<<endl;
    return;
}
*/
