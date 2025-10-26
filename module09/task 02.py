class Car:
    def __init__(self,registration_number,maximum_speed,current_speed = 0,travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def acceleration(self,speed_change):
        self.current_speed += speed_change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

car1 = Car("ABC-123",142)

print(f"Registration Number: {car1.registration_number}")
print(f"Maximum Speed: {car1.maximum_speed} km/h")
print(f"Current Speed: {car1.current_speed} km/h")


car1.acceleration(30)
car1.acceleration(70)
car1.acceleration(50)
print(f"Current speed after acceleration: {car1.current_speed} km/h")
car1.acceleration(-200)
print(f"Final speed after emergency brake: {car1.current_speed} km/h")







