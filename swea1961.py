t = int(input())
for tc in range(1, t+1):
    n = int(input())
    res = ''
    arr = [list(map(int, input().split())) for _ in range(n)]
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(arr[n-j-1][i], end="")
        print('', end=' ')
        for k in range(n):
            print(arr[n-i-1][n-k-1], end="")
        print('', end=' ')
        for l in range(n):
            print(arr[l][n-i-1], end="")
        print()
