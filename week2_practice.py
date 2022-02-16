# 구남이
# 1. 
# num = int(input())
# if num % 2 == 0 :
#     print("짝수")
# else:
#     print("홀수")
# # 2.
# # score = int(input("score : "))
# if score > 90 & score <=100:
#     print("grade is A")
# elif score > 60 & score <= 90:
#     print("grade is B")
# elif score > 60 & score <= 90:
#     print("grade is C")
# elif score > 40 & score <= 60:
#     print("grade is D")
# else:
#     print("grade is E") 

# # 3.
# # phone = input("휴대전화 번호 입력 : ")
# if phone[:3] == "011":
#     print("당신은 SKT 사용자입니다.")
# elif phone[:3] == "016":
#     print("당신은 KT 사용자입니다.")
# elif phone[:3] == "019":
#     print("당신은 LGU 사용자입니다.")
# elif phone[:3] == "010":
#     print("당신은 알수없음 사용자입니다.")

# 4.
# number = input("주민등록번호 : ")
# if number[7] == "1" or number[7] == "3":
#     print("남자")
# elif number[7] == "2" or number[7] == "4":
#     print("여자")

# 5.
# fruit = ["사과", "포도", "홍시"]
# temp = input("좋아하는 과일은 ? ")
# if temp in fruit:
#     print("정답입니다")
# else:
#     print("오답입니다")

# 강수민
# 1. 


while True:
    for i in range(4,6):
        for j in range(1,10):
            print("{0} x {1} = {2}".format(i,j,i*j))
    if i == 5:
        break
# 2.
for i in range(1,5):
    print("밥 {}그릇 주세요~".format(i))

# 3.
name = input("이름을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))
print("{0}씨는 {1}년에 100살 이시네요 ! ".format(name, 100 + 2022 - age))

# 4. 
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        result = "윤년입니다."
    else:
        result = "윤년이 아닙니다."
    return print(result)

# 5.
def delema(XA,XB):
    if XA & XB :
        YA,YB = 5, 5
    elif XA == True or XB == True:
        if XA == True:
            YA = 0
            YB = 10
        elif XB == True:
            YB = 0
            YA = 10
    else:
        YA = 1
        YB = 1
    return YA,YB

print(delema(False, True))

# 박민영
# 1.
num = int(input())
for i in range(1,10):
    print("{0} * {1} = {2}".format(num,i,num*i))

# 2.
def sum_nums(*a):
    sum = 0
    for number in a:
        sum += number
    return sum
print(sum_nums(1,2,3,4,5))

# 3. 
num = int(input()) 
for i in range(1,num+1):
    print("*" * i)

# 4.
num = int(input()) 
for i in range(1,num+1):
    print(" "*(n-i) + "*"*i)

# 5.
cnt = 0
num = int(input("숫자를 입력하세요 : "))
while True:
    cnt += 1
    if num < 10:
        temp = num*10 + num
    else:
        temp = ( num%10 * 10 )  + num//10 + num%10
    if temp == num:
        break
    num = temp
print(cnt)