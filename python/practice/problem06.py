def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    if user_data['id'][-1] == ['1','2','3','4','5','6','7','8','9','0']:
        return True
    else:
        return False

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False