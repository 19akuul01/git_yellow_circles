s = 0
n = int(input())
count = 1
while n != 0:
    s += n
    if s == 10:
        break
    n = int(input())
    count += 1
print(count)