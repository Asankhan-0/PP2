<<<<<<< HEAD
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

r = int(input())

c = Circle(r)

=======
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

r = int(input())

c = Circle(r)

>>>>>>> 2d4f5e0 (Lab4)
print(f"{c.area():.2f}")