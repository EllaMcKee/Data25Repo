class Car:

    def __init__(self, colour, max_speed, mileage, mot):
        self.current_speed = 0
        self.colour = colour
        self.max_speed = max_speed
        self.mileage = mileage
        self.mot = mot

    def accelerate(self, speed_to_accelerate):
        if self.current_speed + speed_to_accelerate > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed += speed_to_accelerate
        return self.current_speed

    def deceleration(self):
        return self.current_speed

    def horn(self):
        print("BEEP BEEEEP")


nascar = Car("Green", 1000, 0)
print(f"The car is currently going {nascar.current_speed} mph")

nascar.accelerate(200)
print(f"The car is currently going {nascar.current_speed} mph")

nascar.accelerate(500)
print(f"The car is currently going {nascar.current_speed} mph")

mot1 = nascar.mot(5000)
print(mot1)