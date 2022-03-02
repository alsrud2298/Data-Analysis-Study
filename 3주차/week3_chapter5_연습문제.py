# 1. 
from turtle import update


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# 2. 
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100

# 3. 
print(all([1,2,abs(-3)-3])) # abs(-3)-3 = 0 이므로 False
print(chr(ord('a')) == 'a') # ord : 문자 > 유니코드 , chr :유니코드 > 문자 True

# 4. 
print(list(filter(lambda x : x > 0, [1,-2,3,-5,8,-3])))

# 5.
print(int("0xea",16))

# 6. 
print(list(map(lambda x : x*3, [1,2,3,4])))

# 7.
print(max([-8, 2, 7, 5, -3, 5, 0, 1]))
print(min([-8, 2, 7, 5, -3, 5, 0, 1]))

# 8.
print(round(17/3, 4))

# 9.
import sys
numbers = sys.argv[1:]
result = 0
for number in numbers:
    result += int(number)
# print(number)
# 10.
#import os
# os.chird("C:doit")
# result = os.poepn("dir")
# print(result.read())
# # 11.
# import glob
# glob.glob("C:/doit/*.py")
# # 12.
import time
time.strftime("%Y/%m/%d %H:%M:%S")
# 13. 
import random
result = []
for i in range(1,7):
    num = random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)
