T = int(input())
for tt in range(T):
    s = input().strip()
    print( f'#{tt+1} {int(s==s[::-1])}' )