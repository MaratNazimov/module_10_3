from random import randint
from threading import Thread, Lock
from time import sleep


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            replenishment = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}.')
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdrawal = randint(50, 500)
            print(f"Запрос на снятие средств: {withdrawal}")
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f"Снятие средств: {withdrawal}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank(0)

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'\nИтоговый баланс: {bk.balance}')
