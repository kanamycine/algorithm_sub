tc = int(input())
for t in range(1, tc+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    res = 1
    for y in range(9):
        x_sum, y_sum = 0, 0
        for x in range(9):
            x_sum += arr[y][x]
            y_sum += arr[x][y]

        if x_sum != 45 or y_sum != 45:
            res = 0
            break

    for y in range(3):
        for x in range(3):
            total = 0
            for dy in range(3):
                for dx in range(3):
                    total += arr[3*y+dy][3*x+dx]

            if total != 45:
                res = 0
                break

    print('#{} {}'.format(t, res))
