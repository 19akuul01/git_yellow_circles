n = float(input())
if n < 0.000001 and n > -0.000001:
    print(1000000)
else:
    print(1 / n)