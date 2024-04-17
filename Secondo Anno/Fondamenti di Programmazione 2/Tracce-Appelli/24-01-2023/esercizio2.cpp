#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class StatisticheVettore{
public:
    virtual double compute(const vector<int>&) = 0; //virtuale pura
};

class MediaVettore : public StatisticheVettore{
    public:
    double compute(const vector<int>& V){
        double sum = 0;
        for(auto x:V) sum+=x;
        if(sum>0)return sum/V.size();
        else return sum;
    }
};

class ModaVettore : public StatisticheVettore{
    public:
    double compute(const vector<int>& V){
        pair<int, int> moda(V[0], 1);
        for(int i=0; i<V.size(); i++){
            double cont = 0;
            for(int j=0; j<V.size(); j++){
                if(i!=j && V[i] == V[j]) cont++;
            }
            if(cont>moda.second){
                moda.first = i;
                moda.second = cont;
            }
        }
        return moda.second;
    }
};

class MedianaVettore : public StatisticheVettore{
    public:
    double compute(const vector<int>& V){
        vector<double> y(V.begin(), V.end());
        sort(y.begin(), y.end());
        if(y.size()%2==0)return(y[y.size()/2]+y[(y.size()/2)-1])/2;
        else return y[y.size()/2];
    }
};

int main(){
    StatisticheVettore* v1 = new MediaVettore;
    StatisticheVettore* v2 = new ModaVettore;
    StatisticheVettore* v3 = new MedianaVettore;

    vector<int> vect {3,1,2,1};
    vector<StatisticheVettore*> StatVect;
    
    StatVect.push_back(v1);
    StatVect.push_back(v2);
    StatVect.push_back(v3);

    for(auto x:StatVect) cout << x->compute(vect) << endl;

    delete v1;
    delete v2;
    delete v3;

    return 0;
}
