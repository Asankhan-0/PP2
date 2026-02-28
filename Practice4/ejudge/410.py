def gen(a, n):
    for i in range(n):
        for x in a:
            yield x

a = input().split()

n = int(input())
for i in gen(a, n):
    print(i, end=' ')
