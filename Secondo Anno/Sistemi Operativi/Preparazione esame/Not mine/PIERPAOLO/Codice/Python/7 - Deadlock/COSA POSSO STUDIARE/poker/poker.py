
'''
Un tavolo rotondo a cui sostano N giocatori (numerati da 0 a N-1) di poker (N>20) è corredato di 3 
posacenere che sono posizionati in origine al centro del tavolo. Ogni posacenere può essere posizionato al 
centro del tavolo oppure di fronte a un certo giocatore.
I giocatori fumano periodicamente, ma per poter svolgere questa operazione è necessario che un 
posacenere sia nelle immediate vicinanze. Un giocatore i può fumare solo se un posacenere risulta 
posizionato di fronte a sé stesso, oppure di fronte a uno dei due giocatori adiacenti. Si assume che i 
giocatori siano disposti circolarmente attorno al tavolo.
Si progetti la struttura dati Tavolo che consenta le operazioni richieste da parte di N Thread giocatori, 
garantendo che le regole di accesso ai posacenere siano rispettate, ed evitando situazioni di inconsistenza, 
deadlock e possibile starvation.



'''




import threading
from threading import Condition, RLock, Lock, Thread
from time import sleep
from random import randint

N=randint(21, 50)

NPOSACENERI=3


def adiacente(posacenere, pos):
    if(posacenere == pos or posacenere== pos+1 or posacenere == pos-1):
        return True
    elif( (posacenere == 0 and pos == N) or (posacenere == N and pos == 0)):
        return True
    return False

class Posacenere:
    # -10 = al centro
    def __init__(self, nome):
        self.name=nome
        self.lock = RLock()
        self.posizione = -10
        self.fumatori = []
        self.fumatore_wait = Condition(self.lock)



    def faiFumare(self, nome_giocatore):
        self.lock.acquire()
        if(adiacente(self.posizione, nome_giocatore) and len(self.fumatori)<3):
            self.fumatori.append(nome_giocatore)
            print(f"Fumatore {threading.current_thread().name}: fuma accanto a lui, al posacenere {self.name} al posto {self.posizione} ")
        else:
            if(len(self.fumatori)!=0):
                self.fumatore_wait.wait()
            else:
                self.posizione = nome_giocatore
                print(f"Fumatore {threading.current_thread().name}: sposta il posacenere {self.name} al posto {self.posizione} ")
    
    def smettiFumare(self, nome_giocatore):
        self.fumatori.remove(nome_giocatore)
        if(len(self.fumatori)==0):
            self.posizione = -10
        self.fumatore_wait.notify()

        

    

class Tavolo:
    def __init__(self):
        self.posaceneri = [Posacenere(i) for i in range(3)]
    
    
    def fuma(self, nome_giocatore):
        for i in range(len(self.posaceneri)):
            # se il posacenere è al centro o è adiacente
            if( self.posaceneri[i].posizione == -10   or   adiacente(self.posaceneri[i].posizione, nome_giocatore)  ):
                self.posaceneri[i].faiFumare(nome_giocatore)
                break
            

    def smettiDiFumare(self, nome_giocatore):
        for i in range(len(self.posaceneri)):
            if(nome_giocatore in self.posaceneri[i].fumatori):
                self.posaceneri[i].smettiFumare(nome_giocatore)
                break


class Giocatore(Thread):
    def __init__(self, id, tavolo):
        super().__init__()
        self.name=id
        self.tavolo=tavolo

    def run(self):
        self.tavolo.fuma(int(self.name))
        sleep(1)
        self.tavolo.smettiDiFumare(int(self.name))


    
def main():

    tavolo = Tavolo()

    giocatori = [Giocatore(i, tavolo) for i in range(N)]

    for giocatore in giocatori:
        #print(f"{giocatore.name} ha iniziato")
        giocatore.start()



    sleep(5)
    print("Finito")

main()