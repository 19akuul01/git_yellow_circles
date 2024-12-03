f = open('17.txt')
lst = (int(x) for x in f)
lst_ch = [x for x in lst if x % 2 == 0]
sr = sum(lst_ch) / len(lst_ch)
count, max_sum = 0, 0
for i in range(len(lst) - 1):
    if (lst[i] % 3 == 0 or lst[i + 1] % 3 == 0) and (lst[i] > sr or lst[i + 1] < sr):
        count += 1
        if lst[i] + lst[i + 1] > max_sum:
            max_sum = lst[i] + lst[i + 1]
print(count)
print(max_sum)