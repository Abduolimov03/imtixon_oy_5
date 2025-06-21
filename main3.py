# 3.Mashina ro‘yxati
# Car(brand, model, year, mileage) nomli namedtuple.
# Foydalanuvchi 5 ta mashina kiritadi. Eng kam yurgan mashinani toping.
#

from collections import namedtuple

Car = namedtuple('Car', ['brand', 'model', 'year', 'mileage'])

cars = []

for i in range(3):
    print(f"{i+1}-mashina:")
    brand = input("Brand: ")
    model = input("Model: ")
    year = int(input("Yil: "))
    mileage = int(input("Yurgan masofa (km): "))
    cars.append(Car(brand, model, year, mileage))
    print()


eng_kam = min(cars, key=lambda car: car.mileage)

print("\nEng kam yurgan mashina:")
print(f"{eng_kam.brand} {eng_kam.model}, {eng_kam.year}-yil, {eng_kam.mileage} km yurgan.")