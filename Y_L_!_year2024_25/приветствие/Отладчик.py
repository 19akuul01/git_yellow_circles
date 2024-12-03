def min_time_to_paint_fence(n, m, cans):
    total_paintable = sum(cans)
    if total_paintable < n:
        return "У Егору не хватит краски"

    time = 0
    boards_painted = 0

    time += 1
    while boards_painted < n:
        for i in range(m):
            if cans[i] > 0:
                cans[i] -= 1
                boards_painted += 1
                time += 1
                break

        if boards_painted < n:
            time += 1

    return time

n = int(input())
m = int(input())
cans = [int(input()) for _ in range(m)]

print(min_time_to_paint_fence(n, m, cans))
