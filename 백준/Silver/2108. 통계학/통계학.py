import sys

N = int(input())
arr = []
cnt = 0
num = 0
C = 0
lst = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

A = round(sum(arr)/len(arr))
B = arr[len(arr)//2]
C=[0]*8001
for i in arr:
    C[i+4000] += 1
t = max(C)
max_v = (C.index(t), t)
C[max_v[0]] = 0
t = max(C)
max_v2 = (C.index(t), t)
if max_v[1] == max_v2[1]:
    C = max_v2[0]-4000
else:
    C = max_v[0]-4000
D = arr[-1] - arr[0]
print(A)
print(B)
print(C)
print(D)