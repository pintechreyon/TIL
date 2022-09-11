import sys
sys.stdin = open('input.txt')

N = list(map(int, input()))
result = 0
while N:
    arr = list(range(10))
    for i in arr:
        if i == 6 or i == 9:
            if 6 in N:
                N.pop(N.index(6))
            elif 9 in N:
                N.pop(N.index(9))
        elif i in N:
            N.pop(N.index(i))
    result += 1
print(result)


