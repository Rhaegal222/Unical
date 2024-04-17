# Ordered list

senza riscrivere tutto quanto, possiamo scrivere una classe `OrderedList` andando a derivare dalla classe `List`

deriviamo da List con il modificatore protected, perchè non vogliamo che siano accessibili tutti i metodi di List, anzi vogliamo cambiare il funzionamento di alcuni

## [Implementazione](../../Implementazioni/OrderedList/OrderedList.h)

## Esempio

```cpp
template <class T>
class OrderedList : protected list<T> {
   public:
    void insert(const T& v);
    void remove(const T& v) { list<T>::remove(v); }
    bool find(const T& v) const { return list<T>::find(v); }
    bool empty() const { return list<T>::empty(); }

    template <class U>
    friend ostream& operator<<(ostream& o, const OrderedList<U>& ol);
};
```

```cpp
template <class T>
void OrderedList<T>::insert(const T& v) {
    if (empty()) {
        // cout << v << " was added as the first element of the list\n";
        list<T>::push_front(v);
        return;
    }
    for (auto it = list<T>::begin(); it != list<T>::end(); it++) {
        if (v < *it) {
            // cout << v << " was added to the list before " << *it << "\n";
            list<T>::insert(it, v);
            return;
        }
    }
    // se non c'è nessun valore più grande di esso
    // cout << v << " was added to the end of the list\n";
    list<T>::push_back(v);
}

template <class U>
ostream& operator<<(ostream& o, const OrderedList<U>& ol) {
    std::cout << "{ ";
    for (int n : ol) {
        std::cout << n << ", ";
    }
    std::cout << "};\n";
    return o;
}
```
