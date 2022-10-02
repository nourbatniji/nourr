class Vehicle():


    def __init__(self):

        self.speed = 0
        self.has_wheels = False
        self.wheels_numbers = 0


    def speed_up(self):

        self.speed += 5
        print("Car Speed Increased")


    def speed_down(self):

        if self.speed == 0:
            print("Car already stopped")

        elif self.speed < 5:
            self.speed = 0
            print("Car Stopped Successfully")

        else:
            self.speed -= 5
            print("Car Speed Decreased")


    def stop(self):

        if self.speed == 0:
            print("Car already stopped")

        else:
            self.speed = 0
            print("Car Stopped Successfully")


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.has_wheels = True
        self.wheels_numbers = 4

    def speed_up(self):
        self.speed += 10
        print("Car Speed Increased")


class Ship(Vehicle):

    def speed_up(self):
        self.speed +=20
        print("Car Speed Increased")


car = Car()
print(car.speed)
car.speed_up()
print(car.speed)
car.speed_down()
print(car.speed_down())







