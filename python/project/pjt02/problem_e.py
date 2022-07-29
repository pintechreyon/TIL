import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.  
    url = f'https://api.themoviedb.org/3/search/movie?api_key=b61d4b9ed11cd4c3f0adecc291fd8b00&language=ko-KR&query={title}&page=1&include_adult=True'
    response = requests.get(url).json()
    if response['total_results'] == 0:
        return 'None'
    mov_re =  response['results']
    m_id = mov_re[0]['id']
    c_url = f'https://api.themoviedb.org/3/movie/{m_id}/credits?api_key=b61d4b9ed11cd4c3f0adecc291fd8b00&language=ko-KR'
    c_response = requests.get(c_url).json()
    casting = c_response['cast']
    cast_member = []
    for i in casting:
        if i['cast_id'] < 10:
            cast_member.append(i['name'])
    crewing = c_response['crew']
    crew_member = []
    for i in crewing:
        if i['department'] == 'Directing':
            crew_member.append(i['name'])

    result = {}
    result['cast'] = cast_member
    result['directing'] = crew_member
    return result



    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
