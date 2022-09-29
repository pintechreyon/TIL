T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc))

    # 알파벳 종류
    N = int(input())
    abchuk = {}
    for _ in range(N):
        Ci, Ki = input().split()
        # print(Ci, Ki)
        # A 10

        # Ci를 key로 Ki를 value로 넣어줘
        abchuk[Ci] = int(Ki)

    # 길이는 10으로 압축풀기
    length = 0
    for a in abchuk.keys(): # A B C
        for number in range(abchuk[a]): #  range(10)range(7) range(5)
            print(a, end='')
            length += 1
            if not length % 10:
                print()
    print()