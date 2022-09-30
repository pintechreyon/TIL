N = input()
A = len(N)
N = int(N)
result = 0
if N > 20:
    for i in range(N-(A*10), N):
        cnt = 0
        for j in str(i):
            cnt += int(j)
        if i + cnt == N:
            result = i
            break
else:
    for i in range(0, N):
        cnt = 0
        for j in str(i):
            cnt += int(j)
        if i + cnt == N:
            result = i
            break
print(result)