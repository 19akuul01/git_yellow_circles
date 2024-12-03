s = input()
count = 1
flag = False
while s != 'СТОП':
    if 'Кот' in s or 'кот' in s:
        flag = True
        break
    count += 1
    s = input()
if flag:
    print(count)
else:
    print(-1)
