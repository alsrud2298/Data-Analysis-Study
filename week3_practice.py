# 구남이
# Q1
lst = [1,2,3,4,4,2,3,5,3]
my_list = sorted(list(set(lst)))
md  = my_dict = {}

for i in my_list:
    md[i] = lst.count(i)

max_count = max(md.values())

if max_count == 1 or max_count == len(lst):
    print("없음")
else:
    for value, count in md.items():
        if count == max(md.values()):
            print(value)

# Q2
def hide_numbers(s):
    new_num = s.replace(s[:-4],'*'*len(s[:-4]))
    return new_num

print(hide_numbers("01033334444"))
print(hide_numbers("027778888"))

# Q3
import random
#correct = random.randint(1,999)
correct = 88
answer = True
while answer:
    num = int(input("숫자를 입력하세요 : "))
    if num > 999 or num < 1:
        print("1 ~ 999 중의 숫자를 입력하세요.")
    if num < correct :
        print("up")
    elif num > correct :
        print("down")
    else:
        print("정답입니다 !")
        answer = False

# Q4 
def solution(n):
    answer = 0
    divisor = n
    while divisor > 0 :
        if n % divisor == 0:
            answer += divisor
        divisor-= 1
    return answer

# print(solution(int(input("숫자를 입력하세요 : "))))

# Q5
def solution(word,n):
    answer = (str(word) * n)[:n]
    return answer

print(solution("수박",4))

# 강수민
# Q1
class Human:
    pass

# Q2
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름 : {0}, 나이: {1}, 성별 : {2}".format(self.name,self.age,self.sex))
    
sumin = Human('sumin', 23, '여자')
sumin.who()

# Q3
per = ["10.31", "", "8.00"]
for i in per:
    try:
            print(float(i))
    except:
        print(0)

# Q4
per = ["10.31", "", "8.00"]
new_per = []
# Q5
num = random.randint(0,10)
if num > 5 :
    print("5보다 큽니다,")
elif num < 5 :
    print("5보다 작습니다.")

# 박민영
# Q1
class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2) 
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + "-" + num2 + "-" + num3
        Account.account_count += 1
    def deposit(self,money):
        if money >= 1:
            self.balance += money
        self.deposit_count += 1
        
        if self.deposit_count % 5 == 0:
            self.balance = self.balance * 1.01
            
    def withdraw(self,money):
        if money > self.balance:
            print("잔고가 부족합니다.")
        else:
            self.balance -= money
        return self.balance
    def display_info(self):
        print("은행이름 : {0}\n예금주 : {1}\n계좌번호 : {2}\n잔고 : {3}원".format(self.bank, self.name, self.account_num,self.balance))

park = Account("박민영", 5000)
lee = Account("이정재", 50000000)
an = Account("안나현", 20000)

list = []
list.append(park)
list.append(lee)
list.append(an)
# 입금 횟수 5의 배수 일 때, 잔고 기준 1% 이자 추가
park.deposit(5000)
park.deposit(5000)
park.deposit(5000)
park.deposit(5000)
park.deposit(5000)
print(park.balance)
for i in list:
    if i.balance >= 1000000:
        i.display_info()