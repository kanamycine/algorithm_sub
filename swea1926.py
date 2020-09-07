n = int(input())
res = []
result = ''
for i in range(1, n+1):
    res.append(str(i))
for j in res:
    if '3' in j or '6' in j or '9' in j:
        length = len(j)
        cnt = 0
        for k in range(length):
            if j[k] == '3' or j[k] == '6' or j[k] == '9':
                cnt += 1
        for l in range(cnt):
            result += '-'
        result += ' '
    else:
        result += j + ' '

print(result)
