# 게시글의 갯수 입력칸
A = int(input("게시글의 총 갯수를 입력하세요"))
# 한 페이지 게시글 수
B = int(input("한 페이지에 필요한 게시글 수를 입력하세요"))

if A%B == 0:
    print(int(A/B))
else:
    print(int(A/B+1))
