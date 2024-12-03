n = int(input())
aifet = 'ABCDEFGHR'
for i in range(n):
    for t in range(n):
        print(aifet[t] + str(n - i), end=' ')
    print()