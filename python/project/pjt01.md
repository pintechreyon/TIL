## 프로젝트 할때 유의사항

프로젝트간 발생한 문제 원인 참고문서 어려웠던 부분 새롭게 시도한 방법은 왜 그렇게 했는지

잘 모아서 리드미만들기

## 가상환경 만들기

python -m venv venv 가상환경 생성

source venv/Scripts/activate  가상환경 활성화

pip list 패키지 목록 확인

pip freeze > requirements.txt 가상환경 내 패키지 목록 txt파일로 출력

pip install -r requirments.txt 파일내에 있는 패키지 목록 설치

gitignore.io에서 복사 후에 .git으로 관리되는 공간에서 .gitignore파일생성 후 저장



#  1. Python을 활용한 데이터 수집

## - Python을 활용하여 주어진 json파일에서 필요한 정보만 추출해서 반환한다

### 1. id, title, poster_path, vote_average, overview, genre_ids의 값을 	   	dictionary로 가지는 함수를 완성한다

> 1. 요구하는 값을 리스트로 만들어서 새로운 dictionary의 key값으로 활용한다
>
>    ```python
>    movie_date =['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
>    ```
>
> 2. 비어있는 dictionary를 만들고 for문에서 movie_date를 key로 하는  dictionary를 만든다.
>
>    ```python
>    new_dict = {}
>        for i in movie_date:
>            new_dict[i] = movie.get(i) #movie는 사전에 주어진 movie.json파일의 값을 호출
>    ```

> 3. 만들어진 dictionary new_dict를 return 받으면 함수가 완성된다
>
>    ```python
>    def movie_info(movie):
>        movie_date = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
>        new_dict = {}
>        for i in movie_date:
>            new_dict[i] = movie.get(i)
>        return new_dict
>    ```

```ba
알게된것 : json 파일명을 활용하여 파일에 있는 데이터를 사용할 수 있다.
		  get 함수를 사용할 시 []인덱스를 활용한 경우와 다르게 error가 뜨지않고 'none'을 반환한다
```



### 2. 1단계에서 만든 데이터에서 genre_ids를 장르 번호가 아닌 장르 이름 리스트 genre_names로 바꿔 반환하는 함수를 완성한다

> 1. 