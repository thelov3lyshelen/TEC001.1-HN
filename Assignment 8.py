import time
import random
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
        print(f"The floor number is {self.current}")
    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
        print(f"The floor number is {self.current}")
    def go_to_floor(self, target):
        if target > self.top or target < self.bottom:
            print("Invalid floor!")
            return
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()
h = Elevator(1, 30)
inp = int(input("You are at the first floor of a 30 story building, type a number to go to that floor: "))
h.go_to_floor(inp)

time.sleep(1)

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]
    def run_elevator(self, elevator_num, destination):
        if 0 <= elevator_num <= len(self.elevators):
            print(f"Elevator {elevator_num} is moving")
            self.elevators[elevator_num - 1].go_to_floor(destination)
        else:
            print("what")
    def fire_alarm(self):
        print("Someone committed arson, initiate emergency")
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)
b = Building(1, 30, 4)
time.sleep(1)
b.run_elevator(1, 6)
time.sleep(1)
b.run_elevator(2, 2)
time.sleep(1)
b.run_elevator(3, 5)
time.sleep(1)
b.run_elevator(4, 3)
time.sleep(2)
b.fire_alarm()
print("All elevators were moved to the bottom floor")


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        travelled_distance = self.current_speed * hours
        self.travelled_distance += travelled_distance

class Race:
    def __init__(self, name, distance, participants):
        self.name = name
        self.distance = distance
        self.participants = participants
    def hour_passes(self):
        for car in self.participants:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self):
        print(f"{'Registration Number':<15} | {'Max Speed':<10} | {'Distance':<12}")
        print("-" * 50)
        for car in self.participants:
            print(f"{car.registration_number:<15} | {car.max_speed:<10} | {car.travelled_distance:<12}")
    def race_finished(self):
        for car in self.participants:
            if car.travelled_distance >= self.distance:
                return True
        return False

cars = []
for i in range(1, 11):
    reg_number = f"Car {i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg_number, max_speed))

grand_derby = Race("Grand Demolition Derby", 8000, cars)
hours_elapsed = 0
while not grand_derby.race_finished():
    grand_derby.hour_passes()
    hours_elapsed += 1

    if hours_elapsed % 10 == 0:
        print(f"Hour {hours_elapsed}:")
        grand_derby.print_status()

print(f"Race finished after {hours_elapsed} hours.")
grand_derby.print_status()