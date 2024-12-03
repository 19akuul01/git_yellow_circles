n = int(input())
while n > 0:
    ost = n % 8
    n //= 8
    print(ost)