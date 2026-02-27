def gen(b):
    for n in range(0, b + 1, 2):
        yield n

b= int(input())
numbers = []
for n in gen(b):
    numbers.append(str(n))
res= ",".join(numbers)       
print(res) 