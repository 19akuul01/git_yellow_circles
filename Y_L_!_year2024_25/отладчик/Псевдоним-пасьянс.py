stone = int(input())
while stone != 0:
    n = int(input())
    if n > 3 or n < 1 or n > stone:
        print(stone)
    else:
        stone -= n
        print(stone)