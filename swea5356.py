tc = int(input())
for t in range(1, tc+1):
    arr = []
    for i in range(5):
        arr.append(input())
    print('#{}'.format(t), end=" ")
    for i in range(15):
        for j in range(5):
            if len(arr[j]) > i:
                print(arr[j][i], end='')
    print()
