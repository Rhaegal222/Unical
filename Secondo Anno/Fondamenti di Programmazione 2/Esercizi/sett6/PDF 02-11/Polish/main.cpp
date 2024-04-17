#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    string espressione;
    cout<<"Inserisci espressione: ";
    getline(cin, espressione); //serve a prendere in input l'intera linea inclusi gli spazi.

    int cont, temp; //cont: conta le posizioni; temp: salva i risultati temporanei.
    char c;
    vector<int> res;

    for (int i = 0; i < espressione.length(); i++)
    {
        if (espressione[i] != '+' && espressione[i] != '*' && espressione[i] !=  '-' && espressione[i] != '/' && espressione[i] != ' ')
        {
            c=espressione[i];
            res.push_back(c-48); //aggiungo il numero a res
            //-48 perchè le cifre in ascii partono da 48(0) e arrivano a 57(9)
        }
        else if(espressione[i] != ' ')
        {
            if (espressione[i] == '+')  //USA IL SINGOLO APICE 
            {
                cont=res.size()-1; //ultima posizione
                temp = res[cont]+res[cont-1];
                res.erase(res.begin()+cont); 
                res[cont-1]=temp; 
        
            }
            
            if (espressione[i] == '*')  //USA IL SINGOLO APICE 
            {
                cont=res.size()-1; //ultima posizione dell'array
                temp = res[cont-1]*res[cont];
                res.erase(res.begin()+cont); 
                res[cont-1]=temp; 
            }
            
            if (espressione[i] == '-')  //USA IL SINGOLO APICE 
            {
                cont=res.size()-1; //ultima posizione
                temp = res[cont-1]-res[cont];
                res.erase(res.begin()+cont); 
                res[cont-1]=temp; 
            
            }
            
            if (espressione[i] == '/')  //USA IL SINGOLO APICE 
            {
                cont=res.size()-1; //ultima posizione
                temp = res[cont-1]/res[cont];
                res.erase(res.begin()+cont); 
                res[cont-1]=temp; 
            
            }
        }
    }

    int a=res[0];
    std::cout<<"Risultato: "<<a;

    return 0;
}