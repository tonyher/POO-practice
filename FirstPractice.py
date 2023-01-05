


class Vehicle:
    def __init__(self, color,wheel, car_doors):
        self.color = color
        self.wheel = wheel
        self.car_doors = car_doors 
    

class Car(Vehicle):
    def __init__(self, speed, cylinder_capacity):
        self.speed = speed
        self.cylinder_capacity = cylinder_capacity
        

Newcar = Car()

