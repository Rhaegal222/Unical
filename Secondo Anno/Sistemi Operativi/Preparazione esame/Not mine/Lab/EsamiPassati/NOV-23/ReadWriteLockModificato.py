from threading import Thread,RLock,Condition, current_thread
from random import random
from time import sleep

#   Nella versione originale di questo codice didattico c'erano alcuni difetti:
#   Uno scrittore puÃ² andare in attesa di sÃ¨ stesso se prende il writelock due volte (non rientranza) 
#   o se prende il writelock e poi il readlock (deadlock) 
#   Sapresti correggere questi problemi da solo? (Trovi una soluzione nella traccia di Novembre 2023): quella di seguito
#

#
# Funzione di stampa sincronizzata, utile per il debug
#
plock = RLock()
debug = False
def dprint(s):
    if debug:
        plock.acquire()
        print(s)
        plock.release()

#
#
#  Codice fornito come materiale preliminare, composto dalla classe DatoCondiviso e dalla classe blocking_queue
#
#
    #
    # Le due classi DatoCondiviso e DatoCondivisoSenzaStarvation sono state modificate per consentire la rientranza
    # In particolare sono state aggiunte e gestite le variabili self.currentWriter e self.numLockScrittura.
    # Rimane come piccolo difetto il fatto che un lettore che ha giÃ  acquisito il lock in lettura non puÃ² prendere il lock in scrittura anche se Ã¨ l'unico lettore.
    # Questo non crea problemi in questa prova di esame, ma potrebbe in generale dare fastidio in altri contesti.
    #
        
class DatoCondiviso():

    def __init__(self,v):
        self.dato = v
        self.numLettori = 0
        self.numLockScrittura = 0
        self.currentWriter = None
        self.lock = RLock()
        self.condition = Condition(self.lock)

    def getDato(self):
        return self.dato
    
    def setDato(self, i):
        self.dato = i


    def acquireReadLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in lettura")
        while self.numLockScrittura>0 and self.currentWriter != current_thread():
            dprint(f"Il thread {current_thread().name} voleva leggere ma trova che c'Ã¨ lo scrittore {self.currentWriter}. Dunque aspetta.")
            self.condition.wait()
        self.numLettori += 1
        dprint(f"Il thread {current_thread().name} prende il lock in lettura")
        self.lock.release()

    def releaseReadLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} rilascia il lock in lettura")
        self.numLettori -= 1
        if self.numLettori == 0:
            self.condition.notify()
        self.lock.release()

    def acquireWriteLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in scrittura")

        while self.numLettori > 0 or self.numLockScrittura > 0 and self.currentWriter != current_thread():
            dprint(f"Il thread {current_thread().name} voleva scrivere su {self}, ma trova che ci sono {self.numLettori} lettori e che currentWrite={self.currentWriter}. Dunque aspetta.")
            self.condition.wait()
        self.numLockScrittura += 1
        self.currentWriter = current_thread()
        dprint(f"Il thread {current_thread().name} acquisisce il lock in scrittura")
        self.lock.release()

    def releaseWriteLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} rilascia il lock in scrittura")
        self.numLockScrittura -= 1
        if self.numLockScrittura == 0:
            self.currentWriter = None
        self.condition.notify_all()
        self.lock.release()


class DatoCondivisoSenzaStarvation(DatoCondiviso):
    SOGLIAGIRI = 5

    def __init__(self,v):
        super().__init__(v)
        self.numScrittoriInAttesa = 0
        self.numGiriSenzaScrittori = 0

    def acquireReadLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in lettura")

        #
        # Consento a un thread che ha giÃ  il lock in scrittura di bypassare il controllo starvation e prendere il lock in lettura.
        #
        while self.currentWriter != current_thread() and ( 
               self.numLockScrittura > 0 or (self.numScrittoriInAttesa > 0 and self.numGiriSenzaScrittori > self.SOGLIAGIRI) 
            ):
            dprint(f"Il thread {current_thread().name} voleva leggere {self}. Trova che {self.numScrittoriInAttesa} scrittori sono in attesa; \
                    Sono passati {self.numGiriSenzaScrittori} giri senza scrittori. Attualmente c'Ã¨ lo scrittore: {self.currentWriter}")
            self.condition.wait()
        self.numLettori += 1
        # 
        # 		 * Il contatore viene incrementato solo se effettivamente ci sono
        # 		 * scrittori in attesa.
        # 		 
        if self.numScrittoriInAttesa > 0:
            self.numGiriSenzaScrittori += 1
        dprint(f"Il thread {current_thread().name} prende il lock in lettura")
        self.lock.release()

    def releaseReadLock(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} rilascia il lock in lettura")
        self.numLettori -= 1
        # 
        # 	Nella versione senza starvation, possono esserci anche dei lettori in attesa. 
        #   E' necessario
        #   dunque svegliare tutti.
        # 			 
        if self.numLettori == 0:
            self.condition.notify_all()
        self.lock.release()

    def acquireWriteLock(self):   # No starvation version
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in scrittura")
 
        self.numScrittoriInAttesa += 1
        while self.numLettori > 0 or self.numLockScrittura>0 and self.currentWriter != current_thread():
            dprint(f"Il thread {current_thread().name} voleva scrivere su {self}, ma trova che ci sono {self.numLettori} lettori e che currentWrite={self.currentWriter}. Dunque aspetta.")
            self.condition.wait()
        self.ceUnoScrittore += 1
        self.currentWriter = current_thread()
        self.numScrittoriInAttesa -= 1
        self.numGiriSenzaScrittori = 0
        dprint(f"Il thread {current_thread().name} prova a prendere il lock in scrittura")
        self.lock.release()

# Resta uguale a DatoCondiviso
#     def releaseWriteLock(self):
#         lock.acquire()
#         ...
#         lock.release()