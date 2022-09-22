import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    C, T = map(int,input().split())
    C_W = list(map(int, input().split()))
    C_W.sort(reverse=True)
    T_W = list(map(int, input().split()))
    T_W.sort(reverse=True)
    lst = []
    for i in T_W:
        for j in range(len(C_W)):
            if i >= C_W[j]:
                lst.append(C_W.pop(j))
                break
    print(f'#{tc} {sum(lst)}')

