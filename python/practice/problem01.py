def max_score(scores):
    pass
    # 여기에 코드를 작성합니다.
    big_num = 0
    for i in scores:
        if i > big_num:
            big_num = i
    return big_num

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
