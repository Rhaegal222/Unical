from threading import * 

'''
Starvation: Quando un thread attende indefinitamente per accedere ad una risorsa, ma non può accedervi perchè un altro thread la sta utilizzando.

Deadlock: Quando due o più thread attendono indefinitamente per accedere ad una risorsa, ma non possono accedervi perchè si bloccano a vicenda.

Questo esercizio è un esempio di come utilizzare i lock per evitare la starvation.
In questo caso abbiamo un array di sedie, e un array di partecipanti. Ogni partecipante deve sedersi su una sedia, ma solo una persona può sedersi su una sedia alla volta.
Per evitare la starvation, bisogna lockare la sedia prima di controllare se è occupata o meno, così da evitare che un altro thread possa occuparla prima che il thread corrente lo faccia.
'''

class Sedia():
    def __init__(self):
        self.lock = Lock()  # Il lock bisogna dichiararlo SEMPRE nella risorsa a cui dobbiamo accedere
        self.occupata = False

class Persona(Thread):  # La classe che dovrà essere il thread sarà quella che dovrà effettuare l'accesso alla risorsa (ovvero le sedie)
    def __init__(self,id,sedie):
        super().__init__()
        self.id = id
        self.sedie = sedie

    def run(self):
        for i in range(len(self.sedie)):
            seduto = False
            self.sedie[i].lock.acquire()    # Bisogna lockare la risorsa prima che venghi realmente occupata, così dopo possiamo controllare se è occupata o meno
            if not self.sedie[i].occupata:  # Serve per evitare la starvation (quando più thread aspettano la stessa risorsa a vuoto)            
                self.sedie[i].occupata = True
                print(f"Sono il thread {self.id}, e sono sulla sedia {i}")
                seduto = True
                self.sedie[i].lock.release()    # Bisogna SEMPRE rilasciare la risorsa dopo averla utilizzata, altrimenti si va in deadlock perchè risulterà sempre occupata
                break
            self.sedie[i].lock.release()
            if seduto: break

        if not seduto:
            print(f"Sono il thread {self.id} e ho perso")

nsedie = 10
lista_sedie = [Sedia() for i in range(nsedie)]
lista_partecipanti = [Persona(i, lista_sedie) for i in range(nsedie + 1)]

for i in range(nsedie + 1):
    lista_partecipanti[i].start() 

'''
Differenza tra il metodo start() e run():

start(): Crea un nuovo thread e chiama il metodo run() del thread. Il metodo run() è il metodo che contiene il codice che il thread deve eseguire.

run(): Esegue il codice del thread. Se chiamiamo il metodo run() direttamente, il codice verrà eseguito nel thread corrente, e non verrà creato un nuovo thread.
'''
