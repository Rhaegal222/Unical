#ifndef LIST_H
#define LIST_H

template <class T>
class List {

    public:
        List();
        void push_back(T value); //Inserisce value alla fine della lista
        void pop_back(); //Rimuove l'ultimo elemento
        T& back(); //Restituisce un riferimento all'ultimo elemento
        const T& back() const; //Restituisce un riferimento costante all'ultimo elemento
        void push_front(T value); //Inserisce un elemento all'inizio della lista
        void pop_front(); //Rimuove il primo elemento
        T& front(); //Restituisce un riferimento al primo elemento
        const T& front() const; //Restituisce un riferimento costante al primo elemento
        bool empty() const; //Controlla se la lista è vuota
        void clear(); //Svuota la lista
        unsigned size() const; //Restituisce il numero di elementi nella lista

        ~List(); //distruttore
        List(const List<T>& l);
        List<T>& operator=(const List<T>& l);
    
    private:
        struct Node {
            Node* previous;
            Node* next;
            T value;
        };
        
        Node* head;
        Node* tail;
};

template <class T>
List<T>::List() {
    head = nullptr;
    tail = nullptr;
}

template <class T>
void List<T>::push_back(T value) {
    Node* node = new Node();
    node->previous = tail;
    node->next = nullptr;
    node->value = value;
    if(tail != nullptr) {
        tail->next = node;
        tail = node;
    }
    else {
        head = node;
        tail = node;
    }
}

template <class T>
void List<T>::pop_back() {
    if(head == tail) {
        delete tail;
        head = nullptr;
        tail = nullptr;
    }
    else {
        Node* tmp = tail->previous;
        tmp->next = nullptr;
        delete tail;
        tail = tmp;
    }
}

template <class T>
T& List<T>::back() {
    return tail->value;
}

template <class T>
const T& List<T>::back() const {
    return tail->value;
}

template <class T>
void List<T>::push_front(T value) {
    Node* node = new Node();
    node->previous = nullptr;
    node->next = head;
    node->value = value;
    if(head != nullptr) {
        head->previous = node;
        head = node;
    }
    else {
        head = node;
        tail = node;    
    }
}

template <class T>
void List<T>::pop_front() {
    if(head == tail) {
        delete head;
        head = nullptr;
        tail = nullptr;
    }
    else {
        Node* tmp = head->next;
        tmp->previous = nullptr;
        delete head;
        head = tmp;
    }
}

template <class T>
T& List<T>::front() {
    return head->value;
}

template <class T>
const T& List<T>::front() const {
    return head->value;
}

template <class T>
bool List<T>::empty() const {
    return head == nullptr; //return tail == nullptr;
}

template <class T>        
void List<T>::clear() {
    while(!empty())
        pop_back();
}

template <class T>
unsigned List<T>::size() const {
    unsigned int sz = 0;
    Node* current = head;
    while(current != nullptr) {
        sz++;
        current = current->next;
    }
    return sz;
}

template <class T>
List<T>::~List() {
    clear();
}

template <class T>
List<T>::List(const List<T>& l) {
    Node* current = l.head;
    while(current != nullptr) {
        push_back(current->value);
        current = current->next;
    }
}

template <class T>
List<T>& List<T>::operator=(const List<T>& l) {
    if(this != &l) {
        clear();
        Node* current = l.head;
        while(current != nullptr) {
            push_back(current->value);
            current = current->next;
        }
    }
    return *this;
}

#endif