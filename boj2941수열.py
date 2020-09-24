n = int(input())
lst = list(map(int, input().split()))
cnta = 1
cnts = 1
maxlen = 1
for i in range(len(lst)-1):
    if lst[i] <= lst[i+1]:
        cnta += 1
    else:
        cnta = 1
    if cnta > maxlen:
        maxlen = cnta

cnt = 1
for i in range(len(lst)-1):
    if lst[i] >= lst[i+1]:
        cnts += 1
    else:
        cnts = 1

    if cnts > maxlen:
        maxlen = cnts
print(maxlen)
