N = int(input())
M = int(input())
line = input()
word = 'I'
cnt = 0
for i in range(N):
    word += 'OI'
for i in range(M-2*(N-1)+1):
    if line[i:len(word)+i] == word:
       cnt += 1
print(cnt)