
from queue import Queue
from random import randint
from threading import Condition, RLock, Thread, current_thread
import time

pizze = { "margherita" : "(.)", #dizionario
          "capricciosa" : "(*)", 
          "diavola" : "(@)",
          "ananas" : "(,)"}



class Ordine:
    nextCodiceOrdine = 0 #variabile statica (comune a tutte le istanze della classe, è propria della classe)
    def __init__(self,tipoPizza,quantita):
        self.tipoPizza = tipoPizza
        self.quantita = quantita
        self.codiceOrdine = Ordine.nextCodiceOrdine #prende il codice dalla classe
        self.pizzePronte = "" #stringa risultato
        Ordine.nextCodiceOrdine += 1

    def prepara(self):
        for i in range(self.quantita):
            self.pizzePronte += pizze[self.tipoPizza] #aggiunge le pizze ordinate al risultato

class BlockingSet(set):# set è una struttura dati di elementi non ordinati e unici in cui è molto efficiente la ricerca (hash set)

    def __init__(self, size = 10):
        super().__init__()
        self.size = size
        self.lock = RLock()
        self.condition = Condition(self.lock)

    def add(self,T):
        with self.lock:
            while len(self) == self.size: #se è piena la coda di pizze aspetta, len(self) è la lunghezza del set
                self.condition.wait()
            self.condition.notify_all() #quando si libera un posto dal set e si può aggiungere risveglia tutti
            return super().add(T) #restisce il set con il nuovo elemento appena inserito

    def remove(self,T):
        with self.lock:
            while not T in self: #se l'elemento da rimuovere non c'è, aspetta che venga inserito
                self.condition.wait()
            super().remove(T) #toglie T appena viene messo nel set e notifica tutti i thread perchè si è liberato un posto
            self.condition.notify_all()
            return True

class Pizzeria:
    
    def __init__(self):
        self.BO = Queue(10) #coda di 10 elementi per gli ordini FIFO
        self.BP = BlockingSet() #buffer pizze NON per forza FIFO

    def getOrdine(self):
        return self.BO.get() #prende il primo elemento

    def putOrdine(self,codicePizza,quantita):
        ordine = Ordine(codicePizza,quantita) #crea un oggetto di tipo ordine e lo mette nel buffer degli ordini, lo restituisce
        self.BO.put(ordine)
        return ordine
        

    def getPizze(self,ordine):
        self.BP.remove(ordine) #prende le pizze (ordine) quando è pronta da Bp

    def putPizze(self,ordine):
        self.BP.add(ordine)

class Pizzaiolo(Thread):

    def __init__(self, name, pizzeria):
        super().__init__()
        self.name = name
        self.pizzeria = pizzeria

    def run(self):


        while True:
            ordine = self.pizzeria.getOrdine() #prende l'ordine e lo elabora in base a quante pizze sono (varia il tempo)
            print(f"[{self.name}] Ricevuto ordine: {ordine.codiceOrdine}")
            tempoDiPreparazione = ordine.quantita
            print(f"[{self.name}] Tempo di preparazione: {tempoDiPreparazione}")
            time.sleep(tempoDiPreparazione)
            ordine.prepara()                             #mette le pizze nella stringa risultato 
            print(f"[{self.name}] Ordine {ordine.codiceOrdine} preparato")
            self.pizzeria.putPizze(ordine)               #aggiunge le pizze pronte al BP
            print(f"[{self.name}] {ordine.codiceOrdine} Pizze '{ordine.tipoPizza}' consegnate")
            #
            #  Sigaretta...
            #             
            time.sleep(randint(1,3))
            print(f"[{self.name}] Finita la pausa")

class Cliente(Thread):
    def __init__(self, name, pizzeria):
        super().__init__()
        self.name = name
        self.pizzeria = pizzeria

    def run(self):
        while True:
                numeroPizze = 1 + randint(0,7)
                tipiPizza = list(pizze.keys())
                codicePizza = tipiPizza[randint(0,len(tipiPizza)-1)]

                print(f"Il cliente {self.name} entra in pizzeria e prova ad ordinare delle pizze")
                ordine = self.pizzeria.putOrdine(codicePizza, numeroPizze)
                print(f"Il cliente {self.name} aspetta le pizze con codice d'ordine numero {ordine.codiceOrdine}")

                time.sleep(randint(0, numeroPizze))

                self.pizzeria.getPizze(ordine)

                print(f"Il cliente {self.name} ha preso le pizze con codice d'ordine numero {ordine.codiceOrdine}")
                print(f"[{self.name}] mangia {ordine.pizzePronte}")
                #
                # Prima o poi mi tornerÃ  fame
                #
                time.sleep(randint(0, numeroPizze))


def main():
    NUMP = 3
    NUMC = 20
    p = []
    c = []
    pizzeria = Pizzeria()

    for i in range(0, NUMP):
        pizzaiolo = Pizzaiolo("Totonno_" + str(i), pizzeria)
        p.append(pizzaiolo)
        pizzaiolo.start()

    for i in range(0, NUMC):
        cliente = Cliente("Ciro_" + str(i), pizzeria)
        c.append(cliente)
        cliente.start()

if __name__ == '__main__':
    main()
