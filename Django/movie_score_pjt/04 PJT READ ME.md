# 04 PJT READ ME

### 가상 환경을 만들고 실행시킨다

```python
python -m venv venv
source venv/Scripts/activate
```

### 장고를 설치해 주거나 기존에 만든 텍스트 파일을 통해 설치한다

```python
pip install django==3.2.13
or
pip install -r 파일이름.txt
```

### 프로젝트와 앱을 만들어 준다

```python
django-admin startproject mypjt
python manage.py startapp movie
```

### Model, URL, View 순으로 명세서에서 필요한 파일들을 만든다.

### base.html을 만들어서 스켈레톤 코드를 저장하고 파일 별로 다른 코드가 들어가는 부분에 블록 태그를 만든다

### base.html을 extend로 받아서 index, detail, new, edit html파일을 만든다.

### index.html을 먼저 만들어서 새로운 정보를 만들 수 있도록 new로 이동하는 하이퍼링크를 만들고 만들어졌을때 목록에 표시되고 제목을 누를 수 있도록 하는 페이지를 만든다. 밑에는 평점 표시

```python
  {% for movie in movies %}
    <p>{{ movie.pk }}</p>

    <a href="{% url 'movies:detail' movie.pk %}">
      <p>{{ movie.title }}</p>
    </a>
    
    <p>{{ movie.score }}</p>
    <hr>
  {% endfor %}
```



### new.html은 명세서에서 필요로 하는 값을 입력할 수 있도록 하고 날짜 선택은 input type을 date로 하고 장르 선택은 input이 아니라 select를 사용하여 드롭다운 형태로 나오게 한다.

```python
#제목 등 텍스트입력칸
    <label for="audience">AUDIENCE</label>
    <input type="text" id="audience" name="audience">
# 날짜입력
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" id="release_date" name="release_date">
# 목록 중 하나를 선택할 수 있는 드롭다운 형태의 박스
    <label for="genre">GENRE</label>
    <select name="genre" id="genre">
      <option value="">장르선택</option>
      <option value="코미디">코미디</option>
      <option value="판타지">판타지</option>
      <option value="어드벤처">어드벤처</option>
    </select>
```

### edit.html은 new와 비슷한 형태로 하나 기존에 입력했던 값을 나타내도록 input태그 안에 value를 활용한다. 마지막에는 원래 상태로 초기화 할 수 있도록 reset 버튼을 넣는다

```python
# 보통 text값은 이렇게 넣는다
<label for="score">SCORE</label>
<input type="text" id="score" name="score" value = '{{movie.score}}'>
#date값은 밸류 설정이 좀 다르다
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" id="release_date" name="release_date" value = {{movie.release_date | date:'Y-m-d'}}>
#reset은 input type을 reset으로 하면 초기값으로 설정된다
    <input type="reset" value="Reset">
```

### detail.html은 가장 상단에 이미지 링크를 입력하면 값을 받아서 나오게 하도록 이미지 태그를 넣는다 그 외 명세서에서 지시한대로 값을 설정하고 delete 버튼은 form태그 안에 csrf_token태그를 사용하여 csrf공격에 대비한다

```python
#이미지 태그를 사용해서 입력받은 값을 사진으로 나타냄
<img src="{{movie.poster_url}}" alt="사진을 넣어주세요">
#delete버튼 만들 때.
<form action="{% url 'movies:delete' movie.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
```



