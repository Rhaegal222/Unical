#ifndef CATENADIMONTAGGIO_H
#define CATENADIMONTAGGIO_H

#include "ListaT.h"
using namespace std;

template <class T>
class CatenaDiMontaggio{
    public:

        void aggiungi(T elemento); //aggiunge un elemento alla fine della lista
        
		void rimuovi(); //rimuove il primo elemento della lista
        
		const T& prossimo() const; //restituisce il primo elemento della lista
       
	    unsigned int size() const;//restituisce il numero di elementi della lista
    
	private:
		List<T> l;
};

template <class T>
void CatenaDiMontaggio<T>::aggiungi(T elemento){
	l.push_back(elemento);
}

template <class T>
void CatenaDiMontaggio<T>::rimuovi(){
	l.pop_front();
}

template <class T>
const T& CatenaDiMontaggio<T>::prossimo() const {
    return l.front();
}

template <class T>
unsigned int CatenaDiMontaggio<T>::size() const {
    return l.size();
}


#endif