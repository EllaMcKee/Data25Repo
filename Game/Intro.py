import time
from pprint import pprint
from random import *
from pokemon_name import *
from pygame import mixer

# ------------------ INTRO BEGINS ------------------ #


intro = True
starters = ["charmander", "squirtle", "bulbasaur"]

while intro:

    print("Welcome to the world of Pokemon!")
    time.sleep(2)
    print("Are you a girl... or a boy?")
    time.sleep(2)
    print("Or neither, or both?")
    time.sleep(2)
    print("This is 2021, after all.")
    time.sleep(2)
    gender = input("What is your gender? ----> ")
    print("Great!")
    time.sleep(2)
    print("Let's get you a starter pokemon.")
    time.sleep(2)
    pprint(starters)
    starter = input("Which do you want? ----> ")
    while starter.lower() not in starters:
        print("Oops, that's not a starter Pokemon. Try again.")
        starter = input("Which do you want? ----> ")
    time.sleep(2)
    print(f"Amazing! {starter} is a truly wonderful Pokemon.")

    # Code to instantiate the selected starter.
    starter = starter.lower()
    if starter == "charmander":
        charmander = pokemon_name2("Fire")
    elif starter == "squirtle":
        squirtle = pokemon_name("Water")
    elif starter == "bulbasaur":
        bulbasaur = pokemon_name3("Grass")

    time.sleep(2)
    print(f"Okay, now let's do a practise battle with your {starter}.")
    time.sleep(2)
    intro = False

# ------------------ BATTLE BEGINS ------------------ #

battle = True

while battle:

    print("You're about to enter your first battle!")
    time.sleep(2)
    opposing_squirtle = pokemon_name("Water")
    print("You're up against the opposing Squirtle.")
    pokemon_health = 100
    opponent_health = 100
    pokemon_max_health = 100
    opponent_max_health = 100

    while opponent_health > 0 and pokemon_health > 0:
        print("What move will you use?")
        time.sleep(2)
        if starter == "charmander":
            print("1 = Flamethrower // 2 = Rest // 3 = Fire Punch // 4 = Ember")
        elif starter == "squirtle":
            print("1 = Water Gun // 2 = Rest // 3 = Scald // 4 = Surf")
        elif starter == "bulbasaur":
            print("1 = Razor Leaf // 2 = Rest // 3 = Solar Beam // 4 = Poison Spore")
        attack_option = input(" ----> ")
        attack_option = int(attack_option)
        if attack_option == 1:
            if starter == "charmander":
                charmander.flamethrower()
            elif starter == "squirtle":
                squirtle.water_gun()
            elif starter == "bulbasaur":
                bulbasaur.razor_leaf()
            time.sleep(2)
            opponent_health -= 10
        elif attack_option == 4:
            if starter == "charmander":
                charmander.ember()
            elif starter == "squirtle":
                squirtle.surf()
            elif starter == "bulbasaur":
                bulbasaur.poison_spore()
            time.sleep(2)
            opponent_health -= 15
        elif attack_option == 3:
            if starter == "charmander":
                charmander.fire_punch()
            elif starter == "squirtle":
                squirtle.scald()
            elif starter == "bulbasaur":
                bulbasaur.solar_beam()
            time.sleep(2)
            opponent_health -= 25
        elif attack_option == 2:
            if starter == "charmander":
                charmander.rest()
            elif starter == "squirtle":
                squirtle.rest()
            elif starter == "bulbasaur":
                bulbasaur.rest()
            if pokemon_health < pokemon_max_health:
                pokemon_health += 10
            elif pokemon_health == pokemon_max_health:
                pokemon_health = 100
            time.sleep(2)
        else:
            print("You missed your turn, input correctly next turn")

        print("---------------------------------------------")

        if opponent_health <= 0:
            time.sleep(2)
            print("You Won!")
            time.sleep(2)
            print("You received $1000 for winning.")
            time.sleep(2)
            break

        pick_number = randint(1, 4)
        for num in [pick_number]:
            if num == 1:
                opposing_squirtle.water_gun()
                pokemon_health -= 10
            elif num == 4:
                opposing_squirtle.surf()
                pokemon_health -= 15
            elif num == 3:
                opposing_squirtle.scald()
                pokemon_health -= 25
            else:
                opposing_squirtle.rest()
                if opponent_health < opponent_max_health:
                    opponent_health += 10
                elif opponent_health == pokemon_max_health:
                    opponent_health = 100
            time.sleep(2)
            if pokemon_health <= 0:
                pokemon_health = 0
                print(f"{starter} health is 0!")
                print(f"{starter} fainted.")
            else:
                print(f"{starter} health is: {pokemon_health}")

        print(f"Your {starter}'s health is: {pokemon_health}")
        print(f"Opponent health is: {opponent_health}")

        print("---------------------------------------------")

        time.sleep(2)
        if pokemon_health <= 0:
            print("You Lose! Better luck next time")
            battle = False
        elif opponent_health > 0 or pokemon_health > 0:
            print("Game isn't over, your turn")

    battle = False

# ------------------ BATTLE ENDS ------------------ #
