from Reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = False
        self.limbs = False

    def hiss(self):
        print("Hisssssssssssss")

    def slither(self):
        print("Slither slither")


sidney = Snake()
print(sidney.cold_blooded)
sidney.hiss()
sidney.slither()
