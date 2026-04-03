<<<<<<< HEAD
def gen(b):
    for n in range(0, b + 1):
        if n%12 == 0:
            yield n

b= int(input())
for num in gen(b):
=======
def gen(b):
    for n in range(0, b + 1):
        if n%12 == 0:
            yield n

b= int(input())
for num in gen(b):
>>>>>>> 2d4f5e0 (Lab4)
    print(num, end=" ")