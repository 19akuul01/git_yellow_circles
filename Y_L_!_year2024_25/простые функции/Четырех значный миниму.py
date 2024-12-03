n = int(input())
d = n % 10
c = n % 100 // 10
b = n % 1000 // 100
a = n // 1000
if a > b:
    pass
else:
    a, b = b, a

print(d)
print(c)
print(b)
print(a)