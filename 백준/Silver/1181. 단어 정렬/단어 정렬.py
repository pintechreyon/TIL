N = int(input())
lst = []
result = []
for i in range(N):
    lst.append(input())
lst = list(set(lst))
lst.sort()
lst.sort(key=len)
for i in lst:
    print(i)