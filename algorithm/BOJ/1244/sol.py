import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
H = int(input())
MW = [list(map(int, input().split())) for _ in range(H)]
for i in MW:
    if i[0] == 1:
        for j in range(1,N+1):
            if j % i[1] == 0:
                if arr[j-1] == 0:
                    arr[j - 1] = 1
                else:
                    arr[j - 1] = 0
    elif i[0] == 2:
        var = 1
        if arr[i[1]-1] == 0:
            arr[i[1] - 1] = 1
        else:
            arr[i[1] - 1] = 0
        while True:
            if i[1] - 1 - var >= 0 and i[1] - 1 + var <= N-1:
                if arr[i[1] - 1 - var] == arr[i[1] - 1 + var]:
                    if arr[i[1] - 1 - var]  == 0:
                        arr[i[1] - 1 - var] = 1
                        arr[i[1] - 1 + var] = 1
                    elif arr[i[1] - 1 - var]  == 1:
                        arr[i[1] - 1 - var] = 0
                        arr[i[1] - 1 + var] = 0
                    var += 1
                else:
                    break
            else:
                break
for i in range(N):
    if 0 < i and i % 20 == 0:
        print()
    print(arr[i], end=' ')


