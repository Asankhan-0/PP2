for i in gen(a, n):
    print(i, end=" ")


    import json
def f(a, b):
    for k, v in b.items():
        if v is None:
            a.pop(k, None)
        elif isinstance(v, dict) and isinstance(a.get(k), dict):
            f(a[k], v)
        else:
            a[k]=v
    return a

a=json.loads(input())
b= json.loads(input())
print(json.dumps(f(a, b), separators=(',', ':'), sort_keys=True))