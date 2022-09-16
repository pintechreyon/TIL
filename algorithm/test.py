def solution(n):
    bi = str(bin(n))
    bi = bi[2:]
    if bi.find('0') == -1:
        list(bi).insert(1, 0)
        result = int(2, ('0b' + str(bi)))
    else:
        if bi[len(bi)-1] == '0':
            bi[len(bi) - 1].replace() = '1'
            result = int('0b' + str(bi))
        else:
            var = bi.rfind('0')
            bi[var] = '1'
            bi[var + 1] = '0'
            result = int('0b' + str(bi))
    return result

A = solution(10)
print(A)