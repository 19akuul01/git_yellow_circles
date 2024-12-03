n = int(input())
cities = set()
for i in range(n):
    cite = input()
    cities.add(cite)
control_cite = input()
if control_cite not in cities:
    print('OK')
else:
    print('TRY ANOTHER')