from threading import Thread,Lock
from time import sleep
from random import random,randrange
import time

class Stampa:
    def __init__(self, nome):
        self.lock = Lock()
        self.nome = nome

    def stampa_nome(self):
        with self.lock:
            start_time = time.time()  # Registra l'ora di inizio
            print(f"{self.nome} iniziato alle {time.strftime('%H:%M:%S', time.localtime(start_time))} \n")
            time.sleep(random())  # Ritardo casuale tra 0 e 1 secondo

        end_time = time.time()    # Registra l'ora di fine
        duration = end_time - start_time
        print(f"{self.nome} terminato alle {time.strftime('%H:%M:%S', time.localtime(end_time))}, durata: {duration:.4f} secondi \n")

threads = []
for i in range(5):
    thread_name = f"Thread {i+1}"
    stampa = Stampa(thread_name)
    t = Thread(target=stampa.stampa_nome)
    threads.append(t)
    time.sleep(random())  # Ritardo casuale tra 0 e 1 secondo
    t.start()

for t in threads:
    t.join()