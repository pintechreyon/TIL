import sys
sys.stdin = open('input.txt')

def preorder(n):
    if n:
        lst.append(n)
        preorder(ch1[n])
        preorder(ch2[n])
    return lst

T = int(input())
for tc in range(1, T+1):
    lst = []
    E, H = map(int, input().split()) #정점 개수, 마지막 정점번호
    V = E + 1
    arr = list(map(int, input().split()))
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    par = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p
    var = preorder(H)
    print(f'#{tc} {len(var)}')