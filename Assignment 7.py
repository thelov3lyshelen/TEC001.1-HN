import random
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



