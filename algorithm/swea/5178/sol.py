import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    V, L, R = map(int, input().split())
    tree = [0] * (V+1)
    for i in range(L):
        idx, num = map(int, input().split())
        tree[idx] = num
    if V % 2 == 1:
        for i in range(L-1, 0, -1):
                tree[i] = tree[i * 2] + tree[i * 2 + 1]
    else:
        for i in range(L, 0, -1):
            if i == V / 2:
                tree[i] = tree[V]
            else:
                tree[i] = tree[i * 2] + tree[i * 2 + 1]
    #for i in range(V, 1, -1):
        # tree[i//2] += tree[i]
    print(f'#{tc} {tree[R]}')
