<<<<<<< HEAD
def gen(b):
    for n in range(b, -1, -1):
        yield n

x = int(input())
for num in gen(x):
=======
def gen(b):
    for n in range(b, -1, -1):
        yield n

x = int(input())
for num in gen(x):
>>>>>>> 2d4f5e0 (Lab4)
    print(num)