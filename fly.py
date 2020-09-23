n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
tmp = 0
total = []
for i in range(n-k+1):
    for j in range(n-k+1):
        for o in range(k):
            for l in range(k):
                tmp += arr[i+o][j+l]
        total.append(tmp)
        tmp = 0

print(max(total))
