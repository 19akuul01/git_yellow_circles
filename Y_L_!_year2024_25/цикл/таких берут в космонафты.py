h = input()
max_, min_ = 0, 300
count = 0
while h != '!':
    if 150 <= int(h) <= 190:
        if int(h) > max_:
            max_ = int(h)
        if int(h) < min_:
            min_ = int(h)
        count += 1
    h = input()
print(count)
print(min_, max_)