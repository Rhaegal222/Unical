#include <list>
#include <iostream>
using namespace std;

bool cmp(const int& rhs, const int& lhs){
    return rhs > lhs;
}

void manualSort(list<int>& lista){
    list<int>::iterator it1, it2;
    for(it1=lista.begin();it1!=lista.end();it1++){
        for(it2=lista.begin();it2!=lista.end();it2++){
            if(it1!=it2 && *it1 < *it2){
                int temp = *it1;
                *it1 = *it2;
                *it2 = temp;
            }
        }
    }
}

int main(){
    list<int> lista{1,2,3,4,5};
    lista.sort(cmp);
    for(auto x:lista) cout << x << " ";
    cout <<endl;
    lista.sort();
    for(auto x:lista) cout << x << " ";
    cout <<endl;
    list<int> lista1{7,2,3,3,5,4,4};
    manualSort(lista1);
    for(auto x:lista1) cout << x << " ";
    cout <<endl;

}