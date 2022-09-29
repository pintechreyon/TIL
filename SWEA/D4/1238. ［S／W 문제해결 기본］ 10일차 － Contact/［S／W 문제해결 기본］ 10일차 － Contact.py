for tc in range(1, 11):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = []
    result = 0
    for i in range(0, N, 2):
        lst.append([arr[i], arr[i+1]])
    lst.insert(0, [0, 0])
    var = [0] * 101
    var[M] = 1
    for i in range(N//2):
        for i in lst:
            if var[i[0]] > 0 and var[i[1]] == 0:
                var[i[1]] = var[i[0]] + 1
    max_num = max(var)
    for i in range(len(var)-1, 0, -1):
        if var[i] == max_num:
            result = i
            break
    print(f'#{tc} {result}')