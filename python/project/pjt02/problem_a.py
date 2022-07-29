import requests


def popular_count():

    url = 'https://api.themoviedb.org/3/movie/popular?api_key=b61d4b9ed11cd4c3f0adecc291fd8b00&language=ko-KR&page=1'
    response = requests.get(url)
    movie_dict = response.json()
    return len(movie_dict['results'])



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
