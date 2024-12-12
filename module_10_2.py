import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str,power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.cnt = 100
        self.day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        n = self.cnt
        #time.sleep(1)
        while n:
            time.sleep(1)
            self.day += 1
            n -= self.power
            print(f'{self.name} сражается {self.day} дней, осталось {n} войнов')
        print(f'{self.name} одержал победу спустя {self.day} дней!')
        print('Все битвы завершены!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
#print('Все битвы завершены!')