/*
Si scriva un programma che, letta una tale sequenza seq(S):
•fornisca in uscita la cardinalità della famiglia, cioè il numero degli insiemi
che essa contiene;
•fornisca in uscita il massimo delle cardinalità degli insiemi della famiglia;
*/
#include <iostream>
using namespace std;

int main(){
    int intero, card_S = 0, card_fam_max = 0, cont_interi = 0;
    while(intero!=-1){
        cin >> intero;
        cont_interi++;
        if (intero == -1){
            cout << "Cardinalita' di S: " << card_S << endl;
            cout << "Massimo della cardinalita': " << card_fam_max-1 << endl;
        }
        else if (intero==0){
            if (cont_interi>card_fam_max)
                card_fam_max = cont_interi;
            if (cont_interi>0)
                card_S++;
            cont_interi = 0;
        }
    }
    return 0;
}