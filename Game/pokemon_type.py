from pokemon import pokemon

class water_type(pokemon):

    def __init__(self, alive, water):
        super().__init__(alive)
        self.water = water

    def swim(self):
        print("This type can swim")

class fire_type(pokemon):
    def __init__(self, alive, fire):
        super().__init__(alive)
        self.fire = fire

    def lava(self):
        print("This type can walk on lava")#

    def function(self):
        print("stuff")

class grass_type(pokemon):
    def __init__(self, alive, grass):
        super().__init__(alive)
        self.grass = grass

    def grow(self):
        print("These pokemon like sunshine")