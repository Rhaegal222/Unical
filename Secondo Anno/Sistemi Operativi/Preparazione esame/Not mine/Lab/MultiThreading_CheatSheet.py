


######################################## Cos'è una Race Condition? ########################################

'''
    Una Race Condition è si verifica quando due o più processi o thread accedono a risorse condivise in modo 
    concorrente e l'output finale dipende dall'ordine in cui vengono eseguite le operazioni.

    Un esempio classico di Race Condition è la "lettura-scrittura" concorrente. 
    Se un thread sta leggendo il valore di una variabile mentre un altro thread la sta modificando, 
    il valore letto potrebbe non corrispondere al valore attuale a causa dell'interferenza tra i thread. 

    Per evitare le Race Condition, è necessario utilizzare meccanismi di sincronizzazione come semafori, mutex o lock, 
    per controllare l'accesso concorrente alle risorse condivise e garantire un'interazione corretta tra i processi o i thread.

'''

import threading

# Variabile condivisa
counter = 0

# Funzione eseguita dai thread
def increment():
    global counter
    for _ in range(1000000):
        counter += 1

# Creazione dei due thread
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Avvio dei thread
thread1.start()
thread2.start()

# Attendi la terminazione dei thread
thread1.join()
thread2.join()

# Stampa del risultato finale
print("Il valore finale del contatore è:", counter)

'''
    In questo esempio, i due thread eseguono la funzione increment, 
    che incrementa la variabile counter per un milione di volte ciascuno. 
    L'obiettivo è ottenere un valore finale di counter pari a 2000000

    Tuttavia, a causa della Race Condition, l'output potrebbe variare. 
    Se entrambi i thread accedono contemporaneamente alla variabile counter per modificarla,
    ad esempio, il valore finale potrebbe essere inferiore a 2000000.

    Per risolvere questa Race Condition, è necessario sincronizzare correttamente l'accesso alla variabile counter 
    utilizzando un meccanismo di lock o un altro meccanismo di sincronizzazione appropriato per garantire l'accesso esclusivo alla risorsa condivisa.

'''



######################################## Cos'è il Deadlock? ########################################

'''
    Il Deadlock è una situazione indesiderata che si verifica in un sistema a più processi 
    quando ogni processo è in attesa di una risorsa che è attualmente detenuta da un altro processo del sistema. 

    Il Deadlock può verificarsi quando quattro condizioni necessarie si verificano contemporaneamente:

    - Mutua esclusione: Almeno una risorsa deve essere in uno stato di mutua esclusione, il che significa che solo un processo alla volta può accedere alla risorsa.
    - Possesso e attesa: Un processo detiene almeno una risorsa mentre attende di acquisire altre risorse che sono attualmente detenute da altri processi.
    - Non prelazione: Le risorse non possono essere prelevate forzatamente dai processi che le detengono; solo il processo che detiene la risorsa può rilasciarla volontariamente.
    - Attesa circolare: Una catena circolare di processi, in cui ogni processo nella catena attende una risorsa detenuta dal successivo processo nella catena.

    Un classico esempio di Deadlock è chiamato "il problema dei Filosofi a cena". 
   
'''

import threading, time

# Classe filosofo
class Filosofo(threading.Thread):
    def __init__(self, nome, forchetta_sinistra, forchetta_destra):
        threading.Thread.__init__(self)
        self.nome = nome
        self.forchetta_sinistra = forchetta_sinistra
        self.forchetta_destra = forchetta_destra

    def run(self):
        while True:
            self.pensare()
            self.mangiare()

    def pensare(self):
        print(f"{self.nome} sta pensando.")

    def mangiare(self):
        print(f"{self.nome} vuole mangiare.")

        # Acquisizione della forchetta sinistra
        self.forchetta_sinistra.acquire()
        print(f"{self.nome} ha la forchetta sinistra.")

        # Aggiungere un ritardo artificiale per simulare il Deadlock
        time.sleep(1)

        # Acquisizione della forchetta destra
        self.forchetta_destra.acquire()
        print(f"{self.nome} ha la forchetta destra e sta mangiando.")

        # Rilascio delle forchette
        self.forchetta_sinistra.release()
        self.forchetta_destra.release()
        print(f"{self.nome} ha finito di mangiare.")

