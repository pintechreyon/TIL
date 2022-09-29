import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, H = input().split()
    arr = []  # H를 10진수로 받기 위한 리스트
    binary = []  # 10진수로 변환된 H를 2진수로 변환해서 받기 위한 리스트
    for i in range(int(N)):  # 16진수를 10진수로 변환
        arr.append(int(H[i], 16))
    for i in arr:  # 10진수를 2진수로 변환
        binary.append(bin(i)[2:])
    for i in range(len(binary)):  # 2진수를 4bit 형식으로 만드는 것이 문제의 조건이므로 부족한 자리수를 0으로 채운다
        while len(binary[i]) < 4:
            binary[i] = '0' + binary[i]
    print(f"#{tc} {''.join(binary)}")
