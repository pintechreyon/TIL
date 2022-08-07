n = int(input())
i = 0
while 1:
    if n <= 2**(i+1) : break
    i += 1
print(1 if n == 1 else (n-2**i)*2)