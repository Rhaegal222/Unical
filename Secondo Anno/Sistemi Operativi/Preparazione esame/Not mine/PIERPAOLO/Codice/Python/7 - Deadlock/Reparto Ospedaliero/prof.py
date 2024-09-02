#!/usr/bin/env python
from threading import Thread,RLock,Condition
from time import sleep
from random import random

DURATAREGIME = 3

class Stanza(object):


    def __init__(self):
        self.giorno = True
        self.visitatori=0
        self.visite = []
        self.medico = False
        self.medici = []
        self.lock = RLock()
        self.conditionVisitatori = Condition(self.lock)
        self.conditionMedici = Condition(self.lock)
        self.conditionDisplay = Condition(self.lock)


    def visitaMedica(self, name):
        with self.lock:
            while self.giorno and (len(self.medici) > 0 or len(self.visite) > 0): #la notte possono sempre entrare i medici
                self.conditionMedici.wait()
            self.medici.append(name)
            self.conditionDisplay.notify()

    def terminaVisitaMedica(self, name):
        with self.lock:
            self.medici.remove(name)
            self.conditionMedici.notify_all()
            self.conditionVisitatori.notify_all()
            self.conditionDisplay.notify()

    def visitaCortesia(self, name):
        with self.lock:
        #  un visitatore che vuol far visita al paziente di giorno deve attendere che termini una eventuale visita medica in corso, di notte deve accertarsi che non ci sia gia' un altro visitatore nella stanza 
            while (self.giorno and len(self.medici) > 0) or (not self.giorno and len(self.visite) > 0):
                self.conditionVisitatori.wait()
            self.visite.append(name)
            self.conditionDisplay.notify()

    def terminaVisitaCortesia(self, name):
        with self.lock:
            self.visite.remove(name)
            if len(self.visite) == 0:
                self.conditionMedici.notify_all()
            self.conditionDisplay.notify()

    def print_(self):
        with self.lock:
            while True:
                self.conditionDisplay.wait() #lavora solo quando viene notificato al cambiamento di qualcosa 
                print("\n(@) | " if self.giorno else "\n(_) | ", end="")
                for visitatore in self.visite:
                    print(visitatore + " ", end="")
                for medico in self.medici:
                    print(medico + " ", end="")
                print("|")

    def setRegime(self, b):
        with self.lock:
            self.giorno = b


class Visitatore(Thread):

    def __init__(self, stanza, name):
        super(Visitatore, self).__init__()
        self.stanza = stanza
        self.name = name

    def run(self):
        while True:
           sleep(random() * 2)
           self.stanza.visitaCortesia(self.name)
           sleep(random() * 2)
           self.stanza.terminaVisitaCortesia(self.name)

class Medico(Thread):

    def __init__(self, stanza, name):
        super(Medico, self).__init__()
        self.stanza = stanza
        self.name = name

    def run(self):
        while True:
                sleep(random() * 2)
                self.stanza.visitaMedica(self.name)
                sleep(random() * 2)
                self.stanza.terminaVisitaMedica(self.name)


class Display(Thread):

    def __init__(self, s):
        super(Display, self).__init__()
        self.stanza = s

    def run(self):
        self.stanza.print_()
        
class SistemaSolare(Thread):
 
    def __init__(self, s):
        super(SistemaSolare, self).__init__() #come fare super().__init__()
        self.s = s

    def run(self):
        while True:
            sleep(DURATAREGIME)
            self.s.setRegime(True)
            sleep(DURATAREGIME)
            self.s.setRegime(False)
 
        
stanza = Stanza()

for i in range(6):    
    medico = Medico(stanza, f"Medico-{i}")
    medico.start()

for i in range(10):    
    amico = Visitatore(stanza, f"Amico-{i}")
    amico.start()

Display(stanza).start()
SistemaSolare(stanza).start()
