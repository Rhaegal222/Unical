#include <vector>
#include "Grafo.h"
#include "GrafoNonOrientato.h"

using namespace std;

void add(int x, vector<int> sol) { sol.push_back(x); }
void remove(int x, vector<int> sol) { sol.pop_back(); }

bool isComplete(vector<int> sol, const Grafo& g){
    return g.n() == size(sol);
}

bool canAdd(int x, vector<int> sol, const Grafo& g) {
    int s = size(sol);
    for(int i = 0; i < s; i++) 
        if(g(i, s) && sol[i] == x) // se sono confinanti
            return false;
    return true;
}

bool solve(vector<int> sol) {
    x = MIN_VAL
    while(x <= MAX_VAL) {
        if(canAdd(x, sol)) {
            add(x, sol)
            if(isComplete(sol)) 
                return true
            else if(solve(sol))
                return true
            else {
                remove(x,sol)
                x = next(x)
            }
        }
        else
            x = next(x)
    }
    return false
}