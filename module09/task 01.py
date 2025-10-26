class Car:
    def __init__(self,registration_number,maximum_speed,current_speed = 0,travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
car1 = Car("ABC-123",142)

print(f"Registration Number: {car1.registration_number}")
print(f"Maximum Speed: {car1.maximum_speed} km/h")
print(f"Current Speed: {car1.current_speed} km/h")
print(f"Travelled Distance: {car1.travelled_distance} km")
