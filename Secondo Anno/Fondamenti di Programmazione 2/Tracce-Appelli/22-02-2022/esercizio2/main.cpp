#include <iostream>
#include "fakeList.h"
#include <iostream>
using namespace std;
int main(){
    fakeList l;
    //cout<<l.getFakeSize()<<endl;
    l.insert(4);
    l.insert(6);
    l.insert(3);
    l.fakeSort(false);
    l.fakeClear(true);
    //cout<<endl<<l.getFakeSize()<< endl;
    return 0;
}
