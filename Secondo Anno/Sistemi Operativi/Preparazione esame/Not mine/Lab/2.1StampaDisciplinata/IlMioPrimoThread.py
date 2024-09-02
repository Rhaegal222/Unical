'''
Esercitazione: stampaDisciplinata
• Riprendi il codice de IlMioPrimoThread.py ed eredita dalla classe Stampa una classe che
chiamerai StampaDisciplinata. All’interno di questa classe, fai in modo che ogni thread
stampi un rigo per volta senza essere interrotto.
• Prova a usare istanze multiple della classe StampaDisciplinata (ad esempio crea una
StampaDisciplinata diversa una per ciascun thread). Cosa succede e perchè?

Risposta:
Ogni thread avrà il proprio oggetto StampaDisciplinata e quindi il proprio oggetto lock.
Questo significa che ogni thread avrà il proprio lock indipendente e non condividerà il lock con gli altri thread.
In termini di sincronizzazione dei thread, ciò significa che i thread non saranno sincronizzati tra loro perché ogni
thread ha il proprio lock. Quindi, anche se un thread ha acquisito il suo lock e sta eseguendo la sua operazione di
tampa, gli altri thread possono ancora acquisire i loro lock e iniziare le loro operazioni di stampa. Di conseguenza,
l’outputdella stampa potrebbe essere interrotto da altri thread, contrariamente all’obiettivo della classe StampaDisciplinata.

• Cambia il codice in maniera tale che ogni thread possa stampare 10 righe consecutive di
simboli senza interferenze o interruzioni di altri thread;
• Cambia il codice in maniera tale che si possa scegliere quante righe consecutive un
thread può stampare senza interferenze di altri thread.
• Sostituisci il codice
for i in range(0,l+1):
print(c, end='', flush=True)
con:
print(l*c)
Cosa succede? Perché? '''

from random import randint
from threading import RLock, Thread



class Stampa:
    def __init__(self):
        pass

    def stampa(self,c,l):
        for i in range(0,l+1):
            print( c, end='', flush=True)
        print('')

    def stampaStriscia(self,c):
        self.stampa(c,50)



class StampaDisciplinata(Stampa):
    def __init__(self):
        super().__init__()
        self.lock = RLock()

    def stampa(self,c,l):
        with self.lock:
            super().stampa(c,l)

    def stampaStriscia(self,c,r):
        with self.lock:
            for i in range(r):
                super().stampaStriscia(c)


class StampatoreDiAsterischi(Thread):

    def __init__(self,s : Stampa):
        super().__init__()
        self.st = s
        self.count = 0

    def run(self):
        
        while self.count < 50:
            self.st.stampaStriscia('*', r)
            self.count += 1

class StampatoreDiTrattini(Thread):

    def __init__(self, s : Stampa):
        super().__init__()
        self.st = s
        self.count = 0

    def run(self):
        
        while self.count < 50:
            self.st.stampaStriscia('-', r)
            self.count += 1



st = StampaDisciplinata()

r=randint(1,10)

john = StampatoreDiAsterischi(st)
al = StampatoreDiTrattini(st)

john.start()
al.start()

print("Main terminato")


    