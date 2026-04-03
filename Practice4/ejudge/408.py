<<<<<<< HEAD
def gen(n):
    for x in range(2, n + 1):
        for i in range(2, int(x**0.5) + 1):
            if x%i== 0:
                break
        else:
            yield x

n = int(input())
for num in gen(n):
=======
def gen(n):
    for x in range(2, n + 1):
        for i in range(2, int(x**0.5) + 1):
            if x%i== 0:
                break
        else:
            yield x

n = int(input())
for num in gen(n):
>>>>>>> 2d4f5e0 (Lab4)
    print(num, end=" ")