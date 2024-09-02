'''
    Scrivere un programma che crea 5 Thread a cui deve essere assegnato un nome differente.
    Ogni thread stampa ciclicamente il proprio nome su standard output.
    Ogni stampa deve essere effettuata su una singola linea e non deve essere interrotta dalle stampe degli altri thread
'''
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name=name
    def run(self):
        while True:
            print(f"Il Thread stampa {self.name}")

def main():
    threads= [MyThread(f"Thread-{i}") for i in range(5)]
    for t in threads:
        t.start()

if __name__ == "__main__":
    main()