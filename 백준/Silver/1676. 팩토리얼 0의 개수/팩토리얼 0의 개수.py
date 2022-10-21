N = int(input())
result = 1
cnt = 0
for i in range(1, N+1):
    result *= i
result_2 = str(result)
for i in (range(len(result_2)-1, -1, -1)):
    if result_2[i] == '0':
        cnt += 1
    else:
        break
print(cnt)