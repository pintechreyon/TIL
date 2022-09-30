N, M = map(int, input().split())
divide = []
double = []
mini = 0
maxi = 0
for i in range(1, N+1):
    if N % i == 0:
        divide.append(i)

for i in range(M, 0, -1):
    if M % i == 0:
        if i in divide:
            maxi = i
            break

for i in range(1, M+1):
    double.append(N*i)

for i in range(1, N+1):
    if M*i in double:
        mini = M * i
        break
print(maxi, mini)
