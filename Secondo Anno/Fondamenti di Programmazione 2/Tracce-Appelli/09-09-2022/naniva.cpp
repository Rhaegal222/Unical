#include<iostream>
#include<vector>
#include<string>

using namespace std;


bool check(vector<string> V, vector<vector<string>> T,int K,vector<string> W){
    //for(auto x:W) cout << x << " "; cout << endl;
    if(W.size()<2){
        return true;
    }
    vector<pair<string,string>> coppia;
    for(int i=0; i<W.size();i++){
        for(int j=i+1; j<W.size();j++){
            coppia.push_back(make_pair(W[i],W[j]));
        }
    }
    bool check, check2;
    for(int i=0; i<T.size();i++ ){
        for(int k =0;k<coppia.size();k++){
            check=false;
            check2=false;
            for(int j=0; j<T.size();j++){
                if(T[i][j]==coppia[k].first)
                    check=true;
                if (check){
                    for(int l=0;l<T.size();l++){
                        if(j!=l){
                            if(T[i][l]==coppia[k].second)
                                check2=true;
                        }
                    }
                }
            }
            if (check && check2)
                return false;
        }
    }
    return true;
}
bool esercizio4(vector<string> V, vector<vector<string>> T,int K,vector<string> W,int j){


    if(W.size()>=K){

        return true;
    }
    if(j==V.size()){

        return false;
    }
    for(int i=j;i<V.size();i++){

        W.push_back(V[i]);
        //cout<<V[i]<<" "<<j<<endl;
        if (check(V,T,K,W)){
            //for (auto x:W) cout<<x; cout<<endl;
            if (esercizio4(V,T,K,W,j+1))return true;
        }
        W.pop_back();

    }

    return false;


}

int main(){

    vector<string> V = {"a","b","c","d","e","f","g","h"};
    
    //vector<vector<string>> T = {{"a","b","c","d","f","h"}, {"b","e","g"}, {"e","a","g"}, {"a","h"}, {"e","f","g","h"},/*{"a","b"},{"b","c"},{"a","c"}*/};
    
    //vector<vector<string>> T = {{"a","b","c","d","e","f","h"}, {"b","e","g"}, {"a","f","g"}, {"a","h"}, {"c","d","g","h"},/*{"a","b"},{"b","c"},{"a","c"}*/};
    
    //vector<vector<string>> T = {{"a","b","c","d","e","f","g","h"}, {"b","e","g"}, {"a","d","g"}, {"g","h"}, {"c","a","g","h"},{"h","b"}/*{"a","b"},{"b","c"},{"a","c"}*/};

    vector<vector<string>> T = {{"a","b","c","d","e","f","g","h"}, {"b","e","g"}, {"a","d","g"}, {"g","h"}, {"d","h"}, {"e","h"}, {"c","a","g","h"},{"h","b"}/*{"a","b"},{"b","c"},{"a","c"}*/};
    
    int K=2;
    vector<string> W;
    if(esercizio4(V,T,K,W,0)) cout << "SI";
    else cout << "NO";

    return 0;
}