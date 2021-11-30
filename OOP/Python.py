from Snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.twolungs = True
        self.venom = False


peter = Python()
patty = Python()
patty.venom = True
print(f"Peter is venomous: {peter.venom}")
print(f"Patty is venomous: {patty.venom}")
