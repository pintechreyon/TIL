T = int(input())
pat = [1,2,3,4,5,6,7,8,9]
for tc in range(1,1+T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(arr[i][j])
        lst.sort()
        if lst != pat:
            result = 0
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(arr[j][i])
        lst.sort()
        if lst != pat:
            result = 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            lst = []
            for k in range(i,i+3):
                for l in range(j, j + 3):
                    lst.append(arr[k][l])
            lst.sort()
            if lst != pat:
                result = 0
    print(f'#{tc} {result}')


