import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
result = 0
for i in range(N):
    arr.append(int(input()))
for i in arr:
    cnt = 0
    if i in arr:
        cnt += 1
    if i+1 in arr:
        cnt += 1
    if i+2 in arr:
        cnt += 1
    if i+3 in arr:
        cnt += 1
    if i+4 in arr:
        cnt += 1
    if cnt > result:
        result = cnt
print(5-result)




