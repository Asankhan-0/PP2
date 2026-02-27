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
