//LISTE ORDINATE
#ifndef LISTAOT_H
#define LISTAOT_H

#include "../ListaT.h"
#include <cassert>
#include<iostream>
using namespace std;
template <class T>
class OrderedList:protected List<T>
{
	public:
	void insert(const T&);
	void remove(const T&v) {List<T>::remove(v);}
	bool find(const T& v) const {return List<T>::find(v);}
	void print() {List<T>::print();}
	bool empty() const {return List<T>::empty();}
};

template <class T>
void OrderedList<T>::insert (const T& v) // INSERIMENTO ORDINATO
{
    Node<T> *n = List<T>::newNode(v);
    if(List<T>::empty()) //testa ==0;
        List<T>::first = List<T>::last = n;
    else
    {
        	Node<T> * prec=NULL;
		Node<T> * corr=List<T>::first;
		while(corr!=NULL && corr->getValue()<v)
		{
			prec=corr;
			corr=corr->nextNode;
		}
		if (prec==NULL) // equivalente a push front
		{
			n->nextNode = List<T>::first;
			List<T>::first = n;
		}
		else if (corr==NULL)  // equivalente a push back
		{
			List<T>::last->nextNode = n;
			List<T>::last = n;
		}
		else
		{
			prec->nextNode=n;
			n->nextNode=corr;
		}	
    }
}
#endif