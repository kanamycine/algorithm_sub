for t in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    tmp = []
    cnt = 0
    for i in range(2, len(lst)-2):
        if lst[i] > lst[i-2] and lst[i] > lst[i-1] and lst[i] > lst[i+1] and lst[i] > lst[i+2]:
            cnt += lst[i] - max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
    print(cnt)
