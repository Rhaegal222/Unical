#include "AlberoB.h"
#include "nodes.cpp"
using namespace std;

bool esercizio3(const AlberoB<int>& tree, int sum){ //AlberoB& tree mancava il tipo di dato dell'albero e const
    if(tree.nullo()) return false;
    sum += tree.radice(); // ho messo questa a rigo 8 invece che 7
    if(tree.foglia() && sum == 0) return true;
    return(esercizio3(tree.figlio(SIN), sum) || esercizio3(tree.figlio(DES), sum)); // non ho messo il parametro sum
}

int main()
{
    UNO.insFiglio(SIN, SETTE);                    /*                        */    
    UNO.insFiglio(DES, NOVE);                     /*           1            */    
    NOVE.insFiglio(DES, NOVEB);                   /*         /    \         */    
    NOVEB.insFiglio(SIN, CINQUEB);                /*        7      9        */    
    SETTE.insFiglio(SIN, DUE);                    /*       / \      \       */
    SETTE.insFiglio(DES, SEI);                    /*      2   6      9      */    
    SEI.insFiglio(SIN, CINQUE);                   /*         / \    /       */    
    SEI.insFiglio(DES, UNDICI);                   /*        5   11 -19      */    

    if(esercizio3(UNO,0))cout<<"SI"; else cout<<"NO";
    return 0;
}
