# 05-1 클래스 

# 계산기 덧셈 함수
result = 0
def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))
# 계산기가 여러대 필요한 경우 ? 클래스를 사용해서 간단하게 해결 가능
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
    # 빼기 기능 추가
    def sub(self, num):
        self.result -=num
        return self.result

cal1 = Calculator() # 객체 생성
cal2 = Calculator() # 객체 생성

print(cal1.add(3))
print(cal1.add(7))
print(cal2.add(4))
print(cal2.add(5))

# 객체마다 고유한 성격을 가진다 ! 동일한 클래스에서 만든 객체들은 서로 영향 주지 않음.
# 객체는 클래스의 인스턴스이다.

# 사칙연산 클래스 
# 메서드 : 클래스 내부의 함수
class FourCal:
    def __init__(self,first,second): # 생성자 : 객체가 생성될 때 자동으로 호출되는 메서드
        self.first = first
        self.second = second
    def setdata(self, first, second): # self에는 생성된 객체가 전달됨.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
        
a = FourCal(4,2)
# FourCal.setdata(a, 4, 2) : 클래스이름.메서드 형태로 호출 시 객체를 첫번째 매개변수에 전달해줘야함 !
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

# 클래스의 상속 : 다른 클래스의 기능을 물려받을 수 있게 만듦.
# 기존 클래스 변경하지 않고 기능 추가/변경 시 사용
# 제곱 기능 추가
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
print(a.add()) # FourCal 클래스의 모든 기능 사용 가능 ! 
print(a.pow())

# 메서드 오버라이딩 : 부모클래스의 메서드 대신 오버라이딩한 메서드 호출됨.
a = FourCal(4,0)
#print(a.div()) ZeroDivisionError 발생
# 오류가 아닌 0을 반환하도록
class SafeFourCal(FourCal):
    def div(self): # FourCal클래스의 div메서드를 동일 이름으로 다시 작성
        if self.second == 0 :
            return 0
        else:
            return self.first/self.second
a = SafeFourCal(4,0)
print(a.div())

# 클래스 변수
class Family:
    lastname = "김" # 클래스 변수
a = Family()
b = Family()
print(a.lastname)
Family.lastname = "박"
# 클래스 변수는 클래스로 만든 모든 객체에 공유됨
print(a.lastname)
print(b.lastname)

# 05-2 모듈
# 모듈 : 함수나 변수 또는 클래스를 모아 놓은 파일

from platform import java_ver
import mod1
print(mod1.add(3,4))
print(mod1.sub(4,1))

from mod1 import * # 모듈 이름 붙이지 않고 바로 함수 사용 가능
print(add(3,4))
print(sub(4,2))

# if __name__ == "__main__" : 직접 파일 실행시에만 if문 다음이 실행됨. 모듈 불러와서 사용 시 수행되지 않음.

# 클래스나 변수 포함한 모듈
import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))

# 05-3 패키지
# 파이썬 모듈을 계층적(디렉토리 구조)으로 관리할 수 있게 해줌
# __init__.py : 해당 디렉토리가 패키지의 일부임을 알려주는 역할
# relative한 접근자
# .. : 부모디렉토리
# . : 현재 디렉토리

# 05-4 예외 처리
# FileNotFoundError : 없는 파일 열려고 시도할 경우 발생
# ZeroDivisionError : 0으로 다른 숫자를 나누는 경우 발생
# IndexError 

# 오류 예외 처리 기법
try :
    4 / 0
except ZeroDivisionError as e : # e : 오류 메세지 변수
    print(e)
    
# finally : 예외 발생 여부에 관계없이 항상 수행
# 사용한 리소스를 close해야할 때 자주 사용

# 여러개의 오류 처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
    
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
    
# try문에 else 사용
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else: # 오류가 발생하지 않았을 시에만 실행됨 
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
        
