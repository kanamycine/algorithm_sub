lst = list(map(int, input().split()))
result = 0
maxHeight = 0
for i in range(len(lst)):
    # i번째 최대 낙차값은 len(arr)
    maxHeight = len(lst) - (i+1)
    for j in range(i+1, len(lst)):
        if lst[i] <= lst[j]:
            maxHeight -= 1

    if result < maxHeight:
        result = maxHeight
print(result)
