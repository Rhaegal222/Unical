from threading import Thread,RLock,Condition, current_thread
from random import random,randint
from time import sleep

#
# Funzione di stampa sincronizzata
#
plock = RLock()
debug = True
def dprint(s):
    if debug:
        plock.acquire()
        print(s)
        plock.release()

class PonteCondiviso():

    def __init__(self):
        self.numAuto = 0
        self.verso=0 #0=mare verso montagna,1=montagna verso mare
        self.lock = RLock()
        self.mareToMontagna = Condition(self.lock)
        self.montagnaToMare = Condition(self.lock)


    def entraMontagna(self,nome):
        self.lock.acquire()
        dprint(f"Il thread {nome} prova ad attraversare dalla montagna")
        while self.numAuto!=0 and self.verso==0:
            dprint(f"Il thread {nome} voleva attraversare ma trova occupato. Dunque aspetta.")
            self.montagnaToMare.wait()
        if(self.numAuto==0):
            self.verso=1
        self.numAuto+=1
        dprint(f"Il thread {nome} prende il lock dalla montagna verso il mare")
        self.lock.release()

    def esciMontagna(self,nome):
        self.lock.acquire()
        dprint(f"Il thread {nome} rilascia il lock dalla montagna verso il mare")
        self.numAuto -= 1
        if self.numAuto == 0:
            self.mareToMontagna.notify_all() #perchè le auto di mareToMontagna stavano dormendo
        self.lock.release()

    def entraMare(self,nome):
        self.lock.acquire()
        dprint(f"Il thread {nome} prova ad attraversare dal mare")
        while self.numAuto!=0 and self.verso==1:
            dprint(f"Il thread {nome} voleva attraversare ma trova occupato. Dunque aspetta.")
            self.mareToMontagna.wait()
        if(self.numAuto==0):
            self.verso=0 #dal mare verso la montagna
        self.numAuto+=1
        dprint(f"Il thread {nome} prende il lock dall marela verso la montagna")
        self.lock.release()

    def esciMare(self,nome):
        self.lock.acquire()
        dprint(f"Il thread {nome} rilascia il lock dalla montagna verso il mare")
        self.numAuto -= 1
        if self.numAuto == 0:
            self.montagnaToMare.notify_all()
        self.lock.release()

class Auto(Thread):

    def __init__(self, nome, ponte, verso):
        super().__init__()
        self.nome = nome
        self.ponte=ponte
        self.verso=verso
        
    def run(self):
        if self.verso==0:
            self.ponte.entraMare(self.nome)
            sleep(0.1)
            self.ponte.esciMare(self.nome)
        else:
            self.ponte.entraMontagna(self.nome)
            sleep(0.1)
            self.ponte.esciMontagna(self.nome)

ponte=PonteCondiviso()

for i in range(10):
    newAuto=Auto(f"auto{i}",ponte,randint(0,1))
    newAuto.run()
