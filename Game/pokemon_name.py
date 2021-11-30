from pokemon_type import water_type
from pokemon_type import fire_type
from pokemon_type import grass_type


class pokemon_name(water_type):
    def __init__(self, water):
        super().__init__(self, water)

    def water_gun(self):
        print("Water Gun did 10 damage!")

    def rest(self):
        print("Squirtle rested and gained 10 health.")

    def scald(self):
        print("Scald did 25 damage!")

    def surf(self):
        print("Surf did 15 damage!")


class pokemon_name2(fire_type):
    def __init__(self,fire):
        super().__init__(self,fire)

    def flamethrower(self):
        print("Flamethrower did 10 damage!")

    def rest(self):
        print("Charmander rested and gained 10 health.")

    def fire_punch(self):
        print("Fire Punch did 25 damage!")

    def ember(self):
        print("Ember did 15 damage!")


class pokemon_name3(grass_type):
    def __init__(self, grass):
        super().__init__(self, grass)

    def razor_leaf(self):
        print("Razor Leaf did 10 damage!")

    def rest(self):
        print("Bulbasaur rested and gained 10 health.")

    def solar_beam(self):
        print("Solar Beam did 25 damage!")

    def poison_spore(self):
        print("Poison Spore did 15 damage! \nLuckily you're not poisoned")
