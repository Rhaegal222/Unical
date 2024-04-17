from random import random
from threading import RLock, Condition, current_thread, Thread
from time import sleep

plock = RLock()
debug = True


def dprint(s):
    if debug:
        plock.acquire()
        print(s)
        plock.release()


class PonteMareMonti:
    def __init__(self):
        self.num_verso_mare = 0
        self.num_verso_monti = 0
        self.lock = RLock()
        self.condition = Condition(self.lock)

    def acquire_lock_mare(self):
        self.lock.acquire()
        dprint(f"Il {current_thread().name} prova a prendere il lock verso il mare")
        while self.num_verso_monti > 0:
            dprint(f"Il {current_thread().name} vuole andare al mare ma il ponte è occupato da quelli che vanno ai monti. Dunque aspetta.")
            self.condition.wait()
        self.num_verso_mare += 1
        dprint(f"Il {current_thread().name} prende il lock verso il mare")
        self.lock.release()

    def release_lock_mare(self):
        self.lock.acquire()
        dprint(f"Il {current_thread().name} è arrivato al mare")
        self.num_verso_mare -= 1
        if self.num_verso_mare == 0:
            self.condition.notify()
        self.lock.release()

    def acquire_lock_monti(self):
        self.lock.acquire()
        dprint(f"Il {current_thread().name} prova a prendere il lock verso i monti")
        while self.num_verso_monti > 0:
            dprint(f"Il {current_thread().name} vuole andare ai monti ma il ponte è occupato da quelli che vanno al mare. Dunque aspetta.")
            self.condition.wait()
        self.num_verso_mare += 1
        dprint(f"Il {current_thread().name} prende il lock verso i monti")
        self.lock.release()

    def release_lock_monti(self):
        self.lock.acquire()
        dprint(f"Il thread {current_thread().name} è arrivato ai monti")
        self.num_verso_monti -= 1
        if self.num_verso_monti == 0:
            self.condition.notify()
        self.lock.release()

class VersoMare(Thread):
    def __init__(self, i, ponte):
        super().__init__()
        self.id = i
        self.ponte = ponte

    def run(self):
        self.ponte.acquire_lock_mare()
        self.ponte.release_lock_mare()


class VersoMonti(Thread):
    def __init__(self, i, ponte):
        super().__init__()
        self.id = i
        self.ponte = ponte

    def run(self):
        self.ponte.acquire_lock_monti()
        self.ponte.release_lock_monti()


Morandi = PonteMareMonti()

for i in range(1, 21):
    car = VersoMare(i, Morandi)
    car.start()

for i in range(21, 42):
    car = VersoMonti(i, Morandi)
    car.start()


