import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    lst = []
    flag = True
    result = 0
    for i in range(0, len(arr), 2):
        lst.append([arr[i], arr[i+1]])
    while flag:
        next = False
        for i in range(len(lst)):
            if next:
                break
            for j in range(len(lst)):
                if i != j:
                    if lst[j][0] in lst[i] or lst[j][1] in lst[i]:
                        lst[i] = lst[i] + lst[j]
                        next = True
                        lst.pop(j)
                        break

        else:
            flag = False
    for i in range(1, N+1):
        if i not in arr:
            result += 1
    print(f'#{tc} {len(lst) + result}')


