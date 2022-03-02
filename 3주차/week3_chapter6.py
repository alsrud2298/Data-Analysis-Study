# 구구단 함수 만들기
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return result
print(GuGu(2))

# 3과 5의 배수 합하기
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총 합을 구하라.
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)

# 게시판 페이징하기
# 게시물의 총 건수와 한 페이지에 보여 줄 게시물의 수를 입력했을 때 총 페이지수를 출력하는 프로그램

def getTotalPage(m,n): # m : 게시물의 총 건수 , n : 한 페이지에 보여줄 게시물 수
    if m % n == 0:
        return m // n
    return m//n + 1

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
