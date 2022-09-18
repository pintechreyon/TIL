import sys
sys.stdin = open('input.txt')

H, M = map(int, input().split())
num = int(input())
if M + num >= 60:
    H = H + (M + num) // 60
    M = (M + num) % 60
else:
    M = M + num
if H >= 24:
    H = H % 24
print(f'{H} {M}')
