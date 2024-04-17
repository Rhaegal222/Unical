#include "Grafo.h"
#include "GrafoNonOrientato.h"

#include <queue>
#include <vector>
#include <List>
#include <iostream>
#include <algorithm>

using namespace std;

/*Esercizio 2*/
void stampaGrafo(const Grafo& g){
        vector<vector<bool>> archi=g.mat_adiacenza();
        cout<<"Numero di nodi: "<<g.n()<<endl<<endl;
        for(int i=0; i<g.n(); i++) 
            cout <<"Grado del nodo "<<i<<": "<<g.grado(i)<<endl;
        cout<<endl<<"Numero di archi: "<<g.m()<<endl<<endl;
        cout<<"Lista archi: "<<endl;
        for(int i=0;i<g.n();i++){
            for(int j=0;j<g.n();j++){
                if(archi[i][j])
                    cout<<"Arco i: "<<i<<" j: "<<j<<endl;
            }
        }
    }

/*Esercizio 3*/
unsigned getGradoMassimo(const GrafoNonOrientato& g){
    unsigned gradoMassimo = 0;
    for(int i=0; i<g.n(); i++){
        if(g.grado(i)>gradoMassimo) gradoMassimo=g.grado(i);
    }
    return gradoMassimo;
}
pair<unsigned, vector<unsigned>> getNodiConGradoMassimo(const GrafoNonOrientato& g){
    vector<unsigned> NodiConGradoMassimo;
    unsigned gradoMassimo = getGradoMassimo(g);

    for(int i=0; i<g.n(); i++)
        if(g.grado(i)==gradoMassimo) NodiConGradoMassimo.push_back(i);

    return pair<unsigned, vector<unsigned>> (gradoMassimo, NodiConGradoMassimo);
}

/*Esercizio 4*/
vector<unsigned> NodiPerOgniGrado(const GrafoNonOrientato& g){
    vector<unsigned> gradi;

    for(int i=0;i<=getGradoMassimo(g);i++){
        int n_nodi = 0;
        for(int j=0;j<g.n();j++){
            if(g.grado(j) == i) n_nodi++;
        }
        gradi.push_back(n_nodi);
    }
    return gradi;
}

bool stessoNumeroNodiStessoGrado(const GrafoNonOrientato& g, const GrafoNonOrientato& h){
    if(getGradoMassimo(g) != getGradoMassimo(h)) return false;
    if(g.n() != h.n()) return false;
    vector<unsigned> gradi_g = NodiPerOgniGrado(g);
    vector<unsigned> gradi_h = NodiPerOgniGrado(h);
    if(gradi_g.size() != gradi_h.size()) return false;
    for(int i=0; i<gradi_g.size(); i++)
        if(gradi_g[i] != gradi_h[i]) return false;
    return true;
}

/*Esercizio 5*/
bool almenoUnNodoAdiacenteATutti(const GrafoNonOrientato& g){
    for(int i=0; i<g.n(); i++){
        if(g.grado(i)>=g.n()-1) return true;}
    return false;
}

/*Esercizio 6*/
int getNumeroDiViciniInComune(vector<unsigned> vicinato1, vector<unsigned> vicinato2){
    int numeroDiViciniInComune = 0;
    for(int i=0; i<vicinato1.size(); i++){
        for(int j=0; j<vicinato2.size(); j++){
            if(vicinato1[i] == vicinato2[j]) numeroDiViciniInComune+=1;
        }
    }
    return numeroDiViciniInComune;
}
pair<unsigned,unsigned> getCoppiaPiuAdiacenti(const GrafoNonOrientato& g){
    pair<unsigned, unsigned> CoppiaPiuAdiacenti;
    int numeroDiViciniInComune = 0;
    for(int i=0; i<g.n(); i++){
        for(int j=0; j<g.n(); j++){
            if(i!=j){
                int temp = getNumeroDiViciniInComune(g.vicinato(i), g.vicinato(j));
                if(temp > numeroDiViciniInComune){
                    numeroDiViciniInComune = temp;
                    CoppiaPiuAdiacenti.first = i;
                    CoppiaPiuAdiacenti.second = j;
                }
            }
        }
    }
    return CoppiaPiuAdiacenti;
}

/*Esercizio 7*/
bool connesso(const GrafoNonOrientato& g){
    vector<bool> verifica(g.n(), false); verifica[0]=true;
    queue<unsigned> coda;
    vector<unsigned> vicinato = g.vicinato(0);
    
    for(auto i : vicinato)
        if(!verifica[i]) coda.push(i);
    
    while(!coda.empty()){
        unsigned nodo = coda.front();
        
        verifica[nodo] = true;
        vector<unsigned> vicinato = g.vicinato(nodo);
        
        for(auto i : vicinato)
            if(!verifica[i]) coda.push(i);
        coda.pop();
    }
    
    for(auto i : verifica) 
        if(!i) 
            return false; 
    return true;
}

/*Esercizio 8*/
bool percorso(const GrafoNonOrientato& g, vector<bool>& visitati, unsigned nodo_vicino, unsigned n){
    queue<unsigned> da_visitare; da_visitare.push(nodo_vicino);
    int passi = 1;

    while(!da_visitare.empty()){
        visitati[da_visitare.front()]=true;
        for(auto x:g.vicinato(da_visitare.front())){
            if(!visitati[x]) da_visitare.push(x);
            else if(x==n && passi>1) return true;
        }
        passi++;
        da_visitare.pop();
    }
    return false;
}

bool inUnCiclo(const GrafoNonOrientato& g, unsigned n){
    cout << "\nIl nodo " << n << " fa parte di un ciclo: ";
    int passi = 0; //conto i passi per evitare di trovare il vicinato

    vector<bool> visitati(g.n(), false); visitati[n] = true;

    vector<unsigned> vicinato_n = g.vicinato(n);

    while(passi<g.vicinato(n).size()){
        bool nodo = percorso(g, visitati, vicinato_n[passi], n);
        if(nodo) return true;
        passi++;
    }
    return false;   
}

/*Esercizio 10*/
bool proprieta_2(const Grafo& g, vector<int> pesi){
    for(int i=0;i<g.n();i++){
        int somma = 0;
        for(auto x:g.vicinato(i)) somma+=pesi[x];
        cout << "Peso: " << g.grado(i)*pesi[i] << " Somma: " << somma;
        //if((g.grado(i)*pesi[i])<=somma) return false;
    }
    return true;
}

int	main(){
    Grafo og(6);
    og(0,1,true); //A->B
    og(1,2,true);og(1,3,true); //B->C; B->E
    og(2,3,true);og(2,4,true); //C->E; C->D
    og(3,5,true); //E->F;
    og(4,5,true); //D->F;

    vector<vector<unsigned>> weights = {{0,5,0,0,0,0},
                                        {0,0,4,3,0,0},
                                        {0,0,0,2,6,0},
                                        {0,0,0,0,0,1},
                                        {0,0,0,0,0,7},
                                        {0,0,0,0,0,0}};

    Grafo og1(2);
    og1(0,1,true);

    GrafoNonOrientato nog1(6);
    nog1(0,1,true); 
    nog1(1,2,true);nog1(1,3,true);
    nog1(2,3,true);nog1(2,4,true);
    nog1(3,5,true);
    nog1(4,5,true);

    GrafoNonOrientato nog2(6);
    nog2(0,1,true);nog2(0,2,true);
    nog2(1,3,true);nog2(1,4,true);
    nog2(2,3,true);
    nog2(3,4,true);
    nog2(4,5,true);

    GrafoNonOrientato nog3(8);
    nog3(0,1,true);
    nog3(1,2,true);nog3(1,3,true);
    nog3(2,6,true);
    nog3(4,5,true);
    nog3(5,6,true);nog3(5,7,true);
    nog3(6,7,true);

    GrafoNonOrientato nog4(4);
    nog4(0,1,true); //A->B
    nog4(1,2,true);nog4(1,3,true); //B->C; B->E

    GrafoNonOrientato nog5(6);
    nog5(0,1,true);nog5(0,2,true);
    nog5(1,3,true);nog5(1,4,true);
    nog5(2,3,true);
    nog5(3,4,true);

    GrafoNonOrientato nog6(6);
    nog6(0,1,true);
    nog6(1,2,true); nog6(1,3,true);
    nog6(2,3,true); nog6(2,4,true);
    nog6(3,5,true);
    nog6(4,5,true);

    /*Esercizio 2*/
    stampaGrafo(og);

    /*Esercizio 3*/
    pair<unsigned, vector<unsigned>> NodiConGradoMassimo = getNodiConGradoMassimo(nog1);
    cout << "\nGrado massimo del Grafo non orientato: " << NodiConGradoMassimo.first << endl;
    cout << "Nodi con Grado massimo del Grafo non orientato: ";
    vector<unsigned> VettoreNodiConGradoMassimo = NodiConGradoMassimo.second;
    for(auto i : VettoreNodiConGradoMassimo) cout << i << " ";

    /*Esercizio 4*/
    cout << "\n\nEntrambi i grafi non orientati hanno lo stesso numero di nodi per ogni possibile grado: ";
    if(stessoNumeroNodiStessoGrado(nog1,nog2)) cout << "SI" << endl;
    else cout << "NO" << endl;

    /*Esercizio 5*/
    cout << "\nAlmeno un nodo adiacente a tutti: ";
    if(almenoUnNodoAdiacenteATutti(nog4)) cout << "SI" << endl;
    else cout << "NO" << endl;

    /*Esercizio 6*/
    pair<unsigned,unsigned> CoppiaPiuAdiacenti = getCoppiaPiuAdiacenti(nog1);
    cout << "\nCoppia di nodi con maggior numero di vicini adiacenti: "  << CoppiaPiuAdiacenti.first << " " << CoppiaPiuAdiacenti.second << endl;

    /*Esercizio 7*/
    cout << "\nGrafo connesso: ";
    if(connesso(nog6)) cout << "SI" << endl;
    else cout << "NO" << endl;

    /*Esercizio 8*/
    if(inUnCiclo(nog6, 0)) cout << "SI" << endl;
    else cout << "NO" << endl;

    /*Esercizio 9*/

    /*Esercizio 10*/
    cout << "Esercizio fatto ma non abbiamo i testcase" << endl;
}