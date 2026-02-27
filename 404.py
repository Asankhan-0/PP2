def squires(a, b):
    for n in range(a, b + 1):
        yield n**2

x = input().split()
a = int(x[0])
b = int(x[1])
for num in squires(a, b):
    print(num)