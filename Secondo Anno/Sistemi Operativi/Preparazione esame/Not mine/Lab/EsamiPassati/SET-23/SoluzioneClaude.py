from queue import Queue
import random
import time
from threading import Lock, Condition, RLock, Thread


pizze = { "margherita" : "(.)", 
          "capricciosa" : "(*)", 
          "diavola" : "(@)",
          "ananas" : "(,)"}


class Tavolo:
    def __init__(self, posti=10):
        self.posti = [None] * posti
        self.lock = Lock()

    def posti_liberi(self):
        with self.lock:
            return self.posti.count(None)

    def occupa_posto(self, pizza):
        with self.lock:
            for i, posto in enumerate(self.posti): #enumerate restituisce una tupla con indice e valore
                if posto is None:
                    self.posti[i] = (pizza, time.time())
                    return True
            return False

    def libera_posto(self, index):
        with self.lock:
            if self.posti[index] and time.time() - self.posti[index][1] >= 3:
                self.posti[index] = None
                return True
            return False

class Sala:
    def __init__(self, num_tavoli):
        self.tavoli = [Tavolo() for _ in range(num_tavoli)]

    def trova_tavolo_libero(self):
        for i, tavolo in enumerate(self.tavoli):
            if tavolo.posti_liberi() == 10:
                return i
        return None

    def deposita_pizza(self, tavolo_index, pizza):
        return self.tavoli[tavolo_index].occupa_posto(pizza)

    def rimuovi_pizza(self, tavolo_index):
        tavolo = self.tavoli[tavolo_index]
        for i in range(10):
            if tavolo.libera_posto(i):
                return True
        return False

class BlockingSet(set):

    def __init__(self, size = 10):
        super().__init__()
        self.size = size
        self.lock = RLock()
        self.condition = Condition(self.lock)

    def add(self,T):
        with self.lock:
            while len(self) == self.size:
                self.condition.wait()
            self.condition.notify_all()
            return super().add(T)

    def remove(self,T):
        with self.lock:
            while not T in self:
                self.condition.wait()
            super().remove(T)
            self.condition.notify_all()
            return 

class Ordine:
    nextCodiceOrdine = 0
    def __init__(self,tipoPizza,quantita):
        self.tipoPizza = tipoPizza
        self.quantita = quantita
        self.codiceOrdine = Ordine.nextCodiceOrdine
        self.pizzePronte = ""
        Ordine.nextCodiceOrdine += 1

    def prepara(self):
        for i in range(self.quantita):
            self.pizzePronte += pizze[self.tipoPizza]


class Pizzeria:
    def __init__(self):
        self.BO = Queue(10)
        self.BP = BlockingSet()

    def getOrdine(self):
        return self.BO.get()

    def putOrdine(self,codicePizza,quantita):
        ordine = Ordine(codicePizza,quantita)
        self.BO.put(ordine)
        return ordine
        

    def getPizze(self,ordine):
        self.BP.remove(ordine)

    def putPizze(self,ordine):
        self.BP.add(ordine)

    def getPizze(self, ordine, quantita=2):
        with self.BP.lock:
            while ordine not in self.BP:
                self.BP.condition.wait()
            pizze = ordine.pizzePronte[:quantita]
            ordine.pizzePronte = ordine.pizzePronte[quantita:]
            if not ordine.pizzePronte:
                self.BP.remove(ordine)
            self.BP.condition.notify_all()
            return pizze

class Cameriere(Thread):
    def __init__(self, name, ristorante):
        super().__init__()
        self.name = name
        self.ristorante = ristorante

    def run(self):
        while True:
            # Genera ordine casuale
            num_pizze = random.randint(1, 10)
            tipo_pizza = random.choice(list(pizze.keys()))
            tavolo = self.ristorante.sala.trova_tavolo_libero()
            
            if tavolo is not None:
                ordine = self.ristorante.pizzeria.putOrdine(tipo_pizza, num_pizze)
                print(f"Cameriere {self.name} ha ordinato {num_pizze} {tipo_pizza} per il tavolo {tavolo}")

                pizze_consegnate = 0
                while pizze_consegnate < num_pizze:
                    pizze = self.ristorante.pizzeria.getPizze(ordine, min(2, num_pizze - pizze_consegnate))
                    time.sleep(1)  # Simula il tempo di trasporto
                    for pizza in pizze:
                        self.ristorante.sala.deposita_pizza(tavolo, pizza)
                        pizze_consegnate += 1
                    print(f"Cameriere {self.name} ha consegnato {len(pizze)} pizze al tavolo {tavolo}")

            time.sleep(random.randint(1, 5))  # Pausa prima del prossimo ordine

class Sparecchiatore(Thread):
    def __init__(self, name, ristorante):
        super().__init__()
        self.name = name
        self.ristorante = ristorante

    def run(self):
        while True:
            for tavolo_index in range(len(self.ristorante.sala.tavoli)):
                if self.ristorante.sala.rimuovi_pizza(tavolo_index):
                    print(f"Sparecchiatore {self.name} ha rimosso una pizza dal tavolo {tavolo_index}")
            time.sleep(1)  # Controlla ogni secondo

class Ristorante:
    def __init__(self, num_tavoli):
        self.pizzeria = Pizzeria()
        self.sala = Sala(num_tavoli)
        
class Pizzaiolo(Thread):

    def __init__(self, name, pizzeria):
        super().__init__()
        self.name = name
        self.pizzeria = pizzeria

    def run(self):

        while True:
            ordine = self.pizzeria.getOrdine()
            tempoDiPreparazione = ordine.quantita
            time.sleep(tempoDiPreparazione)
            ordine.prepara()
            self.pizzeria.putPizze(ordine)
            #
            #  Sigaretta...
            #             
            time.sleep(random.randint(1,3))

def main():
    ristorante = Ristorante(5)  # 5 tavoli
    pizzaioli = [Pizzaiolo(f"Pizzaiolo_{i}", ristorante.pizzeria) for i in range(3)]
    camerieri = [Cameriere(f"Cameriere_{i}", ristorante) for i in range(5)]
    sparecchiatori = [Sparecchiatore(f"Sparecchiatore_{i}", ristorante) for i in range(2)]

    for thread in pizzaioli + camerieri + sparecchiatori:
        thread.start()

    for thread in pizzaioli + camerieri + sparecchiatori:
        thread.join()

if __name__ == '__main__':
    main()

