import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
     N, M = map(int, input().split())
     arr = list(map(int, input().split()))
     arr.sort(reverse=True)
     result = 0
     for i in range(M):
         result += arr[i]
     print(f'#{tc} {result}')