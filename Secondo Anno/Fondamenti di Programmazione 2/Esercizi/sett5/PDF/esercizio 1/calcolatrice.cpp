#include "calcolatrice.h"
using namespace std;

template <class T>
Calcolatrice<T> :: Calcolatrice(T n1, T n2){
    num1 = n1;
    num2 = n2;
}

template <class T>
const T Calcolatrice<T> :: Somma(){return num1 + num2;}

template <class T>
const T Calcolatrice<T> :: Sottrazione(){return num1 - num2;}

template <class T>
const T Calcolatrice<T> :: Moltiplicazione(){return num1 * num2;}

template <class T>
const T Calcolatrice<T> :: Divisione(){return num1 / num2;}