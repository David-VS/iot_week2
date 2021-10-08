class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def surface(self):
        return self.height * self.width

class Room:

    def __init__(self):
        self.walls = []

    def add_wall(self, wall):
        self.walls.append(wall)

    def total_surface(self):
        total = 0
        for w in self.walls:
            total += w.surface()
        return total

    def rolls_needed(self):
        roll_surface = 50
        if self.total_surface() % roll_surface == 0:
            return self.total_surface() / roll_surface
        else:
            return self.total_surface() // roll_surface + 1