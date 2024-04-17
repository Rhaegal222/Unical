#include <iostream>
#include <string>
using namespace std;

int main(){
    
    //Data la seguente porzione di programma, rispondere alle domande corrispondenti: 
    string* nc = new string[2]{"Francesco", "Vecchio"}; 
    //1: La seguente istruzione è corretta? Se sì, cosa stampa?  
        cout << nc[0][2]; //a
    //2: La seguente istruzione è corretta? Se sì, cosa stampa? 
        cout << *(nc + 1); //Vecchio
    //3: La seguente porzione di codice è corretta? Se sì, cosa fa? 
        for (int i = 0; i < nc[0].length();i++) 
            cout << nc[0][nc[0].length() - 1 - i]; //ocsecnarF
    //4: Come andrebbe deallocata la memoria dinamica allocata in questo main? 
        //A: delete nc[2]; 
        //B: delete nc; 
        /*C:*/ delete [] nc; 
        //D: nel main non serve il distruttore.

    return 0; 
}
