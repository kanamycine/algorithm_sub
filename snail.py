n = int(input())
num = [n for n in range(1, n**2 + 1)]
print(num)
arr = [[0]*n for i in range(n)]
print(arr)
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
d = 0
x, y = 0, 0

for i in range(n**2):
    arr[x][y] = num[i]
    x += dx[d]
    y += dy[d]
    if x < 0 or x > n-1 or y < 0 or y > n-1 or arr[x][y] != 0:
        x -= dx[d]
        y -= dy[d]
        d = (d+1) % 4
        x += dx[d]
        y += dy[d]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
