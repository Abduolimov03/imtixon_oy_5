
# 1.Fibonacci generatori
# Generator yozing: kiritilgan `n` ta fibonacci sonlarini chiqaradi
#
# 2.n ta butun sonlardan iborat a massiv berilgan. b massivni hosil qiluvchi decorator yozilsin. b massivning har bir elementi quyidagicha hisoblanadi:
# b[k] = a[0] + a[1] + ... + a[k]
#
# 3.Mashina ro‘yxati
# Car(brand, model, year, mileage) nomli namedtuple.
# Foydalanuvchi 5 ta mashina kiritadi. Eng kam yurgan mashinani toping.
#
# 4.10 ta random son chiqaruvchi threadlar
# Har bir thread bitta random son chiqarsin. Ular tartibsiz chiqishi kerak.
#
# 5.Githubda ‘5-oy imtihoni varinat’ nomli repo ochilsin va har bir masala alohida commit orqali yuborilsin commit ‘1-masala’ korinishida bolsin


##1
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1
n = int(input("nechta fibonacci  kerak?: "))
for i in fibonacci_generator(n):
    print(i, end=' ')