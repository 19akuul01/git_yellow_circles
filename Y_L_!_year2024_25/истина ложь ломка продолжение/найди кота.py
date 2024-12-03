m = int(input())
flag = False
for i in range(m):
    s = input()
    if 'Кот' in s or 'кот' in s:
        fiag = True
        break
if fiag:
    print('МЯУ')
else:
    print('НЕТ')