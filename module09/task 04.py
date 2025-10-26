import random

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def acceleration(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_number, max_speed))

race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.acceleration(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True
            break

print(f"{'Registration':<10} {'MaxSpeed':<10} {'CurSpeed':<10} {'Distance':<10}")
print("-" * 45)
for car in cars:
    print(f"{car.registration_number:<10} {car.maximum_speed:<10} {car.current_speed:<10} {car.travelled_distance:<10.1f}")