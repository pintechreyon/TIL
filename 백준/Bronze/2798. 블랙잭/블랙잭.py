N, M = map(int, input().split())
arr = list(map(int,input().split()))
maxv = 0
var = 0
flag = False
arr. sort()
for i in range(N):
    if flag:
        break
    for j in range(N):
        if flag:
            break
        if i != j:
            for k in range(N):
                if i != k and j != k and arr[i]+arr[j]+arr[k] <= M:
                    var = arr[i] + arr[j] + arr[k]
                    if var > maxv:
                        maxv = var
                    elif var == M:
                        flag = True
                        break
                elif i != k and j != k and arr[i]+arr[j]+arr[k] > M:
                    break

print(maxv)