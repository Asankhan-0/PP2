import json

strin = input()
data = json.loads(strin)
n = int(input())

for i in range(n):
    q = input()
    q = q.replace('[', '.').replace(']', '').strip('.')
    parts = q.split('.')
    
    curr = data
    ok = True
    
    for p in parts:
        if type(curr) == dict and p in curr:
            curr = curr[p]
        elif type(curr) == list and p.isdigit():
            idx = int(p)
            if 0 <= idx < len(curr):
                curr = curr[idx]
            else:
                ok = False
                break
        else:
            ok = False
            break
            
    if ok:
        print(json.dumps(curr, separators=(',', ':')))
    else:
        print("NOT_FOUND")