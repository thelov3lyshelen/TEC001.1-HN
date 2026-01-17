import math
import time
import random

name = str(input("Please fill your name here: "))
print("Hello,", name+"!")

time.sleep(1)

print("We will calculate the circumference of a circle, mind you input the radius?")
radius = float(input("Enter circle radius: "))
circumference = math.pi * 2 * radius
print(f"The circumference is {circumference:.2f}")

time.sleep(1)

print("Let's calculate the perimeter of a rectangle. Again, I need your input on length and width.")
length = float(input("Rectangle length: "))
width = float(input("Rectangle width: "))
perimeter = 2 * (length + width)
print(f"The perimeter of a rectangle is {perimeter:.2f}.")

time.sleep(1)

print("Another activity awaits you: Input 3 random integer numbers!")
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
summation = a + b + c
product = a*b*c
average = (a+b+c)/3
str(summation)
str(product)
str(average)
print("The sum of the numbers is:", str(summation))
print("The product of the numbers is:", str(product))
print("The average of the numbers is:", str(average))

time.sleep(1)

print("Almost there! We will convert medival units to modern units!")
talent = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
totalgrams = (talent * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
grams = totalgrams % 1000
kilograms = int(totalgrams // 1000)
print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")

time.sleep(1)

print("Let me generate a 3-digit code and a 4-digit code:")

time.sleep(1)

def generatecode3digits():
    firstdigit3 = random.randint(0, 9)
    seconddigit3 = random.randint(0, 9)
    thirddigit3 = random.randint(0, 9)
    code3 = f"{firstdigit3}{seconddigit3}{thirddigit3}"
    print(code3)
generatecode3digits()
def generatecode4digits():
    firstdigit4 = random.randint(1, 6)
    seconddigit4 = random.randint(1, 6)
    thirddigit4 = random.randint(1, 6)
    fourthdigit4 = random.randint(1, 6)
    code4 = f"{firstdigit4}{seconddigit4}{thirddigit4}{fourthdigit4}"
    print(code4)
generatecode4digits()
print("Done! Thank you for staying till the end!")
