import json

def diff(a, b, path=""):
    res = []
    keys = set(a.keys()) | set(b.keys())
    for k in keys:
        pa = f"{path}.{k}" if path else k
        va = a.get(k, "<missing>")
        vb = b.get(k, "<missing>")
        if isinstance(va, dict) and isinstance(vb, dict):
            res.extend(diff(va, vb, pa))
        elif va != vb:
            v1 = json.dumps(va, separators=(',', ':')) if va != "<missing>" else "<missing>"
            v2 = json.dumps(vb, separators=(',', ':')) if vb != "<missing>" else "<missing>"
            res.append(f"{pa} : {v1} -> {v2}")
    return res

a = json.loads(input())
b = json.loads(input())
res = diff(a, b)
if res:
    for line in sorted(res):
        print(line)
else:
    print("No differences")