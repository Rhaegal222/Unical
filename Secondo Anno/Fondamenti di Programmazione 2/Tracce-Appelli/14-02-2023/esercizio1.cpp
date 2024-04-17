#include <iostream>
using namespace std;
int main()
{
    int v[] = {2,1,9,9,0,1};
    int* x = v+2;
    int* y = v+4;
    *(x+1) = *x;
    *(y+1) = *y;
    for(int i=0;i<6;++i) cout << v[i];
    cout << endl;

    cout<<(y-x)+(*y+*x); cout << endl;

    int *p, *q = new int[10];
    delete [] q; // io ho messo delete q; delete p;
    int& a = v[1];
    int b = v[0];
    b = *y;
    a = *y;
    for(int i=0;i<6;++i) cout << v[i];
    cout << endl;
    return 0;
}
