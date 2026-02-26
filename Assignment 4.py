import time

try:
    print("Exercise 1")
    time.sleep(1)

    numbers = []

    while True:
        inp = input("Please enter number, Enter to quit: ")
        if inp == "":
            break
        numbers.append(int(inp))
    numbers.sort(reverse = True)
    print("5 greatest numbers: ", numbers[:5])

    time.sleep(1)
    print("Exercise 2")
    time.sleep(1)

    numberinput = int(input("Enter an integer number: "))

    def prime(numberinput):
        if numberinput <= 1:
            return False
        for i in range(2, int(numberinput ** 0.5) + 1):
            if numberinput % 1 == 0:
                return False
        return True

    if prime(numberinput):
        print(numberinput, "is a prime number.")
    else:
        print(numberinput, "is not a prime number.")

    time.sleep(1)
    print("Exercise 3")
    time.sleep(1)

    cities = []
    for i in range(5):
        city = input(f"Enter city {i+1}: ")
        cities.append(city)
    print("Cities entered: ")
    for city in cities:
        print(city)

    time.sleep(1)
    print("Exercise 4")
    time.sleep(1)

    def listsum(numbers):
        return sum(numbers)

    print("Test subjects: 1, 2, 3, 4, 6, 7, 67")
    time.sleep(1)

    custom = [1, 2, 3, 4, 6, 7, 67]
    print("Sum:", listsum(custom))

    time.sleep(1)
    print("Exercise 5")
    time.sleep(1)

    def odds(numbers):
        even = []
        for n in numbers:
            if n % 2 == 0:
                even.append(n)
        return even

    example = [78, 99, 31, 46, 420, 333, 67]
    custom = odds(example)
    print("Test subjects:", example)
    print("Sorted even numbers:", custom)
except:
    print("must have been the wind")