# Creazione delle forchette
forchetta1 = threading.Lock()
forchetta2 = threading.Lock()
forchetta3 = threading.Lock()
forchetta4 = threading.Lock()
forchetta5 = threading.Lock()

# Creazione dei Filosofi
filosofo1 = Filosofo("Filosofo 1", forchetta1, forchetta2)
filosofo2 = Filosofo("Filosofo 2", forchetta2, forchetta3)
filosofo3 = Filosofo("Filosofo 3", forchetta3, forchetta4)
filosofo4 = Filosofo("Filosofo 4", forchetta4, forchetta5)
filosofo5 = Filosofo("Filosofo 5", forchetta5, forchetta1)

# Avvio dei Filosofi
filosofo1.start()
filosofo2.start()
filosofo3.start()
filosofo4.start()
filosofo5.start()

# aspetta che i Filosofi finiscano
filosofo1.join()
filosofo2.join()
filosofo3.join()
filosofo4.join()
filosofo5.join()


'''
    In questo problema, ci sono cinque Filosofi che condividono una tavola con cinque posate 
    (ad esempio, cinque forchette) disposte tra di loro. 
    Ogni filosofo alterna tra il pensare e il mangiare. 
    Tuttavia, ogni filosofo ha bisogno delle due posate (forchette) 
    che si trovano ai suoi lati per poter mangiare.

    Immagina che ogni filosofo afferrasse la forchetta a destra 
    e poi attendesse di afferrare quella a sinistra per iniziare a mangiare. 
    Se tutti i Filosofi prendono contemporaneamente la forchetta a destra, 
    nessuno di loro potrà prendere la forchetta a sinistra, causando un Deadlock. 
    Ogni filosofo aspetta che l'altra forchetta sia rilasciata, 
    ma nessuno la rilascia mai, creando un blocco del sistema.

'''



######################################## Cos'è la Starvation? ########################################   

'''
    La Starvation è una condizione indesiderata che si verifica quando 
    un processo o un thread viene continuamente posto in una situazione di attesa prolungata, 
    impedendogli di avanzare o completare il suo lavoro.

    La Starvation può essere causata da diversi fattori, tra cui:

    - Priorità: Se un processo o un thread ha una bassa priorità rispetto 
                ad altre entità concorrenti, potrebbe essere costantemente posticipato 
                o assegnato una quantità limitata di risorse rispetto agli altri. 

    - Concorrenza:  Se diverse entità concorrenti richiedono 
                    risorse limitate nello stesso momento, potrebbe verificarsi una situazione in cui 
                    alcune entità ottengono accesso alle risorse in modo più frequente o più rapido, 
                    mentre altre rimangono in attesa per un periodo prolungato.

    - Deadlock: Un Deadlock può portare alla Starvation di uno o più processi o thread. 
                Se un insieme di entità concorrenti si blocca in una situazione di attesa reciproca, 
                nessuna di esse può procedere, causando una condizione di Deadlock. 

'''


import threading

# Classe Worker
class Worker(threading.Thread):
    def __init__(self, nome, risorsa):
        threading.Thread.__init__(self)
        self.nome = nome
        self.risorsa = risorsa

    def run(self):
        while True:
            self.usa_risorsa()

    def usa_risorsa(self):
        # Acquisizione della risorsa
        self.risorsa.acquire()
        print(f"{self.nome} ha acquisito la risorsa.")

        # Simulazione di un ritardo nell'uso della risorsa
        import time
        time.sleep(1)

        # Rilascio della risorsa
        self.risorsa.release()
        print(f"{self.nome} ha rilasciato la risorsa.")

# Creazione della risorsa condivisa
risorsa_condivisa = threading.Lock() 

# Creazione dei worker
worker1 = Worker("Worker 1", risorsa_condivisa)
worker2 = Worker("Worker 2", risorsa_condivisa)
worker3 = Worker("Worker 3", risorsa_condivisa)

# Impostazione delle priorità dei worker
worker1.daemon = True
worker2.daemon = True
worker3.daemon = True

# Avvio dei thread
worker1.start()
worker2.start()
worker3.start()

# Attendi la terminazione dei thread
worker1.join()
worker2.join()
worker3.join()

# Attende un po' di tempo per osservare la Starvation
import time
time.sleep(5)



