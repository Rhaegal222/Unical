#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "AlberoB.h"

using namespace std;

void raccogliFoglie(const AlberoB<char>& tree, vector<char>& vector) {

    if (tree.nullo()) return;

    vector.push_back(tree.radice());

    raccogliFoglie(tree.figlio(SIN), vector);
    raccogliFoglie(tree.figlio(DES), vector);

    return;
}

bool esercizio3(const AlberoB<char>& tree) {
    vector<char> vector;

    raccogliFoglie(tree, vector);

    for (int i = 0; i < vector.size()-1; i++) {
        if(vector[i] >= vector[i+1]) {
            return false;
        }
    }

    return true;
}

int main(){
    AlberoB<char> A('A');
    AlberoB<char> B('B');
    AlberoB<char> C('C');
    AlberoB<char> D('D');
    AlberoB<char> E('E');
    AlberoB<char> F('F');

    A.insFiglio(SIN, F);
    B.insFiglio(SIN, C);
    A.insFiglio(DES, D);
    D.insFiglio(SIN, E);
    D.insFiglio(DES, B);

    if(esercizio3(A)) cout << "true";
    else cout << "false";
}