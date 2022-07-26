1. 평균 점수 구하기
key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의
평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오

``` python
get_dict_avg({
	'python' : 80,
	'web' : 83,
	'algorithm' : 90,
	'django' : 89
})

def get_dict_avg(scores):
    #결과값
    result = 0
    #넘겨받은 dict의 value들만 있으면 된다.
    #모든 밸류들을 다 모아놓은 값도 필요하겠다.
    #총합
    #전체길이
    count = 0
    for score in scores.values():
        count += score
    result = count / len(scores)
    return result
```

2. 혈액형 분류하기 여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는 count_blood 함수를 작성하시오.

```python
count_blood([
'A', 'B', 'A', 'O', 'AB', 'AB’,'O', 'A', 'B', 'O', 'B', 'AB’,]) 
# => {'A': 3, 'B': 3, 'O': 3, 'AB': 3
def count_blood(type):
    result = {}
    for blood in type:
        #만약에 이미 result에 blood에 해당하는 키값이 있다면
        #if result['result'] # 이 경우, 키가 없으면 오류가 난다.
        if result.get(blood):
            #그 키값에 1을 추가한다.
            result[blood] += 1
            #없다면
        else:
            #그 키와 밸류를 새로 추가한다.
            result[blood] = 1
    return result
```

