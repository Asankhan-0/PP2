<<<<<<< HEAD
def gen(n):
    for i in range(n+1):
        yield 2**i

n = int(input())
for x in gen(n):
=======
def gen(n):
    for i in range(n+1):
        yield 2**i

n = int(input())
for x in gen(n):
>>>>>>> 2d4f5e0 (Lab4)
    print(x, end=" ")