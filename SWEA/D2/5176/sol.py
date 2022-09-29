import sys
sys.stdin = open('input.txt')

def inorder(n):
    global cnt
    if n <= V:
        inorder(n*2)
        arr[n] = cnt
        cnt += 1
        inorder(n*2+1)
    else:
        return

T = int(input())
for tc in range(1, T+1):
    V = int(input()) #정점 개수, 마지막 정점번호
    arr = [0] * (V + 1)
    cnt = 1
    inorder(1)
    print(f'#{tc} {arr[1]} {arr[V//2]}')
