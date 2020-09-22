for t in range(10):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    tmp = []
    tmptmp = []
    for i in range(100):
        tmp.append(sum(arr[i]))

    for i in range(100):
        for j in range(100):
            tmptmp.append(arr[j][i])
            tmp.append(sum(tmptmp))
        tmptmp = []

    for i in range(100):
        tmptmp.append(arr[i][i])
        tmp.append(sum(tmptmp))
        tmptmp = []

    for i in range(100):
        tmptmp.append((arr[i][99-i]))
        tmp.append(sum(tmptmp))

    print('#{} {}'.format(n, max(tmp)))
