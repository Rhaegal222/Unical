#include "Nodes.cpp"

/* Funzioni Ausiliarie*/
void vectLivelli(const AlberoB<int>& tree, int level, vector<int>& levels){
    if (tree.nullo()) return;
    
    if(level > levels.size()) levels.push_back(0);
    
    levels[level-1] += tree.radice();
    //cout << "";
    //for(auto i : levels) cout << i << " ";
    //cout << endl;

    vectLivelli(tree.figlio(SIN), level+1, levels);
    vectLivelli(tree.figlio(DES), level+1, levels);
}

/*Esercizio 1*/
template<typename T>
void stampaAlbero(AlberoB<T> tree, int pr){
    if(tree.nullo()) return;
    for(int i=0; i<pr; i++) cout << " ";
    cout<<tree.radice()<<endl;
    stampaAlbero(tree.figlio(SIN), pr+1);
    stampaAlbero(tree.figlio(DES), pr+1);
}

/*Esercizio 2*/
template <typename T>
bool isHeap(const AlberoB<T>& tree){
    if(tree.nullo() || tree.foglia()) return true;
    if(!tree.figlio(DES).nullo() && tree.radice() <= tree.figlio(DES).radice()){
        return false;
    }
    
    if(!tree.figlio(SIN).nullo() && tree.radice() <= tree.figlio(SIN).radice()) {
        return false;
    }
    return isHeap(tree.figlio(SIN)) && isHeap(tree.figlio(DES));
}

/*Esercizio 3*/
bool ogniPercorsoRadiceFoglia(const AlberoB<int>& tree, int costo,  int k){
    if(tree.nullo())return true;
    
    costo += tree.radice(); 
    if(costo > k){ 
        cout << "Costo = " << costo << endl;
        return false;
    }
    return ogniPercorsoRadiceFoglia(tree.figlio(DES), costo, k) && ogniPercorsoRadiceFoglia(tree.figlio(SIN), costo, k);
}

/*Esercizio 4*/
bool pariEDispari(const AlberoB<int>& tree, int level){
    if (tree.nullo())
        return true;
    if ((level % 2 == 0 && tree.radice() % 2 != 0) || (level % 2 != 0 && tree.radice() % 2 == 0)){
        return false;
    }
    return pariEDispari(tree.figlio(SIN), level + 1) && pariEDispari(tree.figlio(DES), level + 1);
}

/*Esercizio 5*/
    bool vocaliEConsonanti(const AlberoB<char>& tree, int diff){
    
    if(tree.nullo()) return true;
    if(tree.radice() == 'a' || tree.radice() == 'e' || tree.radice() == 'i' || tree.radice() == 'o' || tree.radice() == 'u') diff++;
    else diff--;
    if(tree.foglia()){
        if (abs(diff)>1) return false; 
        else return true;
    }
    return vocaliEConsonanti(tree.figlio(DES), diff) && vocaliEConsonanti(tree.figlio(SIN), diff);
}

/*Esercizio 6*/
int sommaPath(const AlberoB<int>& tree, int &sum, int num){
    if(tree.nullo()) return sum;
    
    if(tree.foglia()){
        num *= 10;
        num += tree.radice();
        sum+=num;
        return sum;
    }
    else num *= 10;
    
    num += tree.radice();
    sommaPath(tree.figlio(DES), sum, num);
    sommaPath(tree.figlio(SIN), sum, num);
}

/*Esercizio 7*/
bool sommaLivello(const AlberoB<int>& tree, int k){
    vector<int> levels;
    vectLivelli(tree, 1, levels);
    for(auto i : levels){ 
        if(i>k) 
            return false;
    }
    return true;
}

/*Esercizio 8*/
bool sommaLivelliAdiacenti(const AlberoB<int>& tree, int k){
    vector<int> levels;
    vectLivelli(tree, 1, levels);
    for(int i=0; i<levels.size()-1;i++){ 
        if(levels[i]+levels[i+1]>k) 
            return false;
    }
    return true;
}

/*Esercizio 9*/
bool fogliePosEqfoglieNeg(const AlberoB<int>& tree, int& diff){
    if (tree.nullo()) return diff;
    if(tree.foglia()){
        //cout << tree.radice() << " ";
        if(tree.radice()>0) diff++;
        else diff--;
    }
    
    return (fogliePosEqfoglieNeg(tree.figlio(SIN), diff) == fogliePosEqfoglieNeg(tree.figlio(DES), diff) == 0);
}

/*Esercizio 10*/
template<typename T>
void vecToAlbero(const vector<T>& vect){

    vector<AlberoB<T>> nodes;

    for(auto i : vect){
        AlberoB<T> node(i);
        nodes.push_back(node);
    }

    AlberoB<T> tree = nodes[0];

    for(int i=0; i<nodes.size()/2; i++){
        nodes[i].insFiglio(SIN, nodes[(i*2)+1]);
        nodes[i].insFiglio(DES, nodes[(i*2)+2]);
    }

    stampaAlbero(tree, 0);
}