#include <iostream>
using namespace std;
    
//Data la seguente porzione di programma rispondere alle domande corrispondenti:  
void func(char& a, char b){     
    char c = a;     
    a = b;     
    b = c; 
} 
int main(){     
    char* nome = new char[3]{'f','r','a'};    
    //1. La seguente istruzione è corretta? Se sì, cosa stampa?     
        //cout << *(nome[1]) << endl; ERRATA
    
    //2. La seguente istruzione è corretta? Se sì, cosa stampa?     
    cout << *(nome + 2) << endl; //a      
    
    //3. La seguente istruzione è corretta? Se sì, cosa stampa?      
    char* a = &nome[2];     
    cout << *(a - 1) << endl; //r 
    
    //4. Cosa viene stampato dalla seguente porzione di codice?       
    char* nome_prof = new char[3]{'m','a','t'};      
    func (nome_prof[0], nome_prof[1]);      
    cout << nome_prof[0] << " " << nome_prof[1] << endl; //a a

    return 0; 
}
