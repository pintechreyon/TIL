N, M = map(int, input().split())
arr = list(map(int, input().split()))
subsets = [[]]
cnt = 0
for num in arr:
  size = len(subsets)
  for y in range(size):
    subsets.append(subsets[y]+[num])
subsets.pop(0)
for i in range(len(subsets)):
    if sum(subsets[i]) == M:
        cnt += 1
print(cnt)