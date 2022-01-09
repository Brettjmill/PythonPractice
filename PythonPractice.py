import random

# Exercise 1

name = input("Give me your name: ")

age = int(input("Give me your age: "))

reprints = int(input("Tell me how many times to see a message: "))

counter = reprints

centenialYear = str((2022 - age) + 100)

while counter > 0:
    print("You will turn 100 years old in " + centenialYear)
    counter -= 1   

# Exercise 2

num = int(input("Give me a number: "))

if num == 0:
    print("You've entered zero!")
elif num % 4 == 0:
    print("This is a multiple of four!")
elif num % 2 == 0:
    print("You've entered an even number!")
elif num % 2 == 1:
    print("You've entered an odd number!")

# Exercise 3

a = [1,1,2,3,5,8,13,21,34,55,89]

newList = []

for element in a:
    if element < 5:
        newList.append(element)
print(newList)

# Exercise 4

num2 = int(input("Give me a number: "))

list = range(1,num2 + 1)

resultsList = []

for y in list:
    if num2 % y == 0:
        resultsList.append(y)

print(resultsList)

# Exercise 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newList2 = []

if len(a) > len(b):
    for item in b:
        if item in a and item not in newList2:
            newList2.append(item)
if len(b) > len(a):
    for item in a:
        if item in b and item not in newList2:
            newList2.append(item)

print(newList2)

# Exercise 6

palCheck = input("Give me a word to check as a palindrome: ")

halfMark = int(len(palCheck)/2)

if len(palCheck) % 2 == 0:
    frontHalf = palCheck[0:halfMark]
    backHalf = palCheck[-1:halfMark-1:-1]
    
    if frontHalf == backHalf:
        print("Yep, that's a palindrome!")
    else:
        print("Nope, no palindrome!")

if len(palCheck) % 2 == 1:
    frontHalf = palCheck[0:halfMark]
    backHalf = palCheck[-1:halfMark:-1]
    
    if frontHalf == backHalf:
        print("Yep, that's a palindrome!")
    else:
        print("Nope, no palindrome!")

# Exercise 7

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [item for item in a if item % 2 == 0]

print(b)

# Exercise 8

player1 = input("Player 1!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")
player2 = input("Player 2!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")

while player1 != "QUIT" and player2 != "QUIT":
    if player1 == player2:
        player1 = input("TIE! Try again Player 1!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")
        player2 = input("TIE! Try again Player 2!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")

    if player1 == "ROCK" and player2 == "SCISSORS":
        player1 = input("Congrats, Player 1! YOU WIN! Now try again:  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")
        player2 = input("Maybe next time, Player 2! GET YOUR REVENGE!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")

    if player1 == "ROCK" and player2 == "PAPER":
        player1 = input("Maybe next time, Player 1! GET YOUR REVENGE!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")
        player2 = input("Congrats, Player 2! YOU WIN! Now try again:  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")

    if player1 == "SCISSORS" and player2 == "PAPER":
        player1 = input("Congrats, Player 1! YOU WIN! Now try again:  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")
        player2 = input("Maybe next time, Player 2! GET YOUR REVENGE!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")

    if player1 == "SCISSORS" and player2 == "ROCK":
        player1 = input("Maybe next time, Player 1! GET YOUR REVENGE!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")
        player2 = input("Congrats, Player 2! YOU WIN! Now try again:  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")

    if player1 == "PAPER" and player2 == "ROCK":
        player1 = input("Congrats, Player 1! YOU WIN! Now try again:  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")
        player2 = input("Maybe next time, Player 2! GET YOUR REVENGE!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")

    if player1 == "PAPER" and player2 == "SCISSORS":
        player1 = input("Maybe next time, Player 1! GET YOUR REVENGE!  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")
        player2 = input("Congrats, Player 2! YOU WIN! Now try again:  ROCK, PAPER, OR SCISSORS? (also, use caps) -> ")

    if player1 == "QUIT" or player2 == "QUIT":
        print("OK, bye for now!")
        break

# Exercise 9

randNum = random.randint(1,9)

playerGuess = int(input("Guess what the secret number is, from 1 to 9. Type 0 at any time to quit: "))

counter = 0

while playerGuess != 0:

    if randNum > playerGuess:
        counter += 1
        playerGuess = int(input("Too low, guess again! "))

    elif randNum < playerGuess:
        counter += 1
        playerGuess = int(input("Too high, guess again! "))

    else:
        counter += 1
        print("Nailed it!")
        print(f"Took you {counter} guesses!")
        randNum = random.randint(1,9)
        counter = 0
        playerGuess = int(input("Go another round! Guess what the secret number is, from 1 to 9. Type 0 at any time to quit: "))

print("Thanks for playing!")

# Exercise 10

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newList2 = []
result = []

if len(a) > len(b):
    newList2 = [item for item in b if item in a and item not in newList2]
    result = [item for item in newList2 if item in newList2 and item not in result]

if len(b) > len(a):
    newList2 = [item for item in a if item in b and item not in newList2]
    result = [item for item in newList2 if item in newList2 and item not in result]

print(result)
print("This one ain't workin quite yet.  Maybe circle back to it.")

# Exercise 11

num3 = int(input("Give me a number and we'll see if it's a prime: "))

list2 = range(1,num3 + 1)

divisorsList = [item for item in list2 if num3 % item == 0]

if len(divisorsList) > 2:
    print("This number is not prime.")
else:
    print("This number is prime!")