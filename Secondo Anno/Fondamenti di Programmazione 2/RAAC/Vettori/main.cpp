#include <iostream>
#include "CVector.h"
using namespace std;

int main(){
    CVector p1,p2,p3,p4(2,3);
    
    p1.set(3,4);
    p2.set(5,6);

    p3 = p1 + p2;

    return 0;
}
