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
        print("Your journey got disrupted by a fire alarm, returning to the bottom floor")
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
print("Moving to the bottom floor")


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 2000

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


car1 = Car("ABC-123", 142)

print("Car Properties:")
print(f"Registration Number: {car1.registration_number}")
print(f"Maximum Speed: {car1.max_speed} km/h")
print(f"Current Speed: {car1.current_speed} km/h")
print(f"Travelled Distance: {car1.travelled_distance} km")

car1.accelerate(60)
# car1.accelerate(70)
# car1.accelerate(50)
print(f"Current Speed after accelerations: {car1.current_speed} km/h")
# car1.accelerate(-200)
print(f"Final Speed after emergency brake: {car1.current_speed} km/h\n")

car1.drive(1.5)
print(f"Travelled Distance: {car1.travelled_distance} km\n")

cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg_number, max_speed))

race_finished = False
hours_passed = 0

while not race_finished:
    hours_passed += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True
            break

print(f"Race finished in {hours_passed} hours!\n")
print(f"{'Car':<10}{'Max Speed':<12}{'Current Speed':<15}{'Distance Travelled':<20}")
print("-" * 60)
for car in cars:
    print(f"{car.registration_number:<10}{car.max_speed:<12}{car.current_speed:<15}{car.travelled_distance:<20.1f}")

class Race:
    def __init__(self, name, distance, participants):
        self.name = name
        self.distance = distance
        self.participants = cars
    def hour_passes(self):
        for cars in self.participants:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Reg. Number':<15} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance':<10}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.registration_number:<15} | {car.max_speed:<10} | "f"{car.current_speed:<15} | {car.travelled_distance:<10}")
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False
grand_derby = Race("Grand Demolition Derby", 8000, cars)
hours_elapsed = 0
while not grand_derby.race_finished():
    grand_derby.hour_passes()
    hours_elapsed += 1

    if hours_elapsed % 10 == 0:
        print(f"\n--- Hour {hours_elapsed} Status Update ---")
        grand_derby.print_status()

print(f"\n*** RACE FINISHED! Total time: {hours_elapsed} hours ***")
grand_derby.print_status()