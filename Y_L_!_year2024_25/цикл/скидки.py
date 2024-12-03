price = float(input())
total = 0
while price > 0:
    if price > 1000:
        total += 0.95 * price
    else:
        total += price
    price = float(input())
print(total)