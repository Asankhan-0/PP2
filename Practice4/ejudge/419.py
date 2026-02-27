import math
nums = []
while len(nums) < 5:
    nums.extend(input().split())
r, x1, y1, x2, y2 = [float(x) for x in nums]
d1 = math.sqrt(x1**2 + y1**2)
d2 = math.sqrt(x2**2 + y2**2)
dist_ab = math.sqrt((x2-x1)**2 + (y2-y1)**2)

dot_prod = (x1*x2 + y1*y2) / (d1*d2)
gamma = math.acos(max(-1, min(1, dot_prod)))
alpha1 = math.acos(max(-1, min(1, r / d1)))
alpha2 = math.acos(max(-1, min(1, r / d2)))
if gamma > alpha1 + alpha2:
    t1 = math.sqrt(abs(d1**2 - r**2))
    t2 = math.sqrt(abs(d2**2 - r**2))
    arc_angle = gamma - alpha1 - alpha2
    arc_len = r * arc_angle
    
    print(f"{t1 + t2 + arc_len:.10f}")
else:
    print(f"{dist_ab:.10f}")