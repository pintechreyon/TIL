T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    target = []
    result = 0
    flag = False
    pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    for i in arr:
        if i == '0' * M:
            continue
        else:
            target = i
            break
    for i in range(M-56):
        if flag == True:
            break
        num = []
        for j in range(i, i+56, 7):
            if target[j:j+7] not in pattern:
                result = 0
                break
            else:
                num.append(pattern.index(target[j:j+7]))
        if len(num) == 8:
            for k in range(8):
                if k % 2 == 0:
                    result += num[k]*3
                else:
                    result += num[k]
            if result % 10 == 0:
                flag = True
                result = sum(num)
    print(f'#{tc} {result}')
