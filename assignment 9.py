print("i put the text files in the folder for three exercises or idk")
import time

time.sleep(1)

def countlines(filename):
    file = open(filename)
    count = 0
    for line in file:
        if line.strip():
            count = count + 1
    print("total line count in assignment 9 test.txt: ", count)
countlines("assignment 9 test.txt")

def findkeyword(filename, keyword):
    linenumber = []
    keyword = keyword.lower()
    file = open(filename)
    for number, line in enumerate(file, 1):
        if keyword in line.lower():
            linenumber.append(number)
    print(f"keyword '{keyword}' appear in lines: {linenumber} in assignment 9 test.txt")
findkeyword("assignment 9 test.txt", "write")

time.sleep(1)

def calculatesum(filename):
    sumscore = 0
    file = open(filename)
    for number, line in enumerate(file, start = 1):
            parts = line.strip().split(",")
            score = float(parts[1])
            sumscore += score
    averagescore = sumscore / number
    print(f"the average score of 'assignment 9 test2.txt' is {averagescore}, in {number} students")
calculatesum("assignment 9 test2.txt")

time.sleep(1)

def caesar(filename, steps, direction):
    ciphertext = ""
    if direction == "left":
        shift = -steps
    if direction == "right":
        shift = steps
    with open(filename, 'r') as file:
        text = file.read()
    for character in text:
        if character.isupper():
            old = ord(character)
            new = (old + shift - 65) % 26 + 65
            ciphertext += chr(new)
        elif character.islower():
            old = ord(character)
            new = (old + shift - 97) % 26 + 97
            ciphertext += chr(new)
        else:
            ciphertext += character
    with open('ciphertext.txt', 'w') as insert:
        insert.write(ciphertext)
    print("ciphertext written to file, please open it to view results")
caesar("assignment 9 test.txt", 3, "right")


