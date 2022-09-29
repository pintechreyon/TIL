
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    var = 0
    maxv = 0
    for i in range(N):
        for j in range(N):
            var = arr[i]*arr[j]
            if i < j:
                for k in range(len(str(var))-1):
                    if len(str(var)) == 1:
                        break
                    elif str(var)[k] > str(var)[k+1]:
                        break
                    elif k == len(str(var))-2:
                        if maxv < var:
                            maxv = var
    if maxv == 0:
        maxv = -1
    print(f'#{tc} {maxv}')


