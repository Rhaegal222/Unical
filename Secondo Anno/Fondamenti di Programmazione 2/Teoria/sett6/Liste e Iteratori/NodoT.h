// NodoT.h: interface for the NodoT class.

#ifndef NODOT_H
#define NODOT_H

template <class T>
class List;
//DOPO:
template <class T>
class OrderedList;
//DOPO:
template <class T>
class Iterator;

template< class T >
class Node
{
    friend class List<T>;
	//DOPO:
    friend class OrderedList<T>;
    //DOPO:
    friend class Iterator<T>;

    public:
        Node(const T &v): nextNode(0),value(v) {}
        T getValue() const {return value;}
        Node<T>* getNextNode() const {return nextNode;}

    private:
        Node<T>* nextNode;
        T value;
};

#endif