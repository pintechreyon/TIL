# 1. lotto api로 부터 데이터 받아오기
import requests
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1023'
response = requests.get(url).json()
print(type(response))
# 2. 지난주 당첨 번호 알아내기
one = response['drwtNo1']
two = response['drwtNo2']
three = response['drwtNo3']
four = response['drwtNo4']
five = response['drwtNo5']
six = response['drwtNo6']
bonus = response['bnusNo']
number = [one, two, three, four, five, six]
print(number)

# 3. random module 이 가지고 있는 sample이라는 함수를 사용하여1부터 45중에 무작위 6개를 뽑는다.
import random
def my_number(): 
    return random.sample(range(1, 46), 6)
# 4. 그 번호가 당첨 번호와 일치하는지 확인한다.

def matching():
    match = 0
    for i in range(6):
        if my_number()[i] in number:
            match = match + 1
    return match
print(matching())



# 5. 천번 이상 새로운 로또 번호를 생성하여서 매번 당첨이 되었는지 확인해 보는 로직 작성
def percent():
    for i in range(1000):
        random.sample(range(1, 46), 6)
    return matching()

# 6. 1등부터 2등을 포함한 (보너스 번호까지) 4등까지의 각 당첨 횟수 출력하기
result = []
percent()
if percent() == 6:
    result.append('1등')
elif percent() == 5 and bonus in my_number():
    result.append('2등')
elif percent() == 5:
    result.append('3등')
elif percent() == 4:
    result.append('4등')
else:
    result.append('꽝')
print('1등',result.count('1등'))
print('2등',result.count('2등'))
print('3등',result.count('3등'))
print('4등',result.count('4등'))
print('꽝',result.count('꽝'))
