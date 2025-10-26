class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        print(f"Running elevator {elevator_number + 1} to floor {destination_floor}")
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Fire alarm! Moving all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i + 1}:")
            elevator.go_to_floor(elevator.bottom_floor)


building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.fire_alarm()