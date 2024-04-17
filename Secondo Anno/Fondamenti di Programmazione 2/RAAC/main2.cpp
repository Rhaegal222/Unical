#include <iostream>
using namespace std;

void fun1(const int* p, int* q){
    *q = 0;
}

int main()
{
    int a = 2;
    int* p = &a;
    int* q = &a;
    fun1(p, q);
    cout << a;
    return 0;
}
