# ----------------- EXERCISE 1 ----------------- #

name = input("Enter your name. ---> ")
age = int(input("Enter your age. ---> "))

hundred = 100 - age
year = 2021 + hundred

print(f"You will turn 100 in {year}.")

times = int(input("Enter another number. ---> "))

count = 0
while count < times:
    print(f"You will turn 100 in {year}.")
    count += 1

# ----------------- EXERCISE 2 ----------------- #

number = int(input("Hey, give me a number. ---> "))

if number % 4 == 0:
    print("This number is a multiple of 4.")
elif number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")

num1 = int(input("Give me a number to check. ---> "))
num2 = int(input("Give me a number to divide that by. ---> "))

if num1 % num2 == 0:
    print(f"Woah, {num1} divides evenly into {num2}!")
else:
    print(f"No, {num1} doesn't divide evenly into {num2}.")

# ----------------- EXERCISE 3 ----------------- #

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = []

limit = int(input("Input a number. ---> "))

for number in list1:
    if number < limit:
        list2.append(number)

print(f"These are all the numbers smaller than yours: {list2}")

# ----------------- EXERCISE 4 ----------------- #

number = int(input("Input a number. ---> "))
divisors = []

for i in range(2, number):
    if number % i == 0:
        divisors.append(i)
print(divisors)

# ----------------- EXERCISE 5 ----------------- #

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print(common)

# ----------------- EXERCISE 6 ----------------- #

phrase = input("Hey, gimme a string. ---> ")
backward = ''

for letter in range(len(phrase)):
    index = len(phrase) - 1 - letter
    backward += phrase[index]
print(backward)

if phrase == backward:
    print("This is a palindrome!")
else:
    print("This is not a palindrome.")

# ----------------- EXERCISE 7 ----------------- #

list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list2 = []

for i in list1:
    if i % 2 == 0:
        list2.append(i)

print(list2)

# ----------------- EXERCISE 8 ----------------- #

print("Welcome to Rock Paper Scissors!")

game = True
while game:
    first_player = (input("First player, pick! ---> ")).lower()
    second_player = (input("Second player, pick! ---> ")).lower()
    if first_player == second_player:
        print("It's a draw!!")
    elif first_player == "rock":
        if second_player == "paper":
            print("Paper beats rock!")
            print("Second player wins!")
        elif second_player == "scissors":
            print("Rock beats scissors!")
            print("First player wins!")
    elif first_player == "paper":
        if second_player == "rock":
            print("Paper beats rock!")
            print("First player wins!")
        elif second_player == "scissors":
            print("Scissors beat paper!")
            print("Second player wins!")
    elif first_player == "scissors":
        if second_player == "paper":
            print("Scissors beat paper!")
            print("First player wins!")
        elif second_player == "rock":
            print("Rock beats scissors!")
            print("Second player wins!")
    play_again = input("Play again? Y/N ---> ").upper()
    if play_again != "Y":
        game = False
        break
