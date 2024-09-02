from threading import Thread, Condition, Lock
import random
from time import sleep
import string
#
#   BANCONE DEL BAR
#
#   Questo codice simula il workflow tipico dell'arrivo dei clienti in un bar
#   e la loro gestione da parte del barista.
#
#   Il bancone del bar è rappresentato da un vettore di liste, dove ogni lista
#   rappresenta una "colonna" del bancone e cioè un certo numero di clienti che si accodano sulla stessa fila
#   Ogni colonna può contenere al massimo 
#   un numero di elementi pari al numero di "righe" del bancone.
#
#   I clienti che arrivano al bar vengono inseriti in una delle colonne del bancone
#   tra quelle che hanno meno elementi. Se ci sono più colonne con lo stesso
#   numero minimo di elementi, viene scelta una di queste a caso. Se il bancone è pieno,
#   la procedura di inserimento viene messa in attesa.
#
#   Il barista, quando è libero, prende un cliente a caso che trova sulla fila 0
#   e lo serve.  Se non ci sono clienti, la procedura di estrazione viene posta in attesa.
#
#   Ad esempio, lo stato del bancone in un certo momento potrebbe essere:
#
#   OOOOO
#   OO-OO
#   OO--O    
#   -O--O
# 
#  dove O indica che c'è un cliente e - indica che la posizione corrispondente è vuota. Il barista
#  serve prima i clienti sulla prima riga, scegliendo a caso tra quelli che trova.
#  
#  I clienti in arrivo preferiscono accodarsi sulle colonne che hanno meno elementi.  
#    

class BanconeBar:
    def __init__(self, righe, colonne):
        self.righe = righe # 4 - numero di righe del bancone 
        self.colonne = colonne # 5 - numero di colonne del bancone
        self.bancone = [[] for _ in range(colonne)] # [[], [], [], [], []] - lista di liste vuote
        self.lock = Lock() # lock per la mutua esclusione
        self.ceElemento = Condition(self.lock) # condition per la sincronizzazione 
        self.cePostoLibero = Condition(self.lock) # condition per la sincronizzazione 

    def __cisonoElementi(self): # metodo "privato" - restituisce True se c'è almeno un elemento sul bancone, False se è vuoto
        for c in range(self.colonne): # 5
            if len(self.bancone[c]) > 0: # se la colonna ha almeno un elemento
                return True # allora il bancone non è vuoto
        return False # altrimenti il bancone è vuoto

    def __tuttoPieno(self): # metodo "privato" - restituisce True se il bancone è pieno
        for c in range(self.colonne): # 5
            if len(self.bancone[c]) < self.righe: # se la colonna ha meno di 4 elementi
                return False # allora il bancone non è pieno
        return True # altrimenti il bancone è pieno

    def __getIndiciFilaPiuCorta(self): # metodo "privato" - restituisce una lista di indici delle colonne che hanno meno elementi
        minimo = len(self.bancone[0]) # minimo = 4
        for i in range(1, self.colonne): # 1, 5
            if len(self.bancone[i]) < minimo: # se la colonna i-esima ha meno elementi del minimo
                minimo = len(self.bancone[i]) # allora il minimo diventa il numero di elementi della colonna i-esima


        #  return [i for i in range(self.colonne) if len(self.bancone[i]) == minimo] 
        #  equivalente a | | |  
        #                v v v migliore leggibilità

        colonne_con_minimo = [] # lista vuota
        for i in range(self.colonne): # 5
            if len(self.bancone[i]) == minimo: # se la colonna i-esima ha lo stesso numero di elementi del minimo
                colonne_con_minimo.append(i) # aggiungi l'indice della colonna alla lista

        return colonne_con_minimo # restituisci la lista di indici delle colonne che hanno meno elementi

    def get(self): # estrae un elemento, casualmente, dalla prima fila del bancone (se c'è) e lo restituisce
        with self.lock: 
            while (self.__cisonoElementi() == False): # se tutte le colonne del bancone sono vuote
                self.ceElemento.wait() # metti in attesa la procedura di estrazione

            #indici_non_nulli = [i for i in range(self.colonne) if len(self.bancone[i]) > 0] 
            #  equivalente a | | |  
            #                v v v migliore leggibilità

            indici_non_nulli = [] # lista vuota
            for i in range(self.colonne): # 5
                if len(self.bancone[i]) > 0: # se la colonna i-esima ha almeno un elemento
                    indici_non_nulli.append(i) # aggiungi l'indice della colonna alla lista

            indice_scelto = random.choice(indici_non_nulli) # scegli a caso tra gli indici delle colonne che hanno almeno un elemento
            elemento = self.bancone[indice_scelto].pop(0) # estrai il primo elemento della colonna scelta a caso
            self.cePostoLibero.notify_all() # notifica a tutti che c'è un posto libero sul bancone
            return elemento

    def put(self, elemento): # inserisce un elemento sul bancone in una colonna casuale tra quelle che hanno meno elementi
        with self.lock: 
            while self.__tuttoPieno():  # se tutte le colonne del bancone sono piene
                self.cePostoLibero.wait() # metti in attesa la procedura di inserimento
                
            self.bancone[random.choice(self.__getIndiciFilaPiuCorta())].append(elemento) # inserisci l'elemento in una colonna scelta a caso tra quelle che hanno meno elementi
            self.ceElemento.notify_all() # notifica a tutti che c'è un elemento sul bancone
        
    def print_bancone(self): # metodo per stampare il bancone (viene stampato in modo "orizzontale" e riflesso rispetto alla sua rappresentazione)
        with self.lock:
            for r in range(self.righe): # 4
                for c in range(self.colonne): # 5
                    if len(self.bancone[c]) >= r+1: # se la colonna ha almeno r+1 elementi
                        toPrint = self.bancone[c][r]  # stampa l'elemento
                    else: # altrimenti 
                        toPrint = '-' # stampa un trattino

                    print(toPrint, end = '') 
                print()


class Barista(Thread):
    def __init__(self, bancone):
        super().__init__()
        self.bancone = bancone

    def run(self): # EX - prendi_elementi(bancone)
        while True:
            elemento = self.bancone.get() # estrae un elemento dal bancone
            print("Elemento prelevato:", elemento) 
            sleep(1)  # Simula un tempo di elaborazione

class Clienti(Thread):
    def __init__(self, bancone):
        super().__init__() 
        self.bancone = bancone 

    def run(self): # EX - inserisci_elementi(bancone)
        while True:
            elemento = random.choice(string.ascii_uppercase)
            self.bancone.put(elemento) # inserisce un elemento nel bancone
            print("Elemento inserito:", elemento)
            sleep(0.5)  # Simula un tempo di elaborazione

class Display(Thread):
    def __init__(self, bancone):
        super().__init__()
        self.bancone = bancone

    def run(self): # EX - stampa_bancone(bancone)
        while True:
            self.bancone.print_bancone() # stampa il bancone
            sleep(1) # Simula un tempo di elaborazione


'''
numero_righe = 4
numero_colonne = 5
bancone = BanconeBar(numero_righe, numero_colonne) # 4 righe, 5 colonne
'''

bancone = BanconeBar(4, 5) # 4 righe, 5 colonne

barista = Barista(bancone) # crea il barista
creaClienti = Clienti(bancone) # crea i clienti
display = Display(bancone) # crea il display

barista.start() # avvia il barista
creaClienti.start() # avvia i clienti
display.start() # avvia il display