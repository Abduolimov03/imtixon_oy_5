# 4.10 ta random son chiqaruvchi threadlar
# Har bir thread bitta random son chiqarsin. Ular tartibsiz chiqishi kerak.



import threading
import random
import time


def random_son():
    x = random.random()
    time.sleep(x)
    print("sonlar :" , random.randint(1, 100))

threadlar = []

for _ in range(10):
    t = threading.Thread(target=random_son )
    threadlar.append(t)
    t.start()

for t in threadlar:
    t.join()
print('tugadi')
