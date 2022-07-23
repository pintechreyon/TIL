def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    over_num = []
    for i in scores:
        if i >= 60:
            over_num.append(i)
    return len(over_num)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
