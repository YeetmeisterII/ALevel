class Vehicle:
    def __init__(self, name):
        self.name = name
        self.speed = "0"

    def drive(self):
        print(self.name + " drives along at " + self.speed + "mph")


class Car(Vehicle):
    def __init__(self, name):
        self.crack = "60"


class Tank(Vehicle):
    def __init__(self, name):
        super().__init__(name)


    def shoot(self, target):
        print(self.name + " fires at " + target)


my_car = Car("crack car")
my_car.drive()
my_tank = Tank("Challenger 2")
my_tank.drive()
my_tank.shoot("Ford Focus")