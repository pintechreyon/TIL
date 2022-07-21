1. 간단한 N의 약수 (SWEA #1933) 

   입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오.

   ```python
   [제약 사항]
   N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
   [입력]
   입력으로 정수 N이 주어진다.
   [출력]
   정수 N의 모든 약수를 오름차순으로 출력한다.
   [입력 예시]
   10
   [출력 예시]
   1 2 5 10
   #숫자입력
   N = int(input())
   #N을 i로 나눌때 나머지가 0이면 약수
   for i in range(1,N+1):
       if N % i == 0:
           print(i, end=" ")
   ```

   

2. List의 합 구하기 

   정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

   ```python
   list_sum([1, 2, 3, 4, 5]) # => 1
   
   def list_num(sum):
       A = 0
       for i in sum:
           A = A + i
       return A
   ```

   

3. Dictionary로 이루어진 List의 합 구하기 

   Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오

```python
dict_list_sum([{’name’: ’kim’, ’age’: 12},{’name’: ‘lee’, ’age’: 4}]) # => 16

def dict_list_sum(dict):
    num = 0
    for i in dict:
        num += i['age']
    return num
```

4. 2차원 List의 전체 합 구하기 

   정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) # => 55
def all_list_sum(num):
    j = 0
    k = 0
    for i in num:
        for j in i:
            k = k+j
    return k
```

5. 숫자의 의미 

   정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오.  단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.

```python
get_secret_word([83, 115, 65, 102, 89])
def get_secret_word(s1):
    ascii = str()
    for i in s1:
        ascii += chr(i)
    return ascii
```

6. 내 이름은 몇일까? 

   문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.

```python
get_secret_number(’happy’) # => 546
def get_secret_number(s1):
    ascii = int()
    for i in s1:
        ascii += ord(i)
    return ascii
```

7. 강한 이름 

   문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오. 단, 두 문자열의 아스키 숫자의 합이 같은 경우, 둘 다 반환하세요.

```python
get_strong_word(’z’, ’a’) # => ‘z’
get_strong_word(’delilah’, ’dixon’) # => ‘delilah’
def get_strong_word(s1,s2):
    if ord(s1) > ord(s2):
        return s1
    elif ord(s1) < ord(s2):
        return s2
    else:
        return s1,s2
```