# 특정 오류 발생 시 그냥 통과시켜야 할 경우
try:
    f = open("없는 파일", 'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기 → raise 명령어 사용
# Bird 클래스를 상속받는 자식클래스가 반드시 fiy함수를 구현하도록 하고싶은 경우
class Bird:
    def fly(self):
        raise NotImplementedError # 꼭 작성해야하는 부분이 구현되지 않았을 경우 오류 발생을 위해 사용

class Eagel(Bird):
    pass
eagle = Eagel()
# eagle.fly() 예외 발생

# 예외 만들기 : Exception 클래스 상속
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
# say_nick("바보") 예외 발생

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
    
# 05-5 내장함수
# 내장함수 : 별도의 설정 없이 바로 사용할 수 있음.
# 1. abs : 절대값 반환
print(abs(-3))
# 2. all : 반복가능한 자료형을 입력 인수로 받아 하나라도 거짓이면 False 반환
print(all([1,2,3]))
print(all([1,2,0]))
# 3. any : 반복가능한 자료형을 입력 인수로 받아 하나라도 참이 있으면 True, 모두 거짓이면 False
print(any([1,2,3,0]))
print(any(["",0]))
# 4. chr : 유니코드값을 입력받아 그 코드에 해당하는 문자 출력
print(chr(97))
print(chr(44032))
# 5. dir : 객체가 자체적으로 가진 변수나 함수 보여줌
print(dir([1,2,3]))
print(dir({"1":"a"}))
# 6. divmod : 2개의 숫자를 입력으로 받아 a를 b로 나눈 몫과 나머지를 튜플 형태로 반환
print(divmod(7,3))
# 7. enumerate : 순서가 있는 자료형을 입력받아 인덱스 값을 포함하는 enumerate 객체로 돌려줌
for i,name in enumerate(['body','foo','bar']):
    print(i,name)
# 8. eval : 실행가능한 문자열을 입력받아 실행한 결과값을 돌려줌.
print(eval('1+2'))    
print(eval("'hi' + 'a'"))
print(eval('divmod(4,3)'))
# 9. filter : 첫번째 인수로 함수이름, 두번째 인수로 반복가능한 자료형을 받아 반환값이 참인 것만 묶어서 돌려줌
print(list(filter(lambda x : x > 0,[1,-3,2,0,-5,6])))
# 10. hex : 정수값을 16진수로 변환하여 돌려주는 함수
print(hex(234))
# 11. id : 객체의 고유 주소 값(레퍼런스)를 돌려주는 함수
a = 3
print(id(a))
# 12. input : 사용자 입력받는 함수
a = input("Enter : ")
print(a)
# 13. int : 문자열 형태의 숫자나 소수점이 있는 숫자등을 정수형태로 돌려주는 함수
print(int('3'))
# int(x,radix) : radix 진수로 표현된 문자열 x를 10진수로 변환해 출력
print(int('1A',16))
# 14. isinstance(object, class) : 입력받은 인스턴스가 그 클래스의 인스턴스인지 판단하여 True,False 출력
class Person : pass
a = Person()
isinstance(a, Person)
# 15. len : 입력값의 길이(요소의 전채 개수) 돌려주는 함수
print(len("python"))
# 16. list: 반복가능한 자료형을 입력받아 리스트로 변환해 돌려주는 함수
print(list("python"))
# 17. map(f, iterable) : 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려줌
def two_times(x):
    return x*2
print(list(map(two_times, [1,2,3,4])))
# 18. max : 반복가능한 자료형을 입력받아 그 최대값을 돌려주는 함수
print(max([1,2,3]))
# 19. min : 반복가능한 자료형을 입력받아 그 최소값을 돌려주는 함수
print(min("python"))
# 20. oct : 정수형태의 숫자를 8진수 문자열로 바꿔 돌려주는 함수
print(oct(32))
# 21. open : 파일 이름과 읽기방법을 입력받아 파일 객체로 돌려주는 함수. 방법 생략 시 읽기전용모드
# "b" : 바이너리 모드 , w r a 와 함께 사용
# 22. ord : 문자의 유니코드 값을 돌려주는 함수
print(ord('a'))
# 23. pow(x,y) : x의 y제곱한 결과를 돌려주는 함수
print(pow(2,4))
# 24. range(start,stop,step) : 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려줌
print(list(range(1,10,2)))
# 25. round(number,ndigits) : 숫자를 입력받아 반올림 해주는 함수
print(round(5.678,2))
# 26. sorted : 입력값을 정렬한 후 그 결과를 리스트로 돌려주늖 ㅏㅁ수
print(sorted([3,1,2]))
# 27. str : 문자열 형태로 객체를 변환하여 돌려주는 함수
print(str(3))
# 28. sum : 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
print(sum([1,2,3]))
# 29. tuple : 반복 가능한 자료형을 입력받아 튜플형태로 변환해 돌려주는 함수
print(tuple([1,2,3]))
# 30. type : 입력값의 자료형이 무엇인지 알려주는 함수
print(type("abc"))
# 31. zip : 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수
print(list(zip([1,2,3],[4,5,6])))

# 05-6 라이브러리
# 1. sys : 파이썬 인터프리터가 제공하는 변수, 함수를 직접 제어할 수 있게 해주는 모듈
# 2. pickle : 객체 형태는 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
f = open("test.txt",'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f) # 파일에 객체 저장
f.close()
f = open("test.txt",'rb')
data = pickle.load(f) # 저장한 파일 원래 객체 상태로 불러오기
print(data)

# 3. os : 환경변수, 디렉토리, 파일 등 OS자원을 제어할 수 있게 해주는 모듈
import os
os.environ # 현재 시스템의 환경 변수 값 반환
os.getcwd # 현재 자신의 디렉토리 위치 반환
# os.chdir("C:\WINDOWS") # 현재 디렉토리 위치 변경
os.system("dir") # 시스템 명령어 호출
f = os.popen("dir") # 시스템 명령어 실행 결과값 파일 객체로 반환
print(f.read())

# 4. shutil : 파일 복사해주는 모듈
import shutil
shutil.copy("foo.txt",'dst.txt')

# 5. glob : 디렉토리에 있는 파일 읽어서 돌려줌
import glob
# glob.glob("파일주소")

# 6. tempfile : 파일 임시로 만들 때 사용
import tempfile
filename = tempfile.mkstemp() # 중복되지 않는 임시 파일 이름 무작위 생성
print(filename)
f = tempfile.TemporaryFile() # 임시 저장공간으로 사용할 파일 객체 반환, 기본적으로 wb 모드 
f.close() # 임시 생성한 파일 사라짐

# 7. time : 시간과 관련된 함수 
import time
time.time() # 1970/01/01 0:0:0 을 기준으로 지난 시간을 초 단위로 반환
time.localtime(time.time()) # time.time()이 돌려준 실수값을 연,월,일,시,분,초 형태로 바꿔줌
time.asctime(time.localtime(time.time())) # 날짜와 시간을 보기 쉬운 형태로 돌려줌
time.ctime() # 위의 함수를 간편하게 사용 가능 , 항상 현재 시간만 돌려줌 
time.strftime("%x",time.localtime(time.time())) # 시간과 관련된 것을 세밀하게 표현, 다양한 포맷코드 사용 가능
time.sleep(1) # 일정 시간 간격을 둠. 초단위

# 8. calendar : 파이썬에서 달력 볼 수 있게 해주는 모듈
import calendar
#print(calendar.calendar(2015))
print(calendar.prmonth(2015,12))
print(calendar.weekday(2015,12,31)) # 그 날짜에 해당하는 요일정보 돌려줌 (0~6 : 월 ~ 일)
print(calendar.monthrange(2015,12)) # 1일이 무슨 요일인지, 며칠까지 있는지 튜플 형태로 반환

# 9. random : 난수 발생 모듈
import random
random.random() # 0.0 ~ 1.0 사이 실수 중 난수 값 반환
random.randint(1,10) # 1 ~ 10 사이 정수 중 난수 값 반환
data = [1,2,3,4,5]
random.shuffle(data) # 리스트 항목 무작위로 섞기
print(data)
print(random.choice(data)) # 리스트에서 무작위로 하나 선택해 반환
 
# 10. webbrowser : 자신의 시스템에서 사용하는 기본 웹브라우저 자동실행
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com") # 이미 실행된 상태여도 새로운 창으로 열어줌
