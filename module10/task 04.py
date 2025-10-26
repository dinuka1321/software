import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def acceleration(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.acceleration(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("Reg Number | Max Speed | Current Speed | Distance")
        print("-" * 45)
        for car in self.cars:
            print(f"{car.registration_number:10} | {car.maximum_speed:9} | {car.current_speed:13} | {car.travelled_distance:8.1f} km")
        print()

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        race.print_status()

race.print_status()
print(f"Race finished in {hours} hours.")