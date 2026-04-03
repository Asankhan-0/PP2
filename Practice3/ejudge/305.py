<<<<<<< HEAD
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

n = int(input())
sq = Square(n)
=======
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

n = int(input())
sq = Square(n)
>>>>>>> 2d4f5e0 (Lab4)
print(sq.area())