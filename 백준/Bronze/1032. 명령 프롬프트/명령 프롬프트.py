N = int(input())
arr = []
for i in range(N):
    arr.append(input())
maxv = arr[0]
num = len(arr[0])
for i in arr:
    result = ''
    for j in range(num):
        if maxv[j] != i[j]:
            result += '?'
        else:
            result += i[j]
    maxv = result

print(maxv)