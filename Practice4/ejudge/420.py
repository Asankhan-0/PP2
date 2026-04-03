<<<<<<< HEAD
import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

it = iter(data)
m = int(next(it))

g = 0 
n = 0  

for i in range(m):
    scope = next(it)
    val = int(next(it))
    if scope == "global":
        g += val
    elif scope == "nonlocal":
        n += val

=======
import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

it = iter(data)
m = int(next(it))

g = 0 
n = 0  

for i in range(m):
    scope = next(it)
    val = int(next(it))
    if scope == "global":
        g += val
    elif scope == "nonlocal":
        n += val

>>>>>>> 2d4f5e0 (Lab4)
print(g, n)