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