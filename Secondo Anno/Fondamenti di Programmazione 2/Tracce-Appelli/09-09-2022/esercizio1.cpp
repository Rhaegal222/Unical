#include <iostream>
using namespace std;

int main(){
    
    //Data la seguente porzione di programma, rispondere alle domande corrispondenti: 
 
    int* matricola = new int[6] {2,1,9,9,0,1}; 
 
    //1. La seguente istruzione è corretta? Se sì, cosa stampa? 
        cout << *(&matricola[4]); //0
    //2. La seguente istruzione è corretta? Se sì, cosa stampa? 
        cout << *(matricola + 3); //9
    //3. Cosa stampa la seguente porzione di codice?  
        int& second = matricola[1]; 
        matricola[1]++; 
        second ++; 
        cout << second; //3
    //4. Come andrebbe deallocata la memoria dinamica allocata inizialmente? 
        //A: delete matricola[6]; 
        /*B:*/ delete[] matricola; 
        //C: delete matricola; 
        //D: Nel main non va deallocata alcuna memoria dinamica.
    return 0;
}
