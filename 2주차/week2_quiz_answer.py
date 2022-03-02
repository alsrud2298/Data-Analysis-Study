# Q1 하나의 딕셔너리를 입력받아 딕셔너리의 key값을 화면에 출력하는 print_keys 함수를 정의하라.
def print_keys(dict):
    key_list = dict.keys()
    return key_list
result = print_keys({"이름":"김말똥", "나이":30, "성별":0})
print(result)

# Q2 연도가 주어졌을 때, 해당 연도가 윤년인지 판별하여 출력하는 함수를 작성하시오.
# 윤년 : 연도가 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일 때
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        result = "윤년입니다."
    else:
        result = "윤년이 아닙니다."
    return print(result)
leap_year(2020) # 윤년입니다.
leap_year(1999) # 윤년이 아닙니다.

# Q3 알람을 설정할 때 , 설정한 시간보다 45분 앞서는 시간으로 설정해주는 함수를 작성하시오.
def set_early(h,m):
    if m >= 45:
        m -= 45
    elif h == 0:
        m += 15
        h = 23
    else:
        m += 15
        h -= 1
    print("알람이 {}시 {}분으로 설정되었습니다.".format(h,m))

set_early(0, 30) # 알람이 23시 45분으로 설정되었습니다.
set_early(23, 45) # 알람이 23시 0분으로 설정되었습니다.
set_early(12, 25) # 알람이 11시 40분으로 설정되었습니다.

# Q4 당신의 회사에는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# 1주차부터 5주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt','2주차.txt',...와 같이 만듭니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
for num in range(1,6):
    with open("{}주차.txt".format(num),'w',encoding = 'utf8') as f:
        f.write("- {} 주차 주간 보고 - \n 부서 :\n 이름 :\n 업무 요약:".format(num))
        
    

# Q5 1 ~ 10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for문을 사용하여 작성하라.
sum = 0
for i in range(1,11):
    if i % 2 != 0:
        sum += i
print(sum)
        
# Q6 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 
# 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 
# 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(0, 5):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)