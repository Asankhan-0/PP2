<<<<<<< HEAD
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        
        self.index = self.index - 1
        return self.data[self.index]
        
s = str(input())
rev = Reverse(s)
iter(rev)
for char in rev:
=======
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        
        self.index = self.index - 1
        return self.data[self.index]
        
s = str(input())
rev = Reverse(s)
iter(rev)
for char in rev:
>>>>>>> 2d4f5e0 (Lab4)
    print(char, end="")