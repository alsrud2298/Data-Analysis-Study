# Q1) 다음 코드가 동작하도록 Car 클래스를 정의하라.
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
car = Car(2, 1000)
print(car.wheel) # 출력 : 2
print(car.price) # 출력 : 1000
# Q2) 다음 코드가 동작하도록 Bicycle 클래스를 정의하라. 단 Bicycle 클래스는 Car 클래스를 상속받는다.
class Bicycle(Car):
    def __init__(self, wheel, price, brand):
        self.wheel = wheel
        self.price = price
        self.brand = brand
class Bicycle(Car):
    def __init__(self, wheel, price, brand):
        super().__init__(wheel, price)
        self.brand = brand
bicycle = Bicycle(2, 100, "삼천리")
print(bicycle.brand) # 출력 : 삼천리

# Q3) student라는 list에 마민경, 구남이, 박민영, 강수민 을 입력 후 
# enumerate를 사용해 번호를 붙여보자.
# 출력 예제
# 0번 마민경 
# 1번 구남이 ... 
student = ["마민경", "구남이", "박민영", "강수민"]
for num,name in enumerate(student):
    print("{0}번 {1}".format(num,name))

# Q4) 아래 함수의 실행 시간을 축정하시오. time.time() 이용 
# 소수점 두번째까지 반올림
# time.time() : 에포크 이후 초를 나타내는 시간을 부동 소숫점으로 반환하는 함수
# 에포크(epoch) : 시간의 기준점 , 1970년 1월 1일 0시 0분 0초
import math 
import time 
start = time.time() 
math.factorial(100000) 
end = time.time() 
print(round(end-start,2),"초")



# Q5) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건 1 : 승객 별 운행 소요 시간은 5 ~ 50 분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# random 모듈 활용 
# 출력 예제 
# [O] 1번째 손님 ( 소요시간 : 15분 )
# [ ] 2번째 손님 ( 소요시간 : 50분 )
# 총 탑승 승객 : 2분

from random import *
time = randint(5,50)

def total_customer():
    index = 0 # 총 승객 수
    for customer in range(1,51): # 총 승객 50명 
        time = randint(5,50) # 소요 시간 
        if time >= 5 and time <= 15: # 매칭 성공
            print("[O] {0}번째 손님 ( 소요시간 : {1}분 ) ".format(customer,time))
            index += 1 # 탑승 수 증가 처리
        else: # 매칭 실패
            print("[ ] {0}번째 손님 ( 소요시간 : {1}분 ) ".format(customer,time))
    print("총 탑승 승객 : {0}분".format(index))

total_customer()