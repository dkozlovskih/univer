import threading
import time
from random import randint



class Bank:
    def __init__(self):
        self.balans = 0
        self.lock = threading.Lock()
        self.cnt = 0

    def deposit(self):
        for i in range(100):
            d = randint(50, 500)
            if self.balans >= 500 and self.lock.locked():
                self.lock.release()
            self.balans += d
            print(f'Пополнение: {d}. Баланс: {self.balans}')
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            t = randint(50, 500)
            print(f'Запрос на {t}')
            if t <= self.balans:
                self.balans -= t
                print(f'Снятие: {t}. Баланс: {self.balans}')
            elif t > self.balans:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balans}')