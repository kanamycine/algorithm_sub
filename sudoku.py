arr = [list(map(int, input().split())) for _ in range(9)]
tmp = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                tmp += arr[3*i+k][3*j+l]
        print(tmp)
        tmp = 0
