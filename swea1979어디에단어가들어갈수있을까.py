tc = int(input())
for t in range(1, tc+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0]
    dy = [0, 1]
    cnt = 0
    tmp = 0
    res = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                if tmp == K:
                    cnt += 1
                    tmp = 0
                else:
                    tmp = 0
                    x = j + dx[0]
            elif arr[i][j] == 1:
                tmp += 1
                x = j + dx[0]
        if tmp == K:
            cnt += 1
            tmp = 0
        else:
            tmp = 0

    for i in range(N):
        for j in range(N):
            if arr[j][i] == 0:
                if tmp == K:
                    cnt += 1
                    tmp = 0
                else:
                    tmp = 0
                    x = i + dx[0]
            elif arr[j][i] == 1:
                tmp += 1
                x = i + dx[0]
        if tmp == K:
            cnt += 1
            tmp = 0
        else:
            tmp = 0
    print('#{} {}'.format(t, cnt))
