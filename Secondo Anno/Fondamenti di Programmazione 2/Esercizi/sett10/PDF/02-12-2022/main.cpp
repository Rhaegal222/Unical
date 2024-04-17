#include "Grafo.h"
#include "GrafoNonOrientato.h"

#include <queue>
#include <vector>
#include <List>
#include <iostream>
#include <algorithm>

using namespace std;

/*Prendere k elementi, fare la somma, vedere se é la somma massima, se é la somma massima di k elementi stampare la somma, l'indice degli elementi, e gli elementi*/
bool bigger_than(const pair<int,int>& a, const pair<int,int>& b){
    return a.first > b.first;
}
int main()
{   
    int n, k, x, sum=0; cin >> n >> k;
    vector<pair<int, int>> seq;
    for(int i=0;i<n;i++){
        cin >> x;
        seq.push_back(make_pair(x, i));
    }
    
    sort(seq.begin(), seq.end(), bigger_than);
    
    for(int i=0;i<k;i++){
        cout << "Indice: " << seq[i].second << " Valore: " << seq[i].first << endl;  
        sum+=seq[i].first;}

    cout << "Somma: " << sum;

return 0;
}
