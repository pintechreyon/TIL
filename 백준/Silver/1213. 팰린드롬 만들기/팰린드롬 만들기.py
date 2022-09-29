word = input()

S = [0]*26



for i in word:
    S[ord(i)-65] += 1

odd_cnt = 0

result = ''
mid = ''

for i,v in enumerate(S):
    if v == 0:
        continue 

    if  v % 2 ==0:
        result += (chr(i+65)*(v//2))

    else:
        result += (chr(i+65)*(v//2))
        mid = chr(i+65)
        odd_cnt+=1

    if odd_cnt > 1:
        break

if odd_cnt > 1:
    print ("I'm Sorry Hansoo")
else:
    print(result+mid+result[::-1])