<<<<<<< HEAD
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input())
fibgen = fib()
flist = []
for i in range(n):
    number = next(fibgen)
    flist.append(str(number))
result = ",".join(flist)
print(result)
=======
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input())
fibgen = fib()
flist = []
for i in range(n):
    number = next(fibgen)
    flist.append(str(number))
result = ",".join(flist)
print(result)
>>>>>>> 2d4f5e0 (Lab4)
