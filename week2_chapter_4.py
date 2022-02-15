# 04-1 함수
def add(a,b): # a,b는 매개변수 : 함수에 입력으로 전달된 값을 받는 변수
    return a+b
print(add(3,4)) # 3,4는 인수 : 함수를 호출할 때 전달하는 입력값

# 일반적인 함수
def add(a,b):
    result = a+b
    return result
print(add(2,6))

# 입력값이 없는 함수
def say():
    return "Hi"
print(say())

# 결과값이 없는 함수
def add(a,b):
    print("{0}, {1}의 합은 {2}입니다.".format(a,b,a+b))
add(3,4)
# 결과값은 오직 return 명령어로만 돌려받을 수 있음 ! 

# 입력값도 결과값도 없는 함수
def say():
    print("Hi")
say()

# 매개변수 지정하여 호출하기
def add(a,b):
    return a+b
result = add(b = 8, a = 7)
print(result)

# 여러개의 입력값을 받는 함수 만들기 
def add_many(*args): # *number , *python 등 아무 이름이나 사용해도 괜찮음.
# 입력값을 전부 모아서 튜플로 만들어준다. 
    result = 0
    for i in args:
        result += i
    return result
    
result = add_many(1,2,3)
print(result)
result = add_many(1,4,3,3,3,4,6,7,3)
print(result)

def add_mul(choice, *args): 
     if choice == "add": 
         result = 0 
         for i in args: 
             result = result + i 
     elif choice == "mul": 
         result = 1 
         for i in args: 
             result = result * i 
     return result 
result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 파라미터 kwargs
# 모두 딕셔너리로 만들어서 저장됨.
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name = "foo", age = 3)

# 함수의 결과값은 언제나 하나이다. 
# 리턴문을 2개 사용해도 첫번째 리턴문을 만나는 순간 결과값을 돌려준 뒤 함수를 빠져나감.

# 특별한 상황일 때 함수를 빠져나가고 싶은 경우
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 {} 입니다.".format(nick))
    
say_nick("바보")

# 매개변수 초기값 미리 설정하기
# 초기값을 설정한 매개변수는 항상 맨 뒤쪽에 놓아야함 ! 
def say_myself(name, old, man = True):
    print("나의 이름은 {}입니다.".format(name))
    print("나이는 {}살 입니다.".format(old))
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박응용", 27) # man 변수에 입력값 주지 않으면 초기값을 가짐.
say_myself("박응선",27,False)

# 함수 안에 선언한 변수의 효력 범위
# 함수 안에서 사용할 변수의 이름을 함수 밖에서도 동일하게 사용한다면 ? 
a = 1
def vartest(a):
    a  = a+1 # 함수 안에서 새로 만든 매개변수는 함수만의 변수임 ! 
vartest(a)
print(a)

# 함수 안에서 함수 밖의 변수 변경하기
# 1. return 사용하기
a = 1
def vartest(a):
    a = a+1
    return a
a = vartest(a)
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a # global : 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 의미
    # 함수는 독립적으로 존재하는 것이 좋으므로 가급적 사용하지 x
    a = a+1
vartest()
print(a)

# lambda : 함수 생성할 때 사용하는 예약어 def와 동일한 역할
add = lambda a,b : a+b # return 명령어가 없어도 결과값을 돌려준다 ! 
result = add(3,4)
print(result)

# 04-2 사용자 입력과 출력
# 사용자 입력
# input 사용
#a = input() # 입력되는 모든 것을 문자열로 취급함 ! 
#print(a)

#number = input("숫자를 입력하세요 : ")
#print(number)

# print
# " 로 둘러싸인 문자열은 + 연산과 동일
print("life""is""too short")
print("life"+"is"+"too short")
# 문자열 띄어쓰기 -> 콤마
print("life","is","too short")
# 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end = ' ')
    
# 04-3 파일 읽고 쓰기
f = open("새파일.txt",'w')
f.close()
# 이미 존재하는 파일을 다시 쓰기모드로 열면 원래 있던 내용 사라짐.
# 경로 지정
# f = open("파일경로/새파일.txt",'w')
# f.close()

# 파일 쓰기모드로 열어 출력값 적기
# 쓰기모드 : 'w'
f = open("새파일.txt",'w', encoding="utf8")
for i in range(1,11):
    data = "{}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()

# 프로그램 외부에 저장된 파일 읽기
# 읽기모드 : "r"
# readline 함수
f = open("새파일.txt","r", encoding = "utf8")
while True:
    line = f.readline() # 읽고 다음줄로 넘어감
    if not line: break
    print(line)
f.close()

# readlines 함수
f = open("새파일.txt","r",encoding = "utf8")
lines = f.readlines()
for line in lines: print(line.strip()) # 줄바꿈 제거
f.close()

# read 함수
f = open("새파일.txt",'r',encoding='utf8')
data = f.read() # 파일 내용 전체를 문자열로 돌려준다. 
print(data)
f.close()

# 파일에 새로운 내용 추가하기
# 추가모드 : 'a'
f = open("새파일.txt",'a',encoding='utf8')
for i in range(11,20):
    data = "{}번째 줄입니다.\n".format(i)
    f.write(data)
f.close()

# with문과 함께 사용하기
# with 블록을 벗어나는 순간 열린 파일 객체가 자동으로 close됨.
with open("foo.txt","w",encoding='utf8') as f:
    f.write("Life is too short, you need python")

# 4장 연습문제
# Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(num):
    if num%2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    return result
print(is_odd(4))
print(is_odd(3))

#Q2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg_nums(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    avg = sum / len(numbers)
    return avg
print(avg_nums(1,2,3,4,5))
        
# Q3 프로그램 오류 수정하기
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

# Q4 다음 중 출력 결과가 다른 것 한 개를 골라 보자.
print("you" "need" "python") # youneedpython
print("you"+"need"+"python") # youneedpython
print("you", "need", "python") # you need python
print("".join(["you", "need", "python"])) # youneedpython
# 3번

# Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# Q6 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
with open("test.txt", "a", encoding='utf8') as f:
    f.write(input())

# Q7
with open("test.txt","r") as f:
    body = f.read()

body = body.replace('java','python')
with open("test.txt",'w') as f:
    f.write(body)


