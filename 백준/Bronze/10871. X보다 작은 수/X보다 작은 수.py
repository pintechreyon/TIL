N, M = map(int, input().split())
arr = list(map(int, input().split()))
lst = []
for i in arr:
    if i < M:
        lst.append(i)
print(*lst)