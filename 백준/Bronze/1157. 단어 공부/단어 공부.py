arr= [0]*26
word = input()
result = 0
num = 0
for i in word:
    if ord(i) < 97:
        arr[ord(i)-65] += 1
    else:
        arr[ord(i) - 97] += 1
for i in range(26):
    if arr[i] == max(arr):
        result += 1
        num = i
if result == 1:
    print(chr(num+65))
else:
    print('?')