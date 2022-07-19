orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
#1 주문 수 확인
cups = len(orders.split(','))
print(cups)

#2 중복을 제거한 메뉴만을 리스트로 출력하세요(단, 내림차순 정렬하여 출력하라)
orders_list = list(orders.split(','))
menu = []
for i in orders_list:
    if i not in menu:
        menu.append(i)
print(menu)

length = {}
for i in menu:
    len() = i

#리스트를 길이로 만들어서 딕셔너리 만들고 