'''
    In questo esempio, abbiamo tre worker che competono per una risorsa condivisa 
    rappresentata da un oggetto di tipo threading.Lock(). 
    Ogni worker cerca di acquisire la risorsa utilizzando il metodo acquire(), 
    esegue un'operazione (simulata da un ritardo) e quindi rilascia la risorsa utilizzando il metodo release().

    Tuttavia, abbiamo impostato i worker come demoni (worker.daemon = True), 
    il che significa che se il thread principale termina, i worker termineranno automaticamente.
    In questo esempio, il thread principale termina dopo 5 secondi usando time.sleep(5).

    Ciò crea una situazione di Starvation in cui i worker non hanno abbastanza tempo per utilizzare la risorsa. 
    Poiché il thread principale termina dopo solo 5 secondi, 
    i worker vengono interrotti prima che possano completare il loro lavoro in modo equo. 
    Pertanto, alcuni worker potrebbero non essere in grado 
    di acquisire mai la risorsa o potrebbero ottenerla solo occasionalmente, 
    creando una situazione di inedia (Starvation).

'''



######################################## Cos'è il Nested Lockout? ########################################

'''
    Il Nested Lockout si verifica quando un thread o un processo acquisisce un lock (blocco) 
    su una risorsa e successivamente tenta di acquisire nuovamente 
    lo stesso lock sulla stessa risorsa senza rilasciarlo prima. 
    Questo porta a una situazione in cui il thread si blocca su se stesso, 
    impedendo l'avanzamento e creando un Deadlock interno.


'''

import threading

lock = threading.Lock()

def funzione1():
    lock.acquire()
    # Esegui operazioni crittiche
    funzione2()
    lock.release()

def funzione2():
    lock.acquire()
    # Esegui altre operazioni crittiche
    lock.release()

thread1 = threading.Thread(target=funzione1)
thread2 = threading.Thread(target=funzione2)

# Avvio dei thread
thread1.start()
thread2.start()

# Attendi la terminazione dei thread
thread1.join()
thread2.join()

'''
    Una possibile soluzione consiste nell'utilizzare il metodo RLock (reentrant lock) 
    fornito dal modulo threading di Python. 
    A differenza di Lock, RLock consente a un thread di acquisire ripetutamente 
    lo stesso lock senza causare un Deadlock interno. 
    È possibile acquisire un RLock più volte, 
    ma è necessario rilasciarlo lo stesso numero di volte.

'''



######################################## Cos'è il Livelock? ########################################

'''
    Il Livelock si verifica quando due o più thread sono attivi e rispondono tra loro, 
    ma rimangono bloccati in uno stato di attesa perpetua senza fare progressi effettivi. 
    In altre parole, i thread sono attivi e operativi, 
    ma non riescono a completare il loro lavoro a causa di una sequenza di azioni reciproche.

'''

from time import sleep
from threading import Thread
from threading import Lock
 
def task(number, lock1, lock2):
    # Cicla fino a quando Task non è stato completato
    while True:
        # Acquisisci il primo lock
        with lock1:
            # Aspetta un po'
            sleep(0.1)
            # Controlla se il secondo lock è disponibile
            if lock2.locked():
                print(f'Task {number} non può acquisire il secondo lock, lascia stare...')
            else:
                # Acquisisci il secondo lock
                with lock2:
                    print(f'Task {number} ha finito, tutto completato.')
                    break
 
# Crea i lock
lock1 = Lock()
lock2 = Lock()
# Crea i thread
thread1 = Thread(target=task, args=(0, lock1, lock2))
thread2 = Thread(target=task, args=(1, lock2, lock1))

# Avvio dei thread
thread1.start()
thread2.start()

# Attendi la terminazione dei thread
thread1.join()
thread2.join()

'''
Per evitare il Livelock, è necessario modificare la logica di controllo delle persone 
in modo che si raggiunga un accordo o una strategia condivisa per gestire le risorse. 
Il tutto può essere risolto con un'opportuna aggiunta di Lock, Condition o Semafori.

'''
######################################## DIZIONARI IN PYTHON ########################################


mio_dict = {"mia_chiave": "mio_valore", "age": 29, 3.14: "pi greco", "primi": [2, 3, 5, 7]}

print(mio_dict["mia_chiave"])

# output: mio_valore

######################################## FINE ########################################