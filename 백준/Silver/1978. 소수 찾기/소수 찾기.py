import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in arr:
    if i == 1:
        continue
    else:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            cnt += 1
print(cnt)




