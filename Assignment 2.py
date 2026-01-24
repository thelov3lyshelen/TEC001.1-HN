Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import time
import math
def zanderlength():
    length = float(input("Enter the length of the zander in centimeters: "))
    if length < 42:
        print(f"Release the fish back into the lake. It is {42 - length} cm below the size limit.")
    else:
        print("The fish meets the size limit.")
zanderlength()

time.sleep(1)

def cabin():
    cabin_class = input("Enter cabin class (LUX, A, B, C): ")
    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")
cabin()

time.sleep(1)

def hemoglobincheck():
    sex = input("Enter biological sex (M/F): ")
    value = int(input("Enter hemoglobin value (g/l): "))
    if sex == "F":
        if value < 117:
            print("Hemoglobin value is low.")
        elif value <= 155:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    elif sex == "M":
        if value < 134:
            print("Hemoglobin value is low.")
        elif value <= 167:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    else:
        print("Invalid input for biological sex.")
hemoglobincheck()

time.sleep(1)

def leapyear():
    year = int(input("Enter a year: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
leapyear()

time.sleep(1)

def unitprice(diameter, price):
    radius = diameter / 2
    areainm2 = math.pi * (radius ** 2) / 10000
    return price / areainm2
def comparepizzas():
    print("Enter details for Pizza 1:")
    dpizza1 = float(input("Diameter (cm): "))
    ppizza1 = float(input("Price (USD): "))
    print("Enter details for Pizza 2:")
    dpizza2 = float(input("Diameter (cm): "))
    ppizza2 = float(input("Price (USD): "))

    prize1 = unitprice(dpizza1, ppizza1)
    prize2 = unitprice(dpizza2, ppizza2)

    print(f"Pizza 1 unit price: ${prize1:.2f}/m²")
    print(f"Pizza 2 unit price: ${prize2:.2f}/m²")

    if prize1 < prize2:
        print("Pizza 1 offers better value for money.")
    elif prize2 < prize1:
        print("Pizza 2 offers better value for money.")
    else:
        print("Both pizzas offer the same value.")
comparepizzas()
