<<<<<<< HEAD
def gen(b):
    for n in range(1, b+1):
        yield n**2

b = int(input())
for sq in gen(b):
=======
def gen(b):
    for n in range(1, b+1):
        yield n**2

b = int(input())
for sq in gen(b):
>>>>>>> 2d4f5e0 (Lab4)
    print(sq)