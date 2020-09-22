for t in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    for _ in range(n):
        lst[lst.index(max(lst))] -= 1
        lst[lst.index(min(lst))] += 1
    res = max(lst) - min(lst)

    print('#{} {}'.format(t, res))
