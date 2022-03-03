# Q1
chr = 'a:b:c:d'
chr1 = chr.split(':')
print("#".join(chr1))

#Q2 딕셔너리 get 함수 
a = {'A':90, 'B':80}
print(a.get('C',70))

#Q3 리스트 더하기와 extend 함수
a = [1,2,3]
print("전 주소 : " ,id(a))
a = a + [4,5]
print("현 주소 : " ,id(a))
b = [1,2,3]
print("전 주소 : " ,id(b))
b.extend([4,5])
print("현 주소 : " ,id(b))
# 차이점 ? 
# 리스트 덧셈을 사용하면 리스트의 값이 변하는 것이 아니라
# 두 리스트가 더해진 새로운 리스트가 반환됨 ! 
# extend : 주소 값이 변하지 않고 그대로 유지됨.

# Q4 리스트 총 합 구하기 ( 50점 이상 점수의 총합 )
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
total = 0
for score in A:
    if score >= 50:
        total += score
print(total)

# Q5 피보나치 함수

# n 이하까지 0 + 1 + 1 + 2 + ... 
def fibo(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fibo(n-2) + fibo(n-1)
print(fibo(9))
    
    
# Q6 숫자 총합 구하기
num = "65,45,2,3,45,8"
numbers = num.split(",")
total = 0
for n in numbers:
    total += int(n)
print(total)

# Q7 한 줄 구구단
num = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
for i in range(1,10):
    print(num * i,end = " ")
print("\n")
    
# Q8 역순 저장
f = open("./4주차/abc.txt", 'r')
body = f.readlines()
f.close()
# 역순 정렬
body.reverse()
f = open("./4주차/abc.txt",'w')
for line in body:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

# Q9 평균값 구하기
f = open("./4주차/sample.txt",'r')
lines = f.readlines()
f.close()
total = 0
for line in lines:
    total += int(line.strip())

f = open("./4주차/result.txt",'w')
f.write(str(total))
f.write("\n")
f.write(str(total/len(lines)))
f.close()    

# Q10 사칙연산 계산기
class Calculator():
    def __init__(self,numlist):
        self.numlist = numlist
    def sum(self):
        total = 0
        for i in self.numlist:
            total += i
        return total         
    def avg(self):
        total = self.sum()
        return total / len(self.numlist)
    
cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())        
cal2 = Calculator([6,7,8,9,10]) 
print(cal2.sum())
print(cal2.avg())     

# Q11 모듈 사용법
# 1. sys 모듈 사용
# 2. PYTHONPATH 환경 변수 사용
# 3. 현재 디렉터리 사용

# Q12 오류와 예외처리
result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
# 3(IndexError) + 4(finally) = 7  

# Q13 DashInsert 함수
# 홀수가 연속되면 두 수 사이에 - 추가, 짝수 연속 * 추가
num = "4546793"
def DashInsert(n):
    numbers = list(map(int,n)) # 숫자 문자열 -> 숫자 리스트로 변경
    result = []
    for i, num in enumerate(numbers):
        result.append(str(num))
        if i < len(numbers) -1 : # 다음 수가 있다면
            is_odd = num % 2 == 2 # 현재 수가 홀수
            is_next_odd = numbers[i+1] % 2 == 1 # 다음 수가 홀 수
            if is_odd and is_next_odd:
                result.append("-")
            elif not is_odd and not is_next_odd:
                result.append('*')
    print("".join(result))
DashInsert(num)
            
# Q14 문자열 압축하기
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result

print(compress_string("aaabbcccccca"))

# Q15 Duplicate Numbers
def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chkDupNum("012322456789"))
# Q16 모스 부호 해독
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))
# Q17 기초 메타 문자
# a[.]{3,}b -> a....b와 매치 

# Q18 문자열 검색
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
m.start() + m.end()
# 2 + 8
 
# Q19 그루핑
import re

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)

# Q20 전방탐색
# 긍정형 전방탐색 패턴
import re

pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))