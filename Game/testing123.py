from random import *
from pokemon_name import *

charmander = pokemon_name2("Fire")
squirtle = pokemon_name("Water")

battle = True
while battle:
    print("You're about to enter your first battle")
    print("You're up against Squirtle")
    # Attack or rest option
    pokemon_health = 100
    opponent_health = 100
    pokemon_max_health = 100
    opponent_max_health = 100
    while opponent_health > 0 and pokemon_health > 0:
        attack_option = input("Input 1,2,3 or 4:-")
        attack_option = int(attack_option)
        if attack_option == 1:

            charmander.flamethrower()
            opponent_health -= 10
            print(f"Opponent_health {opponent_health}")
        elif attack_option == 4:
            charmander.ember()
            opponent_health -= 15
            print(f"Opponent_health {opponent_health}")
        elif attack_option == 3:
            charmander.fire_punch()
            opponent_health -= 25
            print(f"Opponent_health {opponent_health}")
        elif attack_option == 2:
            charmander.rest()
            if pokemon_health < pokemon_max_health:
                pokemon_health += 10
            elif pokemon_health == pokemon_max_health:
                pokemon_health = 100
            print(f"Pokemon health is: {pokemon_health}")
        else:
            print("You missed your turn, input correctly next turn")

        print("---------------------------------------------")

        if opponent_health <= 0:
            print("You won")
            break

        pick_number = randint(1, 4)
        for num in [pick_number]:
            if num == 1:
                squirtle.water_gun()
                pokemon_health -= 10
                print(f"pokemon health is now {pokemon_health}")
            elif num == 4:
                squirtle.surf()
                pokemon_health -= 15
                print(f"pokemon health is now {pokemon_health}")
            elif num == 3:
                squirtle.scald()
                pokemon_health -= 25
                print(f"pokemon health is now {pokemon_health}")
            else:
                squirtle.rest()
                if opponent_health < opponent_max_health:
                    opponent_health += 10
                elif opponent_health == pokemon_max_health:
                    opponent_health = 100
                    print(f"Opponent pokemon health is: {opponent_health},pokemon health is still {pokemon_health}")

        if pokemon_health <= 0:
            print("Better luck next you lost")
            battle = False
        elif opponent_health > 0 or pokemon_health > 0:
            print("Game isn't over, your turn")
    battle = False
