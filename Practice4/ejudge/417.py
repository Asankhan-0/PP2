import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

A = dx*dx + dy*dy
B = 2*(x1*dx + y1*dy)
C = x1*x1 + y1*y1 - R*R

D = B*B - 4*A*C

if D < 0:
    print("0.0000000000")
else:
    sqrtD = math.sqrt(D)
    t1 = (-B - sqrtD) / (2*A)
    t2 = (-B + sqrtD) / (2*A)
    t_low = max(0, min(t1, t2))
    t_high = min(1, max(t1, t2))
    if t_low > t_high:
        print("0.0000000000")
    else:
        length = math.hypot(dx, dy) * (t_high - t_low)
        print(f"{length:.10f}")