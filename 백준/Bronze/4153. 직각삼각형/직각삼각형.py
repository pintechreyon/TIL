import sys
def fita(a, b, c):
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')

arr = []
while True:
    A = sorted(list(map(int, sys.stdin.readline().split())))
    if A == [0, 0, 0]:
        break
    arr.append(A)
for i in arr:
    fita(*i)