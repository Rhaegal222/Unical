#include <iostream>
using namespace std;

const int dim=10;
bool cerca(const int v[], const int dim, const int x);
int main(){
    int v[dim], x;
    for(int i=0; i<dim; ++i)cin>>v[i];
    cin>>x;
    if(cerca(v, dim, x))
        cout << "Trovato";
    else cout<<"Non Trovato";
    return 0;
}
bool cerca(const int v[], const int dim, const int x){
    bool trovato = false;
    for(int i=0; i<dim&&!trovato; i++){
        if(v[i]==x) trovato = true;
    }
    return trovato;
}