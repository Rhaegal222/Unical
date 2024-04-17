#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

bool cmp(const int& rhs, const int& lhs){
        return rhs > lhs;
    }

class fakeList: protected list<int> {

    public:
    
    int getFakeSize(){return this->size()*2;}

    void insert(int el){
        for(auto x: *this){
            if(x==el){
                this->push_back(el);
                return;
            } 
        }
        this->push_front(el);
    }

    void fakeSort(bool s){
        if(s)
           this->sort();
        else
            this->sort(greater<int>()); //alternativa a cmp
    }

    void manualSort(){
        list<int>::iterator it1, it2;
        for(it1=this->begin();it1!=this->end();it1++){
            for(it2=this->begin();it2!=this->end();it2++){
                if(it1!=it2 && *it1 > *it2){
                    /* *it1, *it2 = *it2, *it1; Non si puó fare: Viene letto come *it1, (*it2 = *it2), *it1; */
                    int temp = *it1;
                    *it1 = *it2;
                    *it2 = temp;
                }
            }
        }
    }

    void fakeClear(bool c){
        if(c) this->clear();
    }
    

};