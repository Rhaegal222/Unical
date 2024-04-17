from threading import RLock, Thread
from time import sleep
from random import randint
import collections


class BankAccount:
    def __init__(self, account_id, account_balance):
        self.id = account_id  # id viene assegnato dalla banca
        self.balance = account_balance  # il saldo iniziale viene definito randomicamente
        self.n_max_transaction = 50  # numero massimo di transazioni registrate
        self.transaction_history = collections.deque()  # inizializzazione della coda delle transazioni
        self.lock = RLock()

    def add_transaction(self, transaction):
        with self.lock:
            '''
            se il numero di transazioni registrate supera la dimensione massima viene eliminata la prima quella più a 
            sinistra, altrimenti viene normalmente aggiunta in coda (a destra).
            '''
            if len(self.transaction_history) == self.n_max_transaction:
                self.transaction_history.popleft()
            self.transaction_history.append(transaction)

    def update_balance(self, amount):
        with self.lock:
            self.balance += amount

    def get_balance(self):
        with self.lock:
            return self.balance


class Printer:
    def __init__(self):
        self.lock = RLock()


class Bank:
    def __init__(self):
        self.bank_accounts = collections.deque()
        self.size = 0
        self.lock = RLock()
        self.printer = Printer()

    def add_account(self, bank_account):
        with self.lock:
            self.size += 1
            self.bank_accounts.append(bank_account)
            print(f"[BANCA] Conto {bank_account.id} aggiunto: {bank_account.balance} euro")

    def get_account_balance(self, bank_account):
        return bank_account.get_balance()

    def rand_account(self):
        with self.lock:
            return self.bank_accounts[randint(0, len(self.bank_accounts) - 1)]

    def transfer(self, sender, receiver, amount):

        if sender.id != receiver.id:
            if sender.id < receiver.id:
                sender.lock.acquire()
                receiver.lock.acquire()
            else:
                receiver.lock.acquire()
                sender.lock.acquire()
            try:
                if self.get_account_balance(sender) < amount or amount < 1:
                    return False
                else:
                    transaction = (sender, receiver, amount)
                    sender.add_transaction(transaction)
                    sender.update_balance(amount * -1)
                    receiver.add_transaction(transaction)
                    receiver.update_balance(amount)
                    with self.printer.lock:
                        print(f"[TRASFERIMENTO] Conto {sender.id} INVIA {amount} euro al Conto {receiver.id}")
                    return True
            finally:
                sender.lock.release()
                receiver.lock.release()
        else:
            return False


class Customer(Thread):

    def __init__(self, bank, account_id, account_balance):
        super().__init__()
        self.account = BankAccount(account_id, account_balance)
        self.bank = bank

    def run(self):
        self.bank.add_account(self.account)
        sleep(2)
        for transaction in range(randint(1, 10)):
            actual_balance = self.bank.get_account_balance(self.account)
            self.bank.transfer(self.account, self.bank.rand_account(), randint(0, actual_balance))


bank = Bank()

for i in range(20):
    balance = randint(10, 1000)
    customer = Customer(bank, i + 1, balance)
    customer.start()
