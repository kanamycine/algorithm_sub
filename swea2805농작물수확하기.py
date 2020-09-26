'''
1
5
14054
44250
02032
51204
52212
'''
tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    mid = n//2
    s = mid
    e = mid
    total = 0

    for i in range(n):
        for j in range(s, e+1, 1):
            total += arr[i][j]

        if i < mid:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print('#{} {}'.format(t, total))
    #
