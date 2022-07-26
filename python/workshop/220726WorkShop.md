# WorkShop


### 무엇이 중복일까
문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는 duplicated_letters 함수를 작성하시오.

```python
duplicated_letters(‘apple’) # => [‘p’]
duplicated_letters(‘banana’) # => [’a’, ‘n’]
def duplicated_letters(s1):
    var = []
    for i in s1:
        if i in s1.replace(i,'',1):
            var += i
    return list(set(var))
```

### 소대소대
문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는 low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만 구성된다.

```python
low_and_up(‘apple’) # => aPpLe
low_and_up(‘banana’) # => bAnAnA
def low_and_up(s1):
    s2 = ''
    v = 1
    for i in s1:
        if v % 2 == 1:
            s2+=i.lower()
        else:
            s2+=i.upper()
        v += 1
    return s2
```

### 솔로 천국 만들기
정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남 기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

```python
lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) # => [4, 3]
def lonely(s1):
    v = 0
    s2 = [s1[0]]
    for i in range(1,len(s1)):
        if s1[i] != s1[i-1] :
            s2.append(s1[i])
    return s2
```