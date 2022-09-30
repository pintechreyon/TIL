word = input()
arr = [-1]*26
for i in range(len(word)):
    if arr[ord(word[i])-97] == -1:
        arr[ord(word[i]) - 97] = i
print(*arr)