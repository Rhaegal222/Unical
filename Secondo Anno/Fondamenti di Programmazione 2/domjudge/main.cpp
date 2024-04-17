#include <iostream>
using namespace std;

void func(char& a, char b){    
    char c = a;    
    a = b;     
    b = c;
}

int main()
{
    char* nome = new char[3]{'f','r','a'};
    //1. La seguente istruzione è corretta? Se sì, cosa stampa?
    //ERRATA cout << *(nome[1]) << endl;   
    cout << nome[1] << endl; //CORRETTA stampa: r
    
    //2. La seguente istruzione è corretta? Se sì, cosa stampa?
    cout << *(nome + 2) << endl; //CORRETTA stampa: a      
    
    //3. La seguente istruzione è corretta? Se sì, cosa stampa? 
    char* a = &nome[2]; // a = a
    cout << *(a - 1) << endl; // r

    //4. Cosa viene stampato dalla seguente porzione di codice?      
    char* nome_prof = new char[3]{'m','a','t'};
    func (nome_prof[0], nome_prof[1]);
    cout << nome_prof[0] << " " << nome_prof[1] << endl; //a a
}
