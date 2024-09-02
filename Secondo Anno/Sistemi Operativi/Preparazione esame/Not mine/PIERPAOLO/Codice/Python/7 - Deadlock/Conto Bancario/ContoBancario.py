import threading
from threading import Condition, RLock, Thread
from time import sleep  
from random import randint  
import collections


class ContoBancario:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo
        self.size = 50
        self.storicoTransazioni = collections.deque()
        self.lock = RLock()

    def aggiungiTransazione(self, transazione):
        with self.lock:
            if(len(self.storicoTransazioni) == self.size):
                self.storicoTransazioni.popleft()
            self.storicoTransazioni.append(transazione)

    def aggiornaSaldo(self, cifra):
        with self.lock:
            self.saldo += cifra

class stampante:
    def __init__(self):
        self.lock = RLock()

class Banca:
    def __init__(self):
        self.ContiBancari = collections.deque()
        self.size = 0
        self.lock = RLock()
        self.stampante=stampante()

    def aggiungiConto(self, contoBancario):
        with self.lock:
            self.size+=1
            self.ContiBancari.append(contoBancario)
            print(f"{threading.current_thread().name}: [BANCA] Conto {contoBancario.id} aggiunto: {contoBancario.saldo} euro")

    def getSaldo(self, contoBancario):
        with contoBancario.lock:
            return contoBancario.saldo

    def contoCasuale(self):
        with self.lock:
            return self.ContiBancari[randint(0,len(self.ContiBancari)-1)]

    def trasferisci(self, contoA, contoB, N):

        if not(contoA.id == contoB.id):
            if contoA.id < contoB.id:
                contoA.lock.acquire()
                contoB.lock.acquire()
            else:
                contoB.lock.acquire()
                contoA.lock.acquire()
            try: 
                if self.getSaldo(contoA) < N:
                    return False
                else:
                    tupla = (contoA, contoB, N)
                    contoA.aggiungiTransazione(tupla)
                    contoA.aggiornaSaldo(N*-1)
                    contoB.aggiungiTransazione(tupla)
                    contoB.aggiornaSaldo(N)
                    with self.stampante.lock:
                        print(f"[TRASFERIMENTO] {N} euro inviati dal conto {contoA.id} al conto {contoB.id}")
                    return True
            except:
                return False            
            finally:
                contoA.lock.release()
                contoB.lock.release()
        else:
            return False    

class Cliente(Thread):

    def __init__(self, b, id, saldo):
        super().__init__()
        self.conto = ContoBancario(id, saldo)
        self.banca = b

    def run(self):
        self.banca.aggiungiConto(self.conto)
        sleep(0.50)
        for i in range(randint(1, 10)):
            saldo = self.banca.getSaldo(self.conto)
            if saldo > 0:
                self.banca.trasferisci(self.conto, self.banca.contoCasuale(), randint(1, saldo))


banca = Banca()

for i in range(20):
    saldo = randint(10, 1000)
    newCliente = Cliente(banca, i+1, saldo)
    newCliente.start()
   
