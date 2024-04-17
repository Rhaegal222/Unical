#include <iostream>
using namespace std;

int main(){
    int* matricola = new int[6]{2,1,9,9,0,1}; //scrivi sul foglio la tua matricola 
    //1. La seguente istruzione è corretta? Se sì, cosa stampa? 
        cout << *(matricola + 3) << *(matricola + 2) << endl; // 99
    //2. La seguente istruzione è corretta? Se sì, cosa stampa? 
        //cout << *(matricola[0])  << endl; // [NON é corretta]    
    //3. Cosa viene stampato dalla seguente porzione di codice?     
        int& a = matricola[4]; 
        int b = matricola[5]; 
        --a; 
        b += 1; 
        cout << matricola[4] << " " << matricola[5] << endl; //-1 1 
    //4. Come andrebbe deallocata la memoria dinamica allocata inizialmente? 
    /*  //A  
            for(int i = 0; i < 6; i++) 
            delete matricola[i]; 
        //B 
            for(int i = 0; i < 6; i++) 
            delete *matricola[i]; 
        //C 
            Nel main non serve deallocare la memoria dinamica. 
        //D [X]
        delete [] matricola;
    */
    return 0;
}