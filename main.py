import csv
import sys

creatures = {}
order = []

# Read input lines
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('; ')
    if len(parts) != 3:
        continue
    creature, habitat, stealth_str = parts
    stealth = int(stealth_str)
    if creature not in creatures:
        power = len(habitat) * (stealth // 2)
        creatures[creature] = {
            'no': len(creatures) + 1,
            'creature': creature,
            'habitat': habitat,
            'stealth': stealth,
            'power': power
        }
        order.append(creature)

# Write to fairytale.csv
with open('fairytale.csv', 'w', newline='') as csvfile:
    fieldnames = ['no', 'creature', 'habitat', 'stealth', 'power']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for creature in order:
        writer.writerow(creatures[creature])