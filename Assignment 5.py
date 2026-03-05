import re
import time
import random

time.sleep(1)

print("Exercise 1")
code = str(input("Input course code to check: "))
def validcode(code):
    pattern = r"^[A-Z]{2,3}\d{3}$"
    return bool(re.match(pattern, code))
print(validcode(code))

time.sleep(1)

print("Exercise 2")
color = str(input("Feed me hex color: "))
def validhexcode(color):
    colorpattern = r"^#[0-9a-fA-F]{6}$"
    return bool(re.match(colorpattern, color))
print(validhexcode(color))

time.sleep(1)

print("Exercise 3")
print("Today is January 16, 2025. The temperature is 11 degrees Celsius.")
paragraph = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
def sumnumbers(paragraph):
    numbers = re.findall(r"\d+", paragraph)
    return sum(int(num) for num in numbers)
print("The sum of all numbers is", sumnumbers(paragraph))

time.sleep(1)

print("Exercise 4")
print("You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321")
numbers = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321"
def redactphonenumbers(numbers):
    phone = r"(\+84\d+|\d{10})"
    return re.sub(phone, "[REDACTED]", numbers)
print(redactphonenumbers(numbers))

time.sleep(1)

print("Exercise 5")
def findpi():
    N = int(input("How many random points to generate? "))
    n = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            n += 1
            
    piapprox = 4 * n / N
    print(f"Approximation of pi with {N} points: {piapprox}")

findpi()
