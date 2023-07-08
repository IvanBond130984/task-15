class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage, capacity=50):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity=capacity
    def seating_capacity(self, capacity=50):
        self.capacity=capacity
        return f'Вместимость одного автобуса {self.name}: {self.capacity} пассажиров'
print('Введите название автомобиля')
name=input()
print('Скорость')
max_speed=input()
print('Введите пробег')
mileage=input()
print('Введите вместимость')
v=input()
a0=Autobus(name, max_speed, mileage)
if len(v)>0:
    print(a0.seating_capacity(v))
else:
    print(a0.seating_capacity())