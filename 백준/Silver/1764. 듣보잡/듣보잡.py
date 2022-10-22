import sys
N, M = map(int, input().split())
lst = set()
lst_2 = set()
for i in range(N):
    lst.add(sys.stdin.readline().rstrip())
for i in range(M):
    lst_2.add(sys.stdin.readline().rstrip())
result = sorted(list(lst&lst_2))
print(len(result))
for i in result:
    print(i)