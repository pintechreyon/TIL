import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
lst = [1, 2, 3, 4, 5, 4, 3, 2]
result = 0
cnt = 0

if N == 2 or N == 3 or N == 4:
    if M % 2 == 1:
        result = M // 2 * 8
        M = 1
    if M % 2 == 0:
        result = M // 2 * 8
        M = 0
if N == 1 or N == 5:
    result = M * 8
    M = 0
if M == 1:
    for i in lst:
        if N == i:
            result += 1
            cnt += 1
        else:
            result += 1
        if cnt == 2:
            break

if M == 0:
    for i in lst:
        if N == i:
            result += 1
            cnt += 1
        if cnt == 1:
            break
        result += 1

result -= 1
print(result)
