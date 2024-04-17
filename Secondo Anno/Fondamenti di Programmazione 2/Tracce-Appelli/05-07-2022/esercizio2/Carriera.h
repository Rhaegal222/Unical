#include <iostream>
#include <string>

using namespace std;

class Carriera
{
private:
    int dim = 50;
    int numAppelli = 0;
    bool* esiti = new bool[dim];
    string* nomiEsami = new string[dim];

public:
    Carriera(){};
    Carriera(Carriera& c){
        this->esiti=c.esiti;
        this->nomiEsami=c.nomiEsami;
        this->numAppelli=c.numAppelli;
    };
    ~Carriera(){
        delete[]esiti;
        delete[]nomiEsami;
    }

    Carriera operator=(Carriera& c){
        this->esiti=c.esiti;
        this->nomiEsami=c.nomiEsami;
        this->numAppelli=c.numAppelli;
        return *this;
    }
    
    void aggiungiTentativo(string nome, bool esito){
        numAppelli++;
        
        if(dim<=numAppelli){
            dim += 50;
            bool* replace_esiti = new bool[dim];
            string* replace_nomiEsami = new string[dim];

            for(int i=0; i<numAppelli-1; i++) replace_esiti[i] = esiti[i];
            for(int i=0; i<numAppelli-1; i++) replace_nomiEsami[i] = nomiEsami[i];

            delete[] esiti;
            delete[] nomiEsami;

            esiti = replace_esiti;
            nomiEsami = replace_nomiEsami;
        }
    
        nomiEsami[numAppelli-1] = nome;
        esiti[numAppelli-1] = esito;
    }
    
    void rimuoviUltimoAppello(){
        numAppelli--;
    }
    
    bool studenteDiligente(){
        int pos = 0, neg = 0;
        for(int i=0; i<numAppelli;i++){
            if(esiti[0]) pos++;
            else neg++;
        }
        if(pos > neg) return true;
        else return false;
    }

    void stampaElencoAppelli(){
		
		cout<<"\n Numero appelli totali:"<<numAppelli<<"\n"<<endl;
		for (int i = 0; i < numAppelli; i++)
		{
			cout<<"Nome esame: "<<nomiEsami[i]<<endl;
			if(esiti[i]==1){
				cout<<"Esito: True"<<endl;
			}
			else{
				cout<<"Esito: False"<<endl;
			}
			cout<<endl;
		}
	}
};
