import sys
sys.stdin = open('input.txt')

def same():
    for i in range(len(target) - len(pat) + 1):
        if target[i:len(pat)+i] == pat:
            return print(f'#{tc} 1')
    return print(f'#{tc} 0')

T = int(input())

for tc in range(1, T+1):
    pat = input()
    target = input()
    same()