N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
a_6 = []
a_1 = []
result = 0
for i in arr:
    a_6.append(i[0])
for i in arr:
    a_1.append(i[1])
var6 = min(a_6)
var1 = min(a_1)
if var6 <= var1 * 6:
    while N > 6:
        N -= 6
        result += var6
    if var6 <= N * var1:
        result += var6
    else:
        result += N * var1
else:
    result = var1 * N
print(result)