#include "eliminaSomma.cpp"

int main()
{
    List<int> T;
    T.pushBack(1);
    T.pushBack(2);
    T.pushBack(3);
    T.pushBack(3);
    T.pushBack(1);

    Iterator<int> it(T);
    for( ;!it.isNull(); ++it)
        cout<<*it<< " ";	// 1 2 3 3 1
    cout << endl;

    it.moveAtFirst();
    eliminaSomma(T,5);  
    // 2 e 3 = 5 quindi elimina 3 che rappresenta il secondo nodo 
    // Primo passaggio risultato // 1 2 3 1
    // Fa un secondo passaggio e rimuove l'altro 3
    
    //Stampo la lista dopo l'esecuzione di eliminaSomma
    for(it.moveAtFirst(); !it.isNull(); ++it)
        cout<<*it<<" ";	// 1 2 1
    cout << endl;

    // 1 e 2 = 3 quindi elimina 2 che rappresenta il secondo nodo
    eliminaSomma(T,3);		// Elimina il 2

    //Stampo la lista dopo l'esecuzione di eliminaSomma
    for(it.moveAtFirst(); !it.isNull(); ++it)
        cout<<*it<<endl;	// 1 1

    eliminaSomma(T,2);		// Elimina il secondo 1

     for(it.moveAtFirst(); !it.isNull(); ++it)
        cout<<*it<<endl;	// 1
    
	eliminaSomma(T,1);	// non fa nulla

    for(it.moveAtFirst(); !it.isNull(); ++it)
        cout<<*it<<endl;	// 1

    return 0;
}