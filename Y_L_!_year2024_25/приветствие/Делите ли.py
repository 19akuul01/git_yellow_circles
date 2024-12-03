n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0 and n != i:
        count += 1
        print(i, end=' ')
    elif n % i == 0 and n == i:
        count += 1
        print(i, end='\n')
if count == 2:
    print('ПРОСТОЕ')
else:
    print('НЕТ')