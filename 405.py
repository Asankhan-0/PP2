def gen(b):
    for n in range(b, -1, -1):
        yield n

x = int(input())
for num in gen(x):
    print(num)