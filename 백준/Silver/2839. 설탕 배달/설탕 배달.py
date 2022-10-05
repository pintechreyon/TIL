N = int(input())
result = 0
K = 0
while True:
    num = N - K * 3
    if num % 5 == 0:
        result = K + num // 5
        break
    if num < 0:
        result = -1
        break
    K += 1
print(result)