n = int(input())
f1, f2 = 1, 1
s = f1 + f2
print(f1)
print(f2)
while s <= n:
    print(s)
    f1 = f2
    f2 = s
    s = f1 + f2