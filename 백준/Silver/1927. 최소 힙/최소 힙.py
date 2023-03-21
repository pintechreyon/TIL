import heapq
import sys
N = int(input())
arr = []
for i in range(N):
    M = int(sys.stdin.readline())
    if M == 0:
        if arr:
            result = heapq.heappop(arr)
            print(result)
        else:
            print(0)
    else:
        heapq.heappush(arr, M)