// ListaT.h: interface for the ListaT class.

#ifndef LISTAT_H
#define LISTAT_H

#include "NodoT.h"
#include <cassert>
#include<iostream>
using namespace std;

template< class T >
class List
{
//DOPO
friend class Iterator<T>;

public :
	List() :first(0),last(0) {}
	~List();
	void pushFront(const T&);
	void pushBack(const T&);
	bool popFront(T& v);
	bool popBack(T& v);
	bool empty() const {return (first==0);}
	void print() const;
	bool find(const T&) const;
    void delNode(Node<T>* &);
    void remove(const T&v);
    Node<T> * front();

protected:  	//SERVE PER FAR ACCEDERE AD EVENTUALI CLASSI DERIVATE
	Node<T> * first; //puntatore al primo nodo
	Node<T> * last;  // puntatore all'ultimo nodo
      Node<T> * newNode(const T&);
     //Funzione di utilità che crea un nuovo nodo
};

template< class T >
List<T>::~List()
{
	if(first == 0) return; //alternativamente invocare empty()
	Node<T> *curr=first;
	Node<T> * tmp;
	while(curr != 0)
	{
		tmp = curr;
		curr = curr->nextNode;
		delete tmp;
	}
}

template< class T >
void List<T>::pushFront(const T& v)
{
    Node<T> *n = newNode(v);
    if(empty()) //testa ==0;
        first = last = n;

    else
    {
        n->nextNode = first;
        first = n;
    }
}

template< class T >
Node<T> *List<T>::newNode(const T &v)
{
    Node<T> *ptr = new Node<T>(v);
    assert(ptr!=0);
    return ptr;
}

template< class T >
void List<T>::pushBack(const T& v)
{
    Node<T> *n = newNode(v);
    if(empty()) //testa ==0;
        first = last = n;

    else
    {
    	last->nextNode = n;
    	last = n;
    }
}

template< class T >
bool List<T>::popFront(T &v)
{
	if( empty())
        return false;
    Node<T>* tmp = first;
	if (last == first)
		first = last = 0;
    else
        first = first->nextNode;
	v = tmp->value;
	delete tmp;
    return true;
}

template< class T >
bool List<T>::popBack(T &v)
{
    if(empty()) //testa ==0;
        return false;
    Node<T>* tmp = last;

	if(first == last)
		first = last = 0;
    else
    {
    Node<T> * curr = first;
    while(curr->nextNode != last )
        curr=curr->nextNode;
    last = curr;
    last->nextNode=0;
    }
	v = tmp->value;
	delete tmp;
    return true;
}


template< class T >
void List<T>::print() const
{
   if( empty())
   {
       cout<<"empty";
       return;
   }
   cout<<"Lista "<<endl;
   Node<T> * ptr = first;
   while(ptr!=0)
   {
       cout<<ptr->value<<" ";
       ptr=ptr->nextNode;
   }
   cout<<endl;
}

template< class T>
bool List<T>::find(const T& v) const
{
    Node<T> * ptr = first;
    while(ptr!=0)
    {
        if(ptr->value == v)
            return true;
        ptr=ptr->nextNode;
    }
    return false;
}

template <class T>
void List<T>::delNode(Node<T>* & pos) 
//N.B. dopo la cancellazione pos punta al nodo successivo a quello cancellato
{
      assert(first!=0);
	assert(pos!=0);
	
	if (pos==first) 
	{
		first=pos->nextNode;
		delete pos;
		pos=first;
	}
	else{

		Node<T> * prec=first;
		while(prec->nextNode!=pos) prec=prec->nextNode;
		Node<T> *tmp = pos;
		prec->nextNode = pos->nextNode;
		if (pos==last) last = prec;
		delete pos;
		pos=prec;
	}
}

template <class T>
void List<T>::remove(const T&v)
{
    if(empty()) return;
    bool found=false;
	Node<int> * n;
	
	for (n=front(); n!=NULL && !found; n=n->getNextNode())
		if (n->getValue()==v) 
		{
			found=true;
			delNode(n); 
		}
	
}

template <class T>
Node<T>* List<T>::front()
{
	return first;
}
#endif