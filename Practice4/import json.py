<<<<<<< HEAD
import json

with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 87)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("=" * 87)
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']

    dn = attributes['dn']
    descr = attributes.get('descr', '')
    speed = attributes['speed']
    mtu = attributes['mtu']
=======
import json

with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 87)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("=" * 87)
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']

    dn = attributes['dn']
    descr = attributes.get('descr', '')
    speed = attributes['speed']
    mtu = attributes['mtu']
>>>>>>> 2d4f5e0 (Lab4)
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")