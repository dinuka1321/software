class Car:
    def __init__ (self,registration_number,maximum_speed,current_speed=0,total_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.total_distance = total_distance

    def accelerate(self, change):
        self.current_speed = self.current_speed + change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,hours):
        self.total_distance = self.total_distance + self.current_speed* hours

class Electric_car(Car):
    def __init__(self,registration_number,maximum_speed,battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(registration_number,maximum_speed)

    def print_run(self,hours):
        super().drive(hours)
        print(f"total distance: {self.total_distance} km")


class Gasoline_car(Car):
    def __init__(self,registration_number,maximum_speed,tank_volume):
        self.tank_volume = tank_volume
        super().__init__(registration_number,maximum_speed)

    def print_run(self,hours):
        super().drive(hours)
        print(f"total distance: {self.total_distance} km")

e = Electric_car("ABC 12",180,52)
g = Gasoline_car("ABC 123",165,32)

e.accelerate(120)
g.accelerate(130)


e.print_run(3)
g.print_run(3)
