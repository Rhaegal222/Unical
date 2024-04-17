#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool cmp(const pair<string, int>& r, const pair<string, int>& l){
        return r.second > l.second;
}

bool esercizio4(){
//    vector<string> S {"ab","cde","xyz","q","q42","8a8b","ccc"};
    
//    for(auto x:S) S_val.push_back(make_pair(x, val(x)));

    vector<pair<string,int>> S_val = {make_pair("ab",11),make_pair("cde",11),make_pair("xyz",12),make_pair("q",8),make_pair("q42",7),make_pair("8a88",34),make_pair("ccc",23)};

    sort(S_val.begin(), S_val.end(), cmp);
    
    for(auto x: S_val) cout << x.second << " "; cout << endl;

    vector<pair<string, int>> S1;
    vector<pair<string, int>> S2;

    int sumS1=0, sumS2=0;

    for(auto x:S_val){
        if(sumS1 <= sumS2){
            S1.push_back(x);
            sumS1+=x.second;
        }
        else{
            S2.push_back(x);
            sumS2+=x.second;    
        }
    }
    for(auto x: S1) cout << x.second << " ";
    cout << endl;
    for(auto x: S2) cout << x.second << " ";

    if(S1.size() == S2.size()) return true;
    else return false;
}

int main()
{
    esercizio4();
    return 0;
}
