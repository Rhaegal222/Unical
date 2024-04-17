#include <vector>
#include <iostream>
#include <algorithm>
#include <list>

#include "Grafo.h"
#include "GrafoNonOrientato.h"

using namespace std;

void dijkstra_single_nodes_single_source(Grafo& g, vector<vector<unsigned>>& weights, vector<bool> visited, int nodo, int dest, int& cost_min, int cost_act){
    if(nodo==dest && cost_min>cost_act){
        cout << "\nNuovo Percorso: " << endl;
        cost_min = cost_act;
    }
    
    visited[nodo] = true;
    vector<unsigned> vicinato = g.vicinato(nodo);
    
    for(auto x:vicinato){
        if(!visited[x]){
            cost_act += weights[nodo][x];
            cout << "Partenza: " << nodo << " Arrivo: " << x << " Costo: " << cost_act << endl;
            dijkstra_single_nodes_single_source(g, weights, visited, x, dest, cost_min, cost_act);
            cost_act -= weights[nodo][x];
        }
    }
}

int main(int argc, char const *argv[])
{
    Grafo og(6);                                /*    1---2      B---C     */
    og(0,1,true); //A->B                        /*   / \ / \    / \ / \    */
    og(1,2,true);og(1,3,true); //B->C; B->E     /*  0   4   3  A   E   D   */
    og(2,3,true);og(2,4,true); //C->E; C->D     /*       \ /        \ /    */
    og(3,5,true); //E->F;                       /*        5          F     */
    og(4,5,true); //D->F;                       /*                         */

    Grafo og1(7);                                /*   *1   2*--6* */
    og1(0,1,true);                               /*   / \ / \ /   */
    og1(1,4,true);                               /*  0  *4*-*3    */
    og1(2,3,true);og1(2,4,true);                 /*       \ /     */
    og1(3,5,true);og1(3,6,true);                 /*       *5*     */
    og1(4,3,true);og1(4,5,true);                 /*               */
    og1(6,2,true);

    Grafo og2(8);
    og2(0,1,true);og2(0,5,true);
    og2(1,2,true);
    og2(2,3,true);
    og2(3,4,true);og2(3,5,true);
    og2(4,5,true);
    og2(5,6,true);og2(5,7,true);
    og2(6,7,true);

    vector<bool> visited(og2.n(), false);

    vector<vector<unsigned>> weights = {{0,1,1,1,1,1,1,1},
                                        {1,0,1,1,1,1,1,1},
                                        {1,1,0,1,1,1,1,1},
                                        {1,1,1,0,1,1,1,1},
                                        {1,1,1,1,0,1,1,1},
                                        {1,1,1,1,1,0,1,1},
                                        {1,1,1,1,1,1,0,1},
                                        {1,1,1,1,1,1,1,0}};

    int costo = 1000000;
    cout << "Calcolo Percorso: " << endl;
    dijkstra_single_nodes_single_source(og2, weights, visited, 0, 5, costo, 0);
    cout << "Costo minimo: " << costo << endl;

  list<int*> lista;
}