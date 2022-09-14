import sys
sys.stdin = open('input.txt')

def inorder(n):
    node = int(n)
    if node:
        inorder(arr[node][2])
        print(arr[node][1], end='')
        inorder(arr[node][3])

for tc in range(1, 11):
    V = int(input()) #정점 개수, 마지막 정점번호
    arr = [input().split() for i in range(V)]
    arr.insert(0, [0,0,0,0])
    for i in arr:
        while len(i) != 4:
            i.append('0')
    print(f'#{tc}', end=' ')
    inorder(arr[1][0])
    print()
