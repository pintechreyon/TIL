T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(input())
    num = N // 4
    var = []
    result = []
    for i in range(num):
        l_1 = ''.join(arr[0:num])
        l_2 = ''.join(arr[num:num*2])
        l_3 = ''.join(arr[num*2:num*3])
        l_4 = ''.join(arr[num*3:num*4])
        var.append(l_1)
        var.append(l_2)
        var.append(l_3)
        var.append(l_4)
        arr.append(arr.pop(0))
    s_var = set(var)
    l_var = list(s_var)
    for i in l_var:
        result.append(int(i, 16))
    result.sort(reverse=True)
    print(f'#{tc} {result[M-1]}')