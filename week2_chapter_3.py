# 03-1 if문 
# 들여쓰니는 언제나 같은 너비로 ! 
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# 조건문 비교 연산자
x = 3
y = 2
print(x < y)
print(x == y)
print(x > y)
print(x != y)

# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
if money > 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# and or not
# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
card = True
if money >= 3000 or card :
    print("택시를 타고 가라")
else:
    print("걸어가라")

# in , not in
print(1 in [1,2,3])
print(1 not in [1,2,3])
print('j' not in 'python')
# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."
pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고가라")
else:
    print("걸어가라")
    
# pass
# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# elif : 개수 제한 없이 사용 가능 
# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라."
if 'money' in pocket:
    print("택시를 타고가라")
elif 'card' in pocket:
    print("택시를 타고가라")
else:
    print("걸어가라")

# 한줄 if문
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식
score = 80
message = "success" if score>=60 else "failure"
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# 가독성에 유리하고 활용성이 좋다.

# 03-2 while문
# while문이 참인 동안 while문 아래 문장이 반복해서 수행됨.
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 {}번 찍었습니다".format(treeHit))
    if treeHit == 10:
        print("나무가 넘어갑니다.")

# 여러가지 선택지 중 하나 입력받기
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number:
"""
number = 0
# while number != 4:
#     print(prompt)
#     number = int(input()) # 사용자의 숫자 입력 받기

# break : while문 강제로 빠져나가기

coffee = 10
money = 300
while money: # 항상 참이다.
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 {}개 입니다.".format(coffee))
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# continue : while문의 맨 처음( 조건문 )으로 돌아가기
# 홀 수만 출력하기
a = 0
while a < 10:
    a += 1
    if a%2 == 0 : continue
    print(a)

# 무한루프
# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

# 03-3 for문
# 1. 전형적 for문
test_list = ['one','two','three']
for i in test_list:
    print(i)

# 2. 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
    print(first + last)

# 3. for문의 응용
print("총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오.")
marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number += 1 
    if mark >= 60:
        print("{}번 학생은 합격입니다.".format(number))
    else:
        print("{}번 학생은 불합격입니다.".format(number))

# for문과 continue
#  60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무 메시지도 전하지 않는 프로그램
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("{}번 학생 축하합니다. 합격입니다.".format(number))
    
# range 함수
a = range(10) # 0 ~ 10 미만 숫자 포함하는 range 객체 생성
    
# 1 ~ 10 까지 더하기
add = 0
for i in range(1,11):
    add += i
print(add)

# 구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = " ")
    print('')

# 리스트 내포
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
# 짝수에만 3 곱하기
result = [num*3 for num in a if num%2 == 0]
print(result)
# 구구단
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)

# 3장 연습문제
# Q1 다음 코드의 결과값은 ? 
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# "shirt"

# Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
sum = 0
num = 0
while num < 1000:
    num += 1
    if num%3 == 0:
        sum += num
        
print(sum)

# Q3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
cnt = 0
while cnt < 5 :
    cnt += 1
    print('*'*cnt)
    
# Q4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

for i in range(1,101): print(i, end =" ")

# Q5 for문을 사용하여 A 학급의 평균 점수를 구해 보자.
class_A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in class_A:
    sum += score
print("\nA학급의 평균 점수는 {}점 입니다.".format(sum/len(class_A)))

# Q6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다. 
# 리스트 내포를 사용하여 표현해보자.
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)