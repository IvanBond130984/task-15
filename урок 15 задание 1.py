class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Autobus(Transport):
    def print_autobus(self):
        print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} км\\час Пробег: {self.mileage} км')
print('Введите название автомобиля')
name=input()
print('Скорость')
max_speed=input()
print('Введите пробег')
mileage=input()
a0=Autobus(name, max_speed, mileage)
a0.print_autobus()