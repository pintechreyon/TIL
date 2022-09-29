import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    V = int(input())
    arr = list(map(int, input().split()))
    arr = [0] + arr
    tree = [0] * (V + 1)
    result = 0
    for a, i in enumerate(arr):
        tree[a] = i
        while True:
            if tree[a] < tree[a//2]:
                tree[a], tree[a//2] = tree[a//2], tree[a]
                a = a//2
            else:
                break
    while V > 1:
        V = V//2
        result += tree[V]
    print(f'#{tc} {result}')
