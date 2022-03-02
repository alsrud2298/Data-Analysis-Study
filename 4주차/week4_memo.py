# 간단한 메모장 만들기
# 필요한 기능 : 메모 추가 , 메모 조회
# 입력 받는 값 : 메모 내용 , 프로그램 실행 옵션
# 출력하는 값 : memo.txt
# 입력 예제 : python week4_memo.py -a "Life is too short"

import sys

option = sys.argv[1]

# 메모 값 읽어 memo.txt에 저장하기
if option == "-a":
    memo = sys.argv[2]
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
# 메모 출력하기
elif option == '-v':
    f = open("memo.txt")
    memo = f.read()
    f.close()
    print(memo)
