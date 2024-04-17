#include <iostream>
#include "../ListaT.h"
#include "../Iterator.h"

using namespace std;

int main(){
    List<char> C;
    C.pushBack('a');
    C.pushBack('a');
    C.pushBack('B');
    C.pushBack('a');
    C.print();		// a a B a

    char c;
    if(C.popFront(c))
        cout<<"dopo aver rimosso "<<c<<" la lista diventa"<<endl; ;
    C.print();		// a B a

    if(C.popBack(c))
        cout<<"dopo aver rimosso "<<c<<" la lista diventa"<<endl;;
    C.print();		// a B
    
    List<char> N;
    Iterator<char> sin(N),des(N);
    sin.insert('a');
    sin.insert('v');
    sin.insert('a');
    N.print();		// a v a

    des.moveAtLast();
    cout<<"valore corrente di des: "<<des.getCurrentValue()<<endl;
    des.insert('i');
    N.print();		// a v i a
    cout<<"valore corrente di des: "<<des.getCurrentValue()<<endl; 
//des si trova sulla i
    des.remove();
    N.print();		// a v a
    cout<<"valore corrente di des: "<<des.getCurrentValue()<<endl; 
//des si trova sulla a finale
    --des;
    cout<<"valore corrente di des: "<<des.getCurrentValue()<<endl; 
//des si trova sulla v
    ++des;
    cout<<"valore corrente di des: "<<des()<<endl; 
//des si trova sulla a finale

	cout<<"verifico siano palindrome "<<endl; //N.B. la lista e’: a v a
	bool palindroma=true;
	sin.moveAtFirst();
	des.moveAtLast();
	cout<<"Situazione iniziale: "<<endl;
    	cout<<sin()<<" " <<des()<<endl; 
//sin si trova sulla prima a e des si trova sulla a finale

	while ((sin!=des)&&(palindroma))
	{
		cout<<sin()<<" "<<des()<<endl;
		if (sin.getCurrentValue()!=des.getCurrentValue())
			palindroma=false;
		else
		{ ++sin;
		  if (sin!=des) --des;
		}
	}
    
	if (palindroma)  cout<<"palindroma"<<endl;
	else cout<<"Non palindroma" <<endl;
}