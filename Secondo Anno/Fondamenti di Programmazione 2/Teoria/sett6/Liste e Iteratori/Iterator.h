/*
ITERATORI SU LISTE

In questa sezione introduciamo il concetto di iteratore sulle liste, che consente di manipolare le liste in modo più semplice. 

Per poter introdurre gli iteratori, sia la classe Node, sia la classe List devono dichiarare la classe

Iterator come friend, per concederle l’accesso ai propri elementi privati.
*/

#ifndef ITERATOR2_H_INCLUDED
#define ITERATOR2_H_INCLUDED

#include "ListaT.h"
#include <iostream>
using namespace std;
#include <cassert>

template< class T >
class Iterator{
public:
	Iterator(List<T> &);
	T getCurrentValue() const;
	void setCurrentValue(const T&);
	T operator()();		//Equivalente a getCurrentValue 

	T operator*();		//Equivalente a getCurrentValue
    bool isNull();
    bool operator!(); //	Opposto di isNull();
    void operator++(); //	Equivalente a  moveNext();

    void operator--(); // 	Equivalente a moveBack();

	void moveAtFirst();
	void moveAtLast();
	//inserisce al posto dell'elemento corrente (tra prec e corr)
	void insert(const T& val);
	//remuove il nodo nella posizione corrente
	void remove();

    Node<T>* begin(){return l.first;}

bool operator== (const Iterator &);
bool operator!= (const Iterator &);

private:
	Node<T> * corr;
	Node<T> * prec;
	List<T>& l;
};

template< class T >
Iterator<T>::Iterator(List<T> & lista):l(lista),corr(lista.first),prec(0)
{}

template< class T >
T Iterator<T>::getCurrentValue() const
{
	assert(corr != NULL);
	return corr->value;
}

template< class T >
T Iterator<T>::operator()()
{
    	assert(corr != NULL);
return corr->value;
}

template< class T >
T Iterator<T>::operator*()
{
    	assert(corr != NULL);
	return corr->value;
}

template< class T >
void Iterator<T>::setCurrentValue(const T& val)
{
	assert(corr != NULL);
	corr->value = val;
}


template< class T >
bool Iterator<T>::isNull()
{
	return (corr == NULL);
}
template< class T >
bool Iterator<T>::operator!()
{
    return (corr != NULL); //restituisce vero se corr esiste;
}


template< class T >
void Iterator<T>::moveAtFirst()
{
	corr = l.first;
	prec = NULL;
}

template< class T >
void Iterator<T>::moveAtLast()
{
	corr = l.first;
	prec = NULL;
	while (corr != l.last)
	{
		prec = corr;
		corr = corr->nextNode;
	}
}

template< class T >
void Iterator<T>::operator++()
{
	assert(corr != NULL);
	prec = corr;
	corr = corr->nextNode;
}

template< class T >
void Iterator<T>::operator--()
{
assert(corr != NULL);
	if (corr == l.first)
	{	corr = NULL;
		prec = NULL;
	}
	else
	{

		Node<T> * tmp = corr;
		corr = l.first;
		prec = NULL;
		while (corr->nextNode != tmp)
		{
			prec = corr;
			corr = corr->nextNode;
        }
	}
}

template< class T >
void Iterator<T>::insert(const T& val)
{
	if (corr == l.first)
	{
		l.pushFront(val);
		corr = l.first;
		prec = NULL;
	}
	else if (prec == l.last)
	{
		l.pushBack(val);
		corr = l.last;
		//prec rimane su quello a cui puntava last prima della  modifica
	}
	else
	{
		Node<T> * N= l.newNode(val);
		N->nextNode = corr;
		prec->nextNode= N;
		corr = N;
	}
}

template<class T>
void Iterator<T>::remove()
{
	assert(corr != NULL);
	if (corr == l.first)
	{
	    T v;
		l.popFront(v);
		corr = l.first;
		prec = NULL;
	}
	else if (corr == l.last)
	{
        	T v;
		l.popBack(v);
		prec = l.last;
		corr = NULL;
	}
	else
	{
		prec->nextNode=corr->nextNode;
		delete corr;
		corr = prec->nextNode;
	}
}

template< class T >
bool Iterator<T>::operator==(const Iterator &i)
{
	return ((&l == &i.l) && (prec == i.prec) && (corr == i.corr));
}

template< class T >
bool Iterator<T>::operator!=(const Iterator &i){
	return ((&l != & i.l) || (prec != i.prec) || (corr != i.corr));
}

#endif // ITERATOR2_H_INCLUDED