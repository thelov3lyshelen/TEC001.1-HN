import time
try:
    print("Exercise 1")

    number = []
    while True:
        inp = input("Enter your list of number: ")
        if inp == "":
            break
        try:
            numbers = float(inp)
            number.append(numbers)
        except ValueError:
            print("Consider this a warning")
    number.sort(reverse=True)
    five = number[:5]
    print("The five greatest numbers:", five)

    time.sleep(1)

    print("Exercise 2")
    seasons = ("spring", "summer", "autumn", "winter")
    month = int(input("Enter month(1-12): "))

    if month == 12 or month == 1 or month == 2:
        print(seasons[3])
    elif 3 <= month <= 5:
        print(seasons[0])
    elif 6 <= month <= 8:
        print(seasons[1])
    elif 9 <= month <= 11:
        print(seasons[2])
    else:
        print("Invalid month number.")
        
    time.sleep(1)

    print("Exercise 3")
    names = set()
    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        if name in names:
            print("Existing name, try again!")
        else:
            print("Name avilable.")
            names.add(name)
    print("\nList of names: ")
    for i in names:
        print(i)

    time.sleep(2)

    print("Exercise 4")
    def frequency(txt):
        words = txt.lower().split()
        total = len(words)
        counts = {}
        for i in words:
            counts[i] = counts.get(i,0) + 1
        sortedwords = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
        five = dict(sortedwords)
        sumfive = sum(five.values())
        proportion = (sumfive / total) * 100
        print(f"Top 5: {five}")
        print(f"Total number of words: {total}")
        print(f"Proportion: {sumfive / total} = {proportion:.2f}%")
    print("Example: Boom and zoom, often abbreviated to BnZ, is another kind of energy fighting, and favors planes with a high top speed and great high-speed maneuverability. This form of energy fighting... nvm too long")
    txt = "Boom and zoom, often abbreviated to BnZ, is another kind of energy fighting, and favors planes with a high top speed and great high-speed maneuverability. This form of energy fighting is generally the easiest to learn, although usually the least effective. This tactic is a sort of hit and run, the player cruising at an altitude above the battlefield comparable to a standard energy trap. When an isolated target is found, the pilot should dive to engage the opponent so that the aircraft can swiftly attack the target and quickly leave the area. In case of an aircraft not being shot down in a single pass, the player can use the speed gained from the dive to stall the opponent should they chase the player up. If the opponent does not much notice or care about the failed pass, another pass may be taken once altitude is regained. Keep in mind however that constant successive passes bleeds an incredible amount of speed, and should a target not follow the player up, it is best to disengage to prevent losing too much energy. Upon a finished engagement, the player should climb back to cruising altitude and search for another target."
    print(frequency(txt))

    time.sleep(2)

    print("Exercise 5")
    def removeodd(numbers):
        evennum = []
        for i in numbers:
            if i % 2 == 0:
                evennum.append(i)
        return evennum

    print("Example: 1, 7, 9, 18, 34, 67, 990")
    numbers = [1, 7, 9, 18, 34, 67, 990]
    print("Cut-down list: ", removeodd(numbers))
except:
    print("boo")
