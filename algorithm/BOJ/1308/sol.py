import sys
sys.stdin = open('input.txt')

A, B, C = map(int, input().split())
ans = 0
for i in range(C+1):
    ans = A//B
    A = A % B * 10
print(ans)
