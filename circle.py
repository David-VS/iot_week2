import math as m

class Circle:

    radius = 1

    def __init__(self, radius):
        self.radius = radius

    #-> expliciet een return type meegeven
    def __str__(self) -> str:
        return "de straal is: " + str(self.radius)

    def omtrek(self):
        return 2 * m.pi * self.radius

    def oppervlakte(self):
        return m.pi * (self.radius ** 2)