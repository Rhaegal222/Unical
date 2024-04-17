import threading
from threading import Condition, RLock, Thread
from time import sleep
from random import randint


class BlockingQueue:

    def __init__(self, size):

        # lista che contiene gli elementi inseriti nella coda
        self.elementi = []

        # dimensione massima della coda
        self.size = size

        # RLock che viene utilizzato per disciplinare le invocazioni simultanee ai metodi put e get
        self.lock = RLock()

        # Condizione che viene utilizzata per notificare i thread che attendono che la coda non sia più tutta piena
        self.conditionTuttoPieno = Condition(self.lock)

        # Condizione che viene utilizzata per notificare i thread che attendono che la coda non sia più tutta vuota
        self.conditionTuttoVuoto = Condition(self.lock)

    #
    # Inserisce un elemento nella coda
    # Se la coda è piena, il thread che invoca il metodo put viene bloccato
    # Se la coda non è piena, il thread che invoca il metodo put inserisce l'elemento nella coda e notifica un thread
    # che attende che la coda non sia più tutta vuota
    #
    def put(self, t):
        with self.lock:
            #
            # Se non ci sono slot liberi, il thread che invoca il metodo put viene bloccato
            #
            while len(self.elementi) == self.size:
                self.conditionTuttoPieno.wait()
            #
            # Questo if serve per evitare notify ridondanti
            # Non ci possono essere consumatori in attesa a meno che, un attimo prima della append(t) la coda non fosse
            # totalmente vuota
            # Se non ci sono consumatori in attesa, non c'è bisogno di notificare nessuno
            # Il codice è corretto anche senza questo if, ma ci saranno notify anche quando non necessari
            #
            if len(self.elementi) == 0:
                self.conditionTuttoVuoto.notify()
            self.elementi.append(t)

    #
    # Estrae un elemento dalla coda
    # Se la coda è vuota, il thread che invoca il metodo get viene bloccato
    # Se la coda contiene almeno un elemento, il thread che invoca il metodo get estrae l'elemento dalla coda e notifica
    # un thread che attende che la coda non sia più tutta piena
    #
    def get(self, index):
        with self.lock:
            #
            # Se non ci sono elementi da estrarre, il thread che invoca il metodo get viene bloccato
            #
            while len(self.elementi) == 0:
                self.conditionTuttoVuoto.wait()
            #
            # Questo if serve per evitare notify ridondanti
            # Non ci possono essere produttori in attesa a meno che, un attimo prima della pop(zero) la coda non fosse
            # totalmente piena
            # Se non ci sono produttori in attesa, non c'è bisogno di notificare nessuno
            # Il codice è corretto anche senza questo if, ma ci saranno notify anche quando non necessari
            #
            if len(self.elementi) == self.size:
                self.conditionTuttoPieno.notify()
            return self.elementi.pop(index)


Ordini = 10
Pizze = 10


class Pizzeria:
    def __init__(self):
        self.BOrdini = BlockingQueue(Ordini)  # crea la coda degli ordini
        self.BPizze = BlockingQueue(Pizze)  # crea la coda delle pizze pronte
        self.lock = RLock()
        self.pizzaPronta = Condition(self.lock)
        self.num_ordine = 0

    def gen_id(self):
        with self.lock:
            self.num_ordine += 1
            return self.num_ordine

    def put_ordine(self, cod_pizza, quant):
        ordine = (cod_pizza, quant)  # crea l'ordine
        scontrino = self.gen_id()  # crea l'id dell'ordine
        ordine += (scontrino,)  # aggiunge all'ordine il suo id
        self.BOrdini.put(ordine)  # aggiunge l'ordine alla coda degli ordini
        return scontrino  # restituisce il codice dell'ordine al cliente che l'ha chiamato

    def get_ordine(self):
        return self.BOrdini.get(0)  # restituisce il primo ordine presente nella coda se la coda non è vuota

    def put_pizza(self, pizza):
        with self.lock:
            self.BPizze.put(pizza)  # inserisce una pizza nella coda se la coda non è piena
            self.pizzaPronta.notify_all()

    def get_pizza(self, riferimento):
        with self.lock:
            while True:
                for pizza in self.BPizze.elementi:
                    if pizza[2] == riferimento:
                        return self.BPizze.get(self.BPizze.elementi.index(pizza))
                self.pizzaPronta.wait()


gusti_pizze = ("Margherita", "Diavola", "Quattro Stagioni", "Calabrese", "Marinara", "Bufalina")


class Cliente(Thread):

    def __init__(self, p, nome):
        super().__init__()
        self.name = nome
        self.pizzeria = p
        self.quant = 0
        self.codicePizza = 0
        self.scontrino = -1

    def run(self):
        i = 6
        while i > 0:
            self.quant = randint(1, 20)
            self.codicePizza = randint(0, 5)
            self.scontrino = self.pizzeria.put_ordine(self.codicePizza, self.quant)
            with self.pizzeria.lock:
                print(f"{self.name}: ha ORDINATO {self.quant} pizze {gusti_pizze[self.codicePizza]}")

            # sleep(0.5 * self.quant)

            pizza = self.pizzeria.get_pizza(self.scontrino)
            if pizza:
                with self.pizzeria.lock:
                    print(f"{self.name}: ha RITIRATO {pizza[1]} pizze {gusti_pizze[pizza[0]]}")

            i -= 1


class Pizzaiolo(Thread):

    def __init__(self, p, nome):
        super().__init__()
        self.name = nome
        self.pizzeria = p

    def run(self):
        while threading.Thread(newCliente):
            pizza = self.pizzeria.get_ordine()
            with self.pizzeria.lock:
                print(f"{self.name}: ha PRESO IN CARICO {pizza[1]} pizze {gusti_pizze[pizza[0]]}")
            # sleep(0.5 * pizza[1])
            self.pizzeria.put_pizza(pizza)
            with self.pizzeria.lock:
                print(f"{self.name}: ha CONSEGNATO {pizza[1]} pizze {gusti_pizze[pizza[0]]}")


Da_Toto = Pizzeria()

for i in range(20):
    newCliente = Cliente(Da_Toto, f"CLIENTE {i + 1}")
    newCliente.start()

for i in range(5):
    newPizzaiolo = Pizzaiolo(Da_Toto, f"PIZZAIOLO {i + 1}")
    newPizzaiolo.start()


