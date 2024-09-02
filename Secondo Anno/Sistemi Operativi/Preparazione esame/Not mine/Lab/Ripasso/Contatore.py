"""
Si vogliono sincronizzare dei threads di tipo "Utilizzatore" sull'utilizzo di una struttura dati condivisa di tipo "Contatore".

In particolare, si deve definire:

-una classe Contatore che fornisce i metodi necessari per gestire un contatore. Le operazioni possibili sono reset() (imposta il
contatore a zero), inc() (aumenta il contatore di 1) e dec() (decrementa il contatore di 1). I metodi pubblici del Contatore 
devono essere Thread-Safe. 

-un tipo di thread Utilizzatore, che ad intervalli casuali modifica il valore del contatore usando i metodi di quest'ultimo

-Arricchire la classe "Contatore" di un metodo attendi(n) che rimane in attesa che il contatore raggiunga il valore "n" ricevuto 
come parametro. 

-Modificare "Utilizzatore" in modo da fargli usare solo i metodi inc() e dec().

-Definire un nuovo tipo di thread, "Azzeratore", che, scelto casualmente un valore n!=0, aspetti che il contatore raggiunga 
il valore n per poi impostarlo a zero.
"""
import threading
from random import randint