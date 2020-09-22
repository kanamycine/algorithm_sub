tc = int(input())
for t in range(1, tc+1):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    result = []
    for i in range(M-N+1):
        for j in range(M-N+1):
            total = 0
            for k in range(N):
                total += sum(arr[i+k][j:j+M])
                result.append(total)

    res = max(result)
    print('#{} {}'.format(t, res))
