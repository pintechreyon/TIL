s = input('숫자를 입력해주세요 : ')
# 입력 숫자 문자열로 변환
def cal(s):
    b = 0
    for i in str(s):
        b+=int(i)
    return b
print(cal(s))

