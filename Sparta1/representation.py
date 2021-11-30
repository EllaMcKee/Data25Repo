# How to represent an object.
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    # Value of the object instead of its location.
    def __repr__(self):
        return f"Location = ({self.latitude}, {self.longitude})"

    # Default representation when printing.
    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


bham_academy = Location(52.488647, -1.887249)
print(bham_academy)
repr(bham_academy)
