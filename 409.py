def gen(n):
    for i in range(n+1):
        yield 2**i

n = int(input())
for x in gen(n):
    print(x, end=" ")