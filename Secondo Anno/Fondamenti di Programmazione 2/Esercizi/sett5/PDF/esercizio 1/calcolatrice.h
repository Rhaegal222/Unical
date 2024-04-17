#ifndef Calcolatrice_h
#define Calcolatrice_h

template <class T>
class Calcolatrice{
    private:
        T num1, num2;
    public:
        Calcolatrice(T num1, T num2);
        //~Calcolatrice();
        const T Somma();
        const T Sottrazione();
        const T Moltiplicazione();
        const T Divisione();
};

#endif