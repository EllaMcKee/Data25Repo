import random

random_number = random.randint(1, 100)
active = True
print("Guess a number between 1 and 100.")

while active:
    guess = int(input())
    if guess == random_number:
        print("You guessed correctly!")
        print("The number was {}.".format(random_number))
        active = False
    elif guess < random_number:
        print("Too low, guess again")
    else:
        print("Too high, guess again")

