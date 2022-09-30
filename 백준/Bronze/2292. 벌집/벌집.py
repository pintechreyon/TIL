N = int(input())
num = 0
cnt = 0
while num < N:
    if num == 0:
        num += 1
    else:
        num += 6 * cnt
    cnt += 1
print(cnt)