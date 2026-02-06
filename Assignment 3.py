import time
import random
try:
    print("Exercise 1")
    time.sleep(0.5)
    print("Initiating countdown...")
    x = 5
    while x > 0:
        print(x)
        time.sleep(1)
        x -= 1
    print("Blastoff!")
    time.sleep(0.5)
    i = 1
    while i <= 1000:
        if i % 3 == 0:
            print(i)
        i += 1

    time.sleep(1)

    print("Exercise 2")

    while True:
        inches = float(input("Enter inches: "))
        if inches < 0:
            break
        print(f"{inches} inches = {inches * 2.54:.2f} cm")

    time.sleep(1)

    print("Exercise 3")

    numbers = []
    while True:
        entry = input("Enter a number (empty to quit): ")
        if entry == "":
            break
        numbers.append(float(entry))

    if numbers:
        print("Smallest:", min(numbers))
        print("Largest:", max(numbers))
    else:
        print("No numbers entered.")

    time.sleep(1)

    print("Exercise 4")

    secret = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number (1-10): "))
        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print("Correct!")
            break

    time.sleep(1)

    print("Exercise 5")

    correctuser = "python"
    correctpass = "rules"

    attempts = 0
    while attempts < 5:
        user = input("Username: ")
        password = input("Password: ")
        if user == correctuser and password == correctpass:
            print("Welcome, " + correctuser + "!")
            break
        else:
            print("Incorrect")
            attempts += 1
    else:
        print("Access denied")

    time.sleep(1)

    print("Exercise 6")

    string = input("Enter your string: ")
    def middlecharacter(string):
        length = len(string)
        mid = length // 2
        if length % 2 == 0:
            return string[mid - 1 : mid + 1]
        else:
            return string[mid]
    print(middlecharacter(string))

    time.sleep(1)

    print("Exercise 7")
    
    phrase = input("Enter your phrase: ")
    def acronym(phrase):
        words = phrase.split()
        output = ""
        for word in words:
            output += word[0].upper()
        return output
    print(acronym(phrase))
    
except:
    print("bro had only one job")


