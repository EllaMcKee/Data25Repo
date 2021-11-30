from Animal import Animal


class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.scaly = True
        self.eggs = "Yes"

    def __seek_heat(self):
        print("It's chilly, where's the sun?")

    def use_venom(self):
        print("Ptoo! Get spiked")

    def attract_through_scent(self):
        print("Heyyy I smell good")


