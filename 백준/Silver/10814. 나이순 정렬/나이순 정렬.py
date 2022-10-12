import sys

N = int(input())
arr = []
for x, i in enumerate(range(N)):
    arr.append(sys.stdin.readline().split()+[x])
arr.sort(key=lambda j: (int(j[0]), j[2]))
for i in range(N):
    print(f'{arr[i][0]} {arr[i][1]}')