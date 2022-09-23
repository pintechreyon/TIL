import sys
sys.stdin = open('input.txt')

def inorder(s1):
    s1 = int(s1)
    if s1:
        inorder(arr[s1][2])
        lst.append(arr[s1][1])
        inorder(arr[s1][3])

for tc in range(1, 11):
    N = int(input())
    lst = []
    arr = [list(input().split()) for _ in range(N)]
    arr.insert(0, [0, 0, 0, 0])
    for i in arr:
        while len(i) < 4:
            i.append(0)
    inorder(arr[1][0])
    print(f"#{tc} {''.join(lst)}")
