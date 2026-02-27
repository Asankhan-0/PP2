def gen(b):
    for n in range(1, b+1):
        yield n**2

b = int(input())
for sq in gen(b):
    print(sq)